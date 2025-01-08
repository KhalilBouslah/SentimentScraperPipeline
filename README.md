# SentimentScraperPipeline
An end-to-end ETL pipeline designed to collect user reviews, analyze sentiments with an NLTK model, and store the results in a database, all orchestrated with Apache Airflow

First you need to install apache airflow locally or on docker (windows use)

#Installation of apache airflow:(using bash)
            
    sudo mdkir airflow && cd airflow

# Create new python Environment:

    python -m venv airflow-env

# install airflow package:
 
    pip install apache-airflow

# activate airflow environment:

    source airflow-env/bin/activate

# Set the Airflow Home Directory:
    export AIRFLOW_HOME=~/airflow

# Open apache airflow(you nee to activate the environment to execute this code):
    python -m airflow standalone

#Your apache airflow is set at localhost:8080 by default and username and password are by default 'airflow' 

#Copy the python scripts to a folder called dags in airflow floder 

#Open your apache airflow on browser and search for dag folder which is by default 'dags' (You can change it by executing airflow.cfg file)





