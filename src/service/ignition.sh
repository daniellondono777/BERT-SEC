#!/bin/bash

##############################################################################################################################   
#
#   The ignition point of the entire system. 
#   Author: D. Santiago Londono
#
#   Project 4359 - BERT SEC
#
##############################################################################################################################


main(){

    source env/prod_env/bin/activate
    pip3 install -r requirements/requirements.txt

    python3 src/core/main.py 
}




main "$@"