"""Quiz Mode - Test your JSL knowledge with timed quizzes."""
import random
import time
from typing import List, Optional, Dict
from jsl_alphabet import jsl_alphabet, get_alphabet_size
from sound_effects import sound_effects


class QuizMode:
    """Quiz Mode for testing JSL knowledge."""
    
    def __init__(self, is_fast: bool = False):
        """
        Initialize Quiz Mode.
        
        Args:
            is_fast: If True, fast-paced quiz (5 seconds per question).
                    If False, slow-paced quiz (10 seconds per question).
        """
        self.is_fast = is_fast
        self.time_limit = 5 if is_fast else 10
        self.total_questions = 10
        
        self.current_index = 0
        self.score = 0
        self.questions = []
        self.current_options = []
        self.game_over = False
        self.selected_answer = None
        self.show_result = False
        self.time_left = self.time_limit
        self.start_time = None
        
        self._generate_questions()
    
    def _generate_questions(self):
        """Generate random questions for the quiz."""
        # Shuffle and select random letters
        shuffled = jsl_alphabet.copy()
        random.shuffle(shuffled)
        self.questions = shuffled[:self.total_questions]
        self.current_index = 0
        self._generate_options()
    
    def _generate_options(self):
        """Generate multiple choice options for current question."""
        if self.current_index >= len(self.questions):
            return
        
        correct_letter = self.questions[self.current_index]
        
        # Get wrong answers
        wrong_letters = [l for l in jsl_alphabet if l.letter != correct_letter.letter]
        random.shuffle(wrong_letters)
        wrong_options = [l.letter for l in wrong_letters[:3]]
        
        # Combine and shuffle
        all_options = [correct_letter.letter] + wrong_options
        random.shuffle(all_options)
        self.current_options = all_options
    
    def get_current_question(self) -> Dict:
        """Get current question information."""
        if self.current_index >= len(self.questions):
            return None
        
        letter = self.questions[self.current_index]
        return {
            'letter': letter.letter,
            'description': letter.description,
            'image_url': letter.image_url,
            'options': self.current_options,
            'question_number': self.current_index + 1,
            'total_questions': self.total_questions,
            'time_left': self.time_left
        }
    
    def get_score(self) -> int:
        """Get current score."""
        return self.score
    
    def get_progress(self) -> str:
        """Get progress string."""
        return f"{self.current_index + 1} / {self.total_questions}"
    
    def is_game_over(self) -> bool:
        """Check if game is over."""
        return self.game_over
    
    def start_question_timer(self):
        """Start timer for current question."""
        self.start_time = time.time()
        self.time_left = self.time_limit
    
    def update_timer(self):
        """Update the timer and check for timeout."""
        if self.start_time and not self.show_result:
            elapsed = time.time() - self.start_time
            self.time_left = max(0, self.time_limit - int(elapsed))
            
            if self.time_left <= 0:
                return True  # Timeout
        return False
    
    def handle_timeout(self):
        """Handle timeout situation."""
        sound_effects.play_incorrect()
        self.show_result = True
        self.selected_answer = None
    
    def submit_answer(self, answer: str) -> bool:
        """
        Submit an answer for the current question.
        
        Args:
            answer: The selected letter
            
        Returns:
            True if answer is correct, False otherwise
        """
        if self.show_result or self.game_over:
            return False
        
        self.selected_answer = answer
        self.show_result = True
        
        correct_answer = self.questions[self.current_index].letter
        is_correct = answer == correct_answer
        
        if is_correct:
            sound_effects.play_correct()
            self.score += 1
        else:
            sound_effects.play_incorrect()
        
        return is_correct
    
    def move_to_next(self):
        """Move to the next question or end the game."""
        if self.current_index + 1 >= self.total_questions:
            self.game_over = True
            if self.score >= 7:
                sound_effects.play_success()
        else:
            self.current_index += 1
            self.show_result = False
            self.selected_answer = None
            self.time_left = self.time_limit
            self.start_time = None
            self._generate_options()
    
    def get_final_results(self) -> Dict:
        """Get final quiz results."""
        percentage = (self.score / self.total_questions) * 100
        return {
            'score': self.score,
            'total': self.total_questions,
            'percentage': percentage,
            'passed': percentage >= 70
        }
    
    def restart(self):
        """Restart the quiz."""
        sound_effects.play_click()
        self.current_index = 0
        self.score = 0
        self.game_over = False
        self.selected_answer = None
        self.show_result = False
        self.time_left = self.time_limit
        self.start_time = None
        self._generate_questions()
    
    def get_correct_answer(self) -> str:
        """Get the correct answer for current question."""
        if self.current_index < len(self.questions):
            return self.questions[self.current_index].letter
        return None
    
    def is_showing_result(self) -> bool:
        """Check if currently showing result."""
        return self.show_result


def run_quiz_mode_console(is_fast: bool = False):
    """Run Quiz Mode in console/terminal mode (for testing)."""
    mode_name = "CHALLENGE MODE (Fast)" if is_fast else "PRACTICE MODE (Slow)"
    quiz = QuizMode(is_fast=is_fast)
    
    print("=" * 60)
    print(mode_name)
    print("=" * 60)
    print(f"\nTime per question: {quiz.time_limit} seconds")
    print(f"Total questions: {quiz.total_questions}")
    print("\nCommands:")
    print("  [A-D] - Select answer option")
    print("  q - Quit")
    print()
    
    while not quiz.is_game_over():
        question = quiz.get_current_question()
        if not question:
            break
        
        print("\n" + "=" * 60)
        print(f"Question {question['question_number']}/{question['total_questions']}")
        print(f"Score: {quiz.get_score()}")
        print("=" * 60)
        print(f"\nImage: {question['image_url']}")
        print(f"\nWhat letter is this?")
        print()
        
        option_labels = ['A', 'B', 'C', 'D']
        for i, option in enumerate(question['options']):
            print(f"  {option_labels[i]}) {option}")
        
        print(f"\nTime remaining: {quiz.time_limit} seconds")
        
        # Get user input (in real implementation, this would be timed)
        while True:
            choice = input("\nYour answer: ").strip().upper()
            
            if choice == 'Q':
                print("\nExiting quiz...")
                return
            
            if choice in option_labels:
                option_index = option_labels.index(choice)
                answer = question['options'][option_index]
                
                is_correct = quiz.submit_answer(answer)
                correct_answer = quiz.get_correct_answer()
                
                if is_correct:
                    print(f"\n✓ Correct! The answer is {correct_answer}")
                else:
                    print(f"\n✗ Incorrect. The correct answer is {correct_answer}")
                
                print("\nMoving to next question...")
                time.sleep(1.5)
                quiz.move_to_next()
                break
            else:
                print("Invalid choice. Please enter A, B, C, D, or Q.")
    
    # Show final results
    results = quiz.get_final_results()
    print("\n" + "=" * 60)
    print("QUIZ COMPLETE!")
    print("=" * 60)
    print(f"\nFinal Score: {results['score']} / {results['total']}")
    print(f"Percentage: {results['percentage']:.1f}%")
    
    if results['passed']:
        print("\n*** Great Job! You passed! ***")
    else:
        print("\n*** Keep Practicing! ***")
    
    print()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--fast':
        run_quiz_mode_console(is_fast=True)
    else:
        run_quiz_mode_console(is_fast=False)
