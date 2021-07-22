from src.domain import User, Auction
import pytest
from src.exceptions import InvalidBid


@pytest.fixture()
def vini():
    return User("Vini", 100.0)


@pytest.fixture()
def auction():
    return Auction("Celular")


def test_should_the_subtract_the_value_user_wallet_when_user_propose_a_bid(vini, auction):
    vini.propose_bid(auction, 50.0)
    assert vini.wallet == 50.0


def test_should_allow_bid_when_the_value_bid_is_less_than_value_wallet(vini, auction):
    vini.propose_bid(auction, 1.0)

    assert vini.wallet == 99.0


def test_should_allow_bid_when_the_value_bid_is_equal_than_value_wallet(vini, auction):
    vini.propose_bid(auction, 100.0)

    assert vini.wallet == 0.0


def test_should_not_allow_bid_when_the_value_bid_is_bigger_than_value_wallet(vini, auction):
    with pytest.raises(InvalidBid):
        vini.propose_bid(auction, 200.0)
