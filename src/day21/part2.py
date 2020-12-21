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

    marked_ingredients = list(marked_ingredients)
    marked_ingredients_idx = 0

    figured_ingredients = {}

    while marked_ingredients:
        marked_ingredients_idx %= len(marked_ingredients)
        ingredient = marked_ingredients[marked_ingredients_idx]
        temp = [(allergen, recipes_count) for allergen, recipes_count in ingredients_allergens_recipes[ingredient].items() if (allergen, recipes_count) in allergens_recipes.items() and allergen not in figured_ingredients.values()]
        if len(temp) == 1:
            figured_ingredients[ingredient] = temp[0][0]
            marked_ingredients.remove(ingredient)
        else:
            temp_max = [(allergen, recipes_count) for allergen, recipes_count in temp if (allergen, recipes_count) in allergens_recipes.items() and allergen not in figured_ingredients.values()]
            if len(temp_max) == 1:
                figured_ingredients[ingredient] = temp[0][0]
                marked_ingredients.remove(ingredient)
        marked_ingredients_idx += 1

    result = [ingredient for ingredient, allergen in sorted(figured_ingredients.items(), key=lambda tup: tup[1])]
    print(','.join(result))


if __name__ == "__main__":
    main()
