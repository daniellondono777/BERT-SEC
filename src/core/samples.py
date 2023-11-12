import pandas as pd
import worker
import uploader as up

# This file is purely for testing dont judge me plz

# df = pd.read_excel('visa_ret.xlsx')
# periodos_fiscales = df['fp'].unique()

# for f in periodos_fiscales:
#     t = df[df['fp'] == f][['val','accn','label','fy','fp']]
#     print(t.head(1))
#     print(t.groupby('label')['val'].mean())
#     print('*-----**-----**-----**-----**-----**-----**-----**-----*')





# print(df[df['accn']=='0001193125-10-020834']['label'].unique())

# res = df.pivot_table(index='fy', columns='label', values='val')

# res = pd.read_excel('pivoted_results.xlsx')
# print(res.dropna(axis=1).columns.to_list())
# res.dropna(axis=1).to_excel('pivoted_dropedna_visa.xlsx')

# transcript_nan_columns = res.dropna(axis=1, thresh=1)
# transcript_nan_columns.to_excel('onlynans_visa.xlsx')



i1 = worker.Worker('19617', 1, '10-K')
df = i1.full_retrieval_()
i2 = up.Uploader(df)
i2.to_send_table_().to_excel('jpmorgan_pivoted.xlsx')