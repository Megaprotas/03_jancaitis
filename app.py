from flask import Flask, render_template, flash, redirect, request, url_for, session
from config import Config
from forms import LoginForm, RegisterForm
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId
import bcrypt
import re
import math
import os

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "mytestdb"
app.config["MONGO_URI"] = os.environ.get("MONGODB_URI")
app.config.from_object(Config)

mongo = PyMongo(app)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if session.get('logged_in'):
        if session['logged_in'] is True:
            return redirect(url_for('get_ingredients'))

    form = LoginForm()

    if form.validate_on_submit():
        users = mongo.db.users
        db_user = users.find_one({'name': request.form['username']})
        if db_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                             db_user['password']) == db_user['password']:
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('get_ingredients', form=form))
            flash('Wrong username/password')
    return render_template('login.html', form=form, page_title="Log in")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('get_ingredients'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hash_pass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'name': request.form['username'],
                          'password': hash_pass,
                          'email': request.form['email']})
            session['username'] = request.form['username']
            return redirect(url_for('get_ingredients'))
        flash('Username already exists')
        return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form, page_title="Sign up")


@app.route('/')
@app.route('/get_ingredients')
def get_ingredients():
    return render_template('ingredients.html', ingredients=mongo.db.ingredients.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           origins=mongo.db.origins.find(),
                           types=mongo.db.types.find(),
                           users=mongo.db.users.find(),
                           times=mongo.db.times.find(),
                           alergens=mongo.db.alergens.find(),
                           page_title="Add the recipe")


@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    ingredients = mongo.db.ingredients
    ingredients.insert_one(request.form.to_dict())
    return redirect(url_for('get_ingredients'))


@app.route('/edit_recipe/<ingredient_id>')
def edit_recipe(ingredient_id):
    editable_recipe = mongo.db.ingredients.find_one({"_id": ObjectId(ingredient_id)})
    origins_list = mongo.db.origins.find()
    types_list = mongo.db.types.find()
    users_list = mongo.db.users.find()
    time_list = mongo.db.users.find()
    alergens_list = mongo.db.users.find()
    return render_template('editrecipe.html', ingredient=editable_recipe,
                                              origins=origins_list,
                                              types=types_list,
                                              users=users_list,
                                              times=time_list,
                                              alergens=alergens_list,
                                              page_title="Edit the recipe")


@app.route('/update_recipe/<ingredient_id>', methods=['POST'])
def update_recipe(ingredient_id):
    ingredients = mongo.db.ingredients
    ingredients.update({'_id': ObjectId(ingredient_id)},
        {
        'type_name': request.form.get('type_name'),
        'name': request.form.get('name'),
        'region_of_origin': request.form.get('region_of_origin'),
        'dish_name': request.form.get('dish_name'),
        'image': request.form.get('image'),
        'prep_time': request.form.get('prep_time'),
        'cooking_time': request.form.get('cooking_time'),
        'serves': request.form.get('serves'),
        'ingredient_1': request.form.get('ingredient_1'),
        'ingredient_2': request.form.get('ingredient_2'),
        'ingredient_3': request.form.get('ingredient_3'),
        'ingredient_4': request.form.get('ingredient_4'),
        'ingredient_5': request.form.get('ingredient_5'),
        'ingredient_6': request.form.get('ingredient_6'),
        'ingredient_7': request.form.get('ingredient_7'),
        'ingredient_8': request.form.get('ingredient_8'),
        'ingredient_9': request.form.get('ingredient_9'),
        'ingredient_10': request.form.get('ingredient_10'),
        'cooking_description': request.form.get('cooking_description'),
        'vegeterian': request.form.get('vegeterian'),
        'vegan': request.form.get('vegan'),
        'gluten_free': request.form.get('gluten_free'),
        'milk': request.form.get('milk'),
        'peanut': request.form.get('peanut'),
        'egg': request.form.get('egg'),
        'soy': request.form.get('soy'),
        'wheat': request.form.get('wheat'),
        'fruit': request.form.get('fruit'),
        'corn': request.form.get('corn'),
        'garlic': request.form.get('garlic'),
        'other': request.form.get('other')
        })
    return redirect(url_for('get_ingredients'))


@app.route('/delete_recipe/<ingredient_id>', methods=["POST"])
def delete_recipe(ingredient_id):
    mongo.db.ingredients.remove({'_id': ObjectId(ingredient_id)})
    return redirect(url_for('get_ingredients'))


@app.route('/search')
def search():
    search_field = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(search_field)), '$options': 'i'}
    results = mongo.db.ingredients.find({
        '$or': [
            {'dish_name': query},
            {'type_name': query},
            {'region_of_origin': query}
        ]
    })
    return render_template('search.html', query=search_field, results=results, page_title='Search results')


@app.route('/get_ingredients_like/<ingredient_id>', methods=["GET", "POST"])
def get_ingredients_like(ingredient_id):
    ingredient = mongo.db.ingredients
    ingredient.find_one_and_update(
        {'_id': ObjectId(ingredient_id)},
        {
            '$inc': {'vote': 1}
        })
    return redirect(url_for('get_ingredients'))


@app.route('/get_ingredients_max_value')
def get_ingredients_max_value():
    most_popular = mongo.db.ingredients.find().sort([('vote', DESCENDING)]).limit(1)
    """change to find_one and remove limit"""
    return render_template('ingredients.html', ingredients=most_popular)


if __name__ == '__main__':
    app.run(debug=True)