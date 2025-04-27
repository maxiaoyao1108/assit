def portfolio_optimization(assets, weights):
    # 简单示例：计算投资组合的预期收益
    expected_returns = [0.1, 0.2, 0.15]  # 假设各资产预期收益
    portfolio_return = sum([asset * weight * return_rate for asset, weight, return_rate in zip(assets, weights, expected_returns)])
    return portfolio_return

    