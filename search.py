import drinks
from fuzzywuzzy import fuzz
from operator import itemgetter

def search(ingredients: list):
    scores = []
    for drink in drinks.drinks:
        score = 0
        for ingredient in ingredients:
            individual_score = []
            for ing in drink.ingredients:
                individual_score.append(fuzz.partial_ratio(ingredient, ing))
            score += max(individual_score)
        score /= len(ingredients)
        scores.append(score)
    results = []
    for pos in range(len(scores)):
        results.append((scores[pos], drinks.drinks[pos]))
    results.sort(key=itemgetter(0))
    return results

search_results = search(['honey', 'lemon', 'gin'])
for i in range(1, 4):
    print(str(search_results[-i][0]) + '\n', search_results[-i][1])