from json import load
path="C:\\Users\\NJ\\Desktop\\python_work\\read_from_json\\data.json"

with open(path)as f:
    record=load(f)
# for f in record:
#       print(f.get("name"))
fw_names=[f.get("name") for f in record]
print(fw_names)
most_rated=max(record,key=lambda d:d.get("rating"))
print(most_rated)