
print("Hello world and welcome to the game FizBuz")
print()

x = 40
for i in range (1,x+1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i = i + 1
print("Game finished")