import fileinput
import sys


greeting = ("Hello, I am your AI NPC! How may I help you...? ;):")
smile_face = ("ƪ(˘⌣˘)ʃ")
intro_0 = ("Press 'S' to continue...:")
intro_1 = ("Choose an option (1-3:")

""""1.) CALCULATE COMPOUND INTEREST
    2.) SOLVE FOR BALANCE"""

PRINCIPLE = 0
RATE = 0
TIME = 0

print(smile_face)

              #Compound Interest
            # | A = P(1+ʳ⁄ₙ)ᵗ |

user_input = int(input(6))

print(greeting),

if user_input ("S"):
    print(intro_0)

while PRINCIPLE <= 0:
    PRINCIPLE = float(input("Enter the principle amount: "))
    if PRINCIPLE <= 0:
        print("Oh NO! Principle can't be less than or equal to zero!:")
while RATE <= 0:
    rate = float(input("Enter the principle amount: "))
    if rate <= 0:
        print("Principle can't be less than or equal to zero:")
while TIME <= 0:
    TIME = int(input("Enter the time in years: "))
    if TIME <= 0:
            print("Time can't be less than or equal to '0'.:")

print(PRINCIPLE)
print(RATE)
print(TIME)

total = PRINCIPLE * (pow((1 + rate / 100), time))
print(f"Balance after {TIME} year/s: ${total:.2f}")


toal = PRINCIPLE * pow((1 + RATE/ 100), TIME)

print(f"Balance")
