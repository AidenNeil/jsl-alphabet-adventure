"""Flask web application for JSL Alphabet Adventure"""

from flask import Flask, render_template, jsonify, request, send_from_directory
import random
import os
from jsl_alphabet import jsl_alphabet, get_alphabet_size
from leaderboard import add_score, get_leaderboard, get_high_score
from jsl_words import jsl_words, get_random_words, get_words_by_difficulty, get_word_count

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jsl-alphabet-adventure-secret-key'

# Store quiz sessions (in production, use proper session management)
quiz_sessions = {}


@app.route('/')
def index():
    """Main page - mode selection"""
    return render_template('index.html')


@app.route('/learn')
def learn_mode():
    """Learn mode page"""
    return render_template('learn.html')


@app.route('/practice')
def practice_select():
    """Practice mode selection page"""
    return render_template('practice_select.html')


@app.route('/practice/type')
def practice_type():
    """Type challenge practice mode"""
    return render_template('practice_type.html')


@app.route('/challenge')
def challenge_select():
    """Challenge mode selection page"""
    return render_template('challenge_select.html')


@app.route('/challenge/cards')
def challenge_cards():
    """Speed match card game page"""
    return render_template('challenge_cards.html')


@app.route('/speed')
def speed_select():
    """Speed mode selection page"""
    return render_template('speed_select.html')


@app.route('/speed/blitz')
def speed_blitz():
    """Speed blitz rapid-fire typing challenge"""
    return render_template('speed_blitz.html')


@app.route('/quiz/<mode>')
def quiz_mode(mode):
    """Quiz mode page (practice, challenge, or speed)"""
    time_limits = {
        'practice': 10,
        'challenge': 5,
        'speed': 2
    }
    time_limit = time_limits.get(mode, 10)
    is_fast = mode in ['challenge', 'speed']
    return render_template('quiz.html', mode=mode, time_limit=time_limit)


@app.route('/memory')
def memory_select():
    """Memory mode selection page"""
    return render_template('memory_select.html')


@app.route('/memory/quiz')
def memory_quiz():
    """Quick memory challenge mode page"""
    return render_template('memory_mode.html')


@app.route('/memory/cards')
def memory_cards():
    """Card matching memory game page"""
    return render_template('memory_cards.html')


@app.route('/survival')
def survival_mode():
    """Survival mode page (3 lives)"""
    return render_template('survival.html')


@app.route('/leaderboard')
def leaderboard_page():
    """Leaderboard page showing all high scores"""
    return render_template('leaderboard.html')


@app.route('/words')
def word_challenge():
    """Word challenge mode - guess JSL words"""
    return render_template('word_challenge.html')


@app.route('/api/alphabet')
def get_alphabet():
    """API endpoint to get all JSL letters"""
    letters = []
    for letter in jsl_alphabet:
        letters.append({
            'letter': letter.letter,
            'description': letter.description,
            'imageUrl': '/' + letter.image_url
        })
    return jsonify(letters)


@app.route('/api/alphabet/<letter>')
def get_letter(letter):
    """API endpoint to get a specific letter"""
    letter_upper = letter.upper()
    for jsl_letter in jsl_alphabet:
        if jsl_letter.letter == letter_upper:
            return jsonify({
                'letter': jsl_letter.letter,
                'description': jsl_letter.description,
                'imageUrl': '/' + jsl_letter.image_url
            })
    return jsonify({'error': 'Letter not found'}), 404


@app.route('/api/quiz/start', methods=['POST'])
def start_quiz():
    """Start a new quiz session"""
    data = request.json
    is_fast = data.get('isFast', False)
    
    # Select 10 random letters
    selected_letters = random.sample(jsl_alphabet, 10)
    
    # Generate questions
    questions = []
    for letter in selected_letters:
        # Get 3 wrong answers
        wrong_letters = [l for l in jsl_alphabet if l.letter != letter.letter]
        wrong_options = random.sample(wrong_letters, 3)
        
        # Combine and shuffle options
        options = [letter.letter] + [l.letter for l in wrong_options]
        random.shuffle(options)
        
        questions.append({
            'letter': letter.letter,
            'description': letter.description,
            'imageUrl': '/' + letter.image_url,
            'options': options,
            'correctAnswer': letter.letter
        })
    
    session_id = str(random.randint(100000, 999999))
    quiz_sessions[session_id] = {
        'questions': questions,
        'currentIndex': 0,
        'score': 0,
        'isFast': is_fast
    }
    
    return jsonify({
        'sessionId': session_id,
        'totalQuestions': len(questions),
        'timeLimit': 5 if is_fast else 10
    })


@app.route('/api/quiz/question/<session_id>')
def get_question(session_id):
    """Get current question for a quiz session"""
    if session_id not in quiz_sessions:
        return jsonify({'error': 'Invalid session'}), 404
    
    session = quiz_sessions[session_id]
    if session['currentIndex'] >= len(session['questions']):
        return jsonify({'gameOver': True})
    
    question = session['questions'][session['currentIndex']]
    return jsonify({
        'question': {
            'letter': question['letter'],
            'imageUrl': question['imageUrl'],
            'options': question['options']
        },
        'currentIndex': session['currentIndex'],
        'totalQuestions': len(session['questions']),
        'score': session['score']
    })


@app.route('/api/quiz/answer', methods=['POST'])
def submit_answer():
    """Submit an answer for the current question"""
    data = request.json
    session_id = data.get('sessionId')
    answer = data.get('answer')
    mode = data.get('mode', 'practice')
    
    if session_id not in quiz_sessions:
        return jsonify({'error': 'Invalid session'}), 404
    
    session = quiz_sessions[session_id]
    current_question = session['questions'][session['currentIndex']]
    
    is_correct = answer == current_question['correctAnswer']
    if is_correct:
        session['score'] += 1
    
    session['currentIndex'] += 1
    
    game_over = session['currentIndex'] >= len(session['questions'])
    
    # Save score to leaderboard when game is over
    if game_over:
        add_score(mode, session['score'], len(session['questions']))
    
    return jsonify({
        'correct': is_correct,
        'correctAnswer': current_question['correctAnswer'],
        'score': session['score'],
        'gameOver': game_over,
        'totalQuestions': len(session['questions'])
    })


@app.route('/api/leaderboard')
def api_leaderboard():
    """Get leaderboard data"""
    all_scores = get_leaderboard()
    return jsonify(all_scores)


@app.route('/api/leaderboard/<mode>')
def api_leaderboard_mode(mode):
    """Get leaderboard for specific mode"""
    scores = get_leaderboard(mode)
    high_score = get_high_score(mode)
    return jsonify({
        'scores': scores,
        'highScore': high_score
    })


@app.route('/api/save-score', methods=['POST'])
def save_score_api():
    """Save a score to the leaderboard"""
    data = request.json
    mode = data.get('mode')
    score = data.get('score')
    total = data.get('total', 10)
    extra = data.get('extra', {})
    
    entry = add_score(mode, score, total, extra)
    high_score = get_high_score(mode)
    
    return jsonify({
        'success': True,
        'entry': entry,
        'highScore': high_score,
        'isNewHighScore': score >= high_score
    })


@app.route('/api/words/quiz/start', methods=['POST'])
def start_word_quiz():
    """Start a new word quiz session"""
    data = request.json
    difficulty = data.get('difficulty', 'easy')
    
    # Get words based on difficulty
    if difficulty == 'mixed':
        selected_words = get_random_words(10)
    else:
        available_words = get_words_by_difficulty(difficulty)
        count = min(len(available_words), 10)
        selected_words = random.sample(available_words, count)
    
    # Generate questions
    questions = []
    for word in selected_words:
        # Get 3 wrong answers from other words
        wrong_words = [w for w in jsl_words if w.word != word.word]
        wrong_options = random.sample(wrong_words, min(3, len(wrong_words)))
        
        # Combine and shuffle options
        options = [word.word] + [w.word for w in wrong_options]
        random.shuffle(options)
        
        questions.append({
            'word': word.word,
            'category': word.category,
            'difficulty': word.difficulty,
            'videoUrl': word.video_url,
            'hint': word.hint,
            'options': options,
            'correctAnswer': word.word
        })
    
    session_id = str(random.randint(100000, 999999))
    quiz_sessions[session_id] = {
        'questions': questions,
        'currentIndex': 0,
        'score': 0,
        'difficulty': difficulty
    }
    
    return jsonify({
        'sessionId': session_id,
        'totalQuestions': len(questions),
        'difficulty': difficulty
    })


@app.route('/api/words/quiz/question/<session_id>')
def get_word_question(session_id):
    """Get current question for a word quiz session"""
    if session_id not in quiz_sessions:
        return jsonify({'error': 'Invalid session'}), 404
    
    session = quiz_sessions[session_id]
    if session['currentIndex'] >= len(session['questions']):
        return jsonify({'gameOver': True})
    
    question = session['questions'][session['currentIndex']]
    return jsonify({
        'question': {
            'word': question['word'],
            'category': question['category'],
            'hint': question['hint'],
            'videoUrl': question['videoUrl'],
            'options': question['options']
        },
        'currentIndex': session['currentIndex'],
        'totalQuestions': len(session['questions']),
        'score': session['score']
    })


@app.route('/api/words/quiz/answer', methods=['POST'])
def submit_word_answer():
    """Submit an answer for the current word question"""
    data = request.json
    session_id = data.get('sessionId')
    answer = data.get('answer')
    difficulty = data.get('difficulty', 'easy')
    
    if session_id not in quiz_sessions:
        return jsonify({'error': 'Invalid session'}), 404
    
    session = quiz_sessions[session_id]
    current_question = session['questions'][session['currentIndex']]
    
    is_correct = answer == current_question['correctAnswer']
    if is_correct:
        session['score'] += 1
    
    session['currentIndex'] += 1
    
    game_over = session['currentIndex'] >= len(session['questions'])
    
    return jsonify({
        'correct': is_correct,
        'correctAnswer': current_question['correctAnswer'],
        'score': session['score'],
        'gameOver': game_over,
        'totalQuestions': len(session['questions'])
    })


@app.route('/api/speed-blitz/submit', methods=['POST'])
def speed_blitz_submit():
    """Submit speed blitz score"""
    data = request.json
    score = data.get('score')
    streak = data.get('streak')
    accuracy = data.get('accuracy')
    
    # Save to leaderboard
    add_score('speed_blitz', score, score, {'streak': streak, 'accuracy': accuracy})
    
    # Get rank
    leaderboard = get_leaderboard('speed_blitz')
    rank = 1
    for entry in leaderboard:
        if entry['score'] > score:
            rank += 1
    
    return jsonify({
        'success': True,
        'rank': rank,
        'total_players': len(leaderboard)
    })


@app.route('/api/speed-blitz/leaderboard')
def speed_blitz_leaderboard():
    """Get speed blitz global leaderboard"""
    leaderboard = get_leaderboard('speed_blitz')
    return jsonify(leaderboard[:50])  # Top 50 players


@app.route('/src/<path:filename>')
def serve_assets(filename):
    """Serve static assets like images"""
    print(f"[IMAGE REQUEST] Serving: src/{filename}")
    file_path = os.path.join('src', filename)
    if os.path.exists(file_path):
        print(f"[IMAGE FOUND] File exists at: {file_path}")
    else:
        print(f"[IMAGE NOT FOUND] File does not exist at: {file_path}")
    return send_from_directory('src', filename)


@app.route('/test-images')
def test_images():
    """Test endpoint to check image availability"""
    test_results = []
    for i, letter in enumerate(jsl_alphabet[:3]):  # Test first 3 letters
        image_path = letter.image_url
        full_path = os.path.join(os.getcwd(), image_path)
        exists = os.path.exists(full_path)
        test_results.append({
            'letter': letter.letter,
            'image_url': image_path,
            'full_path': full_path,
            'exists': exists,
            'api_url': '/' + image_path
        })
    return jsonify({
        'message': 'Image test results',
        'working_directory': os.getcwd(),
        'test_results': test_results
    })


if __name__ == '__main__':
    PORT = 7000
    print("\n" + "="*60)
    print("JSL Alphabet Adventure - Web Version")
    print("="*60)
    print("\nStarting web server...")
    print("\nOpen your browser and go to:")
    print(f"  http://localhost:{PORT}")
    print("\nPress CTRL+C to stop the server")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=PORT)

