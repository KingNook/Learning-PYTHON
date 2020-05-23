# List files in directory as a tree (use Miscellaneous + dummy documents)

import os

def tree(path, files=[]):
    ls = os.listdir(path)
    for item in ls:
        if os.path.isdir(item):
            files.append(tree(f'{path}/{item}', files))
        else:
            files.append(item)
    return files

print(os.listdir('./'))
print(tree('./'))
print([type(i) for i in tree('./')])

'''
for i in os.listdir('./'):
    print(f'{i} : {os.path.isdir(i)}')
'''