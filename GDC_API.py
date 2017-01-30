import os
import pycurl
import json
import re

os.chdir("C:/Users/Jerome/PycharmProjects/Bioinformatics")

GDC_URL = 'https://gdc-api.nci.nih.gov/files/'
GDC_URL_legacy = 'https://gdc-api.nci.nih.gov/legacy/files/'


def Clinical_Data_query():

    with open('gdc_manifest.txt', 'r') as dd:
        payload = []
        for line in dd:
            payload.append(line.rstrip())

    data = json.dumps({
        "filters":{
           "op":"in",
           "content":{
           "field":"files.file_id",
           "value": payload  }},
           "format": "TSV",
           "fields": "case_id,",
           "size": "1000000"
       })



    with open('Clinical_Data.txt', 'wb') as gdc:

          c = pycurl.Curl()
          c.setopt(pycurl.URL, GDC_URL_legacy)
          c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
          c.setopt(pycurl.POST, 1)
          c.setopt(pycurl.POSTFIELDS, data)
          c.setopt(pycurl.WRITEDATA, gdc)
          c.perform()
          c.close()


def CaseID_query():

    with open('gdc_manifest.txt', 'r') as cc:
        payload = []
        for line in cc:
            payload.append(line.rstrip())

    data = json.dumps({
        "filters":{
           "op":"in",
           "content":{
           "field":"files.file_id",
           "value": payload  }},
           "format": "TSV",
           "fields": "cases.case_id",
           "size": "1000000"
       })



    with open('CaseIDs.txt', 'wb') as csd:

          c = pycurl.Curl()
          c.setopt(pycurl.URL, GDC_URL_legacy)
          c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
          c.setopt(pycurl.POST, 1)
          c.setopt(pycurl.POSTFIELDS, data)
          c.setopt(pycurl.WRITEDATA, csd)
          c.perform()
          c.close()


def formatCaseFile():

    with open("CaseIDs.txt","r") as input:
       with open("CaseID.txt","w") as output:
           for line in input:
               if line!="cases_0_case_id"+"\n":
                   output.write(line)


def queryCaseID_test():

    with open('CaseID.txt', 'r') as cc:
        payload = []
        for line in cc:
            payload.append(line.rstrip())

    data = json.dumps({
        "filters":{
           "op":"in",
           "content":{
           "field":"annotation.case_id",
           "value": payload  }},
           "format": "TSV",
           "fields": "file_id,",
           "size": "1000000"
       })

    with open('Classification.txt', 'wb') as cdg:

          c = pycurl.Curl()
          c.setopt(pycurl.URL, GDC_URL)
          c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
          c.setopt(pycurl.POST, 1)
          c.setopt(pycurl.POSTFIELDS, data)
          c.setopt(pycurl.WRITEDATA, cdg)
          c.perform()
          c.close()


Clinical_Data_query()

CaseID_query()

formatCaseFile()

#queryCaseID_test()

