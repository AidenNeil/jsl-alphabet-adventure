"""Leaderboard system for tracking high scores across all game modes"""
import json
import os
from datetime import datetime
from typing import List, Dict

LEADERBOARD_FILE = 'leaderboard.json'

def load_leaderboard() -> Dict:
    """Load leaderboard from file"""
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    
    return {
        'practice': [],
        'challenge': [],
        'memory': [],
        'speed': [],
        'survival': []
    }

def save_leaderboard(data: Dict):
    """Save leaderboard to file"""
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_score(mode: str, score: int, total: int = 10, extra_data: Dict = None):
    """Add a score to the leaderboard"""
    leaderboard = load_leaderboard()
    
    if mode not in leaderboard:
        leaderboard[mode] = []
    
    entry = {
        'score': score,
        'total': total,
        'percentage': round((score / total) * 100, 1) if total > 0 else 0,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Add extra data for specific modes
    if extra_data:
        entry.update(extra_data)
    
    leaderboard[mode].append(entry)
    
    # Sort by score (descending) and keep top 10
    leaderboard[mode] = sorted(
        leaderboard[mode],
        key=lambda x: x.get('score', 0),
        reverse=True
    )[:10]
    
    save_leaderboard(leaderboard)
    
    return entry

def get_leaderboard(mode: str = None) -> Dict:
    """Get leaderboard for a specific mode or all modes"""
    leaderboard = load_leaderboard()
    
    if mode:
        return leaderboard.get(mode, [])
    
    return leaderboard

def get_high_score(mode: str) -> int:
    """Get the highest score for a mode"""
    scores = get_leaderboard(mode)
    if scores:
        return scores[0].get('score', 0)
    return 0

def get_rank(mode: str, score: int) -> int:
    """Get the rank of a score in the leaderboard (1-based)"""
    scores = get_leaderboard(mode)
    for i, entry in enumerate(scores, 1):
        if score >= entry.get('score', 0):
            return i
    return len(scores) + 1

