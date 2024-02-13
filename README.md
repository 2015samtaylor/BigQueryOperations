# Data Transfer from SFTP to Google Cloud Storage and BigQuery

This Python script facilitates the download of a CSV file from an SFTP server and the subsequent upload to both Google Cloud Storage and BigQuery. It is designed to work with Google Cloud Storage and BigQuery, using the `google-cloud-storage` and `google-cloud-bigquery` libraries.

## Prerequisites

1. **Install Required Packages:**
   - Install the necessary Python packages using the following command:
     ```bash
     pip install pysftp pandas google-cloud-storage google-cloud-bigquery
     ```

2. **Google Cloud Service Account Key:**
   - Obtain a service account key JSON file from the [Google Cloud Console](https://console.cloud.google.com/iam-admin/serviceaccounts).
   - Set the path to your service account key file in the script.

## Configuration

1. **SFTP Credentials:**
   - Provide your SFTP credentials (host, username, password) in the script.
   - Adjust the remote and local file paths as needed.

2. **Google Cloud Storage:**
   - Replace the `bucket_name`, `csv_file_path`, and `destination_blob_name` with your Google Cloud Storage details.
   - Make sure you have the necessary permissions to write to the specified bucket.

3. **Google Cloud Service Account Key:**
   - Set the `key_file_path` variable to the path of your service account key JSON file.

## Usage

1. **Download CSV from SFTP:**
   - Run the script to download the CSV file from the specified SFTP server.

2. **Upload to Google Cloud Storage:**
   - The script will then upload the CSV file to the specified Google Cloud Storage bucket.

3. **Replicate in BigQuery:**
   - You can manually load the CSV into BigQuery using the [BigQuery Console](https://console.cloud.google.com/bigquery).
   - Alternatively, you can extend the script to automate the load into BigQuery using the `google-cloud-bigquery` library.

## Additional Notes

- The `pysftp` library is used for SFTP operations.
- Ensure the proper setup of your Google Cloud Storage and BigQuery environment.

---
