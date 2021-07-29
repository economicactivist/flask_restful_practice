from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import Item
from flask_restful import Api

app = Flask(__name__)
app.debug = True
app.secret_key = 'development_key'


api = Api(app)

api.add_resource(Item, '/item/<string:name>') # Route_1





