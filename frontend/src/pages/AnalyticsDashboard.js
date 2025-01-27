import React, { useState, useEffect } from 'react';
import { analyticsService } from '../services/api';

function AnalyticsDashboard() {
  const [analytics, setAnalytics] = useState({
    totalQueries: 0,
    topQueries: [],
    responseTime: 0
  });

  useEffect(() => {
    const fetchAnalytics = async () => {
      try {
        const data = await analyticsService.getAnalytics();
        setAnalytics(data);
      } catch (error) {
        console.error('Failed to fetch analytics', error);
      }
    };

    fetchAnalytics();
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl mb-4">Analytics Dashboard</h1>
      <div className="grid grid-cols-3 gap-4">
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-lg">Total Queries</h2>
          <p className="text-3xl">{analytics.totalQueries}</p>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-lg">Top Queries</h2>
          <ul>
            {analytics.topQueries.map((query, index) => (
              <li key={index}>{query}</li>
            ))}
          </ul>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-lg">Avg. Response Time</h2>
          <p className="text-3xl">{analytics.responseTime}ms</p>
        </div>
      </div>
    </div>
  );
}

export default AnalyticsDashboard;