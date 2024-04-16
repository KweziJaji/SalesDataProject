# SalesDataProject
# Problem Statement 
A Turkish Retail Company owns a chain of stores and they wanted to use data to help them uncover some insights about their business. The company wants to achieve the following using data:

- Help regional managers uncover new opportunities to grow sales and profits for the business.
- Provide a national view of the business.
- Provide information for C-level executives so that they can focus on regional managers and cities they manage to make better decisions and help drive sales and profit growth. 

The company supplied sales data that was collected from the beginning of 2017 to the end of 2019 to be used to uncover insights. The data used was obtained from https://www.kaggle.com/datasets/berkayalan/retail-sales-data

# Solution 
The csv files supplied by the company were stored in a data lake bucket within Google Cloud Storage. A mage orchestration application was created to load the files from Google Cloud Storage, transform the files using Python and the Pandas library and export them to the Google BigQuery data warehouse. Within the big query warehouse data is partitioned daily within the final sales table. The final sales table is the linked to a dashboard in Data Studio that business will use to get the insights.  Terraform is used to manage infrastructure as code and all the Google Cloud resources used within this project are created through Terraform. The pipeline is scheduled to run daily. 
![alt text](https://github.com/KweziJaji/SalesDataProject/blob/main/Solution.JPG?raw=true)
 ## Technology Used 
 - Python was used as a programming language. 
 - Terraform was used for managing infrastructure as code. 
 - Mage was used an orchestrator. 
 - Google Cloud Storage was used as a data lake. 
 - Big Query was used as a data warehouse. 
 - Google Data Studio/ Looker Studio was used for visualisation. 
 ## Dashboard 
  ![alt text](https://github.com/KweziJaji/SalesDataProject/blob/main/Dashboard.JPG?raw=true)
  Dashboard Link: https://lookerstudio.google.com/reporting/1347fff4-3c12-4cf9-a193-1c80e29b810f

# How to replicate solution? 
 ## Pre-requisites
 - Docker must be installed
 - Terraform must be installed
 - Mage must be installed 
 - Google Cloud account must be active

  ## Set Up Google Resources
  -	Create a project in Google Cloud
  -	Set up a service account. The service account needs to have the following roles:
    * BigQuery Admin
    * Compute Admin
    * Storage Admin     
  -	Create a key for the service account and download the json version 
  -	Change directory into the Terraform folder and edit the files to point to your key file
  -	Run the following command to create the GCP resources:
    ```bash
        terraform init
        terraform plan 
        terraform apply
     ```

 ## Mage Application Steps
 -	Clone the solution from GitHub 
 -	Change directory into to the solution folder 
 -	Run docker compose up to get Mage up and running
       ```bash
        docker compose up -d
     ```




