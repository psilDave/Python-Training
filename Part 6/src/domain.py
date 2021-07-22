from src.exceptions import InvalidBid


class User:
    def __init__(self, name, wallet):
        self.__name = name
        self.__wallet = wallet

    @property
    def name(self):
        return self.__name

    @property
    def wallet(self):
        return self.__wallet

    def _user_have_not_balance_to_bid(self, value):
        return value > self.__wallet

    def propose_bid(self, auction: "Expect a Auction's instance'", value):
        if self._user_have_not_balance_to_bid(value):
            raise InvalidBid("The user doesn't have enough balance to make this bid.")
        bid = Bid(self, value)
        auction.propose_a_bid(bid)
        self.__wallet -= value


class Bid:

    def __init__(self, user, value):
        self.user = user
        self.value = value


class Auction:

    def __init__(self, description):
        self.description = description
        self.__bids = []
        self.highest_bid = 0.0
        self.lowest_bid = 0.0

    @property
    def bids(self):
        return self.__bids[:]

    def _have_bids(self):
        return self.__bids

    def _different_users(self, bid: "Expect a Bid's instance"):
        if self.__bids[-1].user != bid.user:
            return True
        raise InvalidBid("The user cannot make two consecutive bids.")

    def _actual_bid_is_bigger_than_old_bid(self, bid: "Expect a Bid's instance"):
        if bid.value > self.__bids[-1].value:
            return True
        raise InvalidBid("The bid's value must be bigger than old bid.")

    def _bid_is_valid(self, bid: "Expect a Bid's instance"):
        return not self._have_bids() or self._different_users(bid) and self._actual_bid_is_bigger_than_old_bid(bid)

    def propose_a_bid(self, bid: "Expect a Bid's instance"):
        if self._bid_is_valid(bid):
            if not self._have_bids():
                self.lowest_bid = bid.value
            self.highest_bid = bid.value
            self.__bids.append(bid)

