import pandas as pd
import worker

# This file is purely for testing dont judge me plz

# df = pd.read_excel('pivoted_try.xlsx')
# periodos_fiscales = df['fp'].unique()


# for f in periodos_fiscales:
#     t = df[df['fp'] == f][['val','accn','label','fy','fp']]
#     print(t.head(1))
#     print(t.groupby('label')['val'].mean())
#     print('*-----**-----**-----**-----**-----**-----**-----**-----*')


# print(df[df['accn']=='0001157523-09-007839']['label'].unique())

# res = df.pivot_table(index='fy', columns='label', values='val')

# res = pd.read_excel('pivoted_results.xlsx')
# print(res.dropna(axis=1).columns.to_list())