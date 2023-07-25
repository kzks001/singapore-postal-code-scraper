from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from loguru import logger
from typing import Dict, List
import csv
import time


def scrape_page(driver, page_number: int) -> Dict[str, List[str]]:
    """
    Scrape a single page for region and postcode data.

    Args:
        driver: Selenium WebDriver.
        page_number (int): The page number to scrape.

    Returns:
        Dict[str, List[str]]: A dictionary where the keys are regions and the values are lists of postcodes.
    """
    url = f"https://sgp.postcodebase.com/all?page={page_number}"
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    soup = BeautifulSoup(driver.page_source, "html.parser")

    data = {}

    # Find all table rows
    for row in soup.find_all("tr")[1:]:  # Skip the header row
        columns = row.find_all("td")
        if columns:
            postcode = columns[0].text[:3]  # Get the first two digits of the postcode
            region = columns[1].text

            # If the region is already in the dictionary, append the postcode to the list
            # Otherwise, add a new list to the dictionary for the region
            if region in data:
                data[region].append(postcode)
            else:
                data[region] = [postcode]

    return data


def scrape_all_pages(start: int, end: int) -> Dict[str, List[str]]:
    """
    Scrape all pages in a range for region and postcode data.

    Args:
        start (int): The first page to scrape.
        end (int): The last page to scrape.

    Returns:
        Dict[str, List[str]]: A dictionary where the keys are regions and the values are lists of postcodes.
    """
    all_data = {}

    # Initialize the WebDriver
    webdriver_service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(service=webdriver_service, options=options)

    for page_number in range(start, end + 1):
        logger.info(f"Scraping page {page_number}")
        data = scrape_page(driver, page_number)

        # Merge the data from this page into the overall data
        for region, postcodes in data.items():
            if region in all_data:
                all_data[region].extend(postcodes)
            else:
                all_data[region] = postcodes

    driver.quit()

    return all_data


def save_to_csv(data: Dict[str, List[str]], filename: str) -> None:
    """
    Save region and postcode data to a CSV file.

    Args:
        data (Dict[str, List[str]]): The data to save, where the keys are regions and the values are lists of postcodes.
        filename (str): The name of the file to save the data to.
    """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Region", "Postcodes"])

        for region, postcodes in data.items():
            writer.writerow([region, ", ".join(postcodes)])


# Scrape all pages and save the data to a CSV file
data = scrape_all_pages(1, 1242)
save_to_csv(data, "./data/postcode_data.csv")
