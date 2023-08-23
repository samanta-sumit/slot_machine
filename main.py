import random

MAX_LINES=3
MAX_BET=500
MIN_BET=1

ROW=3
COLM=3

symbol_count = {
   "A": 8,
   "B": 5,
   "C": 9,
   "D": 7,
}
symbol_value = {
   "A": 8,
   "B": 5,
   "C": 9,
   "D": 7,
}

def check_winnings(columns, lines, bet , values):
   winnings=0
   winnings_lines=[]
   for line in range(lines):
      symbol = columns[0][line]
      for column in columns:
         symbol_to_check = columns[lines]
         if symbol != symbol_to_check:
            break
         else:
            winnings += values[symbol]* bet
            winnings_lines.append(lines + 1)
   return winnings,winnings_lines         


def deposit():
    while True:
        amount = input("enter your deposit  ")
        if amount.isdigit():
            amount =  int(amount)
            if amount > 0:
             break
            else:
             print("amount should be greater then 0.")
        else:
         print("plz enter a no. ")
    return amount

def no_of_lines():
    while True:
        lines = input("enter no. of lines u want to bet on(1- "+ str(MAX_LINES) +") ")
        if lines.isdigit():
            lines =  int(lines)
            if 1<=lines<=MAX_LINES:
             break
            else:
             print("amount should be (1- "+ str(MAX_LINES) +").")
        else:
         print("plz enter a no. ")
    return lines                         


def get_slot_machine(rows,colms,symbols):
    all_symbols= []
    for symbol, symbol_count in symbols.items(): 
       for _ in range(symbol_count):
          all_symbols.append(symbol)  


    columns=[]
    for _ in range(colms):   
           column = []
           current_symbol = all_symbols[:]
           for _ in range(rows):
              value = random.choice(current_symbol)
              current_symbol.remove(value)
              column.append(value)
           columns.append(column)   

    return columns

def print_slot_machine(columns):
   for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
               print(column[row], end="")
        print()     


def get_bet():
    while True:
        amount = input("enter your bet  ")
        if amount.isdigit():
            amount =  int(amount)
            if MIN_BET <= amount <= MAX_BET :
             break
            else:
             print(f"amount should be between {MAX_BET} - {MIN_BET}.")
        else:
         print("plz enter a no. ")
    return amount

def spin(balance):
   
   lines = no_of_lines()
   while True:
            bet = get_bet()
            total_bet = bet * lines
            if  total_bet > balance:
             print(f"your  have insufficiant balance, current balance is {balance} ") 
             break
            else:
             print(f"your betting a amount of ${bet} on {lines} number of lines. total amount is {total_bet} ")
             break
     
   slots = get_slot_machine(ROW, COLM, symbol_count)
   print_slot_machine(slots) 
   winning,winnings_lines=check_winnings(slots,bet,lines,symbol_value)   
   print(f"you won ${winning}")
   print("you won on lines"*winnings_lines)    
   return winning - total_bet

def main():
        
        balance = deposit()
        while True:
           print(f"current balance is {balance}")
           answer = input("press enter if continue or q to exit ")
           if answer == "q":
               break
           balance += spin(balance)

        print(f"you left with {balance}")


       
main()