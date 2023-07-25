# Web Scraping Singapore Postcode Data in Python

## Background

This project is a Python script for scraping postcode and region data from https://sgp.postcodebase.com. This is particularly useful for gathering mass postal code data for geographical and demographic analysis, providing essential information for businesses in areas such as logistics, real estate, retail and more.

Potential use-cases involve leveraging this data for improved business decision making, such as determining potential new store locations based on postal code densities, or optimizing delivery routes in a logistics network.


## Getting Started

You'll need Python 3.9+ installed on your local machine to run this script. Let's set up everything:

### Clone the Repository

```sh
git clone https://github.com/YourUsername/project-repo.git
```

### Install Requirements

We have listed the necessary libraries needed in the `requirements.txt` file. Install them using pip:

```sh
pip install -r requirements.txt
```

This will install `beautifulsoup4`, `selenium`, `loguru`, `webdriver_manager` and other necessary libraries used in the script.

## Running the Script

After installing the dependencies, you can run the script with the following command:

```sh
python main.py
```

This will start scraping the data from the website and save it into `postcode_data.csv`.

## Examples

Running the script as indicated above will scrape all pages from the website and save the data to a CSV file named `postcode_data.csv`. The CSV file will contain two columns: "Region" and "Postcodes". The "Postcodes" column will contain a comma-separated list of the first two digits of each postcode for the region.

Normally the script will automatically scrape pages from 1 through 1242. If you want to scrape a subset of pages, you need to modify the last line of `main.py`:

```python
# example: scrape pages from 50 to 100
data = scrape_all_pages(50, 100)
```

## Future Work

While the script currently serves its purpose, there are always ways to expand or refine its functionality:

* Expanding the script to scrape additional or more specific information.
* Implement error handling for reliable scraping over potential website changes.
* Increase efficiency and reduce sample interval (although respecting ethical and server-load constraints is also important).

## Contributors

[Samuel Koh](mailto:samuelkohzk@gmail.com)





