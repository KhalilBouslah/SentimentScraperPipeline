from airflow import DAG
from airflow.operators.python import PythonOperator  # Updated import
from datetime import datetime
from web_scrapping import get_data
from sentiment_analysis import sentiment
from db_connect import table_load
# Define the DAG
default_args = {
    'owner': 'khalil',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'etl_dags',
    default_args=default_args,
    description='my first etl in airflow'
) 
# Task to run the first notebook
run_etl = PythonOperator(
task_id='run_the_web_scrapping_project',
python_callable=get_data,
dag=dag
    )

run_sentiment = PythonOperator(
task_id='run_sentiment_model',
python_callable=sentiment,
dag=dag)


run_db = PythonOperator(
task_id='load_to_mysql_db',
python_callable=table_load,
dag=dag)

run_etl >> run_sentiment >> run_db
