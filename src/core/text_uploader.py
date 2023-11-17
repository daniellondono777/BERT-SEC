##############################################################################################################################   
#
#   Class for uploading .txt files from the SEC to the cloud
#   Author: D. Santiago Londono
#
#   Project 4359 - BERT SEC
#
##############################################################################################################################

import sys
import re


class TextUploader():

    #
    #   Constructor method of the class
    #   @params
    #       urls: list - List of urls from the SEC to fetch and operate
    #
    def __init__(self, path: str) -> None:
        self.path = path
        self.urls = []
        with open(path, 'r') as file:
            for line in file:
                if line != '':
                    self.urls.append(line)
    

    def scrutinize_(self, string)-> list:
        pattern = r'edgar(.*?)txt'

        match = re.search(pattern, string, re.DOTALL)

        if match:
            return match.group(0)  
        else:
            return None
    
    def scrutinize_all_(self):
        for i in self.urls:
            print(self.scrutinize_(i))
            print('-----')


uploader = TextUploader(sys.argv[1])
uploader.scrutinize_all_()