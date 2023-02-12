


# 1. Fuel Gauge
while True: 
    fraction = input("Fraction: ")
    try: 
        x = int(fraction.split("/")[0])
        y = int(fraction.split("/")[1])
        z = x / y
        
        if z <= 1:
            break
    except(Exception, ValueError, ZeroDivisionError):
        pass
if z*100 <= 1:
    print("E")
elif z*100 >=99:
    print("F")
else:
    print(f"{z*100}%")



#2. Felipe's Taqueria
menu_lookup = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    try:
        food = input("Item: ").title()
    except KeyboardInterrupt:
        print("Total: $", f"{total:.2f}")
        break
    if food in menu_lookup:
        total += menu_lookup[food]
        print("Total: $", f"{total:.2f}")



# 3. Grocery List
grocery_list = {}
while True: 
    try: 
        item = input()
        if item not in grocery_list:
            grocery_list[item] = 0
        grocery_list[item] += 1
    except KeyboardInterrupt:
        for i in sorted(grocery_list):
            print(grocery_list[i]," ",i.upper())
        break



# 4. Outdated
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        if len(date.split("/"))==3:
            if not (1 <= int(date.split("/")[0]) <= 12 and 1 <= int(date.split("/")[1]) <= 31):
                pass
            else:
                print(date.split("/")[2],"-",date.split("/")[0].zfill(2),"-",date.split("/")[1].zfill(2))
                break
        if date.find(",") != -1:
            if date.split(",")[0].split(" ")[0].title() in months:
                if not (1 <= int(date.split(",")[0].split(" ")[1]) <= 31):
                    pass
                else:
                    print(date.split(",")[1], "-", str(months.index(date.split(",")[0].split(" ")[0].title())+1).zfill(2) ,"-",date.split(",")[0].split(" ")[1].zfill(2))
                    break
            else:
                pass
    except Exception:
        print("error")
        pass


























