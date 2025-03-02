def withdraw_money(amount):
    current_balance = 1000

    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance # returning a value from a function

balance = withdraw_money(80)

if (balance <= 50):
    print('You need to make a deposit.')
else:
    print('Your current balance is: ', balance)