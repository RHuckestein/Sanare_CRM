from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()

# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships


class Employees(db.Model):
    _tablename_ = 'employees'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    username = db.Column(db.String(50),
                         autoincrement=False, nullable=False, unique=True)
    password = db.Column(db.String(50),
                         autoincrement=False, nullable=False, unique=True)
    first_name = db.Column(db.String(50),
                           autoincrement=False, nullable=False)
    last_name = db.Column(db.String(50),
                          autoincrement=False, nullable=False)
    phone = db.Column(db.String(50),
                      autoincrement=False, nullable=False, unique=True)
    email = db.Column(db.String(50),
                      autoincrement=False, nullable=False, unique=True)
    refferal_accounts = db.relationship(
        'Refferal_accounts', backref='employees', cascade="all,delete")

    def __init__(self, username: str, password: str, first_name: str, last_name: str, phone: str, email: str):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email
        }


refferal_account_contact_table = db.Table(
    'refferal_account_contacts',
    db.Column(
        'contact_id', db.Integer,
        db.ForeignKey('employees.id'),
        primary_key=True
    ),

    db.Column(
        'refferal_account_id', db.Integer,
        db.ForeignKey('refferal_accounts.id'),
        primary_key=True
    ),
)


class Refferal_accounts(db.Model):
    _tablename_ = 'refferal_accounts'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    date_created = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, autoincrement=True, nullable=False)
    company_name = db.Column(
        db.String(50), autoincrement=False, nullable=False)
    phone = db.Column(db.String(50), autoincrement=False, nullable=False)
    email = db.Column(db.String(50), autoincrement=False, nullable=False)
    address = db.Column(db.String(50), autoincrement=False, nullable=False)
    city = db.Column(db.String(50), autoincrement=False, nullable=False)
    state = db.Column(db.String(2), autoincrement=False, nullable=False)
    zip_code = db.Column(db.String(5), autoincrement=False, nullable=False)
    industry = db.Column(db.String(50), autoincrement=False, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey(
        'employees.id'), nullable=True)

    def __init__(self, id: int, company_name: str, phone: str, email: str, address: str, city: str, state: str, zip_code: str, industry: str, employee_id: int):
        self.id = id
        self.company_name = company_name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.industry = industry
        self.employee_id = employee_id

    def serialize(self):
        return {
            'id': self.id,
            'date_created': self.date_created.isoformat(),
            'company_name': self.company_name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'industry': self.industry,
            'employee_id': self.employee_id
        }


# refferal_account_contacts = db.Table(
#     'refferal_account_contacts',
#     db.Column('contact_id', db.Integer, db.ForeignKey('contacts.id'),
#               primary_key=True, autoincrement=False, nullable=False),
#     db.Column('refferal_account_id', db.Integer, db.ForeignKey(
#         'refferal_accounts.id'), primary_key=True, autoincrement=False, nullable=False)
# )


class Contact(db.Model):
    _tablename_ = 'contacts'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    first_name = db.Column(db.String(50),
                           autoincrement=False, nullable=False)
    last_name = db.Column(db.String(50),
                          autoincrement=False, nullable=False)
    phone = db.Column(db.String(50),
                      autoincrement=False, nullable=False)
    email = db.Column(db.String(50),
                      autoincrement=False, nullable=False, unique=True)

    # def __init__(self, first_name: str, last_name: str, phone: str, email: str):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.phone = phone
    #     self.email = email

    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'first_name': self.first_name,
    #         'last_name': self.last_name,
    #         'phone': self.phone,
    #         'email': self.email
    #     }
