from flask import Flask

# Это callable WSGI-приложение
app = Flask(__name__)

@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'

@app.route('/')
def hello_world():
    return 'Welcome to Flask!'

@app.get('/users')
def users_get():
    return 'GET /users'



@app.post('/users')
def users():
    return 'Users', 302