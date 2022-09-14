print("Hello stranger! What's your name?")
name = input()
print(name + " Welcome to the fire program!")

print("Do you want to see the magic?!")
symbol = input()
print("Ok, let's go!")
print(" ")

n = 50
for i in range(1,n+1):
    if i <= n//2+1:
        for j in range(i):
            print('*',end='')
    elif i >n//2+1:
        for j in range(n//2,0,-1):
            print('*',end='')
    print()