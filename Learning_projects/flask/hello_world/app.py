from flask import Flask, request, render_template, url_for, session
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
app = Flask(__name__)

app.secret_key = 'development_key'

# debug=True for development in console
# $env:FLASK_ENV = "development"

@app.route('/')
def hello_world():
    if 'username' in session:
        return f"User is logged in as {session['username']} "
    return "User is not logged in."
    # app.logger.debug('Hello World from debug')
    # app.logger.info(f'currently in path: {request.path}')
    # app.logger.warning('Hello World from warning')
    # app.logger.error('Hello World from error')
    #return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('hello_world'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('hello_world'))

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name.upper()}"

@app.route("/age/<int:age>")
def age(age):
    return f"Your age is: {age}"

@app.route("/show/<name>", methods=['GET', 'POST'])
def show_name(name):
    # return f"Your name is: {name}"
    return render_template('show.html', name=name)

@app.route("/redirect")
def redirect_():
    return redirect(url_for('show_name', name='John'))

@app.route("/exit")
def exit():
    return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404

@app.route("/api/show/<name>")
def api_show_name(name):
    return {'name': name, 'method': request.method}