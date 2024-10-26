from ticket import Ticket
from scraper import Scraper
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

def main():
    departure = input("Enter your departure: ")
    destination = input("Enter destination: ")
    vehicle = input("Enter vehicle: ")
    search_object = Ticket(departure, destination, vehicle)
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--window-size=1920,1200")
    driver = Chrome(option)
    site = Scraper(driver, search_object).scrape_site("alibaba")
    print(site.get_cheapest_ticket())





