document.addEventListener("DOMContentLoaded", function() {
    const elements = document.querySelectorAll(".animated");

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("in-view");
                observer.unobserve(entry.target); // Stop observing once animation is triggered
            }
        });
    });

    elements.forEach(element => {
        observer.observe(element);
    });
});


