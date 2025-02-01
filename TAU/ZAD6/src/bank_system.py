import asyncio
from unittest.mock import AsyncMock


class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self.balance -= amount

    async def transfer(self, to_account, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for transfer")
        await asyncio.sleep(0.1)  # Symulacja opóźnienia w transakcji
        self.balance -= amount
        to_account.balance += amount


async def process_transaction(transaction_func):
    return await transaction_func()


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number: str, owner: str, initial_balance: float):
        if account_number in self.accounts:
            raise ValueError("Account number already exists")
        self.accounts[account_number] = Account(account_number, owner, initial_balance)

    def get_account(self, account_number: str):
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_number]
