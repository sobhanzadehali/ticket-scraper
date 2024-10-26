from datetime import date
from .vehicle import Vehicle
class Ticket:
    def __init__(self, departure, destination, price, date:date, vehicle:Vehicle):
        self.date = date
        self.departure = departure
        self.destination = destination
        self.price = price
        self.vehicle = vehicle
    
    def __str__(self):
        return f"Date: {self.date}, Departure: {self.departure}, Destination: {self.destination}, Price: {self.price}, with: {self.vehicle}"