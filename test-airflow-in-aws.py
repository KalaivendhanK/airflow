"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

dag_name="test-ariflowdag-in-aws"

default_args={
    "owner": "Kalai",
    "depends_on_past": False,
    "start_date": datetime(2019,7,1),
    "email": ["kalaisundaram93@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2)
}

# dag=DAG(dag_name,default_args=default_args,schedule_interval=timedelta(days=1))
dag=DAG(dag_name,default_args=default_args,schedule_interval='@once')

t1=BashOperator(
    task_id="task1_print_date",
    bash_command='date',
    dag=dag
    )

t2=BashOperator(
task_id="task2_sleep",
bash_command="sleep 10s",
dag=dag
    )

t2.set_upstream(t1)