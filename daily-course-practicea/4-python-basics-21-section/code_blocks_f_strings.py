# while True:
#     password = input("Enter the password.... no exit: ")

password = ""
while "Rakesh" != password:
    password = input("Enter the correct password to crack....: ")

print("You did it :)")


#for loops

loop = ["Rakesh","Rajesh","Mahesh","Suresh"]
for lo in loop:
    print("Your data :", lo)



#Mat case
selction = input("Enter your selection -> ")
match selction:
    case "Rakesh":
        print("You selected Rakesh")
    case "Rajesh":
        print("You selected Rajesh")

    case _:
        print("Nothing matched")


#if else conditions
someInput = input("Enter some input: ")
if(someInput.startswith("R")):
    print("The given name starts with 'R'")
elif(someInput.startswith("A")):
    print("The given name starts with 'A'")
else:
    print("Entered value did not match anything")

#f-Strings

username="rakesh"
password="123456"

combination = f"Hello World  my username {username.capitalize()} and password is {password}"

print(combination)

