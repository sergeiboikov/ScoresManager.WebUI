from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, City
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email doesn"t exist.', category='error')
    return render_template('login.html', user=current_user)


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth_blueprint.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    cities = City.query.filter(City.name != 'Default')
    default_city = City.query.filter_by(name='Default').first()

    if request.method == 'POST':
        email = str(request.form.get('email'))
        full_name = str(request.form.get('name'))
        city_id = request.form['city']
        user_yc_id = request.form.get('user_yc_id')
        notes = request.form.get('notes')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(full_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        # TODO: Uncomment before release
        # elif len(password1) < 7:
        #     flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, name=full_name, city_id=city_id, user_yc_id=user_yc_id, notes=notes, password=generate_password_hash(
                password1, method='sha256'), is_active=True)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user, cities=cities, default_city=default_city)
