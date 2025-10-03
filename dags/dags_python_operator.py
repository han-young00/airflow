import pendulum
from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG, chain
import random

with DAG(
    dag_id="dags_python_operator",
    schedule=None,
    start_date=pendulum.datetime(2025, 10, 2, tz="UTC"),
    catchup=False,
    tags=["example", "example2", "example3"],
) as dag:
    def select_fruit():
        fruit = ['APPLE','BANANA', 'ORANGE']
        rand_int = random.randint(0,2)
        print(fruit[rand_int])
    
    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit
    )

    py_t1

