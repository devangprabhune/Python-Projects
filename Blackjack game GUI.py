import random
import tkinter as tk
from tkinter import messagebox

# --- Game Logic ---
class BlackjackGame:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.user_cards = []
        self.computer_cards = []
        self.is_game_over = False
        self.result = ""
        self.deal_initial_cards()

    def deal_card(self):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    def deal_initial_cards(self):
        for _ in range(2):
            self.user_cards.append(self.deal_card())
            self.computer_cards.append(self.deal_card())

    def calculate_score(self, cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0  # Blackjack
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(self):
        user_score = self.calculate_score(self.user_cards)
        computer_score = self.calculate_score(self.computer_cards)

        if user_score == computer_score:
            self.result = "Draw 😐"
        elif computer_score == 0:
            self.result = "You lose, opponent has Blackjack😰"
        elif user_score == 0:
            self.result = "You win with a Blackjack😎"
        elif user_score > 21:
            self.result = "You lose, card total >21😭"
        elif computer_score > 21:
            self.result = "You win, opponent's card total >21😎"
        elif user_score > computer_score:
            self.result = "You win, your score is higher😎"
        else:
            self.result = "You lose😭"

# --- GUI ---
class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Game")
        self.game = BlackjackGame()

        # Set up the frames
        self.setup_frames()

        # Initialize the GUI components
        self.create_widgets()

        # Display the initial cards
        self.update_display()

    def setup_frames(self):
        # Frame for Dealer
        self.dealer_frame = tk.Frame(self.root, padx=20, pady=10)
        self.dealer_frame.pack()

        # Frame for Player
        self.player_frame = tk.Frame(self.root, padx=20, pady=10)
        self.player_frame.pack()

        # Frame for Buttons
        self.button_frame = tk.Frame(self.root, padx=20, pady=10)
        self.button_frame.pack()

        # Frame for Result
        self.result_frame = tk.Frame(self.root, padx=20, pady=10)
        self.result_frame.pack()

    def create_widgets(self):
        # Dealer Labels
        self.dealer_label = tk.Label(self.dealer_frame, text="Dealer's Cards:", font=("Helvetica", 14))
        self.dealer_label.pack(side=tk.LEFT)

        self.dealer_cards_var = tk.StringVar()
        self.dealer_cards_display = tk.Label(self.dealer_frame, textvariable=self.dealer_cards_var, font=("Helvetica", 14))
        self.dealer_cards_display.pack(side=tk.LEFT)

        # Player Labels
        self.player_label = tk.Label(self.player_frame, text="Your Cards:", font=("Helvetica", 14))
        self.player_label.pack(side=tk.LEFT)

        self.player_cards_var = tk.StringVar()
        self.player_cards_display = tk.Label(self.player_frame, textvariable=self.player_cards_var, font=("Helvetica", 14))
        self.player_cards_display.pack(side=tk.LEFT)

        # Buttons
        self.hit_button = tk.Button(self.button_frame, text="Hit", command=self.hit, width=10, bg="green", fg="white", font=("Helvetica", 12))
        self.hit_button.pack(side=tk.LEFT, padx=10)

        self.stand_button = tk.Button(self.button_frame, text="Stand", command=self.stand, width=10, bg="blue", fg="white", font=("Helvetica", 12))
        self.stand_button.pack(side=tk.LEFT, padx=10)

        self.new_game_button = tk.Button(self.button_frame, text="New Game", command=self.new_game, width=10, bg="orange", fg="white", font=("Helvetica", 12))
        self.new_game_button.pack(side=tk.LEFT, padx=10)

        # Result Label
        self.result_var = tk.StringVar()
        self.result_display = tk.Label(self.result_frame, textvariable=self.result_var, font=("Helvetica", 16))
        self.result_display.pack()

    def update_display(self):
        # Update Dealer's Cards (only show first card initially)
        if not self.game.is_game_over:
            dealer_cards_display = f"{self.game.computer_cards[0]} + ???"
        else:
            dealer_cards_display = ', '.join(map(str, self.game.computer_cards))
        self.dealer_cards_var.set(dealer_cards_display)

        # Update Player's Cards
        player_cards_display = ', '.join(map(str, self.game.user_cards))
        self.player_cards_var.set(player_cards_display)

        # Update Result
        self.result_var.set(self.game.result)

    def hit(self):
        if not self.game.is_game_over:
            self.game.user_cards.append(self.game.deal_card())
            user_score = self.game.calculate_score(self.game.user_cards)
            self.update_display()

            if user_score > 21 or self.game.calculate_score(self.game.user_cards) == 0:
                self.game.is_game_over = True
                self.end_game()

    def stand(self):
        if not self.game.is_game_over:
            # Dealer's turn
            while self.game.calculate_score(self.game.computer_cards) < 17 and self.game.calculate_score(self.game.computer_cards) != 0:
                self.game.computer_cards.append(self.game.deal_card())

            self.game.is_game_over = True
            self.game.compare()
            self.update_display()

    def end_game(self):
        # Reveal dealer's full hand
        self.dealer_cards_var.set(', '.join(map(str, self.game.computer_cards)))

        # Determine result if not already done
        if not self.game.result:
            self.game.compare()
            self.result_var.set(self.game.result)

    def new_game(self):
        self.game.reset_game()
        self.update_display()

# --- Main Application ---
def main():
    root = tk.Tk()
    gui = BlackjackGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
