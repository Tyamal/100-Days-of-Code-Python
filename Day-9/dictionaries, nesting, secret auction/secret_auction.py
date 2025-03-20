# secret_auction.py

def main():
    bids = {}
    bidding_finished = False

    while not bidding_finished:
        name = input("Enter your name: ")
        bid_amount = float(input("Enter your bid: $"))

        bids[name] = bid_amount

        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
        if should_continue.lower() == 'no':
            bidding_finished = True

    # Menentukan pemenang
    winner = max(bids, key=bids.get)
    winning_bid = bids[winner]

    print(f"The winner is {winner} with a bid of ${winning_bid}.")

if __name__ == "__main__":
    main()
