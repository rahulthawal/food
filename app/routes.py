from flask import request
from .recipes import Recipes

from . import app


@app.get("/recipes")
def get_recipe_names():
    recipes = [recipe.get("name") for recipe in Recipes.load()]
    return {"recipeNames": recipes}


@app.get("/recipes/details/<name>")
def get_recipe_by_name(name):
    response = {}
    recipes: list = Recipes.load()
    recipe = Recipes.get_by_name(recipes, name)

    if recipe:
        response = {
            "details": {
                "ingredients": recipe.get("ingredients"),
                "numSteps": len(recipe.get("instructions")),
            }
        }

    return response


@app.post("/recipes")
def insert_recipe():
    data = request.get_json()
    recipes = Recipes.load()
    existing_recipe = Recipes.get_by_name(recipes, data.get("name"))

    if existing_recipe:
        return {"error": "Recipe already exists"}, 400

    recipes.append(data)
    Recipes.write(recipes)
    return "", 201


@app.put("/recipes")
def update_recipe():
    data = request.get_json()
    recipes = Recipes.load()
    existing_recipe = Recipes.get_by_name(recipes, data.get("name"))

    if not existing_recipe:
        return {"error": "Recipe doesn't exists"}, 404

    Recipes.update_recipe(existing_recipe, data)
    Recipes.write(recipes)
    return "", 204
