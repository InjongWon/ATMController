import sys

class Bank:
    def __init__(self):
        self.bank_data = {}

    def add_entry(self, card_num, pin, acc_id, amount):
        self.bank_data[card_num] = {"pin":pin, "account":{acc_id:amount}}

    def add_account(self, card_num, account, amount):
        if card_num in self.bank_data:
            self.bank_data[card_num]["account"][account] = amount

    def check_pin(self, card_num, entered_pin):
        if card_num in self.bank_data and self.bank_data[card_num]["pin"] == entered_pin:
            return self.bank_data[card_num]["account"]
        else:
            return None

    def update_account(self, card_num, account, amount):
        if self.bank_data[card_num]["account"][account] in self.bank_data[card_num]["account"]:
            self.bank_data[card_num]["account"][account] = amount
            return True
        else:
            return False


class Controller:
    def __init__(self, bank, cash):
        self.Bank = bank
        self.accounts = None
        self.cash_bin = cash

    def account_select(self, acc):
        if acc in self.accounts:
            return True
        else:
            return False
        
    def insert(self, card_num, pin):
        self.accounts = self.Bank.check_pin(card_num, pin)
        if self.accounts is None:
            return 0, "Invalid Card or Incorrect Pin!"
        else:
            return 1, "Welcome!"

    def account_actions(self, card_num, acc, action, amount=0):
        if action == "See Balance":
            return self.accounts[acc], 1
        elif action == "Withdraw":
            if self.accounts[acc] >= amount and self.cash_bin >= amount:
                new_balance = self.accounts[acc] - amount
                self.accounts[acc] = new_balance
                self.Bank.update_account(card_num, acc, new_balance)
                return self.accounts[acc], 1
            else:
                return self.accounts[acc], 0
        elif action == "Deposit":
            new_balance = self.accounts[acc] + amount
            self.cash_bin += amount
            self.accounts[acc] = new_balance
            self.Bank.update_account(card_num, acc, new_balance)
            return self.accounts[acc], 1
        else:
            return self.accounts[acc], 2


if __name__ == "__main__":
    empty_bank = Bank()
    # Test Controller on Empty Bank
    empty_atm = Controller(empty_bank, 0)
    valid, message = empty_atm.insert(0, 0)
    if valid == 0:
        print("Test Invalid Message on Empty ATM -- PASS")
    else:
        print("Test Invalid Message on Empty ATM -- FAIL")

    test_bank = Bank()
    test_bank.add_entry(123456789, 1234, "checking", 1000)
    test_bank.add_account(123456789, "savings", 1000)
    test_bank.add_entry(987654321, 7321, "checking", 5000)
    test_atm = Controller(test_bank, 10000)
    action_list1 = [("See Balance",0), ("Withdraw", 50), ("Withdraw", 1000), ("Deposit", 100)]

    if test_atm(123456789, 1234, "checking", action_list1) == "Actions completed":
        print("Test Overdraft handling -- PASS")
    else:
        print("Test Overdraft handling -- FAIL")

    # Test incorrect PIN number
    if test_atm(987654321, 1234, "checking", action_list1) == "Invalid Card or Incorrect Pin!":
        print("Test Incorrect Pin Number -- PASS")
    else:
        print("Test Incorrect Pin Number -- FAIL")

    # Test incorrect Account number
    if test_atm(876504321, 1234, "checking", action_list1) == "Invalid Card or Incorrect Pin!":
        print("Test Incorrect Acc Number -- PASS")
    else:
        print("Test Incorrect Acc Number -- FAIL")



  
