##############################################################################################################################   
#
#   Class for retrieving from the SEC.gov website tax declaration forms from companies.
#   Author: D. Santiago Londono
#
#   Project 4359 - BERT SEC
#
##############################################################################################################################

#
# Currently included in the APIs are the submissions history by filer and the XBRL data from financial statements 
# (forms 10-Q, 10-K,8-K, 20-F, 40-F, 6-K, and their variants).
#

import requests
import pandas as pd
import json

class Worker:
    def __init__(self):
        self.headers = { 'User-Agent' : "something@gmail.com" } # Pasar a variable de ambiente
        self.cf_url = 'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json'
        self.cik_codes_json = ''
        try:
            self.cik_codes_json = requests.get('https://www.sec.gov/files/company_tickers.json').json()
        except:
            print('[*] Error Fetching CIK from sec.gov/files/company_tickers.json')
            exit(0)
        
    
    #
    #   Converts the CIK to the required format given by the specs of the SEC.
    #   @params
    #       cik: str - CIK of the company
    #
    def transform_cik_(self, cik: str)-> str:
        return '{c}{d}'.format(
                            c='0'*(10-len(cik)),
                            d=cik
                            )

    #
    #   Retrieves Filings for a specific company given its CIK
    #   @params
    #       cik: str - CIK of the company
    #       ignore_failure: int - Indicates if in case of failed retrieval it kills the thread.
    #           Not Ignore: 0
    #           Ignore: 1
    #
    def retrieve_(self, cik: str, ignore_failure: int)-> dict:
        try:
            c = self.transform_cik_(cik)
            url = self.cf_url.format(cik=c)
            r = requests.get(url, headers=self.headers).text
            return json.loads(r)['facts']
        except:
            print('[*] Error retrieving data')
            if ignore_failure == 0:
                exit(0)
            else:
                pass
    
    #
    #   Helper function - Finds a list within a dictionary object and returns it
    #   @params
    #       data: dict - Dictionary containing list
    #
    def find_arrays(self, data: dict) -> list:
        if isinstance(data, list):
            return data
        elif isinstance(data, dict):
            arrays = []
            for key, value in data.items():
                if isinstance(value, (list, dict)):
                    arrays.extend(self.find_arrays(value))
            return arrays
        return []
    
    #
    #   Formats the input dictionary and transforms it into a list of Dataframes
    #   @params
    #       facts: dict - 'facts' dictionary withing retrieved JSON
    #       fact: str - either 'us-gaap' or 'dei'
    #
    def format_fact_(self, facts, fact):
        concept = facts[fact]
        _keys = list(concept.keys())
        concept_dataframes = []
        for k in _keys:
            shares = pd.DataFrame(self.find_arrays(concept[k]))
            shares['label'] = k
            concept_dataframes.append(shares)
        return concept_dataframes
        


i1 = Worker()
retrieval = i1.retrieve_('1318605', 1)
print(i1.format_fact_(
                    i1.retrieve_('1318605', 1)
                    , 'us-gaap'))
# print(retrieval)