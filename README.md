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

## App.js Code Explanation

1. Importing necessary modules and CSS:

```
import './App.css';
import * as React from 'react';
import { useEffect, useState } from 'react';
```

- ./App.css for styling.
- React and its hooks useEffect and useState for managing component state and lifecycle.

2. Defining the App component:

```
function App() {
  const [dashboardUrl, setDashboardUrl] = useState(null);
  const [jsonResponse, setJSONResponse] = useState(null);
```

- Declaring state variables dashboardUrl and jsonResponse to store the QuickSight embed URL and the full JSON response, respectively. 

3. Fetching data on component mount:

```
useEffect(() => {
  const timeout = setTimeout(() => {
    fetch([YOUR_API_ENDPOINT]
    ).then((response) => response.json()
    ).then((response) => {
      setDashboardUrl(response.EmbedUrl)
      setJSONResponse(response)
    })
  }, 10);
  return () => clearTimeout(timeout);
}, []);
```

- Using useEffect to fetch data from the API when the component mounts.
- `setTimeout` with a delay of 10 milliseconds to simulate a slight delay before making the fetch request.
- `fetch` to get data from the provided API endpoint and parsing it to JSON.
- Setting the state variables dashboardUrl and jsonResponse with the fetched data.
- Cleaning up the timeout when the component unmounts.

4. Rendering the component:

```
return (
  <>
    <header>
      <h1>Embedded <i>QuickSight</i>: Sample_Dashboard</h1>
    </header>
    <main>
      <iframe
        width="960"
        height="720"
        src={dashboardUrl}>
      </iframe>
    </main>
  </>
);
```

- Returning the JSX to render the component.
- Displaying a header with the title.
- Embedding the QuickSight dashboard using an iframe with the src set to dashboardUrl.

5. Exporting the App component:

```
export default App;
```

- Exporting the App component as the default export.

## Lambda Code Explanation

1. Importing necessary modules:

```
import json, boto3, os
```
- `json` for handling JSON data.
- `boto3` for AWS SDK to interact with AWS services.
- `os` for accessing environment variables.

2. Lambda handler function:

```
def lambda_handler(event, context):
```

- The entry point for AWS Lambda function execution.

3. Get QuickSight dashboard URL:

```
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
```

- Defines a function to generate an anonymous embed URL for the QuickSight dashboard.

4. Extracting AWS Account Id:

```
awsAccountId = context.invoked_function_arn.split(':')[4]
```
- Extracts AWS Account ID from the Lambda function's ARN.

5. Reading environment variable:

```
dashboardId = os.environ['DashboardId']
```

- Reads the DashboardId environment variable.

6. Initialize and get the response:

```
response = {}
response = getQuickSightDashboardUrl(awsAccountId, dashboardId)
```

- Initializes an empty response dictionary and calls the function to get the embed URL.

7. Returning the successful response:

```
return {
    'statusCode': 200,
    'headers': {
        "Access-Control-Allow-Origin": "[YOUR_DOMAIN]",
        "Content-Type": "text/plain"
    },
    'body': json.dumps(response)
}
```

- Returns the embed URL in the response body with HTTP status 200.

8. Exception handling:

```
except Exception as e:
    return {
        'statusCode': 400,
        'headers': {
            "Access-Control-Allow-Origin": "[YOUR_DOMAIN]",
            "Content-Type": "text/plain"
        },
        'body': json.dumps('Error: ' + str(e))
    }
```

- Catches any exceptions and returns an error response with HTTP status 400.

