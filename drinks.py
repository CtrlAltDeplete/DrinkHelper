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

drinks = [
    Drink('Cupid Cocktail', ['2 ounces of Sherry', '1 fresh egg', '1 teaspoon of powdered sugar', 'a little cayenne pepper'], ['Shake well', 'Strain into a medium-sized glass']),
    Drink('El Presidente', ['1 1/2 ounces of light rum', '1/2 ounces of dry vermouth', '1/2 ounces of orange curacao', '1 dash of grenadine'], ['Shake ingredients over ice', 'Strain into a chilled cocktail glass', 'Garnish with orange twist']),
    Drink('Manhattan', ['2 ounces of rye or bourbon', '1/2 ounces sweet vermouth', 'a dash of bitters'], ['Stir with cracked ice and strain', 'Serve with cherry']),
    Drink('Bloody Mary', ['1 1/2 ounces of vodka', '3 ounces of tomato juice', '1/2 ounce of lemon juice', '1 dash of Worcestershire sauce', '1 dash of celery salt', '1 dash of hot sauce'], ['Thoroughly shake all ingredients with ice', 'Strain into tall or squat 8-ounce glass', 'Decorate with celery']),
    Drink('Dark & Stormy', ['2 ounces of dark rum', '3 ounces of ginger beer', '1/2 ounce of lime juice'], ['Combine ingredients in tall glass full of ice', 'Stir']),
    Drink('Bulldog', ['3/4 ounce of gin', '1 1/2 ounces of cherry brandy', 'juice of 1/2 a lime'], ['Shake well with ice', 'strain into pre-chilled cocktail glass']),
    Drink('Mimosa', ['3 ounces of Champagne', '3 ounces of orange juice'], ['Combine in a chilled stem glass', 'Garnish with orange']),
    Drink('Americana', ['1 teaspoon of 100-proof bourbon', '4 ounces of iced Champagne', '1/2 teaspoon of sugar', '1 dash of bitters', '1 slice of fresh peach'], ['Stir bourbon, bitters, and sugar into a pre-chilled Champagne glass', 'Add champagne and peach slice']),
    Drink('Rob Roy', ['1 1/2 ounces of Scotch whisky', '3/4 ounce sweet vermouth', 'dash of bitters (optional)'], ['Shake well with cracked ice', 'Strain into a chilled cocktail glass or serve with ice in an Old Fashioned glass']),
    Drink('Grasshopper', ['1 ounce of green creme de menthe', '1 ounce of white creme de cacao', '1 ounce of heavy cream'], ['Combine and strain through cracked ice']),
    Drink('Corkscrew', ['1 1/2 ounces of light rum', '1/2 ounce of dry vermouth', '1/2 ounce of peach liqueur', '1 slice of lime'], ['Shake well', 'Strain into pre-chilled cocktail glass', 'Add lime slice']),
    Drink('Zombie', ['1 1/4 ounces of heavy-bodied rum', '1 1/4 ounces of white rum', '1 1/4 ounces of gold rum', '1 ounce of lime juice', '1 ounce of lemon juice', '1 ounce of unsweetened pineapple juice', '1 dash of bitters'], ['Shake with cracked ice', 'Pour unstrained into a goblet', 'Decorate with fruit']),
    Drink('Sloe Gin Fizz', ['2 ounces of sloe gin', '1 1/2 ounces of lemon juice', '1 teaspoon of sugar'], ['Shake well with cracked ice', 'Pour into highball glass', 'Top with ice-cold soda'])
]

for drink in drinks:
    print(drink.name)