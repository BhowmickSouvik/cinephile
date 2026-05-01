from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.routes.forms import LoginForm, RegisterForm
from app.models import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth',__name__)


@auth_bp.route("/")
def home():
    if 'user_id' in session:
        return redirect(url_for('tasks.view_tasks'))
    else:
        return redirect(url_for('auth.register'))


@auth_bp.route("/register", methods=["GET","POST"])
def register():
    if 'user_id' in session:
        return redirect(url_for('tasks.view_tasks'))

    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data

        exist_user = User.query.filter_by(email = email).first()

        if exist_user:
            flash("you have alredy registerd")
            return redirect(url_for("auth.login"))

        new_user = User(
            name = form.name.data,
            email = form.email.data,
            password = generate_password_hash(form.password.data)
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Registered successfull!","success")
        return redirect(url_for("auth.login"))

    return render_template("register.html",form=form)



@auth_bp.route('/login', methods=["GET","POST"])
def login():
    if 'user_id' in session:
        return redirect(url_for('tasks.view_tasks'))
    form = LoginForm()
    if form.validate_on_submit(): 
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            session['user_id'] = user.id #crated user.id
            session.permanent = True
            flash('Login Successful','success')

            return redirect(url_for('tasks.view_tasks'))
        
        elif user and not check_password_hash(user.password,password):
            flash("Invalid password!","danger")


        else:
            flash("Invalid user!")
            return redirect(url_for("auth.register"))

    return render_template('login.html',form=form)
 

@auth_bp.route('/logout')
def logout():
    session.pop('user_id',None)
    flash('Logged out','info')
    return redirect(url_for("auth.login"))