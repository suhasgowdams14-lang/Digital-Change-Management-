// Wait for the DOM to be fully loaded before running scripts
document.addEventListener('DOMContentLoaded', () => {
    
    const API_BASE_URL = 'http://127.0.0.1:5000/api';

    // 1. Fetch Key Metrics
    fetch(`${API_BASE_URL}/metrics/latest`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.error(data.error);
                document.getElementById('adoption-rate').textContent = 'Error';
                document.getElementById('readiness-score').textContent = 'Error';
            } else {
                // Format as percentage
                document.getElementById('adoption-rate').textContent = `${(data.adoption_rate * 100).toFixed(0)}%`;
                document.getElementById('readiness-score').textContent = `${(data.readiness_score * 100).toFixed(0)}%`;
            }
        })
        .catch(error => console.error('Error fetching metrics:', error));

    // 2. Fetch and render Sentiment Chart
    fetch(`${API_BASE_URL}/sentiment`)
        .then(response => response.json())
        .then(data => {
            if (data.error) return console.error(data.error);
            
            const ctx = document.getElementById('sentimentChart').getContext('2d');
            new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Positive', 'Neutral', 'Negative'],
                    datasets: [{
                        data: [data.positive, data.neutral, data.negative],
                        backgroundColor: [
                            'rgba(75, 192, 192, 0.7)', // Green
                            'rgba(255, 206, 86, 0.7)', // Yellow
                            'rgba(255, 99, 132, 0.7)'  // Red
                        ],
                        borderColor: '#fff',
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'top',
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching sentiment:', error));

    // 3. Fetch and render Adoption History Chart
    fetch(`${API_BASE_URL}/adoption/history`)
        .then(response => response.json())
        .then(data => {
            if (data.error) return console.error(data.error);

            const ctx = document.getElementById('adoptionChart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.labels, // Dates
                    datasets: [{
                        label: 'Adoption Rate (%)',
                        data: data.data, // Adoption values
                        fill: true,
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        tension: 0.1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        })
        .catch(error => console.error('Error fetching adoption history:', error));
});