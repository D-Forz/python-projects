from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate

from models import User
from database import db
from forms import UserForm

app = Flask(__name__)

# BD configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# flask-migrate configuration
migrate = Migrate(app, db)

# flask-wtf configuration
app.config['SECRET_KEY'] = 'mysecretkey'



@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    users = User.query.all()
    total_users = User.query.count()
    app.logger.debug(f'users list: {users}')
    app.logger.debug(f'total users: {total_users}')
    return render_template('home.html', users=users, total_users=total_users)

@app.route('/details/<int:id>')
def details(id):
    # user = User.query.get(id)
    user = User.query.get_or_404(id)
    app.logger.debug(f'user: {user}')
    return render_template('details.html', user=user)

@app.route('/add', methods=['GET', 'POST'])
def add():
    user = User()
    userForm = UserForm(obj=user)
    if request.method == 'POST':
        if userForm.validate_on_submit():
            userForm.populate_obj(user)
            app.logger.debug(f'user to insert: {user}')
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('add.html', form=userForm)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    user = User.query.get_or_404(id)
    userForm = UserForm(obj=user)
    if request.method == 'POST':
        if userForm.validate_on_submit():
            userForm.populate_obj(user)
            app.logger.debug(f'user to update: {user}')
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('edit.html', form=userForm)

@app.route('/delete/<int:id>')
def delete(id):
    user = User.query.get_or_404(id)
    app.logger.debug(f'user to delete: {user}')
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))