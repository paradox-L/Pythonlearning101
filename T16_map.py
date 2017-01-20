#map grammar format: map(function,arg)

lst_1 = (1,2,3,4,5,6)
lst_2 = map(lambda x : x * 2, lst_1 )
print lst_2

lst_3 = [1,3,5,7,9,11]
lst_4 = map(lambda x, y : x + y, lst_1, lst_3)
print lst_4

st_1 = [1,2,3,4,5,6]
st_2 = [1,3,5,7,9,11]
st_3 = map(None, lst_1)
print st_3
st_4 = map(None, lst_1, lst_2)
print st_4