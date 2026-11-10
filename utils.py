"""Utility functions for the JSL Alphabet Adventure application."""
from typing import Any, List


def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Clamp a value between min and max.
    
    Args:
        value: The value to clamp
        min_value: Minimum allowed value
        max_value: Maximum allowed value
        
    Returns:
        Clamped value
    """
    return max(min_value, min(value, max_value))


def percentage(part: float, total: float) -> float:
    """
    Calculate percentage.
    
    Args:
        part: Part value
        total: Total value
        
    Returns:
        Percentage (0-100)
    """
    if total == 0:
        return 0
    return (part / total) * 100


def format_time(seconds: int) -> str:
    """
    Format seconds as MM:SS.
    
    Args:
        seconds: Time in seconds
        
    Returns:
        Formatted time string
    """
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes:02d}:{remaining_seconds:02d}"


def clear_screen():
    """Clear the console screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_letter(letter: str) -> bool:
    """
    Validate if a string is a single letter.
    
    Args:
        letter: String to validate
        
    Returns:
        True if valid single letter, False otherwise
    """
    return len(letter) == 1 and letter.isalpha()


def get_user_input(prompt: str, valid_options: List[str] = None) -> str:
    """
    Get user input with optional validation.
    
    Args:
        prompt: Input prompt message
        valid_options: List of valid input options (optional)
        
    Returns:
        User input string
    """
    while True:
        user_input = input(prompt).strip()
        
        if valid_options is None:
            return user_input
        
        if user_input.lower() in [opt.lower() for opt in valid_options]:
            return user_input
        
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")


def safe_int_input(prompt: str, min_value: int = None, max_value: int = None) -> int:
    """
    Get integer input from user with validation.
    
    Args:
        prompt: Input prompt message
        min_value: Minimum allowed value (optional)
        max_value: Maximum allowed value (optional)
        
    Returns:
        Integer value
    """
    while True:
        try:
            value = int(input(prompt).strip())
            
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}")
                continue
            
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}")
                continue
            
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            raise


def print_centered(text: str, width: int = 60, fill_char: str = " "):
    """
    Print text centered within a given width.
    
    Args:
        text: Text to center
        width: Total width
        fill_char: Character to fill empty space
    """
    print(text.center(width, fill_char))


def print_box(text: str, width: int = 60, border_char: str = "="):
    """
    Print text in a box.
    
    Args:
        text: Text to display
        width: Box width
        border_char: Border character
    """
    print(border_char * width)
    print_centered(text, width)
    print(border_char * width)
