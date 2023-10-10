from json import load
path="C:\\Users\\NJ\\Desktop\\python_work\\read_from_json\\mdb.json"
with open(path,encoding="utf-8") as f:
    movies=load(f)

    # all movies all name
# movie_name=[m.get("title") for m in movies ]
# print(movie_name)
     #2005 movie
# movie_2005=[m.get("title") for m in movies if m.get("year")=="2005"]
# print(movie_2005)
       # comdey
# movie_Comedy=[m.get("title") for m in movies if "Comedy" in m.get("genres")]
# print(movie_Comedy)

# lengthy movie

# lenthy_movie=max(movies,key=lambda m:int(m.get("runtime")))
# print(lenthy_movie["title"])

# all genres

# all_genres={g for m in movies for g in m.get("genres")} 

# print(all_genres)

# 2015  comedy
Comedy_2015=[m.get("title") for m in movies if "Comedy" in m.get("genres") and  "2015" in m.get("year")]
print(Comedy_2015)

# most relased year
wc={}
for m in movies:
    year=m.get("year")
    if year in wc:
        wc[year]+=1
    else:
        wc[year]=1
print(wc)