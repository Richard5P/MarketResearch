from datetime import datetime
import csv

"""
The app is a Market Research sample tool to demonstrate how Python can be used
to prepare and present a typical market reseach report for business analysis.
There are two primary services: 
    1) Import statistical demographical data from an external file
    2) Prepare and present an ad-hoc market analysis report
The functions for each of those 2 services are contained in separate .py files.
    1)import.py
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

# Contstants
# Initialise statics dictionary with keys
STATS = [
    { 'stats_code':'popu',
      'stats_name':'Population',
      'value_type':'num',
      'country_stats':[{
         'country_code':None ,
	     'country_name': None ,
	     'region_code': None, 
	     'region_name': None,
	     'statistic':[{
		    'year': None,
		    'value': None
		    }]
        }]
    }]

def log_event(eventMsg):
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

def load_dict(stats_code, row):
    """
    loads statical data from stats_code.csv into STATS
    updates STATS with country data for stats_code, iterating through nested structure
    """
    print(stats_code, row)
    

def import_csv2dict(stats_name):
    """
    Imports data from csv file to python dictionary
    Assumes the csv file has headings in the first row, skips it
    Calls function to load remaining rows into STATS
    """
    file_name = stats_name + '.csv'
    print(file_name)
    stats_dict = dict()
    try:
        with open(file_name, 'r', encoding='utf-8-sig', newline='') as csv_file:
            csv_data = csv.reader(csv_file, dialect='excel')
            first_row = True
            for row in csv_data:
                if first_row:
                    # skip the first row of headers as keys already set up
                    print(f'First Row: {row}')
                    first_row = False
                    continue
                else:
                    # Replace with iteration to update nested dictionaries with values
                    print(f'data: {row}')
                    load_dict(stats_name, row)              
                    continue
            print(stats_name)

    except OSError as e:
        print(f'Unable to open CSV file. Please contact system manager with error:\n   >>  {e.args[1]}  <<')
        return False                      


# def load_dictionaries():

def main():
    """
    Entry and exit for the application
    Container and controller for launch of application functions
    """
#    log_event('Application Start')

    import_csv2dict('population')


main()