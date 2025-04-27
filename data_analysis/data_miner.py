from collections import Counter


def data_mining(data):
    if data:
        # 简单示例：统计出现次数最多的元素
        counter = Counter(data)
        most_common = counter.most_common(1)
        return most_common
    return []

    