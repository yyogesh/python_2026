# ==========================================
#       MOVIE TICKET BOOKING SYSTEM
# ==========================================

GST = 0.18

movies = {
    "1": {
        "name": "Avengers Endgame",
        "price": 250,
        "seats": 50,
        "sold": 0
    },
    "2": {
        "name": "Interstellar",
        "price": 300,
        "seats": 40,
        "sold": 0
    },
    "3": {
        "name": "Jawan",
        "price": 180,
        "seats": 70,
        "sold": 0
    }
}

bookings = []


# ------------------------------------------
# Display Menu
# ------------------------------------------
def display_menu():
    print("\n")
    print("=" * 45)
    print("      MOVIE TICKET BOOKING SYSTEM")
    print("=" * 45)
    print("1. View Movies")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. View My Bookings")
    print("5. Revenue Report")
    print("6. Exit")


# ------------------------------------------
# Display Movies
# ------------------------------------------
def display_movies():
    print("\nAvailable Movies")
    print("-" * 60)
    print(f"{'ID':<5}{'Movie':<25}{'Price':<10}{'Seats'}")
    print("-" * 60)

    for key, movie in movies.items():
        print(
            f"{key:<5}"
            f"{movie['name']:<25}"
            f"₹{movie['price']:<9}"
            f"{movie['seats']}"
        )


# ------------------------------------------
# Calculate Bill
# ------------------------------------------
def calculate_bill(price, quantity):

    subtotal = price * quantity
    gst = subtotal * GST
    total = subtotal + gst

    return subtotal, gst, total


# ------------------------------------------
# Generate Receipt
# ------------------------------------------
def generate_receipt(name, movie, qty, subtotal, gst, total):

    print("\n")
    print("=" * 40)
    print("            RECEIPT")
    print("=" * 40)
    print("Customer :", name)
    print("Movie    :", movie)
    print("Tickets  :", qty)
    print("Subtotal : ₹", round(subtotal,2))
    print("GST      : ₹", round(gst,2))
    print("Total    : ₹", round(total,2))
    print("=" * 40)
    print("Booking Successful!")
    print("=" * 40)


# ------------------------------------------
# Book Ticket
# ------------------------------------------
def book_ticket():

    display_movies()

    movie_id = input("\nEnter Movie ID : ")

    if movie_id not in movies:
        print("Invalid Movie!")
        return

    customer = input("Customer Name : ")

    tickets = int(input("Number of Tickets : "))

    if tickets <= 0:
        print("Invalid Ticket Quantity")
        return

    if tickets > movies[movie_id]["seats"]:
        print("Sorry! Seats Not Available.")
        return

    subtotal, gst, total = calculate_bill(
        movies[movie_id]["price"],
        tickets
    )

    movies[movie_id]["seats"] -= tickets
    movies[movie_id]["sold"] += tickets

    booking = {
        "customer": customer,
        "movie": movies[movie_id]["name"],
        "tickets": tickets,
        "total": total
    }

    bookings.append(booking)

    generate_receipt(
        customer,
        movies[movie_id]["name"],
        tickets,
        subtotal,
        gst,
        total
    )


# ------------------------------------------
# View Bookings
# ------------------------------------------
def view_bookings():

    if len(bookings) == 0:
        print("\nNo Bookings Found")
        return

    print("\nBooking History")
    print("-" * 70)

    print(
        f"{'Customer':<20}"
        f"{'Movie':<25}"
        f"{'Tickets':<10}"
        f"{'Total'}"
    )

    print("-" * 70)

    for booking in bookings:

        print(
            f"{booking['customer']:<20}"
            f"{booking['movie']:<25}"
            f"{booking['tickets']:<10}"
            f"₹{round(booking['total'],2)}"
        )


# ------------------------------------------
# Cancel Ticket
# ------------------------------------------
def cancel_ticket():

    if len(bookings) == 0:
        print("\nNo Booking Available.")
        return

    customer = input("Enter Customer Name : ")

    found = False

    for booking in bookings:

        if booking["customer"].lower() == customer.lower():

            for movie in movies.values():

                if movie["name"] == booking["movie"]:
                    movie["seats"] += booking["tickets"]
                    movie["sold"] -= booking["tickets"]

            bookings.remove(booking)

            print("Booking Cancelled Successfully.")
            found = True
            break

    if not found:
        print("Customer Booking Not Found.")


# ------------------------------------------
# Revenue Report
# ------------------------------------------
def revenue_report():

    print("\n")
    print("=" * 70)
    print("Revenue Report")
    print("=" * 70)

    print(
        f"{'Movie':<25}"
        f"{'Sold':<10}"
        f"{'Revenue'}"
    )

    print("-" * 70)

    grand_total = 0

    for movie in movies.values():

        revenue = movie["sold"] * movie["price"]

        grand_total += revenue

        print(
            f"{movie['name']:<25}"
            f"{movie['sold']:<10}"
            f"₹{revenue}"
        )

    print("-" * 70)
    print("Total Revenue : ₹", grand_total)


# ------------------------------------------
# Main Function
# ------------------------------------------
def main():

    while True:

        display_menu()

        choice = input("\nEnter Choice : ")

        if choice == "1":
            display_movies()

        elif choice == "2":
            book_ticket()

        elif choice == "3":
            cancel_ticket()

        elif choice == "4":
            view_bookings()

        elif choice == "5":
            revenue_report()

        elif choice == "6":
            print("\nThank You!")
            print("Visit Again.")
            break

        else:
            print("Invalid Choice")


# ------------------------------------------
# Program Starts Here
# ------------------------------------------
main()