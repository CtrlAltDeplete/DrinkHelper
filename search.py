import drinks
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def search(ingredients: list):
    scores = []
    for drink in drinks.drinks:
        score = 0
        for ingredient in ingredients:
            for ing in drink.ingredients:
                score += fuzz.partial_ratio(ingredient, ing)
        score /= len(drink.ingredients)
        scores.append(score)
    return drinks.drinks[scores.index(max(scores))]

print(search(['gin', 'lemon juice']))