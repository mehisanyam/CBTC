import random

# Defining options
options = ["rock", "paper", "scissors"]

# Defining winnig conditions
condt = {
    "rock": ["scissors"],
    "paper": ["rock"],
    "scissors": ["paper"]
}


def RPS():
    """
    Plays a single round of rock-paper-scissors.

    Returns:
        str: Message indicating who won or if it's a tie.
    """
    # Getting user input
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()

    # Validating user input
    if user_choice not in options:
        return "Invalid input. Please enter Rock, Paper, or Scissors."

    # Get random choice
    random_choice = random.choice(options)

    # Checking for tie
    if user_choice == random_choice:
        return f"It's a tie! Both players chose {random_choice}."

    # Checking for winner
    if user_choice in condt[random_choice]:
        return f"You win! {user_choice} beats {random_choice}."
    else:
        return f"You lose! {random_choice} beats {user_choice}."


def main():
    """
    Runs the main RPS  in   a loop.
  """
    while True:
        # Play a round
        result = RPS()
        print(result)

        # Ask if the user wants to play again
        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break

if __name__ == "__main__":
    main()
