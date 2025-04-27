def risk_monitoring(data, threshold):
    volatility = np.std(data)
    if volatility > threshold:
        print("风险超过阈值！")
    else:
        print("风险在可控范围内。")

    