# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)


QuickSight Dashboard Embed Application
This project is a simple React application that fetches and embeds an Amazon QuickSight dashboard into a web page.

Table of Contents
Installation
Usage
Code Explanation
Backend (AWS Lambda)
Frontend (React App)
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/your-repository.git
cd your-repository
Install dependencies:

sh
Copy code
npm install
Set up environment variables:
Ensure you have set the DashboardId environment variable in your AWS Lambda function configuration.

Usage
Run the React app:

sh
Copy code
npm start
Deploy the Lambda function:
Deploy the lambda_handler function to AWS Lambda.

Access the application:
Open your browser and navigate to http://localhost:3000 to view the embedded QuickSight dashboard.

Code Explanation
Backend (AWS Lambda)
This code is an AWS Lambda function that generates an anonymous embed URL for an Amazon QuickSight dashboard and returns it in the response.

python
Copy code
import json, boto3, os, re, base64

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
Key Points:
Imports necessary modules for handling JSON, interacting with AWS services, and accessing environment variables.
Defines getQuickSightDashboardUrl function to create a QuickSight client and generate an anonymous embed URL for the specified dashboard.
Extracts AWS Account ID from the Lambda function's context object.
Reads DashboardId from environment variables.
Fetches the embed URL and returns it in the response.
Handles exceptions and returns an error response if any occur.
Frontend (React App)
This React component fetches the embed URL from the backend and displays the QuickSight dashboard in an iframe.

javascript
Copy code
import './App.css'; // Importing the CSS file for styling
import * as React from 'react'; // Importing React
import { useEffect, useState } from 'react'; // Importing React hooks

function App() {
  const [dashboardUrl, setDashboardUrl] = useState(null); // State to store the dashboard URL
  const [jsonResponse, setJSONResponse] = useState(null); // State to store the full JSON response

  useEffect(() => {
    // useEffect hook to fetch data when the component mounts
    const timeout = setTimeout(() => {
      fetch([YOUR_API_ENDPOINT] // Replace [YOUR_API_ENDPOINT] with the actual API endpoint URL
      ).then((response) => response.json() // Parsing the response to JSON
      ).then((response) => {
        setDashboardUrl(response.EmbedUrl) // Setting the dashboard URL state with the embed URL from the response
        setJSONResponse(response) // Setting the JSON response state with the full response
      })
    }, 10); // Fetching the data after a timeout of 10 milliseconds
    return () => clearTimeout(timeout); // Cleanup the timeout on component unmount
  }, []);

  return (
    <>
      <header>
        <h1>Embedded <i>QuickSight</i>: Sample_Dashboard</h1>
      </header>
      <main>
        <iframe
          width="960"
          height="720"
          src={dashboardUrl}> {/* Embedding the QuickSight dashboard using the iframe */}
        </iframe>
      </main>
    </>
  );
};

export default App; // Exporting the App component
Key Points:
Imports necessary modules and CSS for styling and React functionalities.
Defines App component that uses React hooks (useState and useEffect) to manage state and side effects.
Fetches the embed URL from the backend API endpoint when the component mounts.
Stores the embed URL in the dashboardUrl state variable.
Embeds the QuickSight dashboard using an iframe with the fetched URL.
Handles component unmounting by clearing the timeout to avoid memory leaks.
