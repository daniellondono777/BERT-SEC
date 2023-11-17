##############################################################################################################################   
#
#   Class for uploading datasets to the cloud
#   Author: D. Santiago Londono
#
#   Project 4359 - BERT SEC
#
##############################################################################################################################

import pandas as pd
from pydrive.auth import GoogleAuth 
from pydrive.drive import GoogleDrive


class Uploader:
    
    #
    #   Constructor method of the class
    #   @params
    #       df: Dataframe - Dataframe returned from full_retrieval
    #
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    #
    #   Pivots the input table and for each fiscal year it keeps the financial records
    #
    def pivot_table_(self)-> pd.DataFrame:
        transcript = self.df.pivot_table(index='fy', columns='label', values='val')
        return transcript

    #
    #   Replaces Nan Values with zeroes
    #
    def to_send_table_(self)-> pd.DataFrame:
        '''
        Argument:
        In financial statements, certain items may not be reported for every fiscal year, 
        leading to missing values. Filling these gaps with zeros is a pragmatic approach 
        as it neither adds nor subtracts from the financial metrics, ensuring consistency 
        and preserving the structure of the data.
        '''
        table = self.pivot_table_().fillna(0)
        return table
    
    #
    #
    #
    def upload_(self)-> None:
        pass

