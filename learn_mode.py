"""Learn Mode - Browse through JSL letters at your own pace."""
from typing import Optional
from jsl_alphabet import jsl_alphabet, get_alphabet_size
from sound_effects import sound_effects
import os


class LearnMode:
    """Learn Mode allows users to browse through JSL letters."""
    
    def __init__(self):
        """Initialize Learn Mode."""
        self.current_index = 0
        self.alphabet_size = get_alphabet_size()
    
    def get_current_letter(self):
        """Get the current letter being displayed."""
        return jsl_alphabet[self.current_index]
    
    def get_current_index(self) -> int:
        """Get the current index."""
        return self.current_index
    
    def get_progress(self) -> str:
        """Get progress string (e.g., '1 / 26')."""
        return f"{self.current_index + 1} / {self.alphabet_size}"
    
    def next_letter(self):
        """Move to the next letter (wraps around to start)."""
        sound_effects.play_click()
        self.current_index = (self.current_index + 1) % self.alphabet_size
    
    def previous_letter(self):
        """Move to the previous letter (wraps around to end)."""
        sound_effects.play_click()
        self.current_index = (self.current_index - 1 + self.alphabet_size) % self.alphabet_size
    
    def jump_to_letter(self, index: int):
        """Jump to a specific letter by index."""
        if 0 <= index < self.alphabet_size:
            sound_effects.play_click()
            self.current_index = index
        else:
            raise ValueError(f"Index {index} out of range (0-{self.alphabet_size - 1})")
    
    def jump_to_letter_by_char(self, letter: str):
        """Jump to a specific letter by character."""
        letter_upper = letter.upper()
        for i, jsl_letter in enumerate(jsl_alphabet):
            if jsl_letter.letter == letter_upper:
                sound_effects.play_click()
                self.current_index = i
                return
        raise ValueError(f"Letter '{letter}' not found")
    
    def get_all_letters(self):
        """Get all letters for navigation."""
        return jsl_alphabet
    
    def display_current_letter(self) -> dict:
        """Get display information for current letter."""
        letter = self.get_current_letter()
        return {
            'letter': letter.letter,
            'description': letter.description,
            'image_url': letter.image_url,
            'progress': self.get_progress(),
            'index': self.current_index
        }
    
    def reset(self):
        """Reset to the first letter."""
        self.current_index = 0


def run_learn_mode_console():
    """Run Learn Mode in console/terminal mode (for testing)."""
    mode = LearnMode()
    
    print("=" * 60)
    print("LEARN MODE - JSL Alphabet")
    print("=" * 60)
    print("\nCommands:")
    print("  n - Next letter")
    print("  p - Previous letter")
    print("  [letter] - Jump to specific letter (e.g., 'A', 'Z')")
    print("  q - Quit")
    print()
    
    while True:
        # Display current letter
        info = mode.display_current_letter()
        print("\n" + "-" * 60)
        print(f"Progress: {info['progress']}")
        print(f"\nLetter: {info['letter']}")
        print(f"Description: {info['description']}")
        print(f"Image: {info['image_url']}")
        print("-" * 60)
        
        # Get user input
        command = input("\nEnter command: ").strip().lower()
        
        if command == 'n':
            mode.next_letter()
        elif command == 'p':
            mode.previous_letter()
        elif command == 'q':
            print("\nExiting Learn Mode...")
            break
        elif len(command) == 1 and command.isalpha():
            try:
                mode.jump_to_letter_by_char(command)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid command. Try 'n', 'p', a letter, or 'q'.")


if __name__ == "__main__":
    run_learn_mode_console()
