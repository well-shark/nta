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


def copy_dir(src, dst, symlinks=False, ignore=None):
    ''' 拷贝目录
    '''
    if not os.path.exists(src):
        raise FileNotFoundError("Source directory not found: {}".format(src))
    
    shutil.copytree(src, dst, symlinks, ignore)


