
from flask import app, request
from flask_restful import Resource

items = []

class Item(Resource):
    def get(self, name):
        # app.logger.debug('GET %s', name)
        global items
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            return {'message': 'Item not found'}, 404
        return item

    def post(self, name):
        # app.logger.debug('POST %s', name)
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

      
    def delete(self, name):
        # app.logger.debug('DELETE %s', name)
        global items
        items = [item for item in items if item['name'] != name]
        return {'message': 'Item deleted'}, 200

    def put(self, name):
        # app.logger.debug('PUT %s', name)
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': 12.99}
            items.append(item)
        else:
            item.update({'price': 12.99})
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items} if items else {'items': 'No items'}




