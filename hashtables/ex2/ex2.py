class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = ['NONE'] * length
    ticket_dict = {}
    
    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination
    
    current_airport = ticket_dict['NONE']
    i = 0
    while current_airport != 'NONE':
        route[i] = (current_airport)
        current_airport = ticket_dict[current_airport]
        i += 1

    return route