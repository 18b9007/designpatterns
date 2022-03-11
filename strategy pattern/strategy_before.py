"""
Example code on support ticket handling before applying Strategy Pattern
Problem: process_tickets function has low cohesion due to the if-else statement of ordering strategies.
More strategies added = if-else statement is extended.
process_tickets having too many responsibilities
"""

import string
import random
from typing import List

def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))
    
class SupportTicket:
    id: str
    customer: str
    issue: str
    
    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue
        
class CustomerSupport:
    
    tickets: List[SupportTicket] = []
    
    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))
        
    def process_tickets(self, processing_strategy: str = "fifo"):
        # if it's empty, don't do anything
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return
        
        if processing_strategy == "fifo":
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif processing_strategy == "filo":
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
        elif processing_strategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.process_ticket(ticket)
    
    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print("Processing ticket id:", ticket.id)
        print("Customer:", ticket.customer)
        print("Issue:", ticket.issue)
        print("==================================")            
            
# create the application
app = CustomerSupport()

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets("random")