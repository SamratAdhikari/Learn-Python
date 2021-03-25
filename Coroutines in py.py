# Coroutines - Word Search

def searcher():
    import time
    # Some 4 sec time consuming task
    book = "This is a book. I am Samrat. I want Megan Fox."
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")


search = searcher()
next(search)
search.send("Samrat")
input("enter")
search.send("Samrat. I")
search.close()
