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

def import_csv(file_name, dict_name):
    """
    Imports data from csv file to python dictionary
    """
    try:
        with open(file_name,'r') as csvFile:
            first_row = True
            for row in csvFile:
                columns = row.split(",")
                print(f'Row: {row} \n Columns: {columns}\n')
                if first_row:
                    keyNames = row
                    first_row = False
                    print(f'Key Names: {keyNames}\n')
                    continue
                i = 0 
 #               while i < len(columns):
 #                   dict_name.append(keyNames[i],columns[i])
 #                   print(f'Key: {keyNames[i]}  Value: {columns[i]}')
    except OSError as e:
        print(f'Unable to open CSV file. Please contact system manager with error:\n   >>  {e.args[1]}  <<')
        return False                      
#   print(dict_name)

# def load_dictionaries():

def main():
    """
    Entry and exit for the application
    Container and controller for launch of application functions
    """
#    log_event('Application Start')
    test_dic = {}
    import_csv('population.csv', test_dic)


main()