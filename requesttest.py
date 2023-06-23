"""
Samuel Lee
06/23/2023
requesttest.py
"""
import requests as re
from requests.exceptions import ReadTimeout
import datetime
import time


CODES = {x:True for x in re.status_codes._codes.keys()}   # Response codes
URL = "http://acciis:8080/webapi/errors/"   # The page that is supposed to stop responding on app crash


def main():
    dt = datetime.datetime  # datetime object is used to create a timestamp
    while True:
        log = ''
        r = response()  # fetches response from the IIS server
        
        if CODES.get(r, False): # checks to see if the returned value from the IIS server was a response code
            log = f'GOOD: {dt.now()}: {r}\n'
        else:
            log = f'ERROR -------: {dt.now()}: {r}\n'
        
        with open('log.txt', 'a') as fd:    # opens log.txt and appends the log string
            fd.write(log)
        
        time.sleep(30)  # waits 30 seconds just to keep the amount of requests down
        


def response():
    try:
        r = re.get(URL, timeout=15) # fires a GET request to URL
        rc = r.status_code  #http status code of the response, good scenario is usually 403
    except ReadTimeout as rt:   # THIS is the 'error' when the app crashes.
        return f'ERROR: {type(rt)}: {rt}'
    except Exception as e:  # there are a few other errors that happen on occasion, but I don't think the app crashes when they happen.
        return f'ERROR: {type(e)}: {e}'
    return rc
        

if __name__ == "__main__":
    main()