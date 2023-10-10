items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":40},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"tomatto","price":120,"avl_qty":5},
    {"id":5,"name":"potatto","price":45,"avl_qty":70},
    {"id":6,"name":"carrot","price":80,"avl_qty":0},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hideandseek","price":50,"avl_qty":50},
    
]
all_name=[i.get("name")for i in items]
print(all_name)

in_stock=[i.get("name") for i in items if i.get("avl_qty")>0]
print(in_stock)

under_50=[i.get("name") for i in items if i.get("price")<50]
print(under_50)

p_20_50=[i.get("name") for i in items if i.get("price") in range(20,50)]

costly_product=max(items,key=lambda i:i.get("price"))
print(costly_product)

stock_sort=sorted(items,reverse=True,key=lambda i:i.get("avl_qty"))
print(stock_sort)