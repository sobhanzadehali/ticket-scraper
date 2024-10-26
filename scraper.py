from .ticket import Ticket
from .website  import Site

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from .settings import config

from datetime import datetime


class Scraper:
    def __init__(self, driver:Chrome, search_obj:Ticket):
        self.driver = driver
        self.search_obj = search_obj # search obj is a ticket object without price
        
    def _get_url(self, name):
        # generate url based on search obj
        url = config[name]["url"]
        url.replace("VEHICLE", self.search_obj.vehicle)\
            .replace("DEPARTURE", self.search_obj.departure)\
                .replace("DESTINATION", self.search_obj.destination)\
                    .replace("DATE",self.search_obj.date.strftime("%Y-%m-%d")) 
        
        return url

    def scrape_site(self, name):
        # get all tickets with selenium
        url = self._get_url(name)
        self.driver.get(url)
        tickets_elements = self.driver.find_elements(By.XPATH, config[name]["ticket_xpath"])
        ticket_list = []
        for i in tickets_elements:
            departure = self.search_obj.departure
            destination = self.search_obj.destination
            price = int(i.find_element(By.XPATH, config[name]["price_xpath"]).text.replace(",",""))
            date = self.search_obj.date
            vehicle = self.search_obj.vehicle

            # create ticket object and add to list
            ticket = Ticket(departure, destination, price, date, vehicle)
            ticket_list.append(ticket)
        site = Site(name, url, ticket_list)
        return site
