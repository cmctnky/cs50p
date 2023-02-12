# Problem Set 0

# 1. Indoor Voice
text = input()
print(text.lower())


# 2. Playback Speed
text = input()
print(text.replace(" ","..."))


# 3. Making Faces
text = input()
print(text.replace(":)", "🙂").replace(":(", "🙁"))

# 4. Einsten
def calculate_mcsquare(arg):
    c = 300000000
    try:
        m = int(arg)
        print("E: ", m*(pow(c,2)))
        return True
    except Exception as e:
        print("Input must be integer")
        return False

m = input("m: ")
calculate_mcsquare(m)

# 5. Tip Calculator 
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.replace("$",""))

def percent_to_float(p):
    return float("0."+p.replace("%",""))

main()