from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import Item, ItemList   # import the Item and ItemList classes
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity

app = Flask(__name__)
app.debug = True
app.secret_key = 'development_key'


api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>') # Route_1
api.add_resource(ItemList, '/items') # Route_2





