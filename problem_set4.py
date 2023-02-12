# 1. Emojize
import emoji

text = input("Input: ")
print(emoji.emojize(text, language="alias"))


# 2. Frank, Ian and Glen's Letters



# 3. Adieu, Adieu


arr = []
while True:
    try:
        name = input("Name: ")
        arr.append(name)
    except KeyboardInterrupt:
        print("Adieu, adieu, to ", end="")
        i = 0
        while i < len(arr):
            if i==0:
                print(arr[i],end="")
            elif i == len(arr)-1:
                print(" and ",arr[i], end="")
            else:
                print(",",arr[i], end="")
            i += 1
        break


# 4. Guessing Game

import random 

def is_valid(arg):
    try:
        if int(arg) and int(arg)>0:
            return True
    except Exception:
        return False

while True:
    level = input("Level: ")
    if is_valid(level):
        rand = random.randint(1, int(level))
        while True:
            guess = input("Guess: ")
            if is_valid(guess):
                if int(guess) > rand:
                    print("Too large!") 
                elif int(guess) < rand:
                    print("Too small!")
                else:
                    print("Just right")
                    break
            pass
        break
    pass




# 5. Little Professor

import random 

def is_valid(arg):
    try:
        if int(arg) and int(arg)>0:
            return True
    except (Exception, ValueError):
        return False

def get_level():
    while True:
        level = input("Level: ")
        if is_valid(level) and int(level) in [1,2,3]:
            break
        else:
            pass
    return int(level)

def generate_integer(level):
    if level==1:
        x = random.randint(1,9)
        y = random.randint(1,9)
    elif level==2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x, y

def main():
    i = 0
    score = 10

    while True:
        level = get_level()
        if is_valid(level):
            break
        pass
    
    while i < 10: 
        x, y = generate_integer(level)
        score_state=False
        while True:
            msg = str(x)+"+"+str(y)+"= "
            z = input(msg)
            if is_valid(z):
                if int(z) == x+y:
                    break
                else:
                    print("EEE")
                    if not score_state:
                        score -= 1
                        score_state=True
                    pass
            else:
                print("EEE")
                if not score_state:
                    score -= 1
                    score_state=True
                pass
        i += 1
    print("Score: ", score)

if __name__ == "__main__":
    main()



# 6. Bitcoin Price Index
import requests, sys

if len(sys.argv) != 2:
    sys.exit("Missing command line arg")
else:
    requests = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Must be a number")
    price = float(requests.json()["bpi"]["USD"]["rate"].replace(",","")) * float(sys.argv[1])

    print(f"${float(price):,.4f}")
    



