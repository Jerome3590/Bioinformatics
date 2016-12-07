import os
import pycurl
import json


os.chdir("C:/Users/Jerome/Documents/Bioinformatics")

GDC_URL = 'https://gdc-api.nci.nih.gov/files'
GDC_URL_legacy = 'https://gdc-api.nci.nih.gov/legacy/files/'

data = 'gdc_manifestAPI.txt'

with open('GDC_metadata.txt', 'wb') as gdc:

    c = pycurl.Curl()
    c.setopt(pycurl.URL, GDC_URL)
    c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
    c.setopt(pycurl.POSTFIELDS, data)
    c.setopt(pycurl.WRITEDATA, gdc)
    c.perform()
    c.close()
