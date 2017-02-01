import os
import pycurl
import json
import platform
from filecmp import cmp

os.chdir("C:/Users/Jerome/PycharmProjects/Bioinformatics")

GDC_URL = 'https://gdc-api.nci.nih.gov/cases/'
GDC_URL_legacy = 'https://gdc-api.nci.nih.gov/legacy/files/'


def filename_query():

    with open('gdc_manifest2.txt', 'r') as ff:
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
           "fields": "file_id,file_name,",
           "size": "1000000"
       })

    with open('File_Names.txt', 'wb') as fff:

        c = pycurl.Curl()
        c.setopt(pycurl.URL, GDC_URL_legacy)
        c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, data)
        c.setopt(pycurl.WRITEDATA, fff)
        c.perform()
        c.close()


def case_id_query():

    with open('FileUUID.txt', 'r') as cc:
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


def format_file_uuids():

    with open("File_UUIDs.txt","r") as input:
       with open("FileUUID.txt","w") as output:
           for line in input:
               if line!="file_id"+"\n":
                  output.write(line)


def format_case_file():

    with open("CaseIDs.txt","r") as csi:
        with open("CaseID.txt","w") as csis:
            for line in csi:
                if line != "cases_0_case_id"+"\n":
                    csis.write(line)


def sample_data_query():

    with open('CaseID.txt', 'r') as ss:
        payload = []
        for line in ss:
            payload.append(line.rstrip())

    data = json.dumps({
        "filters":{
           "op":"in",
           "content":{
           "field":"case_id",
           "value": payload  }},
           "format": "JSN",
           "fields": "files.file_id,files.file_name,samples.sample_id,samples.sample_type,samples.tissue_type,samples.tumor_code,",
           "size": "1000000"
       })

    with open('Query_JSON.txt', 'wb') as sdc:

        c = pycurl.Curl()
        c.setopt(pycurl.URL, GDC_URL)
        c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, data)
        c.setopt(pycurl.WRITEDATA, sdc)
        c.perform()
        c.close()


def data_query():

    with open('CaseID.txt', 'r') as ss:
        payload = []
        for line in ss:
            payload.append(line.rstrip())

    data = json.dumps({
        "filters":{
           "op":"in",
           "content":{
           "field":"case_id",
           "value": payload  }},
           "format": "TSV",
           "fields": "files.file_id,files.file_name,samples.sample_id,samples.sample_type,samples.tissue_type,samples.tumor_code,",
           "size": "1000000"
       })

    with open('Query_TSV.txt', 'wb') as sdc:

        c = pycurl.Curl()
        c.setopt(pycurl.URL, GDC_URL)
        c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, data)
        c.setopt(pycurl.WRITEDATA, sdc)
        c.perform()
        c.close()


def file_uuid_query():

    with open('gdc_manifest2.txt', 'r') as ff:
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
        c.setopt(pycurl.URL, GDC_URL_legacy)
        c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, data)
        c.setopt(pycurl.WRITEDATA, fff)
        c.perform()
        c.close()


def run_gdc_api():

    file_uuid_query()
    if cmp('File_UUIDs.txt', 'File_UUIDs.txt') == True:
        format_file_uuids()
        if cmp('FileUUID.txt', 'FileUUID.txt') == True:
            case_id_query()
            if cmp('CaseIDs.txt', 'CaseIDs.txt') == True:
                format_case_file()
                if cmp('CaseID.txt', 'CaseID.txt') == True:
                    sample_data_query()
                    filename_query()
                    data_query()


run_gdc_api()
