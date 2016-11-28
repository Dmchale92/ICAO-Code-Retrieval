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
        print("[Fibonacci-15-Even.py]-[TEST] - Running Unit Tests...")
        self.test_retrieve_icao()
        print('[Fibonacci-15-Even.py]-[TEST] - Unit Tests completed...')
        return True

    def retrieve_icao(self, country_list=None):
        """
        :return: list of ICAO codes based on country list input
        """
        if country_list is None:
            country_list = self.country_list

        country_codes = []

        """
        Set the data source
        """
        icao_data = requests.get(self.icao_data_url)
        soup = BeautifulSoup(icao_data.text, "html.parser")

        """
        This iterates over the DOM of the data source and pulls out country codes
        based on input country, filtering out duplicate results
        """
        for country in country_list:
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

    def test_retrieve_icao(self):
        country_list = self.retrieve_icao()
        country_list.__len__()
        try:
            assert country_list.__len__() == 29
            print('[icao_request.py]-[TEST] - [test_retrieve_icao] - PASS')
            return True
        except Exception as e:
            print("[icao_request.py]-[TEST] - [test_retrieve_icao] - FAIL: " + str(e))
            return False

ICAOSniffer = ICAOSniffer()

ICAOSniffer()

