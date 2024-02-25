import os
import shutil
dir_train = '.\\train'
dir_val = '.\\val'
for file in os.listdir(dir_train):
    if file.startswith('cat') and file.endswith(".jpg"):
        num = int(file.split('.')[1])
        if num <= 9999:
            shutil.move(os.path.join(dir_train, file), os.path.join(dir_train, 'cat', file))
        else:
            shutil.move(os.path.join(dir_train, file), os.path.join(dir_val, 'cat', file))
    elif file.startswith('dog') and file.endswith(".jpg"):
        num = int(file.split('.')[1])
        if num <= 9999:
            shutil.move(os.path.join(dir_train, file), os.path.join(dir_train, 'dog', file))
        else:
            shutil.move(os.path.join(dir_train, file), os.path.join(dir_val, 'dog', file))





