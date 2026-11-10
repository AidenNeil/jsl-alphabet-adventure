
"""Game Mode Selector - Choose between Learn, Practice, or Challenge modes."""
from typing import Optional, Literal

GameMode = Literal['learn', 'practice', 'challenge']


class GameModeSelector:
    """Handle game mode selection."""
    
    def __init__(self):
        """Initialize the mode selector."""
        self.current_mode: Optional[GameMode] = None
        self.modes = [
            {
                'id': 'learn',
                'title': 'Learn',
                'description': 'Browse all JSL letters at your own pace',
                'icon': '[BOOK]'
            },
            {
                'id': 'practice',
                'title': 'Practice',
                'description': 'Test yourself with a slow-paced quiz',
                'icon': '[ZAP]'
            },
            {
                'id': 'challenge',
                'title': 'Challenge',
                'description': 'Fast-paced quiz to test your skills',
                'icon': '[TROPHY]'
            }
        ]
    
    def get_modes(self) -> list:
        """Get list of available modes."""
        return self.modes
    
    def select_mode(self, mode: GameMode):
        """Select a game mode."""
        if mode not in ['learn', 'practice', 'challenge']:
            raise ValueError(f"Invalid mode: {mode}")
        self.current_mode = mode
    
    def get_current_mode(self) -> Optional[GameMode]:
        """Get the currently selected mode."""
        return self.current_mode
    
    def exit_mode(self):
        """Exit the current mode and return to selection."""
        self.current_mode = None
    
    def display_modes(self):
        """Display available modes (console version)."""
        print("\n" + "=" * 60)
        print("ABC Fast or Slow")
        print("Master JSL Alphabet at Your Own Pace!")
        print("=" * 60)
        print("\nSelect a mode:")
        print()
        
        for i, mode in enumerate(self.modes, 1):
            print(f"{i}. {mode['icon']} {mode['title']}")
            print(f"   {mode['description']}")
            print()
    
    def get_mode_by_number(self, number: int) -> Optional[GameMode]:
        """Get mode ID by number selection."""
        if 1 <= number <= len(self.modes):
            return self.modes[number - 1]['id']
        return None


def run_mode_selector_console():
    """Run mode selector in console mode (for testing)."""
    selector = GameModeSelector()
    
    while True:
        selector.display_modes()
        
        try:
            choice = input("Enter mode number (1-3) or 'q' to quit: ").strip().lower()
            
            if choice == 'q':
                print("\nGoodbye!")
                break
            
            mode_number = int(choice)
            mode = selector.get_mode_by_number(mode_number)
            
            if mode:
                selector.select_mode(mode)
                print(f"\nSelected mode: {mode}")
                print("(In full application, this would launch the selected mode)")
                input("\nPress Enter to return to menu...")
                selector.exit_mode()
            else:
                print("Invalid selection. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    run_mode_selector_console()
