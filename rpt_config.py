import datetime

"""
This file contains the classes, function and variables for
the user processes for configuring the report calculations. 
The file is meant to be imported into and called from a parent file for deployment.
"""
class InvalidPercents(Exception):
    """
    Raise when percents don't add up to 100
    """
    pass

class InvalidDateRange(Exception):
    """
    Raise when years are out of range
    """
    pass

def input_weights():
    """
    Prompts user for study weight report configuration
    """
    print(f'There are 3 report studies available for your report:')
    print(f'\t Disposable Income, Population, Urbanisation\n')
    print(f'Please enter 3 numbers which total to 100 for weighting the percent of each attribute\n')
    pct_unset = True
    while pct_unset:
        try:
            disp_pct = int(input('Disposable Income %: '))
            popu_pct = int(input('Population %: '))
            urba_pct = int(input('Urbanisation %: '))
            if ((disp_pct + popu_pct + urba_pct) != 100):
                raise InvalidPercents
            else:
                return([disp_pct,popu_pct,urba_pct])
        
        except InvalidPercents:
            print('\nAmounts entered do not sum to 100, please try again')
        
        except ValueError:
            print('\nNumbers only, please try again')

def years_loaded(stat_dict):
    """

    """

def input_years(stat_dict):
    """
    Prompts user for date range report configuration
    """
    print(f'The range of years studies available for your report are :')
    first_last_years = years_loaded(stat_dict)
    print(f'Please enter a start year and an end year within that range (inclusive)\n')
    years_unset = True
    while years_unset:
        try:
            start_year = int(input('Report start year:\n'))
            end_year = int(input('Report end year %:\n'))
            if !(start_year >= first_last_years[0] and end_year <= first_last_years[1]):
                raise InvalidDateRange
            else:
                return([start_year, end_year])
        
        except InvalidDataRange:
            print(f'\nYears must be between {range_list[0]} and {range_list[1]}, please try again')

def input_rpt_options(weights, years, regions, stat_dict):
    """
    Collect report options from user
    option functions return a list of values
    """
    print('Next step is to configure your report\n')
    weights = input_weights()
    years = input_years(stat_dict)
#    regions = input_regions()
