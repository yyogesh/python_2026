import zipfile

with zipfile.ZipFile('archive.zip', 'w') as zip_file:
    zip_file.write('file1.txt', 'file1.txt')
    zip_file.write('file2.txt', 'file2.txt')

with zipfile.ZipFile('archive.zip', 'r') as zip_file:
    zip_file.extractall('extracted_files')
    print(zip_file.namelist())


# tar 
# 
import tarfile

with tarfile.open('archive.tar', 'w') as tar_file:
    tar_file.add('file1.txt', arcname='file1.txt')
    tar_file.add('file2.txt', arcname='file2.txt')


with tarfile.open('archive.tar', 'r') as tar_file:
    tar_file.extractall('extracted_files')
    print(tar_file.getnames())  



import tempfile

with tempfile.TemporaryDirectory() as temp_dir:
    print(temp_dir)


import tempfile

with tempfile.NamedTemporaryFile() as temp_file:
    print(temp_file.name)