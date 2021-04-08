from flask import Flask
import random

LOW = 1
HIGH = 10
NUMBER = random.randint(LOW, HIGH)
app = Flask(__name__)



def make_header(function):
    def wrapper():
        return f"<h1>{function()}</h1>"
    return wrapper


def make_center(function):
    def wrapper():
        return f"<center>{function()}</center>"
    return wrapper


@app.route("/")
@make_header
@make_center
def hello():
    return f"Guess the number between {LOW} and {HIGH}<br>" \
           f"<img src='https://media.giphy.com/media/UDU4oUJIHDJgQ/giphy.gif'>"




@app.route("/<int:guess>")
def num_check(guess):
    if guess == NUMBER:
        return f"You've got it right!<br>" \
               f"<img src='https://media.giphy.com/media/l3vRcttCynxJoxIrK/giphy.gif'>"
    elif guess > NUMBER:
        return f"Your guess is too high!<br>" \
               f"<img src='https://media.giphy.com/media/eslk6GMwjUYq50A3Jl/giphy.gif'>"
    else:
        return f"Your guess is too low!<br>" \
               f"<img src='https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif'>"



if __name__ == "__main__":
    app.run(debug=True)