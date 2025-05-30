from flask import Flask
from flask import render_template

# Это callable WSGI-приложение
app = Flask(__name__)


users = [
  {
    'id': 4,
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'johndoe@gmail.com',
  },
  {
    'id': 5,
    'first_name': 'John5',
    'last_name': 'Doe5',
    'email': 'johndoe5@gmail.com',
  },  
]


@app.route("/")
def hello_world():
    #return "Welcome to Flask! 2"
    return [1, 2, 3, "root"]


@app.route("/courses/<id>")
def courses_show(id):
    return f"Course id: {id}"


@app.route("/users/")
def users_get():
    return render_template(
        "users/index.html",
        users=users,
    )


@app.route("/users/<user_id>")
def user_show(user_id):
    users_found = list(filter(lambda u: str(u['id']) == user_id, users))
    if not users_found:
      return "Page not found", 404
    return render_template(
        "users/show.html",
        user=users_found[0],
    )