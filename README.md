# Public_repo_PM

This repo is deployed through aws lambda and aws ai gateway.

Link: https://vlsnbi4m37.execute-api.us-east-2.amazonaws.com/default/py_test_func_pm


I met a lot of issues in task 2:

1) No base_id for given AirTable. Means no acces to work with it by http requests. Only raw html.
Decision/solution: copy given table to my AirTable account.

2) Unclear task with AWS Lambda. How the algorythm should be implemented in AWS and what should be the result? Because I see no option how to implement a LOOP (while True) in HTTP response which AWS Lamba give you back when you use URL for API endpoint.
Solution: NO SOLUTION. The scrippt works through python interpreter, but how to implement it into AWS Lambda - oppen question.

3) Absence of required modules like requests or pyairtable (last one used in script) in AWS Lambda environment.
Decision: deploy Python Lambda functions with .zip file archives using AWS CLI version 2. pyairtable module uploaded to AWS and layer created in Lambda

4) Circular buffer... How should it be implemented: like simple while True loop? Or like independed object defined as a class? Last one is going to take some time...

Also I have some idea for how to solve the issue with loop every 1 second that is showing result on a web page. But I see no place for AWS Lambda there. Rather some web framework or AWS Lambda Aplication at least (I suppose last one should be able for something like this).
