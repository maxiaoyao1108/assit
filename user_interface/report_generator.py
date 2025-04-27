def generate_report(data):
    report = f"数据统计：均值={np.mean(data)}, 标准差={np.std(data)}"
    with open('investment_report.txt', 'w') as f:
        f.write(report)
    print("报告生成成功！")

    