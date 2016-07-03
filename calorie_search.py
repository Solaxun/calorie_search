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


def tuple_sub(x,y):
     return RECIPE(*[x-y for x,y in zip(x,y)])

def is_goal(meals,target=TARGET_2):
    for meal in meals:
        target = tuple_sub(target,meal)
    # print(target)
    if -3<=target.protein<=3 and -3<=target.carbohydrates<=3 and -3<=target.fat<=3:
        return True
    else:
        return False
#successors function gen successors based on meal type? e.g. only expand
#breakfast tagged meals in successor function for  breakfast?

def successors(state):
    recipes = [make_recipe() for i in range(1,301)]
    return recipes

def depth_limited_search(state,limit=3):
    if is_goal(state):
        return state
    elif limit == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False
        for child in successors(state):
            newstate = state+[child]
            result = depth_limited_search(newstate,limit-1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result is not None:
                return result
        return 'cutoff' if cutoff_occurred else None

print(depth_limited_search([]))

