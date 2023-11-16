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


def main():
    companies = pd.DataFrame()
    cik_codes_json = ''
    try:
        cik_codes_json = requests.get('https://www.sec.gov/files/company_tickers.json').json()
        companies = pd.DataFrame.from_dict(cik_codes_json.values())
    except:
        print('[*] Error Fetching CIK from sec.gov/files/company_tickers.json')
        exit(0)
    
    form = sys.argv[0]
    # year = sys.argv[1]

    ciks = companies.sample(10)['cik_str'].to_list()
    for cik in ciks:
        instance_df = Worker(str(cik), 1, form).full_retrieval_()
        upload = Uploader(instance_df)
        upload.upload_()
        time.sleep(10)
    # for cik in ciks: 
    # worker_instance = Worker(cik, form, year) .full_retrieval_
    # Sleep for 10 seconds - I dont wanna mess with the SEC

    # Then the same for the text_worker but we just get the year
    # Here we check if the folder already exists in google drive, if it doesnt then we create it and upload it,
    # else we upload it to its existing
    


if __name__ == '__main__':
    main()