# Bioinformatics: GDC || TGCA Metadata Project

This project is to take a list of GDC UUIDs, 
query the GDC API using a JSON-formatted payload file and 
return TGCA metadata linking back to the GDC UUID.

Original API instructions are via curl shell command. Using Python pycurl instead to add additional file checks and processing.

See the following URL for details. https://gdc-docs.nci.nih.gov/API/Users_Guide/Search_and_Retrieval/#example-http-post-request 

You can place the UUIDs into the example Payload file attached and it will output the file_id, file_name, sample type (tumor, normal, etc.), sequencing center, and the TCGA barcode. Once you run the curl command in the example on the website, it will output the data you are looking for in tab-delimited format. 

Feel free to change the 'fields' line at the bottom to your liking, I'll attach a file that contains all of the available fields in the API. I should also mention that if the UUIDs are from the Legacy Archive, replace 'https://gdc-api.nci.nih.gov/files/' with 'https://gdc-api.nci.nih.gov/legacy/files/' in the shell command.
