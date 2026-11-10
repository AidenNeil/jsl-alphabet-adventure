"""
JSL Alphabet Adventure - Main Application
An interactive application to learn and practice Jamaican Sign Language alphabet.
"""

import sys
from typing import Optional
from game_mode_selector import GameModeSelector, GameMode
from learn_mode import LearnMode
from quiz_mode import QuizMode
from sound_effects import sound_effects
from utils import clear_screen, print_box


class JSLAlphabetApp:
    """Main application class for JSL Alphabet Adventure."""
    
    def __init__(self):
        """Initialize the application."""
        self.mode_selector = GameModeSelector()
        self.current_mode: Optional[GameMode] = None
        self.running = True
    
    def run(self):
        """Run the main application loop."""
        print_box("Welcome to JSL Alphabet Adventure!", width=60)
        print("\nLearn and master Jamaican Sign Language alphabet!\n")
        
        try:
            while self.running:
                if not self.current_mode:
                    self._show_mode_selection()
                else:
                    self._run_current_mode()
        except KeyboardInterrupt:
            print("\n\nExiting application...")
        finally:
            self._cleanup()
    
    def _show_mode_selection(self):
        """Show mode selection screen."""
        self.mode_selector.display_modes()
        
        try:
            choice = input("Enter mode number (1-3) or 'q' to quit: ").strip().lower()
            
            if choice == 'q':
                self.running = False
                return
            
            mode_number = int(choice)
            mode = self.mode_selector.get_mode_by_number(mode_number)
            
            if mode:
                self.current_mode = mode
                self.mode_selector.select_mode(mode)
                clear_screen()
            else:
                print("\nInvalid selection. Please enter 1, 2, or 3.\n")
        except ValueError:
            print("\nInvalid input. Please enter a number or 'q'.\n")
    
    def _run_current_mode(self):
        """Run the currently selected mode."""
        if self.current_mode == 'learn':
            self._run_learn_mode()
        elif self.current_mode == 'practice':
            self._run_quiz_mode(is_fast=False)
        elif self.current_mode == 'challenge':
            self._run_quiz_mode(is_fast=True)
        
        # Return to mode selection
        self.current_mode = None
        self.mode_selector.exit_mode()
        clear_screen()
    
    def _run_learn_mode(self):
        """Run Learn Mode."""
        learn_mode = LearnMode()
        
        print_box("LEARN MODE - JSL Alphabet", width=60, border_char="=")
        print("\nCommands:")
        print("  n - Next letter")
        print("  p - Previous letter")
        print("  [A-Z] - Jump to specific letter")
        print("  q - Return to menu")
        print()
        
        while True:
            # Display current letter
            info = learn_mode.display_current_letter()
            print("\n" + "-" * 60)
            print(f"Progress: {info['progress']}")
            print(f"\nLetter: {info['letter']}")
            print(f"Description: {info['description']}")
            print(f"Image: {info['image_url']}")
            print("-" * 60)
            
            # Get user input
            command = input("\nCommand: ").strip().lower()
            
            if command == 'n':
                learn_mode.next_letter()
            elif command == 'p':
                learn_mode.previous_letter()
            elif command == 'q':
                break
            elif len(command) == 1 and command.isalpha():
                try:
                    learn_mode.jump_to_letter_by_char(command)
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Invalid command. Try 'n', 'p', [A-Z], or 'q'.")
    
    def _run_quiz_mode(self, is_fast: bool):
        """Run Quiz Mode (Practice or Challenge)."""
        mode_name = "CHALLENGE MODE (5 seconds)" if is_fast else "PRACTICE MODE (10 seconds)"
        quiz = QuizMode(is_fast=is_fast)
        
        print_box(mode_name, width=60, border_char="=")
        print(f"\nTime per question: {quiz.time_limit} seconds")
        print(f"Total questions: {quiz.total_questions}")
        print("\nCommands:")
        print("  [1-4] - Select answer option")
        print("  q - Return to menu")
        print()
        input("Press Enter to start...")
        
        while not quiz.is_game_over():
            question = quiz.get_current_question()
            if not question:
                break
            
            print("\n" + "=" * 60)
            print(f"Question {question['question_number']}/{question['total_questions']}")
            print(f"Score: {quiz.get_score()}")
            print("=" * 60)
            print(f"\nImage: {question['image_url']}")
            print(f"\nWhat letter is this?\n")
            
            for i, option in enumerate(question['options'], 1):
                print(f"  {i}) {option}")
            
            print(f"\nTime limit: {quiz.time_limit} seconds")
            
            # Get user input
            while True:
                choice = input("\nYour answer (1-4): ").strip()
                
                if choice == 'q':
                    return
                
                try:
                    choice_num = int(choice)
                    if 1 <= choice_num <= 4:
                        answer = question['options'][choice_num - 1]
                        is_correct = quiz.submit_answer(answer)
                        correct_answer = quiz.get_correct_answer()
                        
                        if is_correct:
                            print(f"\n✓ Correct! The answer is {correct_answer}")
                        else:
                            print(f"\n✗ Incorrect. The correct answer is {correct_answer}")
                        
                        input("\nPress Enter to continue...")
                        quiz.move_to_next()
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 4.")
        
        # Show final results
        self._show_quiz_results(quiz)
    
    def _show_quiz_results(self, quiz: QuizMode):
        """Show quiz results."""
        results = quiz.get_final_results()
        
        print("\n" + "=" * 60)
        print_box("QUIZ COMPLETE!", width=60, border_char="=")
        print(f"\nFinal Score: {results['score']} / {results['total']}")
        print(f"Percentage: {results['percentage']:.1f}%\n")
        
        if results['passed']:
            print("*** Great Job! You passed! ***")
        else:
            print("*** Keep Practicing! ***")
        
        print()
        input("Press Enter to return to menu...")
    
    def _cleanup(self):
        """Clean up resources before exit."""
        sound_effects.cleanup()
        print("\nThank you for using JSL Alphabet Adventure!")


def main():
    """Main entry point for the application."""
    app = JSLAlphabetApp()
    app.run()


if __name__ == "__main__":
    main()
