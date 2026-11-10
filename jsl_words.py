"""JSL Words data structure for word guessing challenges."""
from typing import List, Dict

class JSLWord:
    """Represents a JSL word with its properties."""
    
    def __init__(self, word: str, category: str, difficulty: str, video_url: str = None, hint: str = None):
        self.word = word
        self.category = category
        self.difficulty = difficulty  # easy, medium, hard
        self.video_url = video_url or f'src/jsl_words_videos/{word.lower().replace(" ", "_")}.mp4'
        self.hint = hint
    
    def to_dict(self) -> Dict:
        """Convert to dictionary representation."""
        return {
            'word': self.word,
            'category': self.category,
            'difficulty': self.difficulty,
            'video_url': self.video_url,
            'hint': self.hint
        }
    
    def __repr__(self):
        return f"JSLWord(word='{self.word}', category='{self.category}', difficulty='{self.difficulty}')"


# JSL Words database - Organized by category and difficulty
jsl_words: List[JSLWord] = [
    # EASY WORDS - Common Greetings & Basic
    JSLWord('Hello', 'Greetings', 'easy', hint='A friendly greeting'),
    JSLWord('Thank You', 'Greetings', 'easy', hint='Showing gratitude'),
    JSLWord('Please', 'Greetings', 'easy', hint='Polite request'),
    JSLWord('Sorry', 'Greetings', 'easy', hint='Apologizing'),
    JSLWord('Yes', 'Basic', 'easy', hint='Affirmative answer'),
    JSLWord('No', 'Basic', 'easy', hint='Negative answer'),
    JSLWord('Help', 'Basic', 'easy', hint='Asking for assistance'),
    JSLWord('Stop', 'Basic', 'easy', hint='Command to cease'),
    JSLWord('Go', 'Basic', 'easy', hint='Command to proceed'),
    JSLWord('Come', 'Basic', 'easy', hint='Inviting someone'),
    
    # EASY WORDS - Family
    JSLWord('Mother', 'Family', 'easy', hint='Female parent'),
    JSLWord('Father', 'Family', 'easy', hint='Male parent'),
    JSLWord('Sister', 'Family', 'easy', hint='Female sibling'),
    JSLWord('Brother', 'Family', 'easy', hint='Male sibling'),
    JSLWord('Baby', 'Family', 'easy', hint='Very young child'),
    
    # EASY WORDS - Colors
    JSLWord('Red', 'Colors', 'easy', hint='Color of roses'),
    JSLWord('Blue', 'Colors', 'easy', hint='Color of the sky'),
    JSLWord('Green', 'Colors', 'easy', hint='Color of grass'),
    JSLWord('Yellow', 'Colors', 'easy', hint='Color of the sun'),
    JSLWord('Black', 'Colors', 'easy', hint='Darkest color'),
    
    # MEDIUM WORDS - Actions
    JSLWord('Eat', 'Actions', 'medium', hint='Consuming food'),
    JSLWord('Drink', 'Actions', 'medium', hint='Consuming liquid'),
    JSLWord('Sleep', 'Actions', 'medium', hint='Resting at night'),
    JSLWord('Walk', 'Actions', 'medium', hint='Moving on foot'),
    JSLWord('Run', 'Actions', 'medium', hint='Moving fast'),
    JSLWord('Jump', 'Actions', 'medium', hint='Leap into air'),
    JSLWord('Dance', 'Actions', 'medium', hint='Moving to music'),
    JSLWord('Sing', 'Actions', 'medium', hint='Making music vocally'),
    JSLWord('Read', 'Actions', 'medium', hint='Looking at text'),
    JSLWord('Write', 'Actions', 'medium', hint='Making text'),
    
    # MEDIUM WORDS - Places
    JSLWord('Home', 'Places', 'medium', hint='Where you live'),
    JSLWord('School', 'Places', 'medium', hint='Place of learning'),
    JSLWord('Hospital', 'Places', 'medium', hint='Medical facility'),
    JSLWord('Church', 'Places', 'medium', hint='Place of worship'),
    JSLWord('Store', 'Places', 'medium', hint='Place to buy things'),
    
    # MEDIUM WORDS - Food
    JSLWord('Water', 'Food', 'medium', hint='Clear liquid'),
    JSLWord('Bread', 'Food', 'medium', hint='Baked staple'),
    JSLWord('Rice', 'Food', 'medium', hint='Jamaican staple grain'),
    JSLWord('Chicken', 'Food', 'medium', hint='Common poultry'),
    JSLWord('Fish', 'Food', 'medium', hint='From the sea'),
    
    # HARD WORDS - Complex Concepts
    JSLWord('Beautiful', 'Adjectives', 'hard', hint='Very attractive'),
    JSLWord('Important', 'Adjectives', 'hard', hint='Of great significance'),
    JSLWord('Difficult', 'Adjectives', 'hard', hint='Not easy'),
    JSLWord('Happy', 'Emotions', 'hard', hint='Feeling joy'),
    JSLWord('Sad', 'Emotions', 'hard', hint='Feeling sorrow'),
    JSLWord('Angry', 'Emotions', 'hard', hint='Feeling mad'),
    JSLWord('Surprised', 'Emotions', 'hard', hint='Feeling shocked'),
    JSLWord('Excited', 'Emotions', 'hard', hint='Feeling thrilled'),
    
    # HARD WORDS - Advanced
    JSLWord('Jamaica', 'Places', 'hard', hint='Our beautiful island'),
    JSLWord('Love', 'Emotions', 'hard', hint='Deep affection'),
    JSLWord('Friend', 'Relationships', 'hard', hint='Close companion'),
    JSLWord('Family', 'Relationships', 'hard', hint='Related people'),
    JSLWord('Teacher', 'People', 'hard', hint='Educator'),
    JSLWord('Doctor', 'People', 'hard', hint='Medical professional'),
    JSLWord('Police', 'People', 'hard', hint='Law enforcement'),
]


def get_words_by_difficulty(difficulty: str) -> List[JSLWord]:
    """Get words filtered by difficulty level."""
    return [word for word in jsl_words if word.difficulty == difficulty]


def get_words_by_category(category: str) -> List[JSLWord]:
    """Get words filtered by category."""
    return [word for word in jsl_words if word.category == category]


def get_random_words(count: int = 10, difficulty: str = None) -> List[JSLWord]:
    """Get random words, optionally filtered by difficulty."""
    import random
    if difficulty:
        pool = get_words_by_difficulty(difficulty)
    else:
        pool = jsl_words
    
    return random.sample(pool, min(count, len(pool)))


def get_all_categories() -> List[str]:
    """Get list of all unique categories."""
    return list(set(word.category for word in jsl_words))


def get_word_count() -> int:
    """Get total number of words."""
    return len(jsl_words)


def get_word_by_name(word_name: str) -> JSLWord:
    """Get word by name."""
    for word in jsl_words:
        if word.word.lower() == word_name.lower():
            return word
    raise ValueError(f"Word '{word_name}' not found")

