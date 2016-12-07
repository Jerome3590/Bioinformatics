import pandas as pd
import numpy
import csv
import re
import os


os.chdir("C:/Users/Jerome/Documents/Bioinformatics")

with open('gdc_manifest.txt', 'r') as rf:
    with open('gdc_manifestAPI.txt', 'w') as wf:
        GDC_UUID_API = []
        for line in rf:
            wf.write('"'+line.strip()+'",')
            GDC_UUID_API.append('"'+line.strip()+'",')

df = pd.DataFrame(
    {'GDC UUID': GDC_UUID_API,

     }
)

print(df)
