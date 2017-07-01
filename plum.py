import requests as req
import datetime
import csv
import sys
site = 'www.google.com'
siteinfo = []
#for site in range(1, len(sys.argv)):
r = req.post('https://plumbr.eu/robot/validateDomain', {'domainName': site})
if (r.ok == True):
    rs = req.post('https://plumbr.eu/robot/submit', {'domainName': site, 'reportEmail': 'andreas@cima.dk'})
    dt = datetime.datetime.strftime('')