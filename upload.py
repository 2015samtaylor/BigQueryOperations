import os
from google.cloud import storage
import pysftp
import pandas as pd
pd.set_option('display.max_columns', None)

# # Use
# cnopts = pysftp.CnOpts()
# cnopts.hostkeys = None


# #Get Data from PS Data Export Manager SFTP folder, and move to BigQuery
# with pysftp.Connection(
#     host="sftp.illuminateed.com",
#     username="greendottn",
#     password="*********",
#     cnopts=cnopts
# ) as sftp:
#     # Download a remote file to the local machine
#     remote_file = "/greendottn/custom_report_standards_2024"
#     local_file = "local_file.csv"
#     sftp.get(remote_file, local_file)



# --------------------------------Use BigQuery creds to upload to simple storage-----------------------

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'keys.json'


def upload_csv_to_storage(bucket_name, source_file_path, destination_blob_name):
    """Uploads a CSV file to Google Cloud Storage."""
    # Initialize a Google Cloud Storage client
    storage_client = storage.Client()


    # Specify the bucket and create a blob (object) in the bucket
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)


    # Upload the CSV file
    blob.upload_from_filename(source_file_path)


    print(f"File {source_file_path} uploaded to {destination_blob_name} in {bucket_name}.")


# Replace these with your GCP project and Cloud Storage details
bucket_name = "psholdingbucket"
source_file_path = "students.csv"
destination_blob_name = "student_data/students.csv"


# Call the function to upload the CSV file
upload_csv_to_storage(bucket_name, source_file_path, destination_blob_name)


# --------------------------Once Uploaded to Google Cloud Storage Replicate in DB-----------

#name of bucket in Google Cloud is 
# bucket name is tn-ps
#single region
