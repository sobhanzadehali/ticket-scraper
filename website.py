class Site:
    def __init__(self, name, domain, tickets):
        self.name = name
        self.domain = domain
        self.tickets = tickets #list of tickets
    
    
    def get_cheapest_ticket(self):
        if len(self.tickets)!=0:
            cheapest_ticket = min(self.tickets, key=lambda x: x.price)
            return cheapest_ticket
        else:
            return None
    def get_expensive_ticket(self):
        #returns most expensive ticket , if multiple exist with same price, returns one
        most_expensive_ticket = self.tickets[0]
        for ticket in self.tickets:
            if ticket.price > most_expensive_ticket.price:
                most_expensive_ticket = ticket
        return most_expensive_ticket

    
    def save_tickets(self):
        with open(f"{self.name}_tickets.txt", "w") as file:
            for ticket in self.tickets:
                file.write(str(ticket) + "\n")
        print(f"Tickets saved to {self.name}_tickets.txt")