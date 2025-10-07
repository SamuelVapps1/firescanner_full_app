import React from 'react';

function ScanForm({ venue, timeframe, onVenueChange, onTimeframeChange, onSubmit }) {
  return (
    <div className="form-group">
      <label htmlFor="venue-select">Venue:</label>
      <select
        id="venue-select"
        value={venue}
        onChange={(e) => onVenueChange(e.target.value)}
      >
        <option value="sample_venue">Sample Venue</option>
        <option value="secondary_venue">Secondary Venue</option>
      </select>

      <label htmlFor="timeframe-select" style={{ marginTop: '1rem' }}>Timeframe:</label>
      <select
        id="timeframe-select"
        value={timeframe}
        onChange={(e) => onTimeframeChange(e.target.value)}
      >
        <option value="1h">1 Hour</option>
        <option value="4h">4 Hours</option>
        <option value="1d">1 Day</option>
      </select>

      <button
        type="button"
        onClick={onSubmit}
        style={{ marginTop: '1rem' }}
      >
        Scan
      </button>
    </div>
  );
}

export default ScanForm;