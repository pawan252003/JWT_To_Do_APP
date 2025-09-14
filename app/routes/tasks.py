from flask import Blueprint, request, jsonify
from app.models import Task
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

tasks_bp = Blueprint('tasks', __name__, url_prefix="/tasks")

#View Task
@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": t.id, "title": t.title, "status": t.status} for t in tasks])

# Add task
@tasks_bp.route('/', methods=['POST'])
@jwt_required()
def add_task():
    data = request.get_json()
    user_id = get_jwt_identity()
    task = Task(title=data['title'], user_id=user_id)
    db.session.add(task)
    db.session.commit()
    return jsonify({"msg": "Task added", "task": {"id": task.id, "title": task.title, "status": task.status}}), 201

# Toggle status
@tasks_bp.route('/<int:task_id>', methods=['PUT'])
@jwt_required()
def toggle_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first_or_404()
    task.status = {"Pending": "Working", "Working": "Done", "Done": "Pending"}[task.status]
    db.session.commit()
    return jsonify({"msg": "Task status updated", "task": {"id": task.id, "title": task.title, "status": task.status}})


# Delete task
@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    return jsonify({"msg": "Task deleted"})


# Clear all tasks
@tasks_bp.route('/clear', methods=['DELETE'])
@jwt_required()
def clear_tasks():
    user_id = get_jwt_identity()
    Task.query.filter_by(user_id=user_id).delete()
    db.session.commit()
    return jsonify({"msg": "All tasks cleared"})