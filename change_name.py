import os
import hashlib
import uuid
import time

path = 'C:\\Users\\admin\\Desktop\\反诈\\'


def change_name():
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            s = hashlib.sha1()
            s.update(uuid.uuid4().bytes)
            new_name = file.replace(file.split('.')[0], s.hexdigest().upper())

            os.rename(os.path.join(path, file), os.path.join(path, new_name))


def change_file_md5():
    if os.path.exists(path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(path):
            for file in files:
                src_file = os.path.join(root, file)
                writefile = int(time.time_ns())
                with open(src_file, "a") as f:
                    print(f)
                    f.write(str(writefile))

    print("change file's md5 finished")


if __name__ == '__main__':
    change_name()
    change_file_md5()
