# TASK - 1
name = input("Enter your name: ")
num = int(input("Enter a number: "))

# Even or Odd
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# For Loop
print("Numbers from 1 to", num)
for i in range(1, num + 1):
    print(i)

# While Loop
print("Countdown:")
i = num
while i >= 1:
    print(i)
    i = i - 1

# Thank you message
print("Thank you", name + "!")