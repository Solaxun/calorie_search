import random
from collections import namedtuple

TARGET  = {'protein':220,'carbohydrates':240,'fat':45}
RECIPE = namedtuple('Recipe', 'protein carbohydrates fat')
TARGET_RATIOS = {'protein':0.4,'carbohydrates':0.4,'fat':0.2}
KCAL = 2200
TARGET_2 = RECIPE(0.4*KCAL/4,0.4*KCAL/4,0.2*KCAL/9)
cals = {'protein':4,'carbohydrates':4,'fat':9}

def make_recipe():
    recipe = namedtuple('Recipe', 'protein carbohydrates fat')
    return (recipe(random.choice(range(25,100)),random.choice(range(25,100)),
    random.choice(range(10,25))))

def get_cals(recipe):
    p = recipe.protein * cals.get('protein')
    c = recipe.carbohydrates * cals.get('carbohydrates')
    f = recipe.fat * cals.get('fat')
    return p + c + f

recipes = [make_recipe() for i in range(1,301)]

def tuple_sub(x,y):
     return RECIPE(*[x-y for x,y in zip(x,y)])

def is_goal(meals,target):
    for meal in meals:
        target = tuple_sub(target,meal)
    print(target)
    if -3<=target.protein<=3 and -3<=target.carbohydrates<=3 and -3<=target.fat<=3:
        return True
    else:
        return False
#successors function gen successors based on meal type? e.g. only expand
#breakfast tagged meals in successor function for  breakfast?
def make_plan(meals=[],goal=TARGET_2,num_meals=3):
    """start with random selection from meal options with num_meals
    set.  Then iteratively change one recipe at a time and check 
    constraints, backing up if necessary"""
    if is_goal(meals,TARGET_2):
        return meals
    if len(meals)>=num_meals:
        meals.pop()
    recipe = random.choice(recipes)
    recipes.remove(recipe)
    meals.append(recipe)
    return make_plan(meals)

print(make_plan(num_meals=6))



