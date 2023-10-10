# Observability Template (using Streamlit)
 [Link](https://streamlit.io/)

## Starting the Streamlit app
- As a docker container

    `docker compose up`

- Locally start the app with streamlit command. Make sure you have all the pre-requisites, dependencies in place( Ref. Section 2 of Project Overview )

    `streamlit run Hello.py`

## Project Overview

### 1. Data Files

The CSV files required for Observability templates are placed in [data](data) folder. 

### 2. Dependencies

To run this project, you'll need to install the required libraries and dependencies. You can do this by using the following command:

```bash
pip3 install -r requirements.txt
```
The [requirements.txt](requirements.txt) file contains a list of all the necessary libraries.

### 3. Data Loading

The project loads data from the CSV files into a DuckDB database. DuckDB is used as the storage and query engine for efficient data handling. It is lightweight and highly-performant to manage large datasets with ease.

### 4. Data Operations

Once the data is loaded into DuckDB, data operations and analyses are performed using SQL queries. The results are collected as DataFrames and processed/ visualized using Streamlit APIs.


## Build

To manually build a Docker image
- The docker build command builds an image from a Dockerfile . Run the following command from the app/ directory on your server to build the image:

    `docker build -t streamlit .`

- The -t flag is used to tag the image. Here, we have tagged the image streamlit. If you run:

    `docker images`

- You should see a streamlit image under the REPOSITORY column. For example:
    
      REPOSITORY   TAG       IMAGE ID       CREATED              SIZE 
      streamlit    latest    70b0759a094d   About a minute ago   1.02GB

### Run the Docker container
- Now that you have built the image, you can run the container by executing:

    `docker run -p 8501:8501 streamlit`
- The -p flag publishes the container’s port 8501 to your server’s 8501 port.

- You can now view your Streamlit app in your browser.
  [URL](http://0.0.0.0:8501)