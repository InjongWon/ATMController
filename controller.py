class Bank:
    def __init__(self):
        self.bank_data = {}

    def add_entry(self, card_num, pin, account, amt):
        self.bank_data[card_num] = {"pin":pin, "account":{account:amt}}

    def add_account(self, card_num, account, amt):
        self.bank_data[card_num]["account"][account] = amt

    def check_pin(self, card_num, entered_pin):
        if card_num in self.bank_data and self.bank_data[card_num]["pin"] == entered_pin:
            return self.bank_data[card_num]["account"]
        else:
            return None

    def update_account(self, card_num, account, amt):
        if self.bank_data[card_num]["account"][account] in self.bank_data[card_num]["account"]:
            self.bank_data[card_num]["account"][account] = amt
            return True
        else:
            return False


class Controller:
    def __init__(self, bank, cash):
        self.Bank = bank
        self.accounts = None
        self.cash_bin = cash

    def swipe(self, card_num):
        pin = input("Enter your pin")
        self.accounts = self.Bank.check_pin(card_num, pin)
        if self.accounts is None:
            return 0, "Invalid Card or Incorrect Pin!"
        else:
            return 1, "Welcome!"

    def account_select(self):
        print("These are your accounts:")
        for key in self.accounts:
            print(key)
        acc = input("Select an account")
        if acc in self.accounts:
            return True
        else:
            return False

    def account_actions(self, card_num, acc, action):
        if action == "See Balance":
            return self.accounts[acc], 1
        elif action == "Withdraw":
            amt = input("How much to withdraw?")
            if self.accounts[acc] >= amt and self.cash_bin >= amt:
                new_balance = self.accounts[acc] - amt
                self.accounts[acc] = new_balance
                self.Bank.update_account(card_num, acc, new_balance)
                return self.accounts[acc], 1
            else:
                return self.accounts[acc], 0
        elif action == "Deposit":
            amt = input("How much to deposit?")
            new_balance = self.accounts[acc] + amt
            self.cash_bin += amt
            self.accounts[acc] = new_balance
            self.Bank.update_account(card_num, acc, new_balance)
            return self.accounts[acc], 1

