"""JSL Alphabet data structure and definitions."""
from typing import List, Dict
import os

class JSLLetter:
    """Represents a JSL letter with its properties."""
    
    def __init__(self, letter: str, description: str, image_url: str):
        self.letter = letter
        self.description = description
        self.image_url = image_url
    
    def to_dict(self) -> Dict:
        """Convert to dictionary representation."""
        return {
            'letter': self.letter,
            'description': self.description,
            'image_url': self.image_url
        }
    
    def __repr__(self):
        return f"JSLLetter(letter='{self.letter}', description='{self.description}')"


# JSL Alphabet data
jsl_alphabet: List[JSLLetter] = [
    JSLLetter('A', 'Closed fist with thumb on the side', 'src/jsl_alphabet_test/A.jpg'),
    JSLLetter('B', 'Flat hand with thumb across palm', 'src/jsl_alphabet_test/B.jpg'),
    JSLLetter('C', 'Curved hand forming a C shape', 'src/jsl_alphabet_test/C.jpg'),
    JSLLetter('D', 'Index finger up, other fingers touching thumb', 'src/jsl_alphabet_test/D.jpg'),
    JSLLetter('E', 'Fingers curled over thumb', 'src/jsl_alphabet_test/E.jpg'),
    JSLLetter('F', 'Index and thumb touching, other fingers up', 'src/jsl_alphabet_test/F.jpg'),
    JSLLetter('G', 'Pointing index and thumb horizontally', 'src/jsl_alphabet_test/G.jpg'),
    JSLLetter('H', 'Index and middle finger together horizontally', 'src/jsl_alphabet_test/H.jpg'),
    JSLLetter('I', 'Pinky finger up, others closed', 'src/jsl_alphabet_test/I.jpg'),
    JSLLetter('J', 'Pinky finger makes a J motion', 'src/jsl_alphabet_test/J.jpg'),
    JSLLetter('K', 'Index and middle up, thumb between', 'src/jsl_alphabet_test/K.jpg'),
    JSLLetter('L', 'L shape with index and thumb', 'src/jsl_alphabet_test/L.jpg'),
    JSLLetter('M', 'Thumb under three fingers', 'src/jsl_alphabet_test/M.jpg'),
    JSLLetter('N', 'Thumb under two fingers', 'src/jsl_alphabet_test/N.jpg'),
    JSLLetter('O', 'All fingers forming an O shape', 'src/jsl_alphabet_test/O.jpg'),
    JSLLetter('P', 'K pointing down', 'src/jsl_alphabet_test/P.jpg'),
    JSLLetter('Q', 'G pointing down', 'src/jsl_alphabet_test/Q.jpg'),
    JSLLetter('R', 'Index and middle crossed', 'src/jsl_alphabet_test/R.jpg'),
    JSLLetter('S', 'Fist with thumb across fingers', 'src/jsl_alphabet_test/S.jpg'),
    JSLLetter('T', 'Thumb between index and middle', 'src/jsl_alphabet_test/T.jpg'),
    JSLLetter('U', 'Index and middle up together', 'src/jsl_alphabet_test/U.jpg'),
    JSLLetter('V', 'Peace sign', 'src/jsl_alphabet_test/V.jpg'),
    JSLLetter('W', 'Three fingers up', 'src/jsl_alphabet_test/W.jpg'),
    JSLLetter('X', 'Index finger curved like a hook', 'src/jsl_alphabet_test/X.jpg'),
    JSLLetter('Y', 'Pinky and thumb out', 'src/jsl_alphabet_test/Y.jpg'),
    JSLLetter('Z', 'Index draws a Z in the air', 'src/jsl_alphabet_test/Z.jpg'),
]


def get_jsl_alphabet() -> List[JSLLetter]:
    """Get the complete JSL alphabet list."""
    return jsl_alphabet


def get_letter_by_char(letter: str) -> JSLLetter:
    """Get JSL letter object by character."""
    letter_upper = letter.upper()
    for jsl_letter in jsl_alphabet:
        if jsl_letter.letter == letter_upper:
            return jsl_letter
    raise ValueError(f"Letter '{letter}' not found in JSL alphabet")


def get_alphabet_size() -> int:
    """Get the total number of letters in the alphabet."""
    return len(jsl_alphabet)

