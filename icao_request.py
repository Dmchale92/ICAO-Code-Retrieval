"""
Generic tool for retrieving ICAO (International Civil Aviation Organization) codes based on a list of countries
"""

from bs4 import BeautifulSoup
import requests


class ICAOSniffer(object):
    def __init__(self):
        self.icao_data_url = "https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization_airport_code"
        self.country_list = ["Switzerland",
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

    def __call__(self):
        print(self.display_icao())

    def retrieve_icao(self):
        # This sets the data source
        icao_data = requests.get(self.icao_data_url)

        country_codes = []

        soup = BeautifulSoup(icao_data.text)
        # This iterates over the DOM of the data source and pulls out country codes based on input country, filtering out duplicate results

        for country in self.country_list:
            country_iteration = 0
            for tableData in soup.find_all(title=country):
                if len(str(tableData.parent.parent.a.contents)) < 8 and country_iteration == 0:
                    country_codes.append("Country: " + country + " ICAO: " + str(tableData.parent.parent.a.contents[0]))
                    country_iteration += 1
                else:
                    continue
        return country_codes

    def display_icao(self):
        for country in self.retrieve_icao():
            print(country)
