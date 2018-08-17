#!/usr/bin/env python
# coding=utf-8


def chuangyeban_cb():
    zs = input("请输入创业板指数：")
    ratio = input("请输入收益率：")
    result = float(zs) / (1 + float(ratio))
    print("您的持仓成本线：", "%.2f" % result)


if __name__ == "__main__":
    chuangyeban_cb()
