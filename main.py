from library_clients.library import Library, Book, Client


def main():
    # operation = input("Enter the operation you would like to perform (add,subtract, multiply, divide, square_root, power): ")
    # num1 = int(input("Enter the first number : "))
    # num2 = int(input("Enter the second number : "))
    # print(calculate(operation, num1, num2))
    library = Library()
    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    library.add_book(book1)
    book2 = Book("Pride and Prejudice", "Jane Austen")
    library.add_book(book2)
    client1 = Client("John Doe")
    client1.check_out_book(library, "To Kill a Mockingbird")
    client1.check_out_book(library, "Pride and Prejudice")
    client2 = Client("Jane Doe")
    client2.check_out_book(library, "To Kill a Mockingbird")
    client1.check_in_book(library, "To Kill a Mockingbird")


if __name__ == '__main__':
    main()
