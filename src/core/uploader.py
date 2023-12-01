##############################################################################################################################   
#
#   Class for uploading datasets to the cloud
#   Author: D. Santiago Londono
#
#   Project 4359 - BERT SEC
#
##############################################################################################################################

import pandas as pd
import subprocess
import os

class Uploader:
    
    #
    #   Constructor method of the class
    #   @params
    #       df: Dataframe - Dataframe returned from full_retrieval
    #       cik: str - CIK used to identify the table that will be uploaded
    #
    def __init__(self, df: pd.DataFrame, cik: str):
        self.df = df
        self.cik = cik
    
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
    # Uploads the information to the cloud
    #
    def upload_(self)-> None:
        table = self.to_send_table_()
        
        # Uncomment these lines of code once you have configured your S3 bucket  

        # output_folder = 'direct_uploads'
        # output_filename = f'{self.cik}_10k_tabulated.csv'
        # output_path = os.path.join(output_folder, output_filename)

        # table.to_csv(output_path)

        # shell_script_path = './src/service/s3Upload.sh' 
        # args = [shell_script_path]
        # subprocess.run(['bash', shell_script_path] + args)

        # This is the code for saving the information LOCALLY
        table.to_csv(os.path.join('tmp/filings', '{c}_filings'.format(c=str(self.cik))))



