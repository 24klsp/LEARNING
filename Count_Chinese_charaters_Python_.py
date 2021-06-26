import os
import re

#读取目标文本文件
def get_str(path):
    f = open(path, encoding='UTF-8')
    data = f.read()
    f.close()
    return data

path=input("请输入文件路径：")

word=re.findall('([\u4e00-\u9fa5])',get_str(path))
print("中文字符，除特殊字符外共：",len(word))
