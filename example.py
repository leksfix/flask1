from flask import Flask
import logging
from flask import render_template, request

# Это callable WSGI-приложение
app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)

users = [
  {"id": 1, "first_name": "mike"},
  {"id": 2, "first_name": "mishel"},
  {"id": 3, "first_name": "adel"},
  {"id": 4, "first_name": "keks"},
  {"id": 5, "first_name": "kamila"},
  {
    'id': 40,
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'johndoe@gmail.com',
  },
  {
    'id': 50,
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
    query = request.args.get('query')
    if query:
      app.logger.debug('Users filtered by "{query}"')
      filtered_users = filter(lambda u: u["first_name"].find(query) >=0, users)
    else:
       app.logger.debug("All users selected")
       filtered_users = users
       query = ''
    return render_template(
        "users/index.html",
        users=filtered_users, search=query
    )


@app.route("/users/<user_id>")
def user_show(user_id):
    users_found = list(filter(lambda u: str(u['id']) == user_id, users))
    if not users_found:
      app.logger.error(f"User not found: {user_id}")
      return "Page not found", 404
    return render_template(
        "users/show.html",
        user=users_found[0],
    )