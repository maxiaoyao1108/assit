def rule_based_screening(data):
    # 简单示例：筛选出大于某个阈值的数据
    threshold = 100
    screened_data = [item for item in data if item > threshold]
    return screened_data

    