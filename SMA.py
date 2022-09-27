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
eva_series_test = series + eva_series


def sma(lens, data, far=0):
    if far == 0:
        temp_sma = []
        for i in range(lens):
            temp_sma.append(0)
        for i in range(lens - 1, len(data)):
            a = 0
            for j in range(1, lens + 1):
                a += data[i - j + 1]
            a = a / lens
            temp_sma.append(a)
        return temp_sma
    else:
        temp_fsma = sma(lens, data)
        for i in range(len(series), len(series) + far):
            a = 0
            for j in range(1, lens + 1):
                a += temp_fsma[i - j + 1]
            a = a / lens
            temp_fsma.append(a)
        return temp_fsma


def sse(data, series_data, lens):
    temp_sse = 0
    for i in range(lens, len(series_data)):
        temp_sse += pow(series_data[i] - data[i], 2)
    return temp_sse


if __name__ == '__main__':
    temp = []
    for i in range(2, len(series) // 2):
        SMA_1 = sma(i, series)
        SMA_1.pop()
        temp.append(sse(SMA_1, series, i))
    temp1 = temp.index(min(temp))
    for i in range(len(temp)):
        temp[i] = round(temp[i], 2)
    print(temp)
    print(temp1 + 2)
    print(temp[temp1])

    temp_test = []
    for i in range(2, len(series) // 2):
        SMA_2 = sma(i, series, 31)
        SMA_2.pop()
        temp_test.append(sse(SMA_2, eva_series_test, i))
    temp2 = temp_test.index(min(temp_test))
    for i in range(len(temp_test)):
        temp_test[i] = round(temp_test[i], 2)
    print(temp_test)
    print(temp2 + 2)
    print(temp_test[temp2])
