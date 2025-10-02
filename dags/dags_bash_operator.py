import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="dags_bash_operator",
    schedule=None,
    start_date=pendulum.datetime(2025, 10, 2, tz="UTC"),
    catchup=False,
    tags=["example", "example2", "example3"],
) as dag:
    
    # bash_t1 객체명  task_id : 그래프에 나타나는 ID 두 명칭은 일치를 시켜 주는 것이 좋다.
    bash_t1 = BashOperator(task_id="bash_t1", 
                                      bash_command="echo whoami") # 실행할 명령
    
    bash_t2 = BashOperator(task_id="bash_t2", 
                                      bash_command="echo $HOSTNAME") # 실행할 명령    
    
    bash_t1 >> bash_t2