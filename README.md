# Public_repo_PM

This repo is deployed through aws lambda and aws ai gateway.

Link: https://bsxhyz300b.execute-api.us-east-2.amazonaws.com/?0  # you can replace last value in the link to define starting point from which table value will be  printed


I met a lot of issues in task 2:

1) No base_id for given AirTable. Means no acces to work with it by http requests. Only raw html.
Decision/solution: copy given table to my AirTable account.
Found a lot of ways to share my own table, but 0 ways to request foreign table

2) Unclear task with AWS Lambda. How the algorythm should be implemented in AWS and what should be the result? Because I see no option how to implement a LOOP (while True) in HTTP response which AWS Lamba give you back when you use URL for API endpoint.
Solution: lambda func takes 3 values from the airtable and gives them back in json format like {'0' : 'val'} where key is ID of a value in the table. To use lambda func added a runner which visit API endpoint via link every 1 second

3) Absence of required modules like requests or pyairtable (last one used in script) in AWS Lambda environment.
Decision: deploy Python Lambda functions with .zip file archives using AWS CLI version 2. pyairtable module uploaded to AWS and layer created in Lambda

4) Circular buffer... How should it be implemented: like simple while True loop? Or like independed object defined as a class? Last one is going to take some time...
Decision: realized as while True cycle
