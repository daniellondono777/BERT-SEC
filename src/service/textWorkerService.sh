#!/bin/bash

##############################################################################################################################   
#
#   Daemon - checks if the tmp/text_worker_data folder has files, if it does, then it runs its respective python script.
#   Author: D. Santiago Londono
#
#   Project 4359 - BERT SEC
#
##############################################################################################################################

PROJECT_ROOT=$(dirname $(dirname $(dirname "$0")))
download_folder="/tmp/text_worker_data"
PROJECT_ROOT+=$download_folder


#
#   Filters the urls that will be uploaded, retrieves the CIK and the url of the filing as long as it matches the parameter
#

form=$1

run(){

    directory="tmp/text_worker_data"
    file_to_check="$2"
    script_to_run="$3"

    first_file="$(ls -A "$directory" | head -n 1)"

    if [ "$first_file" ]; then
        cat "$directory/$first_file" | grep ".txt" > "$directory"/results.txt
        # python3 /src/core/samples.py "$directory""/results.txt"
        PROJECT_PATH=$(git rev-parse --show-toplevel)
        python3 $PROJECT_PATH/src/core/text_uploader.py "$directory"/results.txt
    else
        exit 1
    fi
}

run
