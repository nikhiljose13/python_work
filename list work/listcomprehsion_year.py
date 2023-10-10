years=[y for y in range(1800,2026)]
century_year=[y for y in years if y%100==0]
print(century_year)
non_century_year=[y for y in years if y%100!=0]
print(non_century_year)