class Visitors:
    def __init__(self,name,age, category):
        self.name = name
        self.age = age
        self.category = category
        self.tickets = []

    def registerVisitors (self):
        pass

    def purchaseTicket(self, ticket):
        self.tickets.append(ticket)