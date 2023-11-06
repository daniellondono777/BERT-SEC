import time
import pandas as pd
import openpyxl
import requests

#
#   Espacio para importar las vainas de google
#

import worker

def main():
    companies = None
    cik_codes_json = ''
    try:
        cik_codes_json = requests.get('https://www.sec.gov/files/company_tickers.json').json()
        companies = pd.DataFrame.from_dict(cik_codes_json.values())
        print(companies.head(10))
    except:
        print('[*] Error Fetching CIK from sec.gov/files/company_tickers.json')
        exit(0)
    

    
    # Daemon
    # while True:
    #     print('')
    #     time.sleep(11)

if __name__ == '__main__':
    main()