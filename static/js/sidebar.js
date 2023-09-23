document.addEventListener("DOMContentLoaded", function () {
  const body = document.querySelector("body");
  const sidebarToggle = document.getElementById("sidebarToggle");

  sidebarToggle.addEventListener("click", function (event) {
    event.preventDefault(); // Prevent the default behavior of the link/button
    body.classList.toggle("active");
  });
  
  // remove the 'active' class on page load
  body.classList.remove("active");
});
