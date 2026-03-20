class BankAccount:
    def __init__(self, balance, accounts=None):  # creates a BankAccount object
        self.balance = balance  # stores the balance of a single account
        # internal list of accounts; if none is provided, use an empty list
        self._accounts = accounts if accounts is not None else []

    def __len__(self) -> int:
        # len(accounts_list) will call this method
        return len(self._accounts)

    def __iter__(self):
        # when you iterate over the object (for loop, sorted, etc),
        # it returns a SORTED COPY of the internal list
        return iter(sorted(self._accounts))

    @property
    def accounts(self):
        # returns a COPY of the internal list
        # so external code cannot modify the original
        return list(self._accounts)

    def sort_accounts_in_place(self):
        # sorts the INTERNAL list (changes object state)
        self._accounts.sort()

    def __gt__(self, other) -> bool:
        # defines how ">" works between two accounts
        return self.balance > other.balance

    def __lt__(self, other):
        # defines how "<" works (needed for sorting)
        return self.balance < other.balance

    def __eq__(self, other):
        # defines equality between two accounts
        return self.balance == other.balance


# ---------------- MAIN / TEST AREA ----------------

account1 = BankAccount(1500)  # first account
account2 = BankAccount(1000)  # second account

# this object acts like a container of accounts
accounts_list = BankAccount(0, [account1, account2])

# calls __len__()
print(len(accounts_list))

# calls __gt__()
print(account1 > account2)

# BEFORE sorting (copy)
print("Before sort (copy):")
print(accounts_list.accounts)

# sort INTERNAL list
accounts_list.sort_accounts_in_place()

# AFTER sorting (copy)
print("After sort (copy):")
print(accounts_list.accounts)

# ITERATION (uses __iter__)
print("Iterating (always sorted):")
for account in accounts_list:
    print(account.balance)

# USING sorted() directly
print("Using sorted():")
sorted_accounts = sorted(accounts_list)
for account in sorted_accounts:
    print(account.balance)