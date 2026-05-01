from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Task

tasks_bp = Blueprint("tasks",__name__)

@tasks_bp.route('/view', methods=['GET'])
def view_tasks():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    
    user_id = session['user_id']
    tasks =Task.query.filter_by(user_id=user_id).all()
    return render_template("tasks.html", tasks=tasks)

@tasks_bp.route("/add", methods=["POST"])
def add_tasks():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status="Pending", user_id=session["user_id"])
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully", "success")
    
    return redirect(url_for("tasks.view_tasks"))

@tasks_bp.route("/change/<int:task_id>", methods=["POST"])
def change_status(task_id):
    task = Task.query.get(task_id)

    if task:

        if task.user_id != session['user_id']:
            flash('danger')
            return redirect(url_for('tasks.view_tasks'))

        if task.status == "Pending":
            task.status = "working"
        elif task.status == "working":
            task.status = "Done"
        else:
            task.status = "Pending"
        db.session.commit()
    return redirect(url_for("tasks.view_tasks"))

@tasks_bp.route("/clear/<int:task_id>", methods=["POST"])
def clear_tasks(task_id):
    task = Task.query.get(task_id)

    if task:
        if task.user_id != session['user_id']:
            flash('danger')
            return redirect(url_for('tasks.view_tasks'))

        db.session.delete(task)
        db.session.commit()
        flash("Task cleared!", "info")
    return redirect(url_for("tasks.view_tasks"))

@tasks_bp.route("/clearall/",methods=["POST"])
def clear_all():

    Task.query.filter_by(user_id = session['user_id']).delete()
    db.session.commit()
    flash("All task cleared!", "info")
    return redirect(url_for("tasks.view_tasks"))