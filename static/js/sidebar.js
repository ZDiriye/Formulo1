document.addEventListener("DOMContentLoaded", function() {
    // get references to the necessary elements
    const body = document.querySelector("body");
    const storedState = localStorage.getItem("sidebarState");
    const sidebarToggle = document.getElementById("sidebarToggle");

    // check if the sidebar state was stored and apply it if necessary
    if (storedState === "active") {
        body.classList.add("active");
    }

    // add a click event listener to the sidebar toggle button
    sidebarToggle.addEventListener("click", function() {
        // toggle the 'active' class on the body element
        body.classList.toggle("active");
        
        // update the stored state in localStorage
        if (body.classList.contains("active")) {
            localStorage.setItem("sidebarState", "active");
        } else {
            localStorage.removeItem("sidebarState");
        }
    });
});
