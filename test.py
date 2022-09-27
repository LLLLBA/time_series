# -*- coding: utf-8 -*-
# Time : 2022/9/3 12:46
# Author : 罗浩宇 202004040123
# File : test.py
# Software: PyCharm
import matplotlib.pyplot as plt

data = [144,
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
        166,
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


def SES(series, alpha):  # 0.998
    results = []
    avg = sum(series) / len(series)
    results.append(alpha * series[0] + (1 - alpha) * avg)
    for i in range(0, len(series)):
        results.append(alpha * series[i] + (1 - alpha) * results[i])
    return results


def DES(series, alpha, beta):
    level = []
    trend = []
    temp = 0
    level[0] = sum(series) / len(series)
    for i in range(0, len(series)):
        temp += series[i + 1] - series[i]
    trend[0] = temp / len(temp)
    for i in range(0, len(series)):
        level.append(alpha * series[i] + (1 - alpha) * (level[i] + trend[i]))
        trend.append(beta * (level[i + 1] - level[i]) + (1 - beta) * trend[i])
    return level, trend
