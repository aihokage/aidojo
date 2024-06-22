import numpy as np


def assert_positive(val: float) -> None:
    assert val > 1e-6


def extract_mark_up(row):
    return row[:, 5]


REVENUE = 'revenue'
PROFIT = 'profit'
EXPENSES = 'expenses'
MARKUP = 'mark_up'
COSTS_INDICATOR = 'costs_indicator'
COUNTER = 'counter'
Q1 = 'Q1'
Q2 = 'Q2'
Q3 = 'Q3'
Q4 = 'Q4'
Q1_Q2 = 'q1_q2'
Q2_Q3 = 'q2_q3'
Q3_Q4 = 'q3_q4'


if __name__ == '__main__':
    financial_data = np.genfromtxt('data/financial_data.csv', delimiter=',', dtype=str, skip_header=1)
    mark_ups = financial_data[:, 3].astype(float) / financial_data[:, 2].astype(float)
    cost_indicators = financial_data[:, 4].astype(float) / financial_data[:, 2].astype(float)
    financial_data_extended: np.ndarray = np.c_[
        financial_data,
        mark_ups,
        cost_indicators,
        np.zeros(shape=(financial_data.shape[0], 3)).astype(str)
    ]

    financial_data_dict = {}
    for company_name in np.unique(financial_data_extended[:, 0]):
        for quarter_symbol in np.unique(financial_data_extended[:, 1]):
            if company_name not in financial_data_dict:
                financial_data_dict[company_name] = {
                    'mark_up_score': 0
                }
            if quarter_symbol not in financial_data_dict[company_name]:
                financial_data_dict[company_name][quarter_symbol] = {
                    REVENUE: None,
                    PROFIT: None,
                    EXPENSES: None,
                    MARKUP: None,
                    COSTS_INDICATOR: None
                }
            active_row = np.reshape(financial_data_extended[
                                        (financial_data_extended[:, 0] == company_name)
                                        & (financial_data_extended[:, 1] == quarter_symbol)
                                        ], newshape=(10,))
            financial_data_dict[company_name][quarter_symbol][REVENUE] = active_row[2]
            financial_data_dict[company_name][quarter_symbol][PROFIT] = active_row[3]
            financial_data_dict[company_name][quarter_symbol][EXPENSES] = active_row[4]
            financial_data_dict[company_name][quarter_symbol][MARKUP] = active_row[5]
            financial_data_dict[company_name][quarter_symbol][COSTS_INDICATOR] = active_row[6]
        REVENUE_INCREASE = 'revenue_increase'
        if REVENUE_INCREASE not in financial_data_dict[company_name]:
            financial_data_dict[company_name][REVENUE_INCREASE] = {}
        financial_data_dict[company_name][REVENUE_INCREASE][Q1_Q2] \
            = (float(financial_data_dict[company_name][Q2][REVENUE])
               / float(financial_data_dict[company_name][Q1][REVENUE]))
        financial_data_dict[company_name][REVENUE_INCREASE][Q2_Q3] \
            = (float(financial_data_dict[company_name][Q3][REVENUE])
               / float(financial_data_dict[company_name][Q2][REVENUE]))
        financial_data_dict[company_name][REVENUE_INCREASE][Q3_Q4] \
            = (float(financial_data_dict[company_name][Q4][REVENUE])
               / float(financial_data_dict[company_name][Q3][REVENUE]))
        financial_data_dict[company_name][REVENUE_INCREASE][COUNTER] = 0

        for quarters_key, revenue_increase in financial_data_dict[company_name][REVENUE_INCREASE].items():
            if quarters_key != COUNTER and revenue_increase > 1.1:
                financial_data_dict[company_name][REVENUE_INCREASE][COUNTER] += 1
                print(f'Revenue increase above 10% for {company_name} between quarters {quarters_key}')

        if financial_data_dict[company_name][REVENUE_INCREASE][COUNTER] > 1:
            print(f'{company_name} achieved high revenue increase in multiple quarters')

    financial_data_sorted_by_mark_up \
        = financial_data_extended[np.argsort(extract_mark_up(financial_data_extended))][::-1]
    print('Top 4 markups:')
    for i in range(4):
        active_row = financial_data_sorted_by_mark_up[i]
        print(f'Top {i}. markup for {active_row[0]} in {active_row[1]} = {active_row[5]}')

    # Conclusion: Company B scored well!
