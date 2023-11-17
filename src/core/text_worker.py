##############################################################################################################################   
#
#   Class for retrieving from the SEC.gov website tax declaration notes from companies.
#   Author: D. Santiago Londono
#
#   Project 4359 - BERT SEC
#
##############################################################################################################################

#
# Currently included in the APIs are the submissions history by filer and the XBRL data from financial statements 
# (forms 10-Q, 10-K,8-K, 20-F, 40-F, 6-K, and their variants).
#

import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import subprocess

class TextWorker():
    #
    #   Constructor method of the class
    #   @params
    #       fy: str - Fiscal year of the data lookup
    #       form: str - Available filing forms are 10-Q, 10-K,8-K, 20-F, 40-F, 6-K, and their variants.
    #
    def __init__(self, fy: str, form: str) -> None:
        self.fy = fy
        self.form = form
        self.source_url = 'https://www.sec.gov/Archives/edgar/full-index/{fy}/QTR4/'.format(fy=fy) ## Considering we just want the 10-K
        self.headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36' }
    
    #
    #   Returns a dataframe containing the files per fiscal year.
    #
    def fetch_year_folder_(self) -> pd.DataFrame:
        try:
            r = requests.get(self.source_url, headers=self.headers)
            html_content = r.content
            soup = BeautifulSoup(html_content, 'html.parser')
            rows = soup.find_all('div', {'class':'grid_10 push_2'})[0]
            files = rows.find_all('tr')[0]
            name_size = files.find_all('td')
            tabulated = []
            for el in name_size:
                tabulated.append(el.text)
            data = [tabulated[i:i + 3] for i in range(0, len(tabulated), 3)]
            df = pd.DataFrame(data, columns=['file', 'size', 'timestamp'])
            df = df[df['file'].str.contains(r'.\.idx', regex=True)]
            return df

                
        except Exception as e:
            print('[*] Exception while fetching SEC.gov', e)
            exit(0)
    
    #
    #   Returns the file name of the larger file size within the dataframe
    #
    def source_file_getter_(self)-> str:
        file = self.fetch_year_folder_().sort_values(by='size', ascending=False).iloc[0]['file']
        return file
    
    #
    #   Downloads the file to the path specified on the parameter
    #
    def download_file_(self):
        download_location = '/tmp/text_worker_data/'
        filename = self.source_file_getter_()
        os.makedirs(download_location, exist_ok=True)
        source_folder = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        path = source_folder + download_location + filename
        
        try:
            r = requests.get('{su}{p}'.format(su=self.source_url, p=filename), headers=self.headers)
            with open(path, 'wb') as f:
                f.write(r.content)
            script_path = './src/service/textWorkerService.sh'
            args = [self.form]
            subprocess.run(['bash', script_path] + args)

        except Exception as e:
            print('[*] Exception while fetching SEC.gov', e)
            exit(0)




# i1 = TextWorker('2017', '10-K')
# print(i1.download_file_())