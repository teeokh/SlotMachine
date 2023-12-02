import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {  # Here we make a dictionary. The letters are the keys, the numbers are the values / how many times
    # in each col it shows
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8

}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def get_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]  # We check that the first symbol in the row is same as the others
        #  Since columns is a nested list, we access the first column using [0] then the
        #  index [line] in that column. So we end up grabbing the first symbol of each column

        for column in columns:  # Checks each symbol in one row/line, if they are not the same then breaks + no win
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # This will add the line number to the list of winning lines

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():  # Creates symbol_count as a local variable referencing the value
        for _ in range(symbol_count):  # For A, symbol count is 2, so we add symbol 2 times (range = 2)
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):  # This generates the number of times we need to make a column based on cols (3)
        column = []
        current_symbols = all_symbols[:]  # We copy the list so that we're not removing values from the actual list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)  # Removes whatever value is generated (the symbol) from the copied list
            column.append(value)  # Adds the value that is chosen to the column

        columns.append(column)  # We then add the current column to the columns list

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):  # Columns is nested list, so first item will be the first singular column
        for i, column in enumerate(columns):  # Enumerate will give the index + the value, that's why we include `i`
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # end tells program what to end the line with
            else:
                print(column[row], end="")  # This means that we only put divider if we're not at last row of column

        print()  # Then at the end of the row, we can print the new line using default print


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


def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print(f"You cannot bet more than your balance. Your current balance is ${balance}")

    print(f"You are betting ${bet} on ${lines} lines. Total bet: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = get_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings} from lines: ", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play. (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)


main()
