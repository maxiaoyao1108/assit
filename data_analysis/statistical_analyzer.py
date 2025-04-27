import numpy as np


def statistical_analysis(data):
    if data:
        # 简单示例：计算均值和标准差
        mean = np.mean(data)
        std = np.std(data)
        return mean, std
    return None, None

    