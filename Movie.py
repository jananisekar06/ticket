# Movie Ticket Booking System

class Movie:
    def __init__(self, name, available_seats, ticket_price):
        self.name = name
        self.available_seats = available_seats
        self.ticket_price = ticket_price

    def book_seats(self, num_seats):
        if num_seats > self.available_seats:
            return False, "Not enough seats available!"
        self.available_seats -= num_seats
        total_cost = num_seats * self.ticket_price
        return True, total_cost


class TicketBookingSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, name, seats, price):
        movie = Movie(name, seats, price)
        self.movies.append(movie)

    def display_movies(self):
        print("\nAvailable Movies:")
        for idx, movie in enumerate(self.movies, 1):
            print(f"{idx}. {movie.name} - Seats: {movie.available_seats}, Price: ${movie.ticket_price}")

    def book_ticket(self):
        self.display_movies()
        try:
            choice = int(input("\nEnter the movie number you want to book: ")) - 1
            if choice < 0 or choice >= len(self.movies):
                print("Invalid movie selection!")
                return

            movie = self.movies[choice]
            num_seats = int(input(f"Enter the number of tickets for {movie.name}: "))
            success, result = movie.book_seats(num_seats)

            if success:
                print(f"Booking successful! Total cost: ${result}")
            else:
                print(result)
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    def run(self):
        while True:
            print("\n--- Movie Ticket Booking System ---")
            print("1. View Movies")
            print("2. Book Tickets")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_movies()
            elif choice == "2":
                self.book_ticket()
            elif choice == "3":
                print("Thank you for using the system. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")


# Main Execution
if __name__ == "__main__":
    system = TicketBookingSystem()
    # Add sample movies
    system.add_movie("Avengers", 10, 12)
    system.add_movie("Inception", 8, 10)
    system.add_movie("Interstellar", 5, 15)
    system.run()
