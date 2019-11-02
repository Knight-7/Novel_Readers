import platform
import os


if platform.system() == 'Windows':
    if os.path.exists('//tmp'):
        pass
elif platform.system() == 'Linux':
    if not os.path.exists('/home/knight/tmp_pic'):
        os.mkdir('/home/knight/tmp_pic')