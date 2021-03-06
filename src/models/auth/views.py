from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from src import User, db
from src.models.auth.forms import LoginForm, RegistrationForm

auth_blueprint = Blueprint('auth', __name__,  url_prefix="/auth")


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('recipient.index'))
        flash('Invalid username or password.')
    else:
        errors = form.errors.items()
        return render_template('auth/login.html', form=form, errors=errors)
    return render_template('auth/login.html', form=form)


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('recipient.index'))


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    else:
        errors = form.errors.items()
        return render_template('auth/register.html', form=form, errors=errors)
    return render_template('auth/register.html', form=form)

