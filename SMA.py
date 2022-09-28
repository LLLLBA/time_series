# -*- coding: utf-8 -*-
# Time : 2022/9/27 11:21
# Author : 罗浩宇 202004040123
# File : SMA.py
# Software: PyCharm


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


def se(data, series_data):
    temp_sse = 0
    count = 0
    for i in range(len(data)):
        temp_sse += pow(series_data[i] - data[i], 2)
        count += 1
    return pow(temp_sse / count, 0.5)


if __name__ == '__main__':
    total = []
    total_full = []
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
    for i in range(2, len(series)):
        s1 = sma(i, series)[:29]
        s2 = sma(i, eva_series_test)[29:60]
        total.append(se(s1, series))
        total_full.append(se(s2, eva_series))
    for i in range(len(total)):
        total[i] = round(total[i], 2)
    for i in range(len(total_full)):
        total_full[i] = round(total_full[i], 2)
    index1 = total.index(min(total))
    index2 = total_full.index(min(total_full))
    print(index1 + 2, index2 + 2)
    print(min(total), min(total_full))
    print(total)
    print(total_full)