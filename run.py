from datetime import datetime

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
def start_log():
    """
    Opens or creates a log file to record errors and operation results 
    for session.
    """
    log = open('logfile.txt','+a')
    now = datetime.now()
    rundate = now.strftime('%m/%d/%Y %H:%M:%S%f')
    log.write('\nlog for: ' + rundate)

start_log()
