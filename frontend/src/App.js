import React, { useState } from 'react';
import ScanForm from './components/ScanForm';
import ResultsTable from './components/ResultsTable';

function App() {
  const [venue, setVenue] = useState('sample_venue');
  const [timeframe, setTimeframe] = useState('1h');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleScan = async () => {
    setLoading(true);
    setError(null);
    try {
      const query = new URLSearchParams({ venue, timeframe });
      const response = await fetch(`/scan?${query.toString()}`);
      if (!response.ok) {
        const detail = await response.text();
        throw new Error(detail);
      }
      const data = await response.json();
      setResults(data.results);
    } catch (err) {
      setError(err.message || 'Error fetching data');
      setResults([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <h1>FireScanner</h1>
      <ScanForm
        venue={venue}
        timeframe={timeframe}
        onVenueChange={setVenue}
        onTimeframeChange={setTimeframe}
        onSubmit={handleScan}
      />
      {loading && <p>Loading…</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {!loading && !error && results.length > 0 && (
        <ResultsTable results={results} />
      )}
    </div>
  );
}

export default App;