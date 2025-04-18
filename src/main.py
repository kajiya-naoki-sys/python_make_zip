import zipfile

file_name = input()
with zipfile.ZipFile(file_name + '.zip', 'w') as zipf:
    zipf.write(file_name)