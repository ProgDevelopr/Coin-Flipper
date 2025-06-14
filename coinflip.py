import random as rn
import time as tm
try:
    print("""
     ____ _   ______  _______     __
    |  _ | | | |  _ || ____| |   | |
    | |_) | V || | | |  _|  | | | |
    |  __| | | | |_| | |___  | V | 
    |_|    |_| |____||_____|  |_|  
    """)
except SyntaxWarning:
    print("")
print("Made by PyDev \nCTRL + C to exit!")
wins = 0
losses = 0
global tries
tries = 10

while True:
    try:
        choices = [["Heads","h","heads","H"],["Tails","T","tails","t"]]
        choice = rn.choice(choices)
        guess = input("Heads or tails?: ")
        if guess in choice and guess in ["Heads","h","heads","H"]:
            print("It was...\n")
            tm.sleep(2)
            print(f"Heads! You nailed it!")
            wins += 1
            tries -= 1
            print(f"Tries left: {tries}")
        elif guess in choice and guess in ["Tails","T","tails","t"]:
            print("It was...\n")
            tm.sleep(2)
            print(f"Tails! Amazing some might say!")
            wins += 1
            tries -= 1
            print(f"Tries left: {tries}")
        elif guess!=choice:
            print("It was...\n")
            tm.sleep(2)
            print(f"Oof! You got it next time...")
            losses += 1
            tries -=1
            print(f"Tries left: {tries}")
        if tries==0:
            print("Finish! \n ")
            print(f"Wins: {wins}\nLosses: {losses}")
            if wins in [0,1]:
                print("Coin used emotinal damage!")
                break
            elif wins in [2,3]:
                print("i | Task failed success+fully")
                break
            elif wins in [4,5]:
                print("Not bad i say, not bad!")
                break
            elif wins in [6,7]:
                print("You got this far, but how!?")
                break
            elif wins in [8,9]:
                print("How long have you been playing!?")
            elif wins in [10]:
                print("Your adventure makes you discover amazing new worlds!")
                break

    except:
        break
