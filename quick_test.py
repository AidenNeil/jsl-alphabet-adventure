"""Quick test to verify all Python modules are working"""

print("Testing JSL Alphabet Adventure Python Conversion...")
print("=" * 60)

# Test 1: Import all modules
try:
    import jsl_alphabet
    import game_mode_selector
    import learn_mode
    import quiz_mode
    import sound_effects
    import utils
    import main
    print("[OK] All modules imported successfully")
except Exception as e:
    print(f"[ERROR] Import failed: {e}")
    exit(1)

# Test 2: JSL Data
try:
    from jsl_alphabet import jsl_alphabet, get_alphabet_size
    assert get_alphabet_size() == 26, "Should have 26 letters"
    assert jsl_alphabet[0].letter == 'A', "First letter should be A"
    assert jsl_alphabet[25].letter == 'Z', "Last letter should be Z"
    print("[OK] JSL Alphabet data is correct (26 letters A-Z)")
except Exception as e:
    print(f"[ERROR] JSL data test failed: {e}")
    exit(1)

# Test 3: Learn Mode
try:
    from learn_mode import LearnMode
    learn = LearnMode()
    assert learn.get_current_index() == 0, "Should start at index 0"
    learn.next_letter()
    assert learn.get_current_index() == 1, "Should move to index 1"
    learn.jump_to_letter_by_char('M')
    assert learn.get_current_letter().letter == 'M', "Should jump to M"
    print("[OK] Learn Mode working correctly")
except Exception as e:
    print(f"[ERROR] Learn Mode test failed: {e}")
    exit(1)

# Test 4: Quiz Mode
try:
    from quiz_mode import QuizMode
    quiz = QuizMode(is_fast=False)
    assert quiz.time_limit == 10, "Practice mode should have 10 second timer"
    assert quiz.total_questions == 10, "Should have 10 questions"
    
    quiz_fast = QuizMode(is_fast=True)
    assert quiz_fast.time_limit == 5, "Challenge mode should have 5 second timer"
    print("[OK] Quiz Mode working correctly (Practice & Challenge)")
except Exception as e:
    print(f"[ERROR] Quiz Mode test failed: {e}")
    exit(1)

# Test 5: Game Mode Selector
try:
    from game_mode_selector import GameModeSelector
    selector = GameModeSelector()
    modes = selector.get_modes()
    assert len(modes) == 3, "Should have 3 game modes"
    assert modes[0]['id'] == 'learn', "First mode should be learn"
    assert modes[1]['id'] == 'practice', "Second mode should be practice"
    assert modes[2]['id'] == 'challenge', "Third mode should be challenge"
    print("[OK] Game Mode Selector working correctly")
except Exception as e:
    print(f"[ERROR] Game Mode Selector test failed: {e}")
    exit(1)

print("=" * 60)
print("\n*** ALL TESTS PASSED! ***\n")
print("The conversion from TypeScript to Python is complete and working!")
print("\nTo run the application:")
print("  python main.py")
print("\nTo see a demo:")
print("  python demo.py")
