import random
import time
import sys


def spin_animation():
    symbols = ['🔴', '⚫', '🔴', '⚫', '🔴', '⚫', '🔴', '⚫', '🟢']
    for _ in range(10):
        sys.stdout.write("\r" + " ".join(random.choices(symbols, k=5)))
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\n")


def spin_wheel():
    number = random.randint(0, 36)
    color = "🔴" if number % 2 == 1 else "⚫"
    if number == 0:
        color = "🟢"
    return number, color

def bet_type_display():
    print("\n")
    print("********R*O*U*L*E*T*T*E********")
    print("_______________________________")
    print("Select A Betting Option Below And Input the Number For The Selection:")
    print("(1): Bet on individual number from 0-36 (36x your bet)")
    print("(2): Bet on the marble landing on an odd or even number (2x your bet)")
    print("(3): Bet on the marble landing on a red or black square (2x your bet)")
    print("_______________________________")


def main():
    balance = 100
    print("Welcome to Terminal Roulette! You start with $100.")
    bet_type = 0;
    bet_choice = 0;
    bet_payout = 0;

    while balance > 0:
        print(f"Your balance: ${balance}")
        while True:
            bet_type_display()
            user_input = input("Enter choice: ").strip().lower()

            try:
                bet_type = int(user_input)
                if (bet_type>=1 and bet_type<=3):
                    break
                else:
                    print("Input does not match an option.")
                    continue

            except ValueError:
                print("The input is not an integer.")
                continue

        if bet_type == 1:
            while True:
                user_input = input("Chose the number you are betting on (enter number 0-36): ").strip().lower()

                try:
                    bet_choice = int(user_input)
                    if (bet_choice >= 0 and bet_choice <= 36):
                        break
                    else:
                        print("Input does not match an option.")
                        continue
                except ValueError:
                    print("The input is not an integer.")
                    continue
            bet_payout = 35
        elif bet_type == 2:
            while True:
                user_input = input("Chose red or black (enter 1 for red and 2 for black): ").strip().lower()
                try:
                    bet_choice = int(user_input)
                    if (bet_choice >= 1 and bet_choice <= 2):
                        break
                    else:
                        print("Input does not match an option.")
                        continue

                except ValueError:
                    print("The input is not an integer.")
                    continue
            bet_payout = 2
        elif bet_type == 3:
            while True:
                user_input = input("Chose odd or even (enter 1 for odd and 2 for even): ").strip().lower()
                try:
                    bet_choice = int(user_input)
                    if (bet_choice >= 1 and bet_choice <= 2):
                        break
                    else:
                        print("Input does not match an option.")
                        continue

                except ValueError:
                    print("The input is not an integer.")
                    continue
            bet_payout = 2
        else:
            print("Invalid bet type! Try again.")
            continue

        while True:
            user_input = input("Enter your bet amount(integer): ").strip().lower()
            try:
                bet_amount = int(user_input)
                if (bet_amount >= 0 and bet_amount <= balance):
                    break
                else:
                    print("Minimum bet is $1 and cannot exceed balance.")
                    continue

            except ValueError:
                print("The input is not an integer.")
                continue

        balance -= bet_amount
        print(f"Your balance: ${balance}")

        print("Spinning the wheel...")
        spin_animation()
        number, color = spin_wheel()
        print(f"The wheel landed on {color} {number}!")

        if (bet_type == 1):
            if number == bet_choice:
                print("You WON!!!")
                print(f"Your winnings: ${bet_amount*bet_payout}")
                balance = balance + (bet_amount*bet_payout);
                print(f"Your balance: ${balance}")
            else:
                print("You lost!")
                print(f"Your balance: ${balance}")

        if (bet_type == 2):
            if color == '🔴' and bet_choice==1:
                print("You WON!!!")
                print(f"Your winnings: ${bet_amount*bet_payout}")
                balance = balance + (bet_amount*bet_payout);
                print(f"Your balance: ${balance}")
            else:
                print("You lost!")
                print(f"Your balance: ${balance}")

        if (bet_type == 3):
            if number%2 == bet_choice%2:
                print("You WON!!!")
                print(f"Your winnings: ${bet_amount*bet_payout}")
                balance = balance + (bet_amount*bet_payout);
                print(f"Your balance: ${balance}")
            else:
                print("You lost!")
                print(f"Your balance: ${balance}")




        if balance == 0:
            print("You're out of money! Game over!")
            break

        if input("Play again? (y/n): ").strip().lower() != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
