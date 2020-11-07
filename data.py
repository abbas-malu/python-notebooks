import pandas as pd 

data = pd.read_excel('data.xlsx')

lst = data.Musaeed.unique()
x = {}
# print(data.Musaeed.count(lst[0]))
for m in lst:
    x[m] = data.loc[data.Musaeed==m,'Musaeed'].size
print(x)
# print(data.set_index(['Musaeed']).count(level="Location"))
# for z in x:
#     print(z,x[z])
# x = pd.DataFrame(x)
d = [i for i in x]
e = [x[j] for j in x]

m = pd.DataFrame({'Musaeed':d,'Count':e})
m.to_csv('abbas.csv',index=None)