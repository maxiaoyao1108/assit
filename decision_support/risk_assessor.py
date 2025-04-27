import numpy as np


def risk_assessment(data):
    # 简单示例：计算波动率作为风险指标
    volatility = np.std(data)
    return volatility

    