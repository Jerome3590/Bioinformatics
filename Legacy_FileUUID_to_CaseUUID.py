import os
import pycurl
import json


os.chdir("C:/Users/Jerome/PycharmProjects/Bioinformatics")

GDC_URL = 'https://gdc-api.nci.nih.gov/files'

GDC_URL_legacy = 'https://gdc-api.nci.nih.gov/legacy/files/'

with open('gdc_manifest.txt', 'r') as dd:
    payload = []
    for line in dd:
        payload.append(line.rstrip())

data = json.dumps({
    "filters":{
        "op":"in",
        "content":{
            "field":"files.file_id",
            "value": payload }},
    "format":"TSV",

"fields":"cases.case_id",
    "size":"1000000"
})

print(data)

with open('CaseIDs_final.txt', 'wb') as tgc:

    c = pycurl.Curl()
    c.setopt(pycurl.URL, GDC_URL_legacy)
    c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.setopt(pycurl.WRITEDATA, tgc)
    c.perform()
    c.close()
