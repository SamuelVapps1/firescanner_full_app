import React from 'react';

function ResultsTable({ results }) {
  return (
    <table className="results-table">
      <thead>
        <tr>
          <th>#</th>
          <th>Symbol</th>
          <th>Score</th>
          <th>Badges</th>
          <th>Freshness</th>
        </tr>
      </thead>
      <tbody>
        {results.map((item, index) => (
          <tr key={index}>
            <td>{index + 1}</td>
            <td>{item.symbol}</td>
            <td>{item.score}</td>
            <td>{item.badges && item.badges.length > 0 ? item.badges.join(', ') : '-'}</td>
            <td>{item.freshness}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default ResultsTable;