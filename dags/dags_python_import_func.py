import pendulum
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG, chain
from common.common_func import get_sftp
import random

with DAG(
    dag_id="dags_python_import_func",
    schedule=None,
    start_date=pendulum.datetime(2025, 10, 2, tz="UTC"),
    catchup=False,
    tags=["example", "example2", "example3"],
) as dag:
     
    
    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=get_sftp
    )

    py_t1

