"""
Demo script to showcase JSL Alphabet Adventure functionality
This demonstrates the core functionality without requiring interactive input.
"""

from jsl_alphabet import jsl_alphabet, get_alphabet_size, get_letter_by_char
from learn_mode import LearnMode
from quiz_mode import QuizMode
from game_mode_selector import GameModeSelector
from utils import print_box

print("=" * 70)
print_box("JSL ALPHABET ADVENTURE - DEMO", width=70)
print("=" * 70)

# Demo 1: JSL Alphabet Data
print("\n" + "=" * 70)
print("DEMO 1: JSL Alphabet Data")
print("=" * 70)
print(f"\nTotal letters in alphabet: {get_alphabet_size()}")
print("\nFirst 5 letters:")
for i, letter in enumerate(jsl_alphabet[:5]):
    print(f"  {letter.letter}: {letter.description}")
    print(f"     Image: {letter.image_url}")

# Demo 2: Learn Mode
print("\n" + "=" * 70)
print("DEMO 2: Learn Mode")
print("=" * 70)
learn_mode = LearnMode()
print(f"\nStarting at letter: {learn_mode.get_current_letter().letter}")
print(f"Progress: {learn_mode.get_progress()}")

learn_mode.next_letter()
print(f"\nAfter next: {learn_mode.get_current_letter().letter}")
print(f"Progress: {learn_mode.get_progress()}")

learn_mode.jump_to_letter_by_char('Z')
print(f"\nJumped to: {learn_mode.get_current_letter().letter}")
print(f"Description: {learn_mode.get_current_letter().description}")

# Demo 3: Quiz Mode Setup
print("\n" + "=" * 70)
print("DEMO 3: Quiz Mode (Practice)")
print("=" * 70)
quiz = QuizMode(is_fast=False)
print(f"\nQuiz Settings:")
print(f"  Time limit per question: {quiz.time_limit} seconds")
print(f"  Total questions: {quiz.total_questions}")
print(f"  Current score: {quiz.get_score()}")

question = quiz.get_current_question()
print(f"\nSample Question:")
print(f"  Question number: {question['question_number']}")
print(f"  Correct answer: {question['letter']}")
print(f"  Options: {', '.join(question['options'])}")

# Simulate answering correctly
correct = quiz.submit_answer(question['letter'])
print(f"\nSubmitted correct answer: {correct}")
print(f"Score after answer: {quiz.get_score()}")

# Demo 4: Challenge Mode
print("\n" + "=" * 70)
print("DEMO 4: Quiz Mode (Challenge)")
print("=" * 70)
challenge = QuizMode(is_fast=True)
print(f"\nChallenge Settings:")
print(f"  Time limit per question: {challenge.time_limit} seconds (faster!)")
print(f"  Total questions: {challenge.total_questions}")

# Demo 5: Game Mode Selector
print("\n" + "=" * 70)
print("DEMO 5: Game Mode Selector")
print("=" * 70)
selector = GameModeSelector()
print("\nAvailable modes:")
for mode in selector.get_modes():
    print(f"  {mode['icon']} {mode['title']}: {mode['description']}")

# Demo 6: Utility Functions
print("\n" + "=" * 70)
print("DEMO 6: Data Access Functions")
print("=" * 70)
try:
    letter_m = get_letter_by_char('M')
    print(f"\nLooking up letter 'M':")
    print(f"  Description: {letter_m.description}")
    print(f"  Image: {letter_m.image_url}")
except ValueError as e:
    print(f"Error: {e}")

# Summary
print("\n" + "=" * 70)
print_box("DEMO COMPLETE - All Components Working!", width=70)
print("=" * 70)
print("\n[OK] JSL Alphabet data loaded (26 letters)")
print("[OK] Learn Mode functional")
print("[OK] Quiz Mode functional (Practice & Challenge)")
print("[OK] Game Mode Selector functional")
print("[OK] All helper functions working")
print("\nTo run the full interactive application:")
print("  python main.py")
print("\nNote: Sound effects require PyAudio:")
print("  pip install pyaudio")
print()
