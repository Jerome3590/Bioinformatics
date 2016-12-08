import os
import pycurl
import json


os.chdir("C:/Users/Jerome/Documents/Bioinformatics")

GDC_URL = 'https://gdc-api.nci.nih.gov/files'

GDC_URL_legacy = 'https://gdc-api.nci.nih.gov/legacy/files/'

data = json.dumps({
    "filters":{
        "op":"in",
        "content":{
            "field":"files.file_id",
            "value":[
        "4dd5ba61-80ac-440f-aced-ce0d3d468f6b",
        "aba8283e-4cbf-4054-84b8-14523872b111",
        "2a84193a-3d0a-4b2d-a53c-a2a98ba09ab6",
        "b969347a-eaab-491d-84e1-f2f73627fa12",
        "fbc381a8-ff6e-4837-97c2-3d1244d0a473",
        "96569882-c360-4bd9-ae92-aefb0a170092",
        "3c132ab0-474a-4826-95da-9522e2796884",
        "834f9a5e-4fc9-4564-99a6-ef4abe6f5d46",
        "858a700e-12ed-4d61-a76b-0791185967b9",
        "d966cb7a-7cea-44e3-81a6-5d3a371936dc",
        "af5085c1-5b4e-4b88-9f5f-3c049cdd981f",
        "c12c0afc-b94b-424d-afe9-2e8dcc211302",
        "2e057ca9-6e4a-4b9a-bf99-a18da330d4ea",
        "5162dab8-17f6-4c1a-b21f-113eb159c54a",
        "ffc3e9ba-07f4-48b3-b5d2-95df2871d30d",
        "712ca278-6cc2-4bd9-8751-08367bf5a7af",
        "d7fddb99-6df0-4858-a563-7cbf3b99862a",
        "62c70369-5895-49b6-8dcd-7ebe7a1c986b",
        "a4e5b76f-a0e4-48f3-b11d-cc340ee85b57",
        "610d35a6-4a56-4832-8866-16cc6a363c1d",
        "696c2c1b-4216-45e1-b7bb-b2c20fd04fe8",
        "2397cdeb-1296-4fb9-b2e4-81dbb9c58978",
        "b80f3c7a-6ae0-4b04-bba0-09ad4c2cac17",
        "b3d800e8-9ba8-4c9d-a7f0-174d7e47d2e5",
        "7da9390f-cd3c-459b-8f6c-1b1403774fbe",
        "2fe9e43e-4076-4116-a044-9b25a2e2a3c7",
        "b82a7318-bde3-4325-8334-a68bcc17817d",
        "2dd0889c-d56f-48c2-ac12-7c67d8abd78c",
        "afe39273-a7d5-49af-b705-6284ef50e98f",
        "8198214f-589d-4117-bcbf-3661395e7331",
        "5dec5442-a62e-4933-996f-ed8b9f78f564",
        "93156b6c-5d16-484b-9cfa-4a1e79597931",
        "141ca0a2-3b26-4f36-af1d-82b11f157ee1",
        "cf8251aa-40b3-4300-ad8a-871eedca28b4",
        "29421eba-fc14-46fa-b2de-8fad4306b9bd",
        "f15a10ef-17e7-4897-8b37-234bef310794",
        "575a0d20-7b4a-47a3-a4cf-4c05c3606569",
        "8b70fd50-efa5-42b0-8120-1f5787fca8f3",
        "dcfa3c1e-7201-4a09-bc42-376c98c6282e",
        "f35df1b5-db5c-4553-9460-5a4b8c22a573",
        "90616428-a5f3-43af-9252-66a87d424996",
        "df42b092-d6b4-431b-8194-4f411f3809aa",
        "db51959d-ac35-4791-a691-e60400c8af27",
        "0c132393-8d20-4e82-86df-750353016323",
        "77a0da07-9a06-4db5-aede-a74859cb8c4d",
        "91cfbf2a-8043-45a9-a5da-0cdb3cc038e6",
        "916d41f2-5afa-4dbb-8135-6d36133c30a3",
        "d5b92edd-94cc-4491-940d-716c8062c7f9",
        "5c157ae6-8354-4fa6-bae4-32daaafae6a8",
        "73b7ad21-eb54-4953-91e0-0d85c02d92be",
        "f385c106-52ee-46fa-9a39-3ebdb9474ca7",
        "a4ee4f5b-568b-44a4-83f1-adf17e7deec5",
        "fe16c6ef-a6c1-44bb-984c-b6c249712707",
        "fe53998f-f948-4e9d-bdc9-5933cf4582cf",
        "e96c2bdc-243f-40d7-9220-0b2c87f36d98",
        "c868a243-c207-42af-b5f2-0c6372322f91",
        "680a9ce1-4152-443c-bae2-46a6ad62802f",
        "dccfc6d3-e074-430a-b427-20e3f2a874c9",
        "705c140c-7f8a-4078-b908-1394509c3087",
        ]
      }
    },
    "format":"TSV",

"fields":"file_name,file_id,cases.samples.portions.analytes.aliquots.submitter_id,cases.samples.sample_type,analysis.metadata.read_groups.sequencing_center, files.analysis.metadata.read_groups.target_capture_kit_name, files.analysis.created_datetime",
    "size":"1000000"
})

with open('GDC_Metadata.txt', 'wb') as gdc:

    c = pycurl.Curl()
    c.setopt(pycurl.URL, GDC_URL)
    c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, data)
    c.setopt(pycurl.WRITEDATA, gdc)
    c.perform()
    c.close()

