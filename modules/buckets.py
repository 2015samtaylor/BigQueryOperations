import os
from google.cloud import storage
from google.cloud.exceptions import NotFound




def create_bucket(bucket_name, storage_class = 'STANDARD', location='us-south1'):

    storage_client = storage.Client()

    try:
        # Attempt to get the bucket
        bucket = storage_client.get_bucket(bucket_name)
        print(f'Bucket {bucket_name} already exists.')
        return(bucket)  # You may choose to return the existing bucket if needed
    
    except NotFound:
        # Bucket not found, create a new one with storage_class arg and location
        bucket = storage_client.bucket(bucket_name)
        bucket.storage_class = storage_class

        bucket = storage_client.create_bucket(bucket, location=location)
        print(f'Bucket {bucket_name} created in {location} with {storage} storage class.')
        return(bucket)


#blob name is the name of the file once uploaded
#file_path is local file path
#bucket name is GC bucket unique bucket name
def upload_to_bucket(destination_blob_name, local_file, bucket_name):

    #Initialize a Google Cloud Storage client
    storage_client = storage.Client()

    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        # Get the existing blob (if it exists)
        try:
            existing_blob = bucket.get_blob(destination_blob_name)
            existing_updated_time = existing_blob.updated
        except NotFound:
            existing_blob = None
   


        blob.upload_from_filename(os.getcwd() + f'\\{local_file}')
        print(f"File {local_file} uploaded to {bucket_name} in {destination_blob_name}.")

        # Check if the file was overwritten based on blob names
        if existing_blob and existing_blob.name == destination_blob_name:
            print(f"File {destination_blob_name} was overwritten in {bucket_name}.")
        elif existing_blob:
            print(f"File {destination_blob_name} was uploaded as a new file in {bucket_name}.")
        
    except Exception as e:
        print(e)




