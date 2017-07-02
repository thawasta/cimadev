import requests as req
import datetime
import sys

siteinfo = []
sites = ['http://copenhagenevent.dk/', 'https://polterabend.dk/', 'http://www.copenhagenet.dk/']


with open('plumdata.csv', 'ab') as pf:
    for site in sites:
        r = req.post('https://plumbr.eu/robot/validateDomain', {'domainName': site})
        if (r.ok == True):
            rs = req.post('https://plumbr.eu/robot/submit', {'domainName': site, 'reportEmail': 'andreas@cima.dk'})
            print rs
            dt = datetime.datetime.now().strftime('%d/%m/%y - %H.%M')
            pf.write('%s, %s\n' % (site, dt))