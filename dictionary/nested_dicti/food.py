foods=[
    {"id":1,"name":"ghee-roast","price":70,"category":"veg"},
    {"id":2,"name":"chicken-roast","price":170,"category":"non-veg"},
    {"id":3,"name":"cb","price":170,"category":"non-veg"},
    {"id":4,"name":"bb","price":190,"category":"non-veg"},
    {"id":5,"name":"fried-rice","price":140,"category":"veg"},
    {"id":6,"name":"chicken-friedrice","price":170,"category":"non-veg"},
    {"id":7,"name":"nan","price":70,"category":"veg"},
    {"id":8,"name":"alfham","price":370,"category":"non-veg"},
     
]
# total number of items
print(len(foods))

# print name whose category = veg
veg=[f.get("name") for f in foods if f.get("category")=="veg"]
print(veg)

# food names available under rs 100
under_100=[f.get("name") for f in foods if f.get("price")<100]
print(under_100)

# costly item
costly_food=max(foods,key=lambda f:f.get("price"))
print(costly_food)

# costly non-veg food
costly_non=max(foods,key=lambda f:f.get("C")=="non-veg" and f.get("price"))
print(costly_non)

# print all category
category={f.get("category") for f in foods}
print(category)