import time

name = input("Hello stranger! What's your name?\n")

print(name + " Welcome to the fire program!")

print("Do you want to see the magic?!")
input()
print("Ok, let's go!")

while True:
    n = int(input('Enter any number after 10\n'))
    if n > 10:
        break
    else:
        continue

for y in range(1, (n // 2) + 2):
    print("*" * y, end="")
    time.sleep(0.1)
    print()
for y in range(n // 2, 0, -1):
    print("*" * y, end="")
    time.sleep(0.1)
    print()
