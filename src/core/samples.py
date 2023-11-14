# import pandas as pd
# import worker
# import uploader as up

# import os

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



# i1 = worker.Worker('6201', 1, '10-K')
# df = i1.full_retrieval_()
# i2 = up.Uploader(df)
# i2.to_send_table_().to_excel('americanairlines_pivoted.xlsx')



# data = ['company.gz', '1287 KB', '09/06/2014 01:08:55 AM', 'company.idx', '10625 KB', '09/06/2014 01:08:53 AM', 'company.sit', '2223 KB', '09/06/2014 01:08:56 AM', 'company.Z', '2023 KB', '09/06/2014 01:08:55 AM', 'company.zip', '1194 KB', '09/06/2014 01:08:58 AM', 'crawler.idx', '13017 KB', '09/06/2014 01:08:53 AM', 'form.gz', '1531 KB', '09/06/2014 01:08:59 AM', 'form.idx', '10625 KB', '09/06/2014 01:08:54 AM', 'form.sit', '2213 KB', '09/06/2014 01:09:00 AM', 'form.Z', '1979 KB', '09/06/2014 01:08:59 AM', 'form.zip', '1438 KB', '09/06/2014 01:09:03 AM', 'master.gz', '1089 KB', '09/06/2014 01:09:03 AM', 'master.idx', '6524 KB', '09/06/2014 01:08:52 AM', 'master.sit', '2010 KB', '09/06/2014 01:09:04 AM', 'master.Z', '1819 KB', '09/06/2014 01:09:03 AM', 'master.zip', '1056 KB', '09/06/2014 01:09:05 AM', 'sitemap.quarterlyindex.xml', '1 KB', '05/16/2012 10:53:01 AM', 'sitemap.quarterlyindex1.xml', '6365 KB', '09/06/2014 01:08:51 AM', 'sitemap.quarterlyindex2.xml', '6368 KB', '09/06/2014 01:08:51 AM', 'sitemap.quarterlyindex3.xml', '2558 KB', '09/06/2014 01:08:51 AM', 'xbrl.gz', '1 KB', '09/06/2014 01:09:05 AM', 'xbrl.idx', '1 KB', '09/06/2014 01:08:54 AM', 'xbrl.sit', '1 KB', '09/06/2014 01:09:05 AM', 'xbrl.Z', '1 KB', '09/06/2014 01:09:05 AM', 'xbrl.zip', '1 KB', '09/06/2014 01:09:05 AM']

# result = [data[i:i + 3] for i in range(0, len(data), 3)]
# df = pd.DataFrame(result, columns=['file', 'size', 'timestamp'])
# print(type(df.sort_values(by='size', ascending=False).iloc[0]['file']))


# source_folder = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# text_worker_data = '/tmp/text_worker_data/'

# print(source_folder+text_worker_data)

print('HELLOOOO')