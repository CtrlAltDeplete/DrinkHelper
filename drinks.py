import ingredients
import copy

class Drink:
    def __init__(self, name: str, ingredients: list, directions: list):
        self.name = name
        self.ingredients = ingredients
        self.directions = directions

    def __str__(self):
        s = self.name + '\nIngredients:'
        for ingredient in self.ingredients:
            s += '\n' + ingredient
        s += '\nDirections:'
        for direction in self.directions:
            s += '\n' + direction
        return s

    def get_ingredients(self):
        raw_ingredients = copy.deepcopy(self.ingredients)
        processed_ingredients = []
        for raw_ingredient in raw_ingredients:
            for ing in ingredients.ingredients:
                if ing in raw_ingredient.lower():
                    processed_ingredients.append(ing)
                    if not ' or ' in raw_ingredient.lower():
                        break
        return processed_ingredients

drinks = [
    Drink('Cupid Cocktail', ['2 ounces of Sherry', '1 fresh egg', '1 teaspoon of powdered sugar', 'a little cayenne pepper'], ['Shake well', 'Strain into medium-sized glass']),
    Drink('El Presidente', ['1 1/2 ounces of light rum', '1/2 ounces of dry vermouth', '1/2 ounces of orange curacao', '1 dash of grenadine'], ['Shake ingredients over ice', 'Strain into a chilled cocktail glass', 'Garnish with orange twist']),
    Drink('Manhattan', ['2 ounces of rye or bourbon', '1/2 ounces sweet vermouth', 'a dash of bitters'], ['Stir with cracked ice and strain', 'Serve with cherry']),
    Drink('Bloody Mary', ['1 1/2 ounces of vodka', '3 ounces of tomato juice', '1/2 ounce of lemon juice', '1 dash of Worcestershire sauce', '1 dash of celery salt', '1 dash of hot sauce'], ['Thoroughly shake all ingredients with ice', 'Strain into tall or squat 8-ounce glass', 'Decorate with celery']),
    Drink('Dark & Stormy', ['2 ounces of dark rum', '3 ounces of ginger beer', '1/2 ounce of lime juice'], ['Combine ingredients in tall glass full of ice', 'Stir']),
    Drink('Bulldog', ['3/4 ounce of gin', '1 1/2 ounces of cherry brandy', 'juice of 1/2 a lime'], ['Shake well with ice', 'strain into pre-chilled cocktail glass'])
]

for drink in drinks:
    print(drink.name, drink.get_ingredients())