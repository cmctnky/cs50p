

# 1. camelCase

text = input("camelCase: ").replace(" ","")
print("snake_case: ", end="")
for i in text:
    if i.isupper():
        print("_",end="")
    print(i.lower(), end="")



# 2. Coke Machine

amount = 50
while True:
    print("Amount Due: ", amount)
    inserted = int(input("Insert Coin: "))
    if inserted not in [25, 10, 5]:
        continue
    else:
        amount -= inserted

    if amount <= 0:
        print("Change Owed: ", abs(amount))
        break


# 3. Just setting up my twttr
vowels = "aeiou"

text = input("Input: ")
print("Output: ", end="")
for i in text:
    if i not in vowels:
        print(i, end="")



# 4. Vanity Plates
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    punctuation = "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
    numerical_state = False
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            i = 0
            while i < len(s):
                if s[i] not in punctuation:
                    if i>1:
                        if s[i].isalpha() == False:
                            if not numerical_state and s[i] == "0":
                                return False
                            else:
                                numerical_state = True
                        else:
                            if numerical_state:
                                return False
                    i += 1
                else:
                    return False
        else:
            return False
    else:
        return False
    return True

main()

# 5. Nutrition Facts
cal_lookup = {
    "apple" : "130",
    "avocado" : "50",
    "banana" : "110",
    "cantaloupe" : "50",
    "grapefruit" : "60",
    "grapes" : "90",
    "honeydew melon" : "50",
    "kiwifruit" : "90",
    "lemon" : "15",
    "lime" : "20",
    "nectarine" : "60",
    "orange" : "80",
    "peach" : "60",
    "pear" : "100",
    "pineapple" : "50",
    "plums" : "70",
    "strawberries" : "50",
    "sweet cherries" : "100",
    "tangerine" : "50",
    "watermelon" : "80",
}

fruit = input("Item: ").lower()
if fruit in cal_lookup:
    print("Calories: ", cal_lookup[fruit])



