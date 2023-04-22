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

def input_weights():
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
                return((disp_pct,popu_pct,urba_pct))
        
        except InvalidPercents:
            print('\nAmounts entered do not sum to 100, please try again')
        
        except ValueError:
            print('\nNumbers only, please try again')

def input_years():
    print(f'The range of years studies available for your report are ')
    print(f'\t Disposable Income, Population, Urbanisation\n')
    print(f'Please enter 3 numbers which total to 100 for weighting the percent of each attribute\n')
    years_unset = True
    while years_unset:
        try:
            disp_pct = int(input('Disposable Income %:\n'))
            popu_pct = int(input('Population %:\n'))
            urba_pct = int(input('Urbanisation %:\n'))
            if (disp_pct + popu_pct + urba_pct != 100):
                raise InvalidPercents
            else:
                return([disp_pct,popu_pct,urba_pct])
        
        except InvalidPercents:
            print('\nAmounts entered do not sum to 100, please try again')

def input_rpt_options(weights, years, regions, stat_dict):
    """
    Collect report options from user
    option functions return a list of values
    """
    print('Next step is to configure your report\n')
    weights = input_weights()
    print(weights)
#    years = input_years()
#    regions = input_regions()
