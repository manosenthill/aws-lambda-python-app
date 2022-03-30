# Task Planner API
## Requirement
As a User, I should be able to create tasks(TODO) which is planned to complete.
Request should have name of the tasks, priority and due date.

## Architecture

![image](/img/aws-lambda-arch.png)

## Implementation

1. Dynamo DB
    
2. Lambda function

    2.1 Code
    
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
