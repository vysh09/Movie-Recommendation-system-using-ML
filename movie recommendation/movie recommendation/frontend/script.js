async function getRecommendations() {
  const genre = document.getElementById("genre").value;

  if (!genre) {
    alert("Please select a genre.");
    return;
  }

  const response = await fetch("http://127.0.0.1:5000/recommend", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ genre })
  });

  const data = await response.json();
  const resultsDiv = document.getElementById("results");

  if (data.movies) {
    resultsDiv.innerHTML = "<h3>Recommended Movies:</h3>" + data.movies.map(movie => `<p>${movie}</p>`).join("");
  } else {
    resultsDiv.innerHTML = "<p>No results found.</p>";
  }
}
