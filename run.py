from datetime import datetime
import csv

"""
The app is a Market Research sample tool to demonstrate how Python can be used
to prepare and present a typical market reseach report for business analysis.
There are two primary services: 
    1) Import statistical demographical data from an external file
        Note: input files were created from XLXS spreadsheet and saved in CSV UTF-8(Comma delimited) format
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
STATS = [{'stats_code':'disp',
        'stats_name':'Disposable Income',
        'value_type':'val',
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
    },
    {'stats_code':'popu',
        'stats_name':'Population',
        'value_type':'num',
        'country_stats':[{
            'country_code':None ,
	        'country_name': None ,
	        'region_code': None, 
	        'region_name': None,
	        'statistics':[{
		        'year': None,
		        'value': None
		    }]
        }]
    }
]

# List to hold years from header to be zipped with values
YEAR_KEYS = []

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

def load_country_stats(stats_code, data_row, header_row):
    """
    loads the country_stats keys with values from header row in file
    """
    for stat in STATS:
        if stat['stats_code'] == stats_code:
            for country in stat['country_stats']:
                country['country_code'] = data_row[0]
                country['country_name'] = data_row[1]
                country['region_code'] = data_row[2]
                country['region_name'] = data_row[3]
                load_statistics(country['statistics'], data_row, header_row)
        print(stat)

def load_statistics(stat_dict, data_row, header_row):
    """
    loads annual statistical data for each country from stats_code.csv into STATS
    uses header row for year value and data rows for values
    """
    value_row = data_row
    key_row = header_row
    for i in range(2,len(value_row)):
        stat_dict.append({key_row[i]:value_row[i]})


def import_csv2dict(stats_name):
    """
    Imports data from csv file to python dictionary
    Assumes the csv file has headings in the first row for statistics keys
    Calls function to load remaining rows into STATS
    """
    stats_code = stats_name[:4]
    file_name = stats_name + '.csv'
    header_row = []
    try:
        with open(file_name, 'r', encoding='utf-8-sig', newline='') as csv_file:
            csv_data = csv.reader(csv_file, dialect='excel')
            first_row = True
            for row in csv_data:
                if first_row:
                    header_row = row
                    first_row = False
                    continue
                else:
                    load_country_stats(stats_code, row, header_row)          
                    continue

    except OSError as e:
        print(f'Unable to open CSV file. Please contact system manager with error:\n   >>  {e.args[1]}  <<')
        return False                      

def main():
    """
    Entry and exit for the application
    Container and controller for launch of application functions
    """
#    log_event('Application Start')
    import_csv2dict('population')


main()