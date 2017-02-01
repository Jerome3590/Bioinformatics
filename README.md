# Bioinformatics: GDC || TCGA Metadata Project

This project is to take a list of GDC UUIDs, 
query the GDC API using a JSON-formatted payload file and 
return TCGA metadata linked back to the GDC UUID.

Original API instructions are via curl shell command. Using Python pycurl instead to add additional file checks and processing.

See the following URL for details. https://gdc-docs.nci.nih.gov/API/Users_Guide/Search_and_Retrieval/#example-http-post-request 

You can place the legacy TCGA UUIDs into the example Payload file attached and it will output the file_id, file_name, sample type (tumor, normal, etc.), sample_id, etc.  

Feel free to change the 'fields' line at the bottom to your liking, attached is also a file that contains all of the available fields in the API. I should also mention that if the UUIDs are from the Legacy Archive, replace 'https://gdc-api.nci.nih.gov/files/' with 'https://gdc-api.nci.nih.gov/legacy/files/'. I used the the legacy URL to get GDC UUIDs and then queried GDC URL at 'cases' endpoint for GDC data.
