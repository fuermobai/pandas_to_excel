import pandas as pd
df = pd.DataFrame({'ID':[1,2,3],'Name':['Luo','Han','Niu']})
df = df.set_index('ID')
print(df)
df.to_excel('C:/Users/Administrator/Desktop/output.xlsx')
print('done!')
