## airflow
airflow pipeline test 

# Description:**
    1. This runs chain of commands through airflow dags. 
    2. Airflow hosted on AWS EC2(AmazonImage)

# **Steps to install and configure airflow :**
    Reference: https://blog.sicara.com/automate-aws-tasks-boto3-airflow-hooks-593c3120e8fc

    1. Install pip for python

    2. Install airflow
        `sudo yum install apache-airflow`

    3. Initialize the database
        `airflow initdb`

    4. start the web server, default port is 8080
        `airflow webserver -p 8080`

    5. start the scheduler
        `airflow scheduler`
 
    6. Connect to airflow UI
        - open the port 8080 by adding the tcp port 8080 in security group for the EC2 instance
        - open localbrowser and connect to http://<public-ip>:8080      eg: http://22.2222.22.2:8080




# **Dag Lists:**

**1. test-ariflowdag-in-aws**

**Description:**
    This dag executes only once . Main job is to insert random data into dynamodb

    1. There are three steps:
        - Prints current date
        - Executes python script to create random data and insert it into dynamodb (supported by api gateway and lambda)
        - sleeps for 10 sec

**Future Plans:**
    Integrate it with an application/web application to store app data to dynamodb.
