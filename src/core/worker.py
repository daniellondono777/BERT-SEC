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
    #
    #   Constructor method of the class
    #   @params
    #       cik: str - CIK of the company
    #       ignore_failure: int - Indicates if in case of failed retrieval it kills the thread.
    #                       Not Ignore: 0
    #                       Ignore: 1
    #       form: str - Available filing forms are 10-Q, 10-K,8-K, 20-F, 40-F, 6-K, and their variants. 
    #
    def __init__(self, cik: str, ignore_failure: int, form: str):
        self.headers = { 'User-Agent' : "something@gmail.com" } 
        self.cf_url = 'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json'
        self.cik = cik
        self.ignore_failure = ignore_failure
        self.form = form
    
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
    def format_fact_(self, facts, fact)-> pd.DataFrame:
        concept = facts[fact]
        _keys = list(concept.keys())
        concept_dataframes = []
        for k in _keys:
            shares = pd.DataFrame(self.find_arrays(concept[k]))
            shares['label'] = k
            concept_dataframes.append(shares)
        
        df = pd.concat(concept_dataframes, ignore_index=True)
        return df

    #
    #   Performs the full process for obtaining a companies filings. Formats and concatenates the 
    #   us-gaap and dei data. 
    #
    #   Returns dataframe with the end date, value, account number, fiscal year, fiscal period, date filled, frame, label, and start date of filing. 
    #
    def full_retrieval_(self)-> pd.DataFrame:
        try:
            retrieval = self.retrieve_(self.cik, self.ignore_failure)
            formated_us_gaap = self.format_fact_(retrieval,'us-gaap')
            formated_dei = self.format_fact_(retrieval,'dei')
            df = pd.concat([formated_dei, formated_us_gaap], axis=0)
            return df[df['form'] == self.form]
        except:
            print('[*] Error performing full_retrieval_')
            return pd.DataFrame()
