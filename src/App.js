import './App.css';
import * as React from 'react';
import { useEffect, useState } from 'react';


 function App() {
  const [dashboardUrl, setDashboardUrl] = useState(null);
  const [jsonResponse, setJSONResponse] = useState(null);

  useEffect(() => {
    const timeout = setTimeout(() => {
      fetch("https://qr65fmyfni.execute-api.us-east-1.amazonaws.com/default/Test_function"
      ).then((response) => response.json()
      ).then((response) => {
        setDashboardUrl(response.EmbedUrl)
        setJSONResponse(response)
      })
    }, 10);
    return () => clearTimeout(timeout);
  }, []);

  return (
    <>
      <header>
        <h1>Embedded QuickSight: Sample_Dashboard</h1>
      </header>
      <main>
        <iframe
            width="960"
            height="720"
            src="https://us-east-1.quicksight.aws.amazon.com/sn/accounts/851725462481/dashboards/63a1942f-c9d9-4ee5-b102-53351028e463?directory_alias=thriambaksqsaccount">
        </iframe>
      </main>
    </>
  );
};

export default App;
