document.addEventListener("DOMContentLoaded", function () {
    const currentPagePath = window.location.pathname;
      
    const racesNavItems = document.querySelectorAll(".nav-races");
    const driversNavItems = document.querySelectorAll(".nav-drivers");
    const teamsNavItems = document.querySelectorAll(".nav-teams");

    // check if the current page matches each navigation item and add the "active" class
    if (currentPagePath.startsWith("/races")) {
      racesNavItems.forEach((item) => {
        item.classList.add("active");
      });
    } else if (currentPagePath.startsWith("/drivers")) {
      driversNavItems.forEach((item) => {
        item.classList.add("active");
      });
    } else if (currentPagePath.startsWith("/teams")) {
      teamsNavItems.forEach((item) => {
        item.classList.add("active");
      });
    }
});