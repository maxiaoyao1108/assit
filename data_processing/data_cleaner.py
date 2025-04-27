def clean_data(data):
    if data:
        # 简单示例：去除缺失值
        cleaned_data = [item for item in data if item is not None]
        return cleaned_data
    return []

    