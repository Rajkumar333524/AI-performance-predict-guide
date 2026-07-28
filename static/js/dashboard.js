document.addEventListener("DOMContentLoaded", () => {

    console.log("Dashboard Loaded");

    const totalPredictions =
        document.getElementById("totalPredictions");

    const avgScore =
        document.getElementById("avgScore");

    const performanceLevel =
        document.getElementById("performanceLevel");

    const progressBar =
        document.getElementById("progressBar");

    if (avgScore) {

        let score =
            parseFloat(avgScore.innerText);

        if (!isNaN(score)) {

            progressBar.style.width =
                score + "%";

            progressBar.innerText =
                score.toFixed(1) + "%";

            if (score >= 80) {

                progressBar.style.background =
                    "green";

            } else if (score >= 50) {

                progressBar.style.background =
                    "orange";

            } else {

                progressBar.style.background =
                    "red";
            }
        }
    }

    const cards =
        document.querySelectorAll(".dashboard-card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";
        card.style.transform =
            "translateY(20px)";

        setTimeout(() => {

            card.style.transition =
                "0.5s";

            card.style.opacity = "1";

            card.style.transform =
                "translateY(0px)";

        }, index * 200);
    });

    const chartCanvas =
        document.getElementById("performanceChart");

    if (chartCanvas) {

        const scores =
            JSON.parse(
                chartCanvas.dataset.scores
            );

        const labels =
            JSON.parse(
                chartCanvas.dataset.labels
            );

        new Chart(chartCanvas, {

            type: "line",

            data: {

                labels: labels,

                datasets: [{

                    label: "Performance",

                    data: scores,

                    borderWidth: 3,

                    fill: false
                }]
            },

            options: {

                responsive: true,

                plugins: {

                    legend: {

                        display: true
                    }
                }
            }
        });
    }
});