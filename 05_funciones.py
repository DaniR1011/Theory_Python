def buy(list, budget):
 print(f"Mi lista a comprar: {list} | presupuesto: {budget}")
 
buy(['patatas', 'huevos', 'aceite'], 100)

def carrito_suma(list_prices):
 total = 0
 for price in list_prices:
  total += price
 return total
 
carrito_price = carrito_suma([5, 2, 7, 9, 10])
print(carrito_price)

def best_restaurant_stars(stars_list):
 maximo = stars_list[0]
 for star in stars_list:
  if star > maximo:
   maximo = star
 return maximo

best_restaurant = best_restaurant_stars([5, 10, 99, 30, 70, 90, 75])
print(best_restaurant)