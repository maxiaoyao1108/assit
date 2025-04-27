def compliance_check(data):
    # 简单示例：检查数据是否符合某个规则
    if all(item > 0 for item in data):
        print("数据符合合规要求。")
    else:
        print("数据不符合合规要求。")

    