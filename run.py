"""
The app is a Market Research sample tool to demonstrate how Python can be used
to prepare and present a typical market reseach report for business analysis.
There are two primary services: 
    1) Import statistical demographical data from an external file
        Note: input files were created from XLXS spreadsheet and saved in CSV UTF-8(Comma delimited) format
    2) Prepare and present an ad-hoc market analysis report
The functions for each of those 2 services are contained in separate .py files.
    1)loadcsv.py
    2)report.py
This run.py contains the functions to:
   - initiate the app
   - initiate the error and results logging
        + functions for OS file operations
   - select the service to run
   - call the selected service
   - return a validation of the service run
   - allow the user to select another service or exit the app
"""

from loadcsv import *
from datetime import datetime


def log_event(event_msg):
    """
    Opens or creates a log file to record errors and operation results 
    for session.
    """
    try:
        with open('logfile.txt','+a') as log:
            now = datetime.now()
            rundate = now.strftime('%m/%d/%Y %H:%M:%S%f')
            log.write('\n' + rundate + '\t'+ event_msg)
    except OSError as e:
        print(f'Unable to open log file. Please contact system manager with error:\n   >>  {e.args[1]}  <<')
        return False       
    return True
#    log_event('Import Complete')
#    print('Report data is ready\n')
   
### start of input classes and functions
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
    pct_unset = True
    while pct_unset:
        try:
            disp_pct = int(input('Disposable Income %:\n'))
            popu_pct = int(input('Population %:\n'))
            urba_pct = int(input('Urbanisation %:\n'))
            if (disp_pct + popu_pct + urba_pct != 100):
                raise InvalidPercents
            else:
                return((disp_pct,popu_pct,urba_pct))
        
        except InvalidPercents:
            print('\nAmounts entered do not sum to 100, please try again')

def input_rpt_options(weights, years, regions, user_name):
    """
    Collect report options from user
    option functions return a list of values
    """
    print('Next step is to configure your report\n')
    weights = input_weights()
    print(weights)
#    years = input_years()
#    regions = input_regions()


#### end of input functions                 

def main():
    """
    Entry and exit for the application
    Container and controller for launch of application functions
    """
    # variables to be passed to reports
    weights = None
    years = None
    regions = None
    user_name = input('Please enter your name:\n')
    log_event('Application Start: '+user_name)
    print(f'Hello {user_name}\n')
    stats_dict = import_csv2dict('population')
    print(stats_dict)
    input_rpt_options(weights, years, regions, user_name)

main()