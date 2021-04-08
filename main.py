from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_italic(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper



@app.route("/bye/")
@make_bold
@make_italic
@make_underlined
def bye():
    return "Bye!"


@app.route("/gif")
def gif():
    return "<img src='https://media.giphy.com/media/3oEjHOg7qLtB6AqLo4/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)