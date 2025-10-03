import pendulum
from airflow.decorators import task
from airflow.sdk import DAG

with DAG(
    dag_id="dags_python_task_decorator",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
) as dag:
    
    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)

    python_task_1 = print_context("task_operator 실행")