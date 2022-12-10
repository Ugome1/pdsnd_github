import pandas as pd
import numpy as np


DADO_DATA = {'sales': 'report.csv'}

def user_input():
    """Takes user input"""

    while True:
        input_value = ["january", "febuary", "march", "april", "may","june","july","august","september","october","november","december"]
        month = input("Enter month: ").lower()
        if month in input_value:
            print("Month inputed: ", month)
            break
        else:
            print("Invalid input")

    return month

print("-"*40)


def load_data(month):
    """Load data"""

    df = pd.read_csv('report.csv')
    dfmod = df.fillna(" ")
    dfmod1 = dfmod.head(12)
    dfmod2 = dfmod1.iloc[:,:23]
    print(dfmod2)
    dfmod2 = dfmod2[dfmod2['MONTH'] == month.upper()]
    print(dfmod2)
    return dfmod2

print("-"*40)


def month_data(dfmod2):
    """Lists the data for that month"""
    print('\n')
    
    print('ORDER STAT')
    print("="*20)
    print('\n')

    working_days = dfmod2['WORKING DAYS']
    print('Number of working days:', working_days.to_string(index = False))
    print('\n')

    over_all_total = dfmod2['OVER ALL TOTAL']
    print('All time orders:', over_all_total.to_string(index = False))
    print('\n')

    print('\n')
    print('COST REPORT')
    print("="*20)

    dfmod2['Operating cost'] = dfmod2['OPERATIONS SALARIES'] + dfmod2['VENDOR SETTLEMENT'] + dfmod2['FUEL'] + dfmod2['BIKE SERVICING'] + dfmod2['AIRTIME'] + dfmod2['UTILITY EXPENSES']
    Operating = dfmod2['Operating cost']
    print('Your operating cost is:', Operating.to_string(index = False))
    print('\n')

    dfmod2['Direct cost'] = dfmod2['OPERATIONS SALARIES'] + dfmod2['FUEL'] + dfmod2['BIKE SERVICING'] + dfmod2['AIRTIME'] + dfmod2['UTILITY EXPENSES']
    Direct = dfmod2['Direct cost']
    print('Your Direct cost is:', Direct.to_string(index =  False))
    print('\n')

    dfmod2['Overall cost'] = dfmod2['ADMIN SALARY'] + dfmod2['OPERATIONS SALARIES'] + dfmod2['VENDOR SETTLEMENT'] + dfmod2['FUEL'] + dfmod2['BIKE SERVICING'] + dfmod2['AIRTIME'] + dfmod2['UTILITY EXPENSES']
    Overall = dfmod2['Overall cost']
    print('Your Overall cost is:', Overall.to_string(index =  False))
    print('\n')

    print("-"*20)
    print('\n')

    print('REVENUE REPORT')
    print("="*20)
    print('\n')

    Net_revenue = dfmod2['GMV']
    print('Your Revenue is:', Net_revenue.to_string(index =  False))
    print('\n')

    dfmod2['Net income'] = dfmod2['GMV'] - dfmod2['Operating cost']
    Revenue = dfmod2['Net income']
    print('Your Net income is:', Revenue.to_string(index =  False))
    print('\n')

    dfmod2['Profit margin'] = (dfmod2['Net income']/ dfmod2['GMV'])* 100
    Margin = dfmod2['Profit margin']
    print('Your Profit margin is:', Margin.to_string(index =  False))
    print('\n')


    #Net profit margin =
    print("-"*20)
    print('\n')


def main():
    while True:
        month = user_input()
        dfmod2 = load_data(month)

        month_data(dfmod2)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
