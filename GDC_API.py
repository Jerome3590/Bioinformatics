import os
import pycurl
import json

os.chdir("C:/Users/Jerome/PycharmProjects/Bioinformatics")

GDC_URL = 'https://gdc-api.nci.nih.gov/cases/'
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



def formatFileUUIDs():

    with open("File_UUIDs.txt","r") as input:
       with open("FileUUID.txt","w") as output:
           for line in input:
               if line!="file_id"+"\n":
                   output.write(line)


def formatCaseFile():

    with open("CaseIDs.txt","r") as input:
       with open("CaseID.txt","w") as output:
           for line in input:
               if line!="cases_0_case_id"+"\n":
                   output.write(line)



def Sample_Data_query():

    with open('CaseID.txt', 'r') as ss:
        payload = []
        for line in ss:
            payload.append(line.rstrip())

    data = json.dumps({
        "filters":{
           "op":"in",
           "content":{
           "field":"cases_id",
           "value": payload  }},
           "format": "TSV",
           "fields": "samples.sample_id,samples.sample_type,samples.tissue_type,samples.tumor_code",
           "size": "1000000"
       })

    print(data)

    with open('Sample_Data.txt', 'wb') as sdc:

          c = pycurl.Curl()
          c.setopt(pycurl.URL, GDC_URL)
          c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
          c.setopt(pycurl.POST, 1)
          c.setopt(pycurl.POSTFIELDS, data)
          c.setopt(pycurl.WRITEDATA, sdc)
          c.perform()
          c.close()


def FileUUID_query():

    with open('gdc_manifest.txt', 'r') as ff:
        payload = []
        for line in ff:
            payload.append(line.rstrip())

    data = json.dumps({
        "filters":{
           "op":"in",
           "content":{
           "field":"files.file_id",
           "value": payload  }},
           "format": "TSV",
           "fields": "file_id,",
           "size": "1000000"
       })

    with open('File_UUIDs.txt', 'wb') as fff:

          c = pycurl.Curl()
          c.setopt(pycurl.URL, GDC_URL)
          c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
          c.setopt(pycurl.POST, 1)
          c.setopt(pycurl.POSTFIELDS, data)
          c.setopt(pycurl.WRITEDATA, fff)
          c.perform()
          c.close()



#FileUUID_query()
#formatFileUUIDs()

#CaseID_query()
#formatCaseFile()

#Clinical_Data_query()

Sample_Data_query()

