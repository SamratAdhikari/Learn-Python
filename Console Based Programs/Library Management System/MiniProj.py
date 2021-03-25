
# Library Management System

#To generate a secret code if the person who added the book wants to remove the book...
import random
#secret_key = ["7898", "1060", "2072", "2058", "5641"]


#To slow down the program
from time import sleep

class Library:
    def __init__(self, name_lib, book_list):
        self.name_lib = name_lib
        self.book_list = book_list
        self.lend_list = {}

        for books in self.book_list:
            self.lend_list[books] = None

    #To display all the books in the library...
    def display_books(self):
        for index, book in enumerate(self.book_list, start=1):
            print(f"{index} : {book}")

    #To lend any desired book to the client if the said book aint already lent by sb else...
    def lend_books(self, book, name):
        if book in self.book_list:
            if self.lend_list[book] is None:
                self.lend_list[book] = name
                print(f"The book {book} was successfully lent. Please return the book soon...")
            else:
                print(f"Sorry This book is lend by someone else...")

        else:
            print("No such book in the library!!!")

    #To add a book recommended by the client in case its not in the list...
    def add_book(self, book):
        #sec_gen = random.choice(secret_key)
        if book not in self.book_list:
            self.book_list.append(book)
            self.lend_list[book] = None
            print(f"The book {book} successfully added to the Library...")
            #print(f"Please use the code {sec_gen} if you wish to remove your book from the library...")
        else:
            print(f"The book with the name '{book}' is already in the library...")

    #To return lent books back to the library...
    def return_book(self, book, name):
        if book in self.lend_list and self.lend_list[book] == name :
            self.lend_list[book] = None
            print("You returned the book without any damage. Thanks for reading our books.")

        elif book not in self.lend_list or self.lend_list[book] != name:
            print(f"Sorry "
                  f"Either the book '{book}' was never lent to anyone!!!"
                  f"Or it was not lent by {name}")

    #To delete any book in the list...
    def delete_book(self, book):
        self.book_list.remove(book)
        print(f"Book {book} successfully deleted!")

def que():
    print("Type:\n"
          "\t'd' to Display all the books in the Library\n"
          "\t'a' to Add a book in the Library\n"
          "\t'l' to Lend a book from the Library\n"
          "\t'r' to Return previously lent book to the Library\n"
          "\t'del' to Remove any book from the library\n"
          "\t'q' to Exit the program")


def main():
    book_list = ["Harry Potter", "Manga", "Song of Ice and Fire"]
    name_lib = "Leaf"
    client = Library(name_lib, book_list)
    print(f"\t\t\t\t\t\tWelcome To {name_lib} Library...")
    print()

    Exit = True
    while (Exit is not False):
        que()

        ask = input("\t\tYour Input: ")
        if ask == "q":
            print("The program is exiting...")
            Exit = False
        elif ask == "d":
            print()
            client.display_books()
            sleep(4)
            print()
            print()

        elif ask == "a":
            print()
            ask_add = input("Enter the name of the book that you want to add: ")
            client.add_book(ask_add.capitalize())
            sleep(3)
            print()
            print()


        elif ask == "l":
            print()
            client.display_books()
            print()
            book = input("Enter the name of the book that you want to lend: ")
            name = input("Enter your name: ")
            client.lend_books(book, name)
            sleep(3)
            print()
            print()

        elif ask == "r":
            print()
            ask_return_book = input("Enter the name of the book that you want to return: ")
            ask_return_name = input("Enter the name of the client who lent the book: ")
            client.return_book(ask_return_book, ask_return_name)
            sleep(3)
            print()
            print()

        elif ask == "del":
            print()
            client.display_books()
            print()
            #ask_code = input("Enter the code to prove that you are the manager of the Library: ")
            #if ask_code == sec_gen:
            ask_delete_book = input("Enter the name of the book that you want to remove from the Library: ")
            if ask_delete_book in book_list:
                print(f"The book {ask_delete_book} successfully removed from the Library...")
            elif ask_delete_book not in book_list:
                print("The book is not in the Library...")
            sleep(3)
            print()
            print()

        else:
            print()
            print("Invalid Input!!!")
            sleep(1)
            print()
main()


