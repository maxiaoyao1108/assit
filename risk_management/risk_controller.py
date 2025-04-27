def risk_control(data, threshold):
    volatility = np.std(data)
    if volatility > threshold:
        # 简单示例：减少部分数据以降低风险
        new_data = data[:len(data) // 2]
        return new_data
    return data

    