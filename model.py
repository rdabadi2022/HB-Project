from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Health_Condition(db.Model):
    """Data model for health condition."""
    __tablename__= "health_conditions"

    condition_id = db.Column(db.Integer, primary_key = True, autoincrement=True, nullable = False)
    condition_name = db.Column(db.String(50), nullable = False)
    condition_description = db.Column(db.String(), nullable = False)
    min_carbs = db.Column(db.Integer)
    max_carbs = db.Column(db.Integer)
    min_Cholesterol = db.Column(db.Integer)
    max_Cholesterol = db.Column(db.Integer)
    min_SaturatedFat = db.Column(db.Integer)
    max_SaturatedFat = db.Column(db.Integer)
    min_Sugar = db.Column(db.Integer)
    max_Sugar = db.Column(db.Integer)
    min_Iron = db.Column(db.Integer)



def connect_to_db(flask_app, db_uri="postgresql:///health", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


# class Recipe(db.model):
#     """Data model for recipe."""
#     __tablename__= "recipes"

#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String(250))
#     image = db.Column(db.String(250))
#     calories = db.Column(db.Integer)
#     protein = db.Column(db.String(10))
#     fat = db.Column(db.String(10))
#     carbs = db.Column(db.String(10))

#     def __repr__(self):
#         return f"<Recipe(id={self.id}, title='{self.title}')>"
#     # Assuming you have already created the database and connected to it
# # ...

# # Function to populate the recipes table
# def populate_recipes(data):
#     for recipe_data in data:
#         recipe = Recipe(
#             id=recipe_data['id'],
#             title=recipe_data['title'],
#             image=recipe_data['image'],
#             calories=recipe_data['calories'],
#             protein=recipe_data['protein'],
#             fat=recipe_data['fat'],
#             carbs=recipe_data['carbs']
#         )
#         db.session.add(recipe)
    
#     db.session.commit()
#     print("Recipes table populated successfully!")

# Assuming you have retrieved the data from the API and stored it in a variable called `api_data`
# ...

# Call the function to populate the recipes table
# populate_recipes(api_data)






    

