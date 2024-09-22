# A list is a collection of items in a particular order
bicycles = ['trek', 'cannondale', 'redline', 'specialised']
print(bicycles)
print(bicycles[0].title()) #index positions start from 0 not 1
print(bicycles[3].title())
print(bicycles[-1].title())
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
print(f"Hey Tom, nice bike, what is it a {bicycles[2]}?")

#Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'dacati'
print(motorcycles)
motorcycles.append('dacati')
print(motorcycles)

#append to add to list, append will add to end of list
motorcycles = []

motorcycles.append('motor')
motorcycles.append('adding more to list')
print(motorcycles)

#inserting elements into a list
motorcycles = ['honda','ducati']
motorcycles.insert(0, 'porsche')
print(motorcycles)

#removing an item using the del statement
motorcycles = ['honday', 'test', 'ferrari']

del motorcycles[0]
print(motorcycles)

#removing item from a list using pop() method

motorcycles = ['honday', 'porsche', 'buggati']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#using pop() to print statement of last motorcycle we bought

motorcycles = ['honday','yamaha','suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
print(f"the last motorcycle I owned was a {last_owned.title()}")

#popping items from any position

first_owned = motorcycles.pop(0)
print(f"the first motorcycle i owned was a {first_owned.title()}")
print(motorcycles)

#removing an item by value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

#use remove() to work with a value thats being removed from the list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")