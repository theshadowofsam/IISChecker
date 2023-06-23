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
    dt = datetime.datetime
    while True:
        log = ''
        r = response()
        
        if CODES.get(r, False):
            log = f'GOOD: {dt.now()}: {r}\n'
        else:
            log = f'ERROR -------: {dt.now()}: {r}\n'
        
        with open('log.txt', 'a') as fd:
            fd.write(log)
        
        time.sleep(30)
        


def response():
    try:
        r = re.get(URL, timeout=15)
        rc = r.status_code
    except ReadTimeout as rt:   # THIS is the 'error' when the app crashes.
        return f'ERROR: {type(rt)}: {rt}'
    except Exception as e:  # there are a few other errors that happen on occasion, but I don't think the app crashes when they happen.
        return f'ERROR: {type(e)}: {e}'
    return rc
        

if __name__ == "__main__":
    main()