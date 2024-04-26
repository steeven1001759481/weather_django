function fetchTemperature() {
	// Simulate fetching temperature data (replace this with actual API call)
	setTimeout(() => {
		temperature = document.getElementById('temperature').textContent;
		// Update background color based on temperature
		const box = document.getElementById('weatherBox');
		if (temperature < 15) {
		box.style.backgroundColor = '#6495ED'; // Light blue for low temperature
		} else if (temperature >= 15 && temperature < 25) {
		box.style.backgroundColor = '#FFD700'; // Gold for moderate temperature
		} else {
		box.style.backgroundColor = '#FF6347'; // Tomato red for high temperature
		}
	}, 500); // Simulated delay for demonstration
	}
		// Initial call to fetch temperature data
fetchTemperature();
