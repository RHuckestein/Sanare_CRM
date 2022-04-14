from flask import Blueprint, jsonify, abort, request
from ..models import Employees, db
import hashlib
import secrets


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('employees', __name__,
               url_prefix='/employees')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    employees = Employees.query.all()  # ORM performs SELECT query
    result = []
    for t in employees:
        result.append(t.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id: int):
    u = Employees.query.get_or_404(id)
    # req body must contain user_id and content
    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        u.username = request.json['username']

    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        u.password = scramble(request.json['password'])

    u.first_name = request.json['first_name']
    u.last_name = request.json['last_name']
    u.phone = request.json['phone']
    u.email = request.json['email']

    try:
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)
