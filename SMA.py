# -*- coding: utf-8 -*-
# Time : 2022/9/27 11:21
# Author : 罗浩宇 202004040123
# File : SMA.py
# Software: PyCharm
series = [144.15,
          149.59,
          174.57,
          230.03,
          339.19,
          295.54,
          155.64,
          163.81,
          143.64,
          185.34,
          206.45,
          314.64,
          290.42,
          219.11,
          210.59,
          203.60,
          261.45,
          285.38,
          196.98,
          178.41,
          168.82,
          311.01,
          296.28,
          305.10,
          364.97,
          610.10,
          598.44,
          530.53,
          517.44,
          ]
eva_series = [166.14,
              168.62,
              204.81,
              335.90,
              301.07,
              156.26,
              146.75,
              71.42,
              167.21,
              231.60,
              316.88,
              292.89,
              234.64,
              247.01,
              214.70,
              259.65,
              274.07,
              416.43,
              368.40,
              300.24,
              290.88,
              289.23,
              302.18,
              361.27,
              644.36,
              598.91,
              504.83,
              536.57,
              528.92,
              528.18,
              587.37,
              ]
eva_series_test = series + eva_series


def sma(lens, data):
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


def sse(data, series_data, lens):
    temp_sse = 0
    count = 0
    for i in range(lens, len(series_data)):
        temp_sse += pow(series_data[i] - data[i], 2)
        count += 1
    return temp_sse / count


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
    for i in range(2, len(eva_series_test) - 1):
        SMA_2 = sma(i, eva_series_test)
        SMA_2.pop()
        temp_test.append(sse(SMA_2, eva_series_test, i))
    temp2 = temp_test.index(min(temp_test))
    for i in range(len(temp_test)):
        temp_test[i] = round(temp_test[i], 2)
    print(temp_test)
    print(temp2 + 2)
    print(temp_test[temp2])
