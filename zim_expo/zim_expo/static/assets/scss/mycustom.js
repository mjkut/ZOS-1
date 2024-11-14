
/* Destinations Js*/

document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".province-filter button");
    const destinations = document.querySelectorAll(".destination-item");

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const province = button.getAttribute("data-province");

            destinations.forEach(destination => {
                if (province === "all" || destination.getAttribute("data-province") === province) {
                    destination.style.display = "block";
                } else {
                    destination.style.display = "none";
                }
            });
        });
    });
});

