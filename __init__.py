import os
from PIL import Image
import functools
import shutil

#自己的类
import copy_img.img_reader
import copy_img.input_info
import copy_img.copy_init

#全局变量
imgSuffix = ""  #图片格式
iconSourcePath = ""  #图片资源路径
#目标路径
hdpi = ""
mdpi = ""
xhdpi = ""
xxhdpi = ""
xxxhdpi = ""
#图片名称
imgName = ""