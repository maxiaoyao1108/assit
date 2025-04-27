def anomaly_detection(data):
    # 简单示例：假设均值加减两倍标准差以外的数据为异常
    mean = np.mean(data)
    std = np.std(data)
    lower_bound = mean - 2 * std
    upper_bound = mean + 2 * std
    anomalies = [item for item in data if item < lower_bound or item > upper_bound]
    return anomalies

    