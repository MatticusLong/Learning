# simple slot machine game
import random

symbols = ["🍒", "🍉", "🍇", "7️"]

def spin_slot_machine():
    # Generate three random symbols
    slot_result = [random.choice(symbols) for _ in range(3)]
    return slot_result

def play_slot_machine():
    print("Welcome to the Slot Machine!")
    while True:
        input("Press Enter to spin the slot machine...")
        slot_result = spin_slot_machine()
        print("Result:", " | ".join(slot_result))
        
        if slot_result == ["7️", "7️", "7️"]:
            print("Jackpot! You win! 🎉")
        else:
            print("Try again! Better luck next time! 🍀")
        
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break
    print("Thanks for playing! Goodbye!")

# Start the slot machine game
play_slot_machine()