from domain import User, Bid, Auction, Evaluator

gui = User("Gui")
yuri = User("Yuri")

bid_yuri = Bid(yuri, 100)
bid_gui = Bid(gui, 150)

auction = Auction("Celular")

auction.bids.append(bid_yuri)
auction.bids.append(bid_gui)

for bid in auction.bids:
    print(f'The user {bid.user.name} has bid for {bid.value}')

evaluator = Evaluator()
evaluator.evaluate(auction=auction)

print(f'The lowest bid was {evaluator.lowest_bid} and the highest bid was {evaluator.highest_bid}')
