import json, boto3, os, re, base64

def lambda_handler(event, context):

    try:
        def getQuickSightDashboardUrl(awsAccountId, dashboardId):
            #Create QuickSight client
            quickSight = boto3.client('quicksight');
            #Generate Anonymous Embed url
            response = quickSight.get_dashboard_embed_url(
                 AwsAccountId=awsAccountId,
                 DashboardId=dashboardId,
                 IdentityType='ANONYMOUS',
                 Namespace = 'default'
                 )
            return response
        

        #Get AWS Account Id
        awsAccountId = context.invoked_function_arn.split(':')[4]
    
        #Read in the environment variable
        dashboardId = os.environ['DashboardId']
    
        response={} 
    
        response = getQuickSightDashboardUrl(awsAccountId, dashboardId)
       
        return {'statusCode':200,
                'headers': {"Access-Control-Allow-Origin": "http://localhost:3000",
                            "Content-Type":"text/plain"},
                'body':json.dumps(response)
                } 


    except Exception as e: #catch all
        return {'statusCode':400,
                'headers': {"Access-Control-Allow-Origin": "http://localhost:3000",
                            "Content-Type":"text/plain"},
                'body':json.dumps('Error: ' + str(e))
                }         