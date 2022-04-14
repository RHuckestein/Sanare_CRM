
from flask import Blueprint, jsonify, abort, request
from ..models import Refferal_accounts, db, Employees, refferal_account_contact_table

bp = Blueprint('refferal_accounts', __name__,
               url_prefix='/refferal-accounts')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    refferal_accounts = Refferal_accounts.query.all()  # ORM performs SELECT query
    result = []
    for r in refferal_accounts:
        result.append(r.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'employee_id' not in request.json or 'phone' not in request.json:
        return abort(400)
    # user with id of user_id must exist
    Employees.query.get_or_404(request.json['employee_id'])
    # construct Tweet
    t = Refferal_accounts(
        id=request.json['id'],
        employee_id=request.json['employee_id'],
        company_name=request.json['company_name'],
        phone=request.json['phone'],
        email=request.json['email'],
        address=request.json['address'],
        city=request.json['city'],
        state=request.json['state'],
        zip_code=request.json['zip_code'],
        industry=request.json['industry']
    )
    db.session.add(t)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(t.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    t = Refferal_accounts.query.get_or_404(id)
    try:
        db.session.delete(t)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)