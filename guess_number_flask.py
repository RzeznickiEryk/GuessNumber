from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def guess_number_flask():
    minimum = int(request.form.get('min', 1))
    maximum = int(request.form.get('max', 1000))
    guess = request.form.get('guess')

    if request.method == 'POST':
        answer = request.form.get('action')

        if answer == 'too_small':
            minimum = int(guess)
        elif answer == 'too_big':
            maximum = int(guess)
        elif answer == 'you_win':
            return "you win"

    guess = int((maximum - minimum) / 2) + minimum

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Guess Number Flask</title>
    </head>
    <body>
        <h1>I will guess your number in range of 1 to 1000</h1>
        <form method="POST">
            <input type="hidden" name="min" value="{minimum}">
            <input type="hidden" name="max" value="{maximum}">
            <input type="hidden" name="guess" value="{guess}">
            {f"<p>Is your number {guess}?</p>" if guess else ""}
            <button type="submit" name="action" value="too_small">Too small</button>
            <button type="submit" name="action" value="too_big">Too big</button>
            <button type="submit" name="action" value="you_win">You win</button>
        </form>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)
