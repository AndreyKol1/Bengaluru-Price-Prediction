async function loadCities() {
    try {
        const response = await fetch('/static/cities.json'); 
        const cities = await response.json();

        const citySelect = document.getElementById('city-select');

        cities.forEach(city => {
            const option = document.createElement('option');
            option.value = city.trim();  
            option.textContent = city.trim();
            citySelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error loading cities:', error);
    }
}

loadCities();