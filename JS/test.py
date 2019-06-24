"""
import unittest

from flask_pymongo import PyMongo

import app as app_module

app = app_module.app

app.config["TESTING"] = True
app.config["WTF_CSRF_ENABLED"] = False
app.config["MONGO_DBNAME"] = "mytestdb"
""" app.config["MONGO_URI"] = "mongodb://Eddie:abc123@ds127995.mlab.com:27995/mytestdb" """

mongo = PyMongo(app)
app_module.mongo = mongo


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            mongo.db.users.delete_many({})
            mongo.db.ingredients.delete_many({})


class AppTests(AppTestCase):
    def get_ingredients_test(self):
        test_result = self.client.get('/get_ingredients')
        data = test_result.data.decode('utf-8')
        assert test_result.status == '200 OK'
        assert 'Some Curry' in data

    def register_test(self):
        test_result = self.client.post('/register', follow_redirects=True, data=dict(
            username='JohnDoe',
            password='123456',
            password2='123456',
            email='forest.lithuania@gmail.com',
        ))
        data = test_result.data.decode('utf-8')
        assert test_result.status == '200 OK'
        assert 'milestone_project04' in data

    def test_insert_recipe(self):
        test_result = self.client.post('/insert_recipe', follow_redirects=True, data={
            'dish_name': 'Some curry',
            'cooking_description': 'Some long read text'
        })
        data = test_result.data.decode('utf-8')
        assert 'Some Curry' in data

"""
