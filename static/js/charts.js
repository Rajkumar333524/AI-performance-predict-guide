document.addEventListener("DOMContentLoaded", () => {

    console.log("Charts Loaded");

    const chartCanvas =
        document.getElementById("performanceChart");

    if (!chartCanvas) {
        console.log("Chart Canvas Not Found");
        return;
    }

    const scores =
        JSON.parse(
            chartCanvas.dataset.scores || "[]"
        );

    const labels =
        JSON.parse(
            chartCanvas.dataset.labels || "[]"
        );

    new Chart(chartCanvas, {

        type: "bar",

        data: {

            labels: labels,

            datasets: [{

                label: "Performance Score",

                data: scores,

                backgroundColor: [
                    "#3498db",
                    "#2ecc71",
                    "#f39c12",
                    "#e74c3c",
                    "#9b59b6",
                    "#1abc9c"
                ],

                borderWidth: 1
            }]
        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            scales: {

                y: {

                    beginAtZero: true,

                    max: 100
                }
            },

            plugins: {

                legend: {

                    display: true
                },

                title: {

                    display: true,

                    text: "Student Performance Analysis"
                }
            }
        }
    });

});