#!/usr/bin/env python
# coding=utf-8

import os
import re


def renameFile(path):
    filelist = os.listdir(path)
    for filename in filelist:
        print("原文件名:", filename)
        m = re.match(r'\[小晓家园www.xxjy.org]', filename)
        if m:
            dname = re.sub(r'\[小晓家园www.xxjy.org]', "", filename, 1).strip()
            print(dname)
            os.rename(path + os.path.sep + filename, path + os.path.sep + dname)
        else:
            print("不匹配")


if __name__ == "__main__":
    renameFile("D:\Download\潜伏")
