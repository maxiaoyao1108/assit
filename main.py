from data_collection import market_data_collector, economic_data_collector, news_collector
from data_processing import data_cleaner, data_storer
from data_analysis import data_miner, statistical_analyzer, ml_modeler
from investment_opportunity import rule_based_screening, anomaly_detector, trend_analyzer
from decision_support import risk_assessor, portfolio_optimizer, decision_tools
from user_interface import visualizer, interactive_ui, report_generator
from risk_management import risk_monitor, risk_controller, compliance_checker
from data_update import data_updater
import numpy as np


if __name__ == "__main__":
    # 数据收集
    market_data = market_data_collector.collect_market_data()
    economic_data = economic_data_collector.collect_economic_data()
    news_data = news_collector.collect_news_data()

    # 数据处理
    cleaned_market_data = data_cleaner.clean_data(market_data)
    cleaned_economic_data = data_cleaner.clean_data(economic_data)
    cleaned_news_data = data_cleaner.clean_data(news_data)

    data_storer.store_data(cleaned_market_data, 'market_data')
    data_storer.store_data(cleaned_economic_data, 'economic_data')
    data_storer.store_data(cleaned_news_data, 'news_data')

    # 数据分析
    mined_data = data_miner.data_mining(cleaned_market_data)
    mean, std = statistical_analyzer.statistical_analysis(cleaned_market_data)
    X = np.array(cleaned_market_data[:-1]).reshape(-1, 1)
    y = np.array(cleaned_market_data[1:])
    model = ml_modeler.ml_modeling(X, y)

    # 投资机会发现
    screened_data = rule_based_screening(cleaned_market_data)
    anomalies = anomaly_detector.anomaly_detection(cleaned_market_data)
    trend = trend_analyzer.trend_analysis(cleaned_market_data)

    # 投资决策辅助
    risk = risk_assessor.risk_assessment(cleaned_market_data)
    portfolio_return = portfolio_optimizer.portfolio_optimization([100, 200, 300], [0.3, 0.3, 0.4])
    scenario_data = decision_tools.scenario_analysis(cleaned_market_data, 'optimistic')

    # 用户界面
    visualizer.visualize_data(cleaned_market_data)
    interactive_ui.interactive_ui()
    report_generator.generate_report(cleaned_market_data)

    # 风险管理
    risk_monitor.risk_monitoring(cleaned_market_data, 10)
    new_data = risk_controller.risk_control(cleaned_market_data, 10)
    compliance_checker.compliance_check(cleaned_market_data)

    # 数据更新
    data_updater.data_update()

    