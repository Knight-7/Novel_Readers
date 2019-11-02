import platform
import os


if platform.system() == 'Windows':
    if not os.path.exists('C:/tmp_pic'):
        os.mkdir('C:/tmp_pic')
elif platform.system() == 'Linux':
    if not os.path.exists('/home/knight/tmp_pic'):
        os.mkdir('/home/knight/tmp_pic')