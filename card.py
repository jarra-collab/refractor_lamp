
class Card:
    # Defining valid ranks and suits
    accepted_ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    accepted_suits = ["Heart", "Diamond", "Spade", "Club"]

    def __init__(self, rank, suit):
        # 1. Check if suit is a string
        if not isinstance(suit, str):
            raise TypeError(f"Suit must be a string, not {type(suit).__name__}")
        
        # 2. Check if rank is a string
        if not isinstance(rank, str):
            raise TypeError(f"Rank must be a string, not {type(rank).__name__}")

        # Normalize inputs to uppercase to match accepted lists
        rank_upper = rank.upper()
        suit_title = suit.capitalize() # e.g., "heart" becomes "Heart"

        # 3. Check if rank and suit are in the accepted lists
        if rank_upper not in self.accepted_ranks:
            raise ValueError(f"Invalid rank: {rank}. Must be one of {self.accepted_ranks}")
        
        if suit_title not in self.accepted_suits:
            raise ValueError(f"Invalid suit: {suit}. Must be one of {self.accepted_suits}")

        # Assigning attributes
        self.rank = rank_upper
        self.suit = suit_title

    def __repr__(self):
        # Returns a string representation of the card
        return f"{self.rank} of {self.suit}s"

# Main execution block
if __name__ == "__main__":
    try:
        card1 = Card("A", "Spade")
        card2 = Card("10", "Heart")
        
        print(f"Card 1: {card1}")
        print(f"Card 2: {card2}")
    except (TypeError, ValueError) as e:
        print(f"Error creating card: {e}")

