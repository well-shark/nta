from genericpath import isfile
import os
import shutil


def copy_file(src, dst, symlinks=False):
    ''' 拷贝文件
    '''
    if not os.path.exists(src):
        raise FileNotFoundError("Source file not found: {}".format(src))

    if symlinks:
        os.symlink(src, dst)
    else:
        shutil.copy(src, dst)


def copy_dir(src, dst, symlinks=False):
    ''' 拷贝目录
    '''
    if not os.path.exists(src):
        raise FileNotFoundError("Source directory not found: {}".format(src))

    shutil.copytree(src, dst, symlinks)


def copy(src, dst, symlinks=False):
    '''拷贝文件或目录
    '''
    if os.path.isfile(src):
        copy_file(src, dst, symlinks)
    elif os.path.isdir(src):
        copy_dir(src, dst, symlinks)
    else:
        raise ValueError("Unsupported file or directory type: {}".format(src))


def find_caps(path):
    ''' 递归遍历目录下所有数据包文件
    '''
    for root, dirs, files in os.walk(path):
        for file in files:
            if is_cap_file(file):
                yield os.path.join(root, file)
        for dir in dirs:
            find_caps(os.path.join(root, dir))


def is_cap_file(path:str):
    '''判断文件是否属于数据包类型
    '''
    caps_type = ['.pcap', '.pcapng']
    return os.path.splitext(path)[-1] in caps_type


if __name__ == '__main__':
    cnt = 0
    for cap_file in find_caps('/mnt/d/dataset/iscx_vpn_2016'):
            cnt += 1
            print(cap_file)
    print(cnt)