# 1. Deep Thought
text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
text = text.replace(" ","")
if text=="42" or text.lower()=="forty-two" or text.lower()=="fortytwo":
    print("Yes")
else:
    print("No")


# 2. Home Federal Savings Bank
text = input("Greeting: ")

if text.lower()[0:5]=="hello":
    print("$0.00")
else:
    if text.lower()[0]=="h":
        print("$20.00")
    else:
        print("$100.00")


# 3.1. File Extensions - Split Function
def mime_type(arg):
    if arg.find(".") != -1:
        arg = arg.lower().split(".")[1]
        if arg == "jpg" or arg=="jpeg":
            print("image/jpeg")
        elif arg=="gif":
            print("image/gif")
        elif arg=="png":
            print("image/png")
        elif arg=="txt":
            print("text/plain")
        elif arg=="pdf":
            print("application/pdf")
        elif arg=="zip":
            print("application/zip")
        else:
            print("application/octet-stream")
    else:
        print("application/octet-stream")

filename = "happy.jpg"
mime_type(filename)


# 3.2. File Extensions - Endswith Function
filename = "happy.jpg"

if filename.endswith(".jpg") or filename.endswith(".jpeg"):
    print("image/jpeg")
elif filename.endswith(".png"):
    print("image/png")
elif filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith("txt"):
    print("text/plain")
elif filename.endswith("pdf"):
    print("application/pdf")
elif filename.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")

# 3.3. File Extensions - Dict Lookup Table

lookup = {
    "jpg" : "image/jpeg",
    "jpeg": "image/jpeg",
    "png" : "image/png",
    "gif" : "image/gif",
    "txt" : "plain/text",
    "pdf" : "application/pdf",
    "zip" : "application/zip"
}
def mime_type(arg):
    try:
        print(lookup[filename.split(".")[1]])
    except:
        print("application/octet-stream")

filename = "happy.jpg"
mime_type(filename)



# 4. Math Interpreter - Spaghetti

math = input("Expression: ")

if math.find("+") != -1: 
    print(float(math.split("+")[0]) + float(math.split("+")[1]))
elif math.find("-") != -1:
    print(float(math.split("-")[0]) - float(math.split("-")[1]))
elif math.find("*") != -1:
    print(float(math.split("*")[0]) * float(math.split("*")[1]))
elif math.find("/") != -1:
    print(float(math.split("/")[0]) / float(math.split("/")[1]))
else:
    print("Not a valid math expression")


# 5. Meal Time

def main():
    time = convert(input("What time it is? "))
    if 7.00 <= time <= 8.00: 
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")    

def convert(time):
    try:
        return float(time.split(":")[0]) + (float(time.split(":")[1])/60)
    except:
        print("Time format must be xx:yy")

if __name__ == "__main__":
    main()


