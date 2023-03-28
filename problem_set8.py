
# Seasons of Love
from datetime import date
import re

def main():
    date = input("Date of birth: ")
    try:
        year, month, day = check_birthday(date)
        day_diff = date.today() - date(int(year), int(month), int(day))
        minute_diff = day_diff*24*60
        #inflect ile rakamlar yazıya dökülebilir
    except:
        print("Invalid Date")
def check_birthday(par):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", par):
        a, b, c = par.split("-")
        return a, b, c
    
if __name__=="__main__":
    main()

# Cookie Jar

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity error")
        self.capacity_ = capacity
        self.size_ = 0
    

    def __str__(self):
        return self.size_ * '🍪'
    

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("capacity limit")
        if self.size_ + n > self.capacity_:
            raise ValueError("capacity limit")
        self.size_ += n
        
    def withdraw(self, n):
        if self.size_ < n:
            raise ValueError("not enough cookies")
        self.size_ -= n

    @property
    def capacity(self):
        return self.capacity_
    
    @property
    def size(self):
        return self.size_

jar = Jar()
jar.deposit(2)
jar.withdraw(123)

print(jar)

