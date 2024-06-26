## README: Data Pipeline Automation

### Overview
This project demonstrates a data pipeline automation process using Python. It transfers the contents of the SFTP, & uploads it to Google Cloud Storage (GCS) buckets. Lastly it then loads the data into BigQuery for database storage. 

The general flow and population works the same across for all instances. The requested SFTP folder & all of its files within are on the remote server. The folder and all of its contents are replicated onto a Google Cloud Bucket. Then a database is created based on the name of the initial SFTP folder, and all files in the bucket are iterated through to create the tables. 

The name of the bucket will assume the first portion of the SFTP folder name. The name of the local directory created will also be the name of the SFTP folder nested within the 'SFTP_folders' directory. 
Class instances are created based on the name of the SFTP folder. Example shown below:

```python
instance = Create(
               project_id='powerschool-420113',
               location = 'us-south1',
               bucket=f'{SFTP_folder_name}bucket-iotaschools-1',
               local_dir = fr'S:\SFTP\\{SFTP_folder_name}',
               db = SFTP_folder_name,
               append_or_replace='replace',
               )

main("powerschool")
main("EIS")
```

### Installation
1. Clone the repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.

### Usage
1. **Setup Google Cloud Platform (GCP) Credentials**:
   - Set up your Google Cloud Platform (GCP) credentials by creating a service account and downloading the JSON key file. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of your JSON key file.
   

3. **Running the Script**:
   - Execute the script to start the data pipeline automation process. It will perform the following steps:
     - Connect to the SFTP server and download a remote file.
     - Create a new bucket in Google Cloud Storage (GCS) or use an existing one.
     - Upload the downloaded folder to the GCS bucket.
     - Load the data from the GCS bucket into a BigQuery table.
     - Execute a SQL query on the BigQuery table for data analysis.
     - Refer to log file created for more in depth step by step of the process.



4. **Customization**:
   - Modify the `Create` class attributes to fit your specific data pipeline requirements.
   - Customize the SQL queries to analyze different datasets in BigQuery.

### Dependencies
- **Python Libraries**:
  - `pandas`: Data manipulation library.
  - `pandas_gbq`: Google BigQuery integration for Pandas.
  - `pysftp`: SFTP client library.
  - `google-cloud-storage`: Google Cloud Storage client library.
  - `google-cloud-bigquery`: Google BigQuery client library.

### Notes
- Ensure that the SFTP server, Google Cloud Storage, and BigQuery environments are properly configured with the necessary permissions and access credentials.
- Ensure that the service account associated with the connection has proper IAM credentials to interact with GCS and Big Query. 

### Potential Concerns and Improvements with pre-processing

- Potential with headers issues if file read in is not header=0
- More complex pre-processing modules could be created to maintain the dtypes
- Potential data type issues, doing calculations on column data when they are coming across as strings.

