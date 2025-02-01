import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from unittest.mock import AsyncMock, patch
from bank_system import Account, Bank, InsufficientFundsError


@pytest.fixture
def sample_account():
    return Account("12345", "John Doe", 100.0)


@pytest.fixture
def bank():
    return Bank()


def test_deposit(sample_account):
    sample_account.deposit(50.0)
    assert sample_account.balance == 150.0


def test_withdraw(sample_account):
    sample_account.withdraw(40.0)
    assert sample_account.balance == 60.0


def test_withdraw_insufficient_funds(sample_account):
    with pytest.raises(InsufficientFundsError):
        sample_account.withdraw(200.0)


@pytest.mark.asyncio
async def test_transfer():
    acc1 = Account("111", "Alice", 200.0)
    acc2 = Account("222", "Bob", 50.0)

    await acc1.transfer(acc2, 100.0)

    assert acc1.balance == 100.0
    assert acc2.balance == 150.0


@pytest.mark.asyncio
async def test_transfer_insufficient_funds():
    acc1 = Account("111", "Alice", 50.0)
    acc2 = Account("222", "Bob", 50.0)

    with pytest.raises(InsufficientFundsError):
        await acc1.transfer(acc2, 100.0)


def test_create_account(bank):
    bank.create_account("555", "Charlie", 300.0)
    assert bank.get_account("555").balance == 300.0


def test_create_duplicate_account(bank):
    bank.create_account("123", "User1", 100.0)
    with pytest.raises(ValueError):
        bank.create_account("123", "User2", 200.0)


def test_get_account(bank):
    bank.create_account("777", "Daniel", 500.0)
    account = bank.get_account("777")
    assert account.owner == "Daniel"


def test_get_account_not_found(bank):
    with pytest.raises(ValueError):
        bank.get_account("999")


@pytest.mark.asyncio
async def test_process_transaction(bank):
    async def mock_transaction():
        return "Transaction Complete"

    result = await bank.process_transaction(mock_transaction)
    assert result == "Transaction Complete"


@patch("bank_system.Account.transfer", new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_mocked_transfer(mock_transfer):
    mock_transfer.return_value = None

    acc1 = Account("111", "Alice", 500.0)
    acc2 = Account("222", "Bob", 100.0)

    await acc1.transfer(acc2, 200.0)

    mock_transfer.assert_called_once()