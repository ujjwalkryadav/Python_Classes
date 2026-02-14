# ============================================================
# Encapsulation in Python
# Demonstration using Public, Protected, and Private members
# Real-life analogy: Medicine Capsule (data hidden & controlled)
# ============================================================


class Shivam:
    # ---------------- PUBLIC DATA ----------------
    # Public members can be accessed from anywhere
    shivam_bank_name = "SBI"
    shivam_account_type = "Salary Account"

    # ---------------- PROTECTED DATA ----------------
    # Protected members (single underscore)
    # Should be accessed inside class or child class
    _shivam_account_no = 78979379

    # ---------------- PRIVATE DATA ----------------
    # Private members (double underscore)
    # Highly sensitive data
    __shivam_bank_balance = 200000
    __shivam_atm_pin = 8989

    # ---------------- PUBLIC METHOD ----------------
    # This method provides controlled access to private data
    def shivam_bank_info(self):
        print("Bank Name:", self.shivam_bank_name)
        print("Account Type:", self.shivam_account_type)
        print("Account Number:", self._shivam_account_no)
        print("Bank Balance:", self.__shivam_bank_balance)

    # ---------------- PRIVATE METHOD ----------------
    # Private method (cannot be accessed directly)
    def __validate_pin(self, pin):
        return pin == self.__shivam_atm_pin

    # ---------------- PUBLIC METHOD ----------------
    # Controlled access to withdraw money
    def withdraw_money(self, pin, amount):
        if self.__validate_pin(pin):
            if amount <= self.__shivam_bank_balance:
                self.__shivam_bank_balance -= amount
                print("Withdrawal Successful")
                print("Remaining Balance:", self.__shivam_bank_balance)
            else:
                print("Insufficient Balance")
        else:
            print("Invalid ATM PIN")


# ---------------- OBJECT CREATION ----------------
shivam_obj = Shivam()

# ---------------- PUBLIC ACCESS ----------------
print(shivam_obj.shivam_bank_name)

# ---------------- PROTECTED ACCESS (Allowed but not recommended) ----------------
print(shivam_obj._shivam_account_no)

# ---------------- PRIVATE ACCESS (NOT ALLOWED) ----------------
# print(shivam_obj.__shivam_atm_pin)   # ERROR

# ---------------- CONTROLLED ACCESS USING METHOD ----------------
shivam_obj.shivam_bank_info()

# ---------------- WITHDRAW USING ENCAPSULATION ----------------
shivam_obj.withdraw_money(8989, 50000)
shivam_obj.withdraw_money(1111, 10000)