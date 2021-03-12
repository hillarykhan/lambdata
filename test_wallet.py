import pytest
from lambdata.wallet import Wallet

@pytest.fixture
def empty_wallet():
    """Returns a wallet instance with a zero balance"""
    return Wallet()

@pytest.fixture
def wallet():
    """Returns wallet of balance 20"""
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    # wallet = Wallet()
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    # wallet = Wallet(20)
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    # wallet = Wallet(20)
    wallet.add_cash(100)
    assert wallet.balance == 120


def test_wallet_spend_cash(wallet):
    # wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10
