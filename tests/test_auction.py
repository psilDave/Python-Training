from unittest import TestCase
from src.domain import User, Bid, Auction
from src.exceptions import InvalidBid

class TestAuction(TestCase):

    def setUp(self):
        # Create users
        self.gui = User("Gui", 500)
        self.yuri = User("Yuri", 500)
        self.vini = User("Vini", 500)

        # Create users bid
        self.bid_yuri = Bid(self.yuri, 100)
        self.bid_gui = Bid(self.gui, 150)
        self.bid_vini = Bid(self.vini, 200)

        # Create the auction
        self.auction = Auction("Celular")

    def test_that_returns_the_highest_and_lowest_bid_did_in_ascending_order(self):

        # Test Case - 1
        self.auction.propose_a_bid(self.bid_yuri)
        self.auction.propose_a_bid(self.bid_gui)


        # Test Result - 1
        lowest_value_expected = 100
        highest_value_expected = 150
        self.assertEqual(lowest_value_expected, self.auction.lowest_bid)
        self.assertEqual(highest_value_expected, self.auction.highest_bid)

    def test_that_should_not_allow_propose_a_bid_in_descending_order(self):

        # Test Result - 2
        with self.assertRaises(InvalidBid):
            # Test Case - 2
            self.auction.propose_a_bid(self.bid_gui)
            self.auction.propose_a_bid(self.bid_yuri)


    def test_that_should_returns_the_same_value_to_variables_highest_and_lowest_bid_when_the_auction_has_only_one_bid(
            self):

        # Test Case - 3
        self.auction.propose_a_bid(self.bid_gui)

        # Test Result - 3
        self.assertEqual(150, self.auction.highest_bid)
        self.assertEqual(150, self.auction.lowest_bid)

    def test_that_returns_the_highest_and_lowest_bid_when_the_auction_has_3_bids(self):

        # Test Case - 4
        self.auction.propose_a_bid(self.bid_yuri)
        self.auction.propose_a_bid(self.bid_gui)
        self.auction.propose_a_bid(self.bid_vini)

        # Test Result - 4
        lowest_value_expected = 100
        highest_value_expected = 200
        self.assertEqual(lowest_value_expected, self.auction.lowest_bid)
        self.assertEqual(highest_value_expected, self.auction.highest_bid)

    def test_that_should_allow_to_propose_a_bid_if_there_are_not_bids_in_auction(self):

        # Test Case - 5
        self.auction.propose_a_bid(self.bid_gui)

        # Test Case - 5
        number_bids = len(self.auction.bids)
        self.assertEqual(1, number_bids)

    def test_that_should_allow_to_propose_a_bid_if_the_user_is_different_from_the_ones_who_bid_previously(self):

        # Test Case - 6
        self.auction.propose_a_bid(self.bid_yuri)
        self.auction.propose_a_bid(self.bid_gui)

        # Test Case - 6
        number_bids = len(self.auction.bids)
        self.assertEqual(2, number_bids)

    def test_that_should_not_allow_to_propose_a_bid_if_the_user_is_equal_from_the_ones_who_bid_previously(self):
        # Test Case - 7
        gui_2 = Bid(self.gui, 200)

        # Test Result - 7
        with self.assertRaises(InvalidBid):
            self.auction.propose_a_bid(self.bid_gui)
            self.auction.propose_a_bid(gui_2)
