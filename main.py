import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# We need the user's deposit and the user's bet
# The user needs to enter a deposit amount until they enter a VALID amount (if they give -ve or something then no)

def deposit():
    while True:
        amount = input("Please enter the amount you'd like to deposit: $")
        if amount.isdigit():
            amount = int(amount)  # If string is only digits, we convert the input to an int
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Amount must be a number!")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Please enter the number of lines you'd like to bet on (1 - " + str(MAX_LINES) + " ): ")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines >= 1:
                break
            else:
                print("Please enter a number between 1 and 3")
        else:
            print("Amount must be a number!")

    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? (" + str(MIN_BET) + " - " + str(MAX_BET) + "): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter value between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a number")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print(f"You cannot bet more than your balance. Your current balance is ${balance}")

    print(f"You are betting ${bet} on ${lines} lines. Total bet: ${total_bet}")


main()