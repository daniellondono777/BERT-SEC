# from pydrive.auth import GoogleAuth 
# from pydrive.drive import GoogleDrive

import sys

# gauth = GoogleAuth() 
# gauth.LocalWebserverAuth()
# # drive = GoogleDrive(gauth)



# # file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('fffffffffff')}).GetList() 
# # for file in file_list: print('title: %s, id: %s' % (file['title'], file['id']))

# import subprocess

# form = '10-K'
# script_path = './src/service/textWorkerService.sh'
# args = [form]
# subprocess.run(['bash', script_path] + args)
print('ENTRA ENTRA ENTRA')
file_path = sys.argv[1]
print(file_path)
with open(file_path, 'r') as file:
    for line in file:
        print(line)
    print('SAMPELS')