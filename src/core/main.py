##############################################################################################################################   
#
#   Main class for running the program.
#   Author: D. Santiago Londono
#
#   Project 4359 - BERT SEC
#
##############################################################################################################################

import sys
import time
import pandas as pd
import openpyxl
import requests
from worker import Worker
from uploader import Uploader
import os


def main():
    companies = pd.DataFrame()
    cik_codes_json = ''
    try:
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36' }
        cik_codes_json = requests.get('https://www.sec.gov/files/company_tickers.json', headers=headers).json()
        companies = pd.DataFrame.from_dict(cik_codes_json.values())
    except:
        print('[*] Error Fetching CIK from sec.gov/files/company_tickers.json')
        exit(0)

    form = "10-K" 

    ciks = companies.sample(200)['cik_str'].to_list() # We first try with 100 companies just for testing purposes, here you input the number you desire.  

    for cik in ciks:
        files = os.listdir('tmp/filings')
        instance_df = Worker(str(cik), 1, form).full_retrieval_()
        if not instance_df.empty and instance_df.shape[0] > 0 and '{}_filings.csv' not in files: # Also check that the filing does not exist in the folder tmp/filings
            uploader = Uploader(instance_df, cik)
            uploader.upload_()
            time.sleep(10)
    
    # Here we'd run the same process for a text_worker instance
    


if __name__ == '__main__':
    main()


