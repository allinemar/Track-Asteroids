let asteroidsData = [];


async function loadAsteroids() {
    try {
        const response = await fetch("http://0.0.0.0:8000/asteroids");
        const data = await response.json();

        console.log(data);

        if (!data || data.length === 0) return;

        asteroidsData = data;

        const asteroid = data.reduce((a, b) => a.miss_distance_km < b.miss_distance_km ? a : b);

        document.getElementById("name").innerHTML = `<span class="no-break">Name:</span><br><span lass="no-break">${asteroid.name}</span>`;
        document.getElementById("approach-date").innerHTML = `<span class="no-break">Aproach Date:</span><br><span class="no-break">${new Date(asteroid.approach_date).toLocaleString()}</span>`;
        document.getElementById("nearest-distance").innerHTML = `<span class="no-break">Nearest Distance from Earth:</span><br><span class="no-break">${Number(asteroid.miss_distance_km).toLocaleString()}km</span>`;
        document.getElementById("is-hazardous").innerHTML = `<span class="no-break">Dangerous:</span><br><span class="no-break">${asteroid.is_hazardous ? "Yes" : "No"}</span>`;
        document.getElementById("diameter-min").innerHTML = `<span class="no-break">Minimum Diameter:</span><br><span class="no-break">${Number(asteroid.diameter_min).toLocaleString()} km</span>`;
        document.getElementById("diameter-max").innerHTML = `<span class="no-break">Maximum Diameter:</span><br><span class="no-break">${Number(asteroid.diameter_max).toLocaleString()} km</span>`;
        document.getElementById("magnitude").innerHTML = `<span class="no-break">Magnitude:</span><br><span class="no-break">${Number(asteroid.magnitude).toLocaleString()}</span>`;
    } catch (error) {
        console.log("Failed to fetch data", error);
    }

}

function selectOptions() {
    const select = document.getElementById("asteroid-size");
    select.InnerHTML="";
    asteroidsData.forEach(it => {
        const option = document.createElement("option");
        option.value = it.name;
        option.textContent = it.name;
        select.appendChild(option);
    });

    select.addEventListener("change", choice);
}

function choice(event) {
    
    const target = event.target.value;
    const asteroid = asteroidsData.find(it => it.name === target);
    if (!asteroid) return;
    const container = document.querySelector(".comparison-area");
    const asteroidDiv = document.getElementById("asteroid-graph");
    const christImg = container.querySelector("img");

    let asteroidSize = asteroid.diameter_max * 550 / 0.038;
    const containerWidth = container.clientWidth;
    const maxTotalWidth = containerWidth * 0.9;
    const christWidth = 300;
    const totalNeededWidth = asteroidSize + christWidth + 30;
    if (totalNeededWidth > maxTotalWidth) {
        const scaleFactor = maxTotalWidth / totalNeededWidth;
        asteroidSize *= scaleFactor;
        christImg.style.width = (christWidth * scaleFactor) + "px";
    } else {
        christImg.style.width = "40%";
    }
    asteroidDiv.style.width = asteroidSize + "px";
    asteroidDiv.style.height = asteroidSize + "px";
    
}



async function init() {
    await loadAsteroids();
    document.getElementById("asteroid-graph").style.width = "300px";
    document.getElementById("asteroid-graph").style.height = "300px";
    selectOptions();
}

document.addEventListener("DOMContentLoaded", init);
