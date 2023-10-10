from json import load
path="C:\\Users\\NJ\\Desktop\\python_work\\read_from_json\\countries.json"
with open(path,encoding="utf-8") as f:
    countries=load(f)
    # 1 all coun name
# countries_name=[c.get("name") for c in countries]
# print(countries_name)
# # ind border
ind_bord=[c.get("borders") for c in countries if  c.get("name")=="India"]
# print(ind_bord)

# all_bod={b for c in countries for b in c.get("borders")} 

# print(all_bod)
# name_cap=[[c.get("name"),c.get("capital")]for c in countries]
# print(name_cap)

all_region={c.get("region") for c in countries } 
print(all_region)