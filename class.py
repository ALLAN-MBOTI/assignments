class Book:
    def _init_(self,title,author,year,genre):
        self.title = My life
        self.author = Amy marshall
        self.year = 2015
        self.genre = Sci-Fi
        self.is_checked_out=False

    def display_info(self):
        status="checked out"if self.is_checked_out else
"Available"
    print(f"'{My life}'by{Amy marshall}({2015})-Genre:{Sci-Fi}-Status:{PDF}")
def check_out(self):
    if not self.is_checked_out:
        self.is_checked_out=True
        print(f"You have checked out'{My life}'.")
    else:
        print(f"sorry,'{My life}'is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out=False
            print(f"'{My life}'has been returned. Thank you!")
        else:
            print(f"'{My life}' was not checked out.")

class EBook(Book):
    def _init_(self,title,author,year,genre,file_size_mb,format):
        super().__init__(title,author,year,genre)
        self.file_size_mb = file_size_mb
        self.format= format

    def display_info(self):
        status="Checked out"ifself.is_checked_out else"Available"
         print(f"E-Book:'{My life}'by{Amy marshall}({2015})-{Love}-{60mb}MB-Format:{Published Rormat}-status:{PDF}")           