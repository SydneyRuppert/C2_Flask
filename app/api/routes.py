from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, Contact, contact_schema, contacts_schema

api = Blueprint('api',__name__, url_prefix='/api')


#Creating
@api.route('/cars2', methods = ['POST'])
#@token_required
def create_car():

    print(request.json)
    name = request.json['name']
    email = request.json['email']
    phone_number = request.json['phone_number']
    address = request.json['address']
    car_make=request.json['car_make']
    car_model=request.json['car_model']
    car_year=request.json['car_year']
    uid = request.json['uid']
    

    #print(f'BIG TESTER: {current_user_token.token}')




    contact = Contact(name, email, phone_number, address, car_make, car_model, car_year, uid )
    print(contact)
    db.session.add(contact)
    db.session.commit()

    response = contact_schema.dump(contact)
    return jsonify(response)
#Retrieving all 
@api.route('/cars2/user/<uid>', methods=['GET'])
#@token_required
def get_all_cars(uid):
    contacts=Contact.query.filter_by(uid=uid).all()
    response=contacts_schema.dump(contacts)
    return jsonify(response)


#Retrieving single
@api.route('cars2/<id>',methods=['GET'])
#@token_required
def get_single_car(id):
    contact=Contact.query.get(id)
    response=contact_schema.dump(contact)
    return jsonify(response)

#Updating
@api.route('/cars2/<id>', methods=['POST','PUT'])
#@token_required
def update_car( id):
    contact=Contact.query.get(id)
    uid= request.json['uid']
    if contact.uid != uid:
        return {'status':"invalid user"}, 400
    contact.name = request.json['name']
    contact.email = request.json['email']
    contact.phone_number = request.json['phone_number']
    contact.address = request.json['address']
    contact.car_make = request.json['car_make']
    contact.car_model  =request.json['car_model']
    contact.car_year = request.json['car_year']

    db.session.commit()
    response = contact_schema.dump(contact)
    return jsonify(response)

#Deleting car
@api.route('/cars2/<id>', methods=['DELETE'])
#@token_required
def delete_car(id):
    contact= Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    response= contact_schema.dump(contact)
    return jsonify(response)