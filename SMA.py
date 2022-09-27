# -*- coding: utf-8 -*-
# Time : 2022/9/27 11:21
# Author : 罗浩宇 202004040123
# File : SMA.py
# Software: PyCharm
series = [144,
          150,
          175,
          230,
          339,
          296,
          156,
          164,
          144,
          185,
          206,
          315,
          290,
          219,
          211,
          204,
          261,
          285,
          197,
          178,
          169,
          311,
          296,
          305,
          365,
          610,
          598,
          531,
          517,
          ]
eva_series = [166,
              169,
              205,
              336,
              301,
              156,
              147,
              71,
              167,
              232,
              317,
              293,
              235,
              247,
              215,
              260,
              274,
              416,
              368,
              300,
              291,
              289,
              302,
              361,
              644,
              599,
              505,
              537,
              529,
              528,
              587,
              ]


def SMA(lens, data):
    temp = []
    for i in range(lens):
        temp.append(0)
    for i in range(lens - 1, len(data)):
        a = 0
        for j in range(1, lens + 1):
            a += data[i - j + 1]
        a = a / lens
        temp.append(a)
    return temp


def SSE(data, series_data, lens):
    temp = 0
    for i in range(lens, len(series_data)):
        temp += pow(series_data[i] - data[i], 2)
    return temp


if __name__ == '__main__':
    temp = []

    for i in range(2, len(series) // 2):
        SMA_1 = SMA(i, series)
        SMA_1.pop()
        temp.append(SSE(SMA_1, series, i))
    temp1 = temp.index(min(temp))
    print(temp)
    print(temp[temp1])
