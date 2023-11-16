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
    if [ "$#" -ne 2 ]; then
        echo "Usage: $0 declaration_form fiscal_year"
        exit 1
    fi

    form=$1
    year=$2

    source env/prod_env/bin/activate
    pip3 install -r requirements/requirements.txt

    python3 src/core/main.py "$form" "$year"
}




main "$@"