class Bank:
    bank_name = "islamic bank" # classs variable

    @classmethod
    def change_bank_name(cls, name): #method to chnage name
        cls.bank_name = name  # changing the name

if __name__ == "__main__":
    user1 = Bank()
    user2 = Bank()

    print("before changing bank name:")
    print(f"user1's bank name: {user1.bank_name}")
    print(f"user2's bank name: {user2.bank_name}")

    Bank.change_bank_name("world islamic bank")

    print("\nAfter channging name")
    print(f"user1's bank name: {user1.bank_name}")
    print(f"user2's bank name: {user2.bank_name}")