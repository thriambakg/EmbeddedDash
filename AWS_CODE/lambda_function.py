import json, boto3, os

def lambda_handler(event, context):
    try:
        def getQuickSightDashboardUrl(awsAccountId, dashboardId):
            # Create QuickSight client
            quickSight = boto3.client('quicksight')
            
            # Generate Anonymous Embed URL
            response = quickSight.get_dashboard_embed_url(
                AwsAccountId=awsAccountId,
                DashboardId=dashboardId,
                IdentityType='ANONYMOUS',
                Namespace='default'
            )
            return response

        # Get AWS Account Id from the context object
        awsAccountId = context.invoked_function_arn.split(':')[4]

        # Read in the environment variable for DashboardId
        dashboardId = os.environ['DashboardId']

        # Initialize response dictionary
        response = {}

        # Get the QuickSight dashboard embed URL
        response = getQuickSightDashboardUrl(awsAccountId, dashboardId)

        # Return successful response with the embed URL
        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "[YOUR_DOMAIN]",  # Replace [YOUR_DOMAIN] with the actual domain
                "Content-Type": "text/plain"
            },
            'body': json.dumps(response)
        }

    except Exception as e:
        # Catch all exceptions and return an error response
        return {
            'statusCode': 400,
            'headers': {
                "Access-Control-Allow-Origin": "[YOUR_DOMAIN]",  # Replace [YOUR_DOMAIN] with the actual domain
                "Content-Type": "text/plain"
            },
            'body': json.dumps('Error: ' + str(e))
        }