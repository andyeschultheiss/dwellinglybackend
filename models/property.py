from db import db
from models.user import UserModel

class PropertyModel(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(250))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zipcode = db.Column(db.String(20))
    propertyManager = db.Column(db.Integer(), db.ForeignKey('users.id'))
    tenants = db.Column(db.Integer())
    dateAdded = db.Column(db.String(50))
    archived = db.Column(db.Boolean)


    def __init__(self, name, address, city, state, zipcode, propertyManager, tenants, dateAdded, archived):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.propertyManager = propertyManager
        self.tenants = tenants
        self.dateAdded = dateAdded
        self.archived = False

    def json(self):
        return {
            'id': self.id, 
            'name':self.name, 
            'address': self.address, 
            'city': self.city, 
            'state': self.state, 
            'zipcode': self.zipcode,
            'propertyManager': self.propertyManager,
            'tenants': self.tenants,
            'dateAdded': self.dateAdded,
            'archived': self.archived
        }
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() #SELECT * FROM property WHERE id = id LIMIT 1
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
