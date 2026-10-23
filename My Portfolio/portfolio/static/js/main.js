
document.addEventListener("DOMContentLoaded", () => {
    // Add a smooth reveal effect to elements
    const elements = document.querySelectorAll(
        ".project-card, .skill-card, .experience-card, .education-card"
    );

    elements.forEach((element, index) => {
        element.style.opacity = "0";
        element.style.transform = "translateY(20px)";
        element.style.transition = "opacity 0.5s ease, transform 0.5s ease";

        setTimeout(() => {
            element.style.opacity = "1";
            element.style.transform = "translateY(0)";
        }, 100 * index);
    });

    // Update the footer year automatically
    const year = document.querySelector("#current-year");
    if (year) {
        year.textContent = new Date().getFullYear();
    }
});
