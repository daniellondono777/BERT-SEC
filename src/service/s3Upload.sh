#!/bin/bash

if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
else
    echo ".env file not found"
    exit 1
fi

if [[ -z $AWS_PROFILE || -z $S3_BUCKET || -z $LOCAL_FOLDER_PATH || -z $S3_FOLDER_PATH ]]; then
    echo "One or more required environment variables are not set"
    exit 1
fi

if [ $# -eq 0 ]; then
    echo "Please provide the path to the file to upload"
    exit 1
fi

file_to_upload="$1"

if [ ! -f "$file_to_upload" ]; then
    echo "File does not exist: $file_to_upload"
    exit 1
fi

aws s3 cp "$file_to_upload" "s3://$S3_BUCKET/$S3_FOLDER_PATH/$(basename "$file_to_upload")" --profile "$AWS_PROFILE"

if [ $? -eq 0 ]; then
    echo "File upload successful to S3 bucket: $S3_BUCKET"
else
    echo "File upload failed"
fi
