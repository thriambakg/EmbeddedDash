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
        setJSONResponse(response) /* Setting the JSON response state with the full response, for development purposes, 
                                     you can display this on the page itself for quick error comprehension. */
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
