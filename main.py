# Write your code below this line 👇
print("Hello, Taha!")
# Check the number of Charcters in an input
string=input("\nEnter a string: ")
number=len(string)
print(f"\n'{string}' has {number} characters")
# Check if the number is odd or even
string=input("\nEnter the number you wish to check: ")

number=int(string)

if number%2==0:
    print(f"The number {number} is even!")
else:
    print(f"The number {number} is odd!")