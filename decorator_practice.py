class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def authentication_decorator(function):
    def wrapper(*args):
        if args[0].is_logged_in:
            return function(args[0])
    return wrapper


@authentication_decorator
def create_blog(user):
    print(f"This is {user.name}'s blog post. ")


new_user = User("Mat")
new_user.is_logged_in = True
create_blog(new_user)


def logging_decorator(function):
    def wrapper(*args):
        print(f"You've called: {function.__name__}{args}\nIt returned: {function(*args)}")
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a + b + c


a_function(1, 2, 3)


