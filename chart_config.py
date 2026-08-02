"""
chart_config.py - 各行业图表定义（严格对照PDF布局）
"""

# ============================================================
# 行业配置
# 每个行业包含：
#   summary_text: 正文摘要（可周更）
#   kpi_cards: 指标卡片（最多4张显示在详情页）
#   charts: 图表列表（2×2布局）
#   prosperity_indicators: 纳入景气指数的指标
#   table_metrics: PDF表格中展示的所有指标（含分类）
# ============================================================

# 图表类型
TREND = 'trend'
SEASONAL = 'seasonal'

INDUSTRIES = ['煤炭', '钢铁', '有色', '石化', '基础化工']

INDUSTRY_CONFIG = {
    # ──────────────────────────────────────────────────────────
    # 煤炭（PDF Page 1）
    # ──────────────────────────────────────────────────────────
    '煤炭': {
        'color': '#4e8fd4',
        'summary_text': (
            '本周秦港现货煤825元/吨，周环比持平，动力煤价格偏稳运行。'
            '供给端晋陕蒙安监约束仍存，部分煤矿复产节奏偏慢，发运成本倒挂压制市场煤集港；'
            '需求端25省电厂日耗环比下降2.1%至580.5万吨，迎峰度夏用煤需求预期仍在，但电厂库存及长协保障较充足；'
            '库存方面主流港口及秦港库存环比下降，电厂库存小幅去化。短期煤价预计维持震荡运行。'
        ),
        'kpi_cards': [
            {'label': '秦港动力煤', 'series': '秦港动力煤价', 'unit': '元/吨', 'direction': 1},
            {'label': '秦皇岛港库存', 'series': '秦皇岛港库存', 'unit': '万吨', 'direction': -1},
            {'label': '25省电厂库存', 'series': '25省电厂库存', 'unit': '万吨', 'direction': -1},
            {'label': '25省电厂日耗', 'series': '25省电厂日耗', 'unit': '万吨', 'direction': 1},
        ],
        # PDF表格中所有指标（含分类和频次）
        'table_metrics': [
            {'category': '价格', 'label': '秦皇岛动力煤', 'series': '秦港动力煤价', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '价格', 'label': '平仓价:山西优混', 'series': '山西优混平仓价', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '价格', 'label': '秦港长协价', 'series': '秦港长协价', 'unit': '元/吨', 'direction': 1, 'frequency': '月度'},
            {'category': '库存', 'label': '煤炭库存:CCTD主流港口', 'series': 'CCTD港口库存', 'unit': '万吨', 'direction': -1, 'frequency': '周度'},
            {'category': '库存', 'label': '秦皇岛港库存', 'series': '秦皇岛港库存', 'unit': '万吨', 'direction': -1, 'frequency': '日度'},
            {'category': '库存', 'label': '25省电厂煤炭库存', 'series': '25省电厂库存', 'unit': '万吨', 'direction': -1, 'frequency': '日度'},
            {'category': '需求', 'label': '25省煤炭终端日耗', 'series': '25省电厂日耗', 'unit': '万吨', 'direction': 1, 'frequency': '日度'},
        ],
        'charts': [
            {
                'id': 'coal_price',
                'title': '价格：秦港现货煤价',
                'default_type': TREND,
                'series': [
                    {'name': '秦港动力煤价', 'label': '秦皇岛港动力煤价格', 'unit': '元/吨', 'color': '#4e8fd4'},
                ],
                'yaxis': {'title': '元/吨'},
            },
            {
                'id': 'plant_inv',
                'title': '库存：25省电厂煤炭库存',
                'default_type': SEASONAL,
                'series': [
                    {'name': '25省电厂库存', 'label': '25省电厂煤炭库存', 'unit': '万吨', 'color': '#4e8fd4'},
                ],
                'yaxis': {'title': '万吨'},
            },
            {
                'id': 'qhd_inv',
                'title': '库存：秦港煤炭库存',
                'default_type': SEASONAL,
                'series': [
                    {'name': '秦皇岛港库存', 'label': '秦皇岛港口', 'unit': '万吨', 'color': '#4e8fd4'},
                ],
                'yaxis': {'title': '万吨'},
            },
            {
                'id': 'daily_consumption',
                'title': '需求：25省煤炭日耗',
                'default_type': SEASONAL,
                'series': [
                    {'name': '25省电厂日耗', 'label': '25省煤炭终端日耗', 'unit': '万吨', 'color': '#4e8fd4'},
                ],
                'yaxis': {'title': '万吨'},
            },
        ],
        'prosperity_indicators': [
            {'series': '秦港动力煤价', 'yoy_type': 'pct', 'direction': 'positive'},
            {'series': '25省电厂日耗', 'yoy_type': 'pct', 'direction': 'positive'},
            {'series': '25省电厂库存', 'yoy_type': 'pct', 'direction': 'negative'},
            {'series': '秦皇岛港库存', 'yoy_type': 'pct', 'direction': 'negative'},
        ],
    },

    # ──────────────────────────────────────────────────────────
    # 钢铁（PDF Page 2，黑色）
    # ──────────────────────────────────────────────────────────
    '钢铁': {
        'color': '#e06c75',
        'summary_text': (
            '价格方面，本周螺纹钢3100元/吨、周环比下降1.0%，热卷3270元/吨、周环比下降1.2%，钢价延续震荡格局。'
            '供给端钢厂盈利比例仍处较低水平，开工率和铁水产量环比回落，五大材产量环比下降2.3%至818.3万吨；'
            '需求端地产及传统建筑用钢需求偏弱，加之多雨天气影响施工，五大材表观消费环比下降1.5%至811.9万吨。'
            '成材产量虽有所下降，但终端需求仍处于较弱水平，五大材库存小幅累库。短期钢价预计震荡运行。'
        ),
        'kpi_cards': [
            {'label': '上海热卷', 'series': '上海热卷价格', 'unit': '元/吨', 'direction': 1},
            {'label': '上海螺纹', 'series': '上海螺纹价格', 'unit': '元/吨', 'direction': 1},
            {'label': '五大材库存', 'series': '五大材库存', 'unit': '万吨', 'direction': -1},
            {'label': '高炉开工率', 'series': '高炉开工率', 'unit': '%', 'direction': 1, 'scale': 1},
        ],
        # PDF表格中所有指标（含分类和频次）
        'table_metrics': [
            {'category': '价格', 'label': '上海热卷', 'series': '上海热卷价格', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '价格', 'label': '上海螺纹', 'series': '上海螺纹价格', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '价格', 'label': '青岛港铁矿石价格指数', 'series': '铁矿石价格', 'unit': '美元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '库存', 'label': '钢材贸易商+社会库存', 'series': '五大材库存', 'unit': '万吨', 'direction': -1, 'frequency': '周度'},
            {'category': '库存', 'label': '重点钢企库存', 'series': '重点钢企库存', 'unit': '万吨', 'direction': -1, 'frequency': '旬度'},
            {'category': '需求', 'label': '铁水产量', 'series': '铁水产量', 'unit': '万吨', 'direction': 1, 'frequency': '周度'},
            {'category': '需求', 'label': '247家高炉开工率', 'series': '高炉开工率', 'unit': '%', 'direction': 1, 'scale': 100, 'frequency': '周度'},
            {'category': '需求', 'label': '粗钢产量', 'series': '五大材产量', 'unit': '万吨', 'direction': 1, 'frequency': '周度'},
            {'category': '需求', 'label': '粗钢表需', 'series': '五大材表需', 'unit': '万吨', 'direction': 1, 'frequency': '周度'},
            {'category': '盈利', 'label': '钢厂盈利率', 'series': '钢厂盈利率', 'unit': '%', 'direction': 1, 'scale': 100, 'frequency': '周度'},
            {'category': '盈利', 'label': '螺纹盈利', 'series': '螺纹盈利', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '盈利', 'label': '热卷盈利', 'series': '热卷盈利', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
        ],
        'charts': [
            {
                'id': 'steel_price',
                'title': '价格：钢材价格',
                'default_type': TREND,
                'series': [
                    {'name': '上海热卷价格', 'label': '上海热卷', 'unit': '元/吨', 'color': '#e06c75'},
                    {'name': '上海螺纹价格', 'label': '上海螺纹', 'unit': '元/吨', 'color': '#d19a66'},
                ],
                'yaxis': {'title': '元/吨'},
            },
            {
                'id': 'steel_demand',
                'title': '消费：五大材钢材消费量',
                'default_type': SEASONAL,
                'series': [
                    {'name': '五大材表需', 'label': '五大材表需', 'unit': '万吨', 'color': '#e06c75'},
                ],
                'yaxis': {'title': '万吨'},
            },
            {
                'id': 'steel_inv',
                'title': '库存：钢材贸易商+社会库存',
                'default_type': SEASONAL,
                'series': [
                    {'name': '五大材库存', 'label': '钢材库存，贸易商+钢厂', 'unit': '万吨', 'color': '#e06c75'},
                ],
                'yaxis': {'title': '万吨'},
            },
            {
                'id': 'steel_profit',
                'title': '盈利：钢材利润',
                'default_type': TREND,
                'series': [
                    {'name': '螺纹盈利', 'label': '螺纹盈利', 'unit': '元/吨', 'color': '#e06c75'},
                    {'name': '热卷盈利', 'label': '热卷盈利', 'unit': '元/吨', 'color': '#d19a66'},
                ],
                'yaxis': {'title': '元/吨', 'zeroline': True},
            },
        ],
        'prosperity_indicators': [
            {'series': '上海热卷价格', 'yoy_type': 'pct', 'direction': 'positive'},
            {'series': '螺纹盈利', 'yoy_type': 'diff', 'direction': 'positive'},
            {'series': '高炉开工率', 'yoy_type': 'diff', 'direction': 'positive'},
            {'series': '五大材库存', 'yoy_type': 'pct', 'direction': 'negative'},
        ],
    },

    # ──────────────────────────────────────────────────────────
    # 有色（PDF Page 3）
    # ──────────────────────────────────────────────────────────
    '有色': {
        'color': '#98c379',
        'summary_text': (
            '价格方面，本周1#铜现货环比下跌0.8%至105615元/吨，A00铝现货环比上涨1.6%至23625元/吨。'
            '宏观层面美联储降息预期反复，美元指数波动影响有色价格；'
            '铜方面铜矿TC/RC持续为负，矿端偏紧格局未改，铜社会库存环比上升2.5%至11.2万吨；'
            '铝方面国内电解铝现货库存环比下降5.3%至95.3万吨，库存延续去化对铝价形成支撑，但电解铝产量及产能利用率仍处高位，供应端压力仍存。短期预计高位震荡。'
        ),
        'kpi_cards': [
            {'label': 'A00铝价', 'series': 'A00铝价格', 'unit': '元/吨', 'direction': 1},
            {'label': '1#铜价', 'series': '1#铜价格', 'unit': '元/吨', 'direction': 1},
            {'label': '铜社会库存', 'series': '铜社会库存', 'unit': '万吨', 'direction': -1},
            {'label': '电解铝利润', 'series': '电解铝利润', 'unit': '元/吨', 'direction': 1},
        ],
        # PDF表格中所有指标（含分类和频次）
        'table_metrics': [
            {'category': '价格', 'label': 'A00铝', 'series': 'A00铝价格', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '价格', 'label': '1#铜', 'series': '1#铜价格', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '价格', 'label': '伦敦金', 'series': '伦敦金价格', 'unit': '美元/盎司', 'direction': 1, 'frequency': '日度'},
            {'category': '库存', 'label': '铜社会库存', 'series': '铜社会库存', 'unit': '万吨', 'direction': -1, 'frequency': '周度'},
            {'category': '库存', 'label': '铝社会库存', 'series': '电解铝库存', 'unit': '万吨', 'direction': -1, 'frequency': '周度'},
            {'category': '盈利', 'label': '电解铝税前利润', 'series': '电解铝利润', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '盈利', 'label': 'TC', 'series': '铜精矿TC', 'unit': '美元/干吨', 'direction': 1, 'frequency': '日度'},
            {'category': '盈利', 'label': 'RC', 'series': '铜精矿RC', 'unit': '美分/磅', 'direction': 1, 'frequency': '日度'},
        ],
        'charts': [
            {
                'id': 'copper_price',
                'title': '价格：1#铜现货价格',
                'default_type': TREND,
                'series': [
                    {'name': '1#铜价格', 'label': '1#铜现货价格', 'unit': '元/吨', 'color': '#98c379'},
                ],
                'yaxis': {'title': '元/吨'},
            },
            {
                'id': 'copper_inv',
                'title': '库存：铜社会库存',
                'default_type': TREND,
                'series': [
                    {'name': '铜社会库存', 'label': '铜社会库存', 'unit': '万吨', 'color': '#98c379'},
                ],
                'yaxis': {'title': '万吨'},
            },
            {
                'id': 'aluminum_inv',
                'title': '库存：电解铝社会库存',
                'default_type': TREND,
                'series': [
                    {'name': '电解铝库存', 'label': '电解铝社会库存', 'unit': '万吨', 'color': '#56b6c2'},
                ],
                'yaxis': {'title': '万吨'},
            },
            {
                'id': 'copper_tc',
                'title': '盈利：铜精矿现货TC',
                'default_type': TREND,
                'series': [
                    {'name': '铜精矿TC', 'label': '铜精矿现货TC', 'unit': '美元/干吨', 'color': '#98c379'},
                ],
                'yaxis': {'title': '美元/干吨', 'zeroline': True},
            },
        ],
        'prosperity_indicators': [
            {'series': '1#铜价格', 'yoy_type': 'pct', 'direction': 'positive'},
            {'series': 'A00铝价格', 'yoy_type': 'pct', 'direction': 'positive'},
            {'series': '电解铝利润', 'yoy_type': 'diff', 'direction': 'positive'},
            {'series': '铜社会库存', 'yoy_type': 'pct', 'direction': 'negative'},
        ],
    },

    # ──────────────────────────────────────────────────────────
    # 石化（PDF Page 4-5）
    # ──────────────────────────────────────────────────────────
    '石化': {
        'color': '#c678dd',
        'summary_text': (
            '价格方面，本周布伦特原油价格下跌6.9%至90.1美元/桶，NYMEX HH天然气价格下跌3.2%至2.79美元/百万英热附近。'
            '美伊先停火后再度互袭、局势反复，油价先跌后反弹，红海航运中断仍为油价提供较强底部支撑。'
            '海外高频数据中，美国炼厂开工率升至97.2%，商业原油库存环比下降1.7%；'
            '国内主营炼厂开工率70.20%，环比上升0.12ppt，山东地炼一次常减压开工负荷53.7%，较上周下降0.48ppt。'
        ),
        'kpi_cards': [
            {'label': '布伦特原油', 'series': '布伦特原油', 'unit': '美元/桶', 'direction': 1},
            {'label': 'NYMEX天然气', 'series': 'NYMEX天然气', 'unit': '美元/百万英热', 'direction': 1},
            {'label': '美国原油库存', 'series': '美国商业原油库存', 'unit': '千桶', 'direction': -1},
            {'label': '汽油裂解价差', 'series': '汽油裂解价差', 'unit': '元/吨', 'direction': 1},
        ],
        # PDF表格中所有指标（含分类和频次）
        'table_metrics': [
            {'category': '价格', 'label': '布伦特原油', 'series': '布伦特原油', 'unit': '美元/桶', 'direction': 1, 'frequency': '日度'},
            {'category': '价格', 'label': 'NYMEX天然气', 'series': 'NYMEX天然气', 'unit': '美元/百万英热', 'direction': 1, 'frequency': '日度'},
            {'category': '库存', 'label': '美国商业原油库存', 'series': '美国商业原油库存', 'unit': '千桶', 'direction': -1, 'frequency': '周度'},
            {'category': '库存', 'label': '美国成品油库存', 'series': '美国成品油库存', 'unit': '千桶', 'direction': -1, 'frequency': '周度'},
            {'category': '需求', 'label': '山东地炼开工率', 'series': '山东地炼开工率', 'unit': '%', 'direction': 1, 'scale': 100, 'frequency': '周度'},
            {'category': '需求', 'label': '美国炼厂开工率', 'series': '美国炼厂开工率', 'unit': '%', 'direction': 1, 'scale': 100, 'frequency': '周度'},
            {'category': '需求', 'label': '汽油供应+柴油供应', 'series': '美国成品油需求', 'unit': '千桶/日', 'direction': 1, 'frequency': '周度'},
            {'category': '盈利', 'label': '汽油裂解价差', 'series': '汽油裂解价差', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '盈利', 'label': '柴油裂解价差', 'series': '柴油裂解价差', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '盈利', 'label': '乙烯裂解毛利', 'series': '乙烯裂解毛利', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
        ],
        'charts': [
            {
                'id': 'oil_gas_price',
                'title': '价格：布伦特油价和NYMEX气价',
                'default_type': TREND,
                'dual_axis': True,
                'series': [
                    {'name': '布伦特原油', 'label': '布伦特油价', 'unit': '美元/桶', 'color': '#c678dd', 'axis': 'y1'},
                    {'name': 'NYMEX天然气', 'label': 'NYMEX天然气（右轴）', 'unit': '美元/百万英热', 'color': '#56b6c2', 'axis': 'y2'},
                ],
                'yaxis': {'title': '美元/桶'},
                'yaxis2': {'title': '美元/百万英热'},
            },
            {
                'id': 'us_crude_inv',
                'title': '库存：美国商业原油库存',
                'default_type': SEASONAL,
                'series': [
                    {'name': '美国商业原油库存', 'label': '美国商业原油库存', 'unit': '千桶', 'color': '#c678dd'},
                ],
                'yaxis': {'title': '百万桶'},
                'unit_scale': 0.001,  # 千桶→百万桶
            },
            {
                'id': 'refinery_op',
                'title': '需求：山东炼厂和美国炼厂开工率',
                'default_type': TREND,
                'series': [
                    {'name': '山东地炼开工率', 'label': '山东地炼开工率', 'unit': '%', 'color': '#c678dd', 'scale': 100},
                    {'name': '美国炼厂开工率', 'label': '美国炼厂开工率', 'unit': '%', 'color': '#56b6c2', 'scale': 100},
                ],
                'yaxis': {'title': '%'},
            },
            {
                'id': 'crack_spread',
                'title': '盈利：汽柴油裂解价差和乙烯裂解毛利',
                'default_type': TREND,
                'series': [
                    {'name': '汽油裂解价差', 'label': '汽油裂解价差', 'unit': '元/吨', 'color': '#c678dd'},
                    {'name': '柴油裂解价差', 'label': '柴油裂解价差', 'unit': '元/吨', 'color': '#d19a66'},
                    {'name': '乙烯裂解毛利', 'label': '乙烯蒸汽裂解毛利', 'unit': '元/吨', 'color': '#56b6c2'},
                ],
                'yaxis': {'title': '元/吨', 'zeroline': True},
            },
        ],
        'prosperity_indicators': [
            {'series': '布伦特原油', 'yoy_type': 'pct', 'direction': 'positive'},
            {'series': '汽油裂解价差', 'yoy_type': 'diff', 'direction': 'positive'},
            {'series': '山东地炼开工率', 'yoy_type': 'diff', 'direction': 'positive'},
            {'series': '美国商业原油库存', 'yoy_type': 'pct', 'direction': 'negative'},
        ],
    },

    # ──────────────────────────────────────────────────────────
    # 基础化工（PDF Page 6-7）
    # ──────────────────────────────────────────────────────────
    '基础化工': {
        'color': '#e5c07b',
        'summary_text': (
            '液氯市场走高，截至7月31日华东市场液氯价格上涨105元/吨至124元/吨，部分企业检修叠加下游刚需采购导致液氯价格上调。'
            '硫磺价格高位持稳，长江港口颗粒硫磺参考价报9170元/吨，地缘风险不确定性仍在，市场流通现货货源紧缺。'
            '六氟磷酸锂价格上涨3.45%至105000元/吨，终端电池厂排产普遍上调带动需求释放。'
            'PX-PTA-涤纶长丝产业链价格区间震荡，但长丝市场产销承压、库存增加，下游纺织市场新增订单不足。'
        ),
        'kpi_cards': [
            {'label': '化工价格指数', 'series': '化工价格指数', 'unit': '', 'direction': 1},
            {'label': 'PTA库存天数', 'series': 'PTA库存天数', 'unit': '天', 'direction': -1},
            {'label': '涤纶长丝开工率', 'series': '涤纶长丝开工率', 'unit': '%', 'direction': 1, 'scale': 100},
            {'label': 'POY价差', 'series': 'POY价差', 'unit': '元/吨', 'direction': 1},
        ],
        # PDF表格中所有指标（含分类和频次）
        'table_metrics': [
            {'category': '价格', 'label': '化工产品价格指数', 'series': '化工产品价格指数', 'unit': '', 'direction': 1, 'frequency': '日度'},
            {'category': '价格', 'label': '短纤市场价格', 'series': '短纤价格', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '价格', 'label': 'DTY市场价格', 'series': '涤纶DTY价格', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '价格', 'label': '乙烯CFR', 'series': '乙烯CFR价格', 'unit': '美元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '价格', 'label': '硫酸铵', 'series': '硫酸铵价格', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '价格', 'label': '除草剂价格指数', 'series': '除草剂价格指数', 'unit': '', 'direction': 1, 'frequency': '日度'},
            {'category': '库存', 'label': 'PTA库存天数', 'series': 'PTA库存天数', 'unit': '天', 'direction': -1, 'frequency': '周度'},
            {'category': '库存', 'label': 'POY库存天数', 'series': 'POY库存天数', 'unit': '天', 'direction': -1, 'frequency': '周度'},
            {'category': '库存', 'label': 'FDY库存天数', 'series': 'FDY库存天数', 'unit': '天', 'direction': -1, 'frequency': '周度'},
            {'category': '库存', 'label': 'DTY库存天数', 'series': 'DTY库存天数', 'unit': '天', 'direction': -1, 'frequency': '周度'},
            {'category': '生产', 'label': '涤纶长丝开工率', 'series': '涤纶长丝开工率', 'unit': '%', 'direction': 1, 'scale': 100, 'frequency': '日度'},
            {'category': '盈利', 'label': 'PX-石脑油价差', 'series': 'PX石脑油价差', 'unit': '美元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '盈利', 'label': 'POY-PTA-MEG价差', 'series': 'POY价差', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '盈利', 'label': 'FDY-PTA-MEG价差', 'series': 'FDY价差', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '盈利', 'label': 'DTY-PTA-MEG价差', 'series': 'DTY价差', 'unit': '元/吨', 'direction': 1, 'frequency': '日度'},
            {'category': '盈利', 'label': '石脑油裂解动态利润', 'series': '石脑油裂解利润', 'unit': '美元/吨', 'direction': 1, 'frequency': '日度'},
        ],
        'charts': [
            {
                'id': 'chem_price',
                'title': '价格：中国化工产品价格指数及乙烯价格',
                'default_type': TREND,
                'dual_axis': True,
                'series': [
                    {'name': '化工价格指数', 'label': '中国化工产品价格指数', 'unit': '', 'color': '#e5c07b', 'axis': 'y1'},
                    {'name': '乙烯CFR价格', 'label': '乙烯（右轴）', 'unit': '美元/吨', 'color': '#56b6c2', 'axis': 'y2'},
                ],
                'yaxis': {'title': '指数'},
                'yaxis2': {'title': '美元/吨'},
            },
            {
                'id': 'pta_poy_inv',
                'title': '库存：PTA及涤纶长丝(POY)库存天数',
                'default_type': TREND,
                'dual_axis': True,
                'series': [
                    {'name': 'POY库存天数', 'label': 'POY库存天数（左轴）', 'unit': '天', 'color': '#e5c07b', 'axis': 'y1'},
                    {'name': 'PTA库存天数', 'label': 'PTA库存天数（右轴）', 'unit': '天', 'color': '#56b6c2', 'axis': 'y2'},
                ],
                'yaxis': {'title': '天（POY）'},
                'yaxis2': {'title': '天（PTA）'},
            },
            {
                'id': 'poy_op_rate',
                'title': '生产：涤纶长丝开工率',
                'default_type': TREND,
                'series': [
                    {'name': '涤纶长丝开工率', 'label': '涤纶长丝开工率', 'unit': '%', 'color': '#e5c07b', 'scale': 100},
                ],
                'yaxis': {'title': '%'},
            },
            {
                'id': 'px_poy_spread',
                'title': '盈利：PX-石脑油及涤纶长丝(POY)价差',
                'default_type': TREND,
                'dual_axis': True,
                'series': [
                    {'name': 'PX石脑油价差', 'label': 'PX-石脑油价差（左轴）', 'unit': '美元/吨', 'color': '#e5c07b', 'axis': 'y1'},
                    {'name': 'POY价差', 'label': 'POY-PTA-MEG价差（右轴）', 'unit': '元/吨', 'color': '#56b6c2', 'axis': 'y2'},
                ],
                'yaxis': {'title': '美元/吨'},
                'yaxis2': {'title': '元/吨'},
            },
        ],
        'prosperity_indicators': [
            {'series': '化工价格指数', 'yoy_type': 'pct', 'direction': 'positive'},
            {'series': 'POY价差', 'yoy_type': 'diff', 'direction': 'positive'},
            {'series': '涤纶长丝开工率', 'yoy_type': 'diff', 'direction': 'positive'},
            {'series': 'PTA库存天数', 'yoy_type': 'pct', 'direction': 'negative'},
        ],
    },
}

# ============================================================
# 景气度状态阈值
# ============================================================
PROSPERITY_LEVELS = [
    (80, '强景气', '#f8b739'),   # >80
    (60, '景气', '#98c379'),     # 60-80
    (40, '中性', '#61afef'),     # 40-60
    (0, '低迷', '#e06c75'),      # <40
]


def get_prosperity_level(score):
    """根据分数返回 (label, color)"""
    if score is None or (hasattr(score, '__float__') and __import__('math').isnan(score)):
        return '无数据', '#666666'
    for threshold, label, color in PROSPERITY_LEVELS:
        if score >= threshold:
            return label, color
    return '低迷', '#e06c75'
