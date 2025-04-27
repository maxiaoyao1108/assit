def scenario_analysis(data, scenario):
    # 简单示例：根据不同情景调整数据
    if scenario == 'optimistic':
        adjusted_data = [item * 1.1 for item in data]
    elif scenario == 'pessimistic':
        adjusted_data = [item * 0.9 for item in data]
    else:
        adjusted_data = data
    return adjusted_data

    