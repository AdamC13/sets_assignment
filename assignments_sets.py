
#1
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def compare_routes(your_route, their_route):
    both = your_route.intersection(their_route)
    just_your_airline = your_route.difference(their_route)
    not_shared = your_route.symmetric_difference(their_route)
    return [both, just_your_airline, not_shared]


print(compare_routes(our_routes, competitor_routes))
#2
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def remove_dups(item):
    item = set(item)
    print(item)
    return item
   
remove_dups(customer_ids)