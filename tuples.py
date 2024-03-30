#1
def format_itineraries(itineraries):
    changed = ""
    for i, itinerary in enumerate(itineraries, start=1):
        traveler_name, origin, destination = itinerary
        changed += f"{i}{traveler_name} From {origin} To {destination}"
    return changed
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_itineraries = format_itineraries(itineraries)
print(formatted_itineraries)

#2
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, title, author):
    added_book = (title, author)
    if added_book in library:
        print("Error: This book already exists in the library.")
    else:
        library.append(added_book)
        print("book was added")

add_book(library, "Animal Farm", "George Orwell")
print(library)

#3task1
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]
def avg_close_price(stock_data, stock_key):
    total_closing_price = 0
    count = 0

    for data in stock_data:
        if data[0] == stock_key:
            total_closing_price += data[2]
            count += 1
    
    if count == 0:
        print(f"No data found for '{stock_key}'.")
        return None
    else:
        return total_closing_price / count
    
stock_symbol = "AAPL"
avg_price = avg_close_price(stock_data, stock_symbol)
print(f"average closing price of {stock_symbol}: {avg_price}")

#3task2
attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    # More attendees...
]
def list_attendees_by_event(attendees, event_name):
    event_attendees = [attendee[0] for attendee in attendees if attendee[1] == event_name]
    return event_attendees

def attendees_per_event(attendees):
    attendees_per = {}
    for attendee in attendees:
        event_name = attendee[1]
        if event_name in attendees_per:
            attendees_per[event_name] += 1
        else:
            attendees_per[event_name] = 1
    return attendees_per

event = "Python Conference"
attendees_each_event = attendees_per_event(attendees)
for event, count in attendees_each_event.items():
    print(f"{event}: {count}")