# Write a program to implement a class name BookStore

class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks =  BookStore.NoOfBooks + 1
    
    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {BookStore.NoOfBooks}")
    
bobj1 = BookStore("Linux System Programming","Robert Love")
bobj1.Display()

bobj2 = BookStore("C Programming","Dennis Richie")
bobj2.Display()