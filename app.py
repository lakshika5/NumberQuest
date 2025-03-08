import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize game variables
secret_number = random.randint(1, 100)
attempts = 0

@app.route('/')
def index():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global secret_number, attempts
    guess = int(request.form['guess'])
    attempts += 1
    
    if guess > secret_number:
        message = "Your guess is too high!"
    elif guess < secret_number:
        message = "Your guess is too low!"
    else:
        message = f"Congratulations! You've guessed the number in {attempts} attempts. Wanna play again? Click Restart!"
        secret_number = random.randint(1, 100)  # Reset the game
    
    return render_template('index.html', message=message, attempts=attempts)

if __name__ == '__main__':
    app.run(debug=True)
