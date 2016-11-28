__author__ = 'David McHale'

from bs4 import BeautifulSoup
import requests

###
# This is a generic tool for retrieving ICAO codes based on a list of countries
###
def main(page_url = "https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization_airport_code"):

    # This sets the data source
    r = requests.get(page_url)
    country_list = ["Switzerland",
                    "Albania",
                    "Armenia",
                    "Austria",
                    "Belgium",
                    "Bosnia and Herzegovina",
                    "Bulgaria",
                    "Croatia",
                    "Cyprus",
                    "Czech Republic",
                    "Denmark",
                    "Estonia",
                    "Finland",
                    "France",
                    "Georgia (country)",
                    "Germany",
                    "Greece",
                    "Hungary",
                    "Republic Of Ireland",
                    "Italy",
                    "Latvia",
                    "Lithuania",
                    "Luxembourg",
                    "Malta",
                    "Moldova",
                    "Monaco",
                    "Montenegro",
                    "Netherlands",
                    "Norway",
                    "Poland",
                    "Portugal",
                    "Republic of Macedonia",
                    "Romania",
                    "Serbia",
                    "Slovakia",
                    "Slovenia",
                    "Spain",
                    "Sweden",
                    "Turkey",
                    "Ukraine",
                    "United Kingdom"]
    country_codes = []

    # This iterates over the DOM of the data source and pulls out country codes based on input country, filtering out duplicate results
    soup = BeautifulSoup(r.text)

    for country in country_list:
        country_iteration = 0
        for tableData in soup.find_all(title=country):
            if len(str(tableData.parent.parent.a.contents)) < 8 and country_iteration == 0:
                country_codes.append("Country: " + country + " ICAO: " + str(tableData.parent.parent.a.contents[0]))
                country_iteration += 1
            else:
                continue
    for country in country_codes:
        print(country)
main()
