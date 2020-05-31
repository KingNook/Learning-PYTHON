import zipfile

# Writing to zip file
'''
with zipfile.ZipFile('Lorem.zip', 'w', compression=zipfile.ZIP_DEFLATED) as f:
    f.write('./Lorem/Lorem.txt')
'''

# Reading from zip file
# ZipFile.namelist() - returns list of files in zipfile
# ZipFile.extractall(dir) - extracts file into directory called 'dir'
'''
with zipfile.ZipFile('Lorem.zip', 'r') as f:
    f.extractall('Lorem')
'''
