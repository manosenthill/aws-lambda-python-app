# Task Planner API
## Requirement
As a User, I should be able to create tasks(TODO) which is planned to complete.
Request should have name of the tasks, priority and due date.

Create Rest API which stores data into Dynamo db. 
## Architecture

![image](/img/aws-lambda-arch.png)

## Implementation

1. Dynamo DB
    
    create table called "tasks", provide partition key(primary key) as "id"
2. Lambda function

    2.1 Code
    
    - reads the environment variable to get table name "tasks".
    - uses boto3 python library which connects to dynamo db.
    - stores the input data to dynamo db.
    
    2.2 Test
    
    Below are sample input request to test. 
    ~~~
    {
      "id": "1",
      "name": "1st event",
      "status": "open"
    }
    ~~~

3. API Gateway
