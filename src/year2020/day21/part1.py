from src.common.common import get_lines


def parse_recipe(line):
    ingredients, allergens = line.split(' (')

    ingredients = ingredients.split(' ')
    allergens = allergens[len('contains '):-1].split(', ')

    return ingredients, allergens


def main():
    lines = get_lines()

    recipes = [parse_recipe(line) for line in lines]

    allergens_recipes = {}
    ingredients_allergens_recipes = {}

    for ingredients, allergens in recipes:
        for allergen in allergens:
            allergens_recipes.setdefault(allergen, 0)
            allergens_recipes[allergen] += 1
        for ingredient in ingredients:
            ingredient_allergens = ingredients_allergens_recipes.setdefault(ingredient, {})
            for allergen in allergens:
                ingredient_allergens.setdefault(allergen, 0)
                ingredient_allergens[allergen] += 1

    marked_ingredients = set()

    for allergen, allergen_count in allergens_recipes.items():
        ingredients = [ingredient for ingredient, ingredient_allergens in ingredients_allergens_recipes.items() if (allergen, allergen_count) in ingredient_allergens.items()]
        marked_ingredients.update(ingredients)

    safe_ingredients = ingredients_allergens_recipes.keys() - marked_ingredients

    recipes_with_safe_ingredients = 0

    for ingredients, allergens in recipes:
        recipes_with_safe_ingredients += sum(ing in ingredients for ing in safe_ingredients)

    print(recipes_with_safe_ingredients)


if __name__ == "__main__":
    main()
