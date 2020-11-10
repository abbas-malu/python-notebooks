import pandas as pd 

data = pd.read_excel('data.xlsx')

lst = data.Musaeed.unique()
x = {}
# print(data.Musaeed.count(lst[0]))
for m in lst:
    x[m] = data.loc[data.Musaeed==m,'Musaeed'].size
f = {}
for n in lst:
    f[n] = data.loc[data.Musaeed==n,'Location']
print(f)
# print(x)
# print(data.set_index(['Musaeed']).count(level="Location"))
# for z in x:
#     print(z,x[z])
# x = pd.DataFrame(x)
d = [i for i in x]
e = [x[j] for j in x]
mohalla = [f[k] for k in f]

m = pd.DataFrame({'Musaeed':d,'Count':e,'Mohalla':mohalla})
m.to_csv('abbas1.csv',index=None)
print(data._get_value(data.Musaeed==lst[20],'Location'))