import collections
import multiprocessing


def calculate_price_in_rupees(DishName):
    return {
        'dish': DishName.dish,
        'price': round(DishName.price * 77.85, 2)
    }


DishName = collections.namedtuple('DishName', [
    'dish',
    'price',
])
if __name__ == "__main__":
    DishNames = (
        DishName(dish='Shrimp Carbonara', price=1815),
        DishName(dish='Lobster Bisque', price=1882),
        DishName(dish='Spaghetti with Meatballs', price=1867),
        DishName(dish='Tom Kha Ghai', price=1930),
        DishName(dish='Cordon Bleu', price=1939),
        DishName(dish='Coq au Vin', price=1928),
        DishName(dish='Pomme Frites', price=1951),
    )
    
pool = multiprocessing.Pool()
result = pool.map(calculate_price_in_rupees, DishNames)
print(result)
'''
[{'dish': 'Shrimp Carbonara', 'price': 141297.75}, 
{'dish': 'Lobster Bisque', 'price': 146513.7}, 
{'dish': 'Spaghetti with Meatballs', 'price': 145345.95}, 
{'dish': 'Tom Kha Ghai', 'price': 150250.5}, 
{'dish': 'Cordon Bleu', 'price': 150951.15}, 
{'dish': 'Coq au Vin', 'price': 150094.8}, 
{'dish': 'Pomme Frites', 'price': 151885.35}]
'''
