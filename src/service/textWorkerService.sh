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
#   Run the its respective python script whenever it finds a file
#

run(){
    local form=$1
    local year=$2

    output_folder='./tmp/feeding_data/'
    output_file="$output_folder/data_"$year".txt"

    if [ -n "$(find "$PROJECT_ROOT" -maxdepth 1 -type f)" ]; then
        files=($(find "$PROJECT_ROOT" -maxdepth 1 -type f))
        for element in "${files[@]}"; do
            cat "$element" | grep -w "$form" >> "$output_file"
        done
    else
        echo "The folder is empty or does not exist."
        exit 0
    fi
}

run '8-K' '2000'
