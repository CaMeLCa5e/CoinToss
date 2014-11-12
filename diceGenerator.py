import random

def rollDie(number):
    rolls = [0] * 6
    for i in range(0, number):
        roll=int(random.randint(1,6))
        rolls[roll - 1] += 1
    return rolls

if __name__ == "__main__":
    result = rollDie(1000)
    print(result)