from flask import Blueprint, jsonify, abort, request
from ..models import Contact

bp = Blueprint('contacts', __name__,
               url_prefix='/contacts')