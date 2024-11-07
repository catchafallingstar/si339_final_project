// Handling Broken Images
const images = document.querySelectorAll('img');
images.forEach(function (img) {
    img.addEventListener('error', function () {
        img.src = '../images/default_image.jpg';  // Provide a path to a default image
        img.alt = 'Default Image';
    });
});

let lastScrollPosition = 0;
const navbar = document.querySelector('nav');

window.addEventListener('scroll', () => {
    const currentScrollPosition = window.scrollY;

    if (currentScrollPosition > lastScrollPosition) {
        // User is scrolling down - hide the navbar
        navbar.classList.add('navbar-hidden');
    } else {
        // User is scrolling up - show the navbar
        navbar.classList.remove('navbar-hidden');
    }

    lastScrollPosition = currentScrollPosition;
});
// for the main page click
document.addEventListener("DOMContentLoaded", function() {
    var coll = document.getElementsByClassName("collapsible");
    for (var i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
            var container = this.parentElement;
            container.classList.toggle("expanded"); // Toggle the 'expanded' class

            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.display === "block") {
                content.style.display = "none";
            } else {
                content.style.display = "block";
            }
        });
    }
});
// icon on main page
function toggleNav() {
    var navBar = document.getElementById("nav-bar");
    navBar.classList.toggle("active");
}

// Close the navigation bar when a link inside it is clicked, or outside is clicked
document.addEventListener("DOMContentLoaded", function() {
    var navBar = document.getElementById("nav-bar");
    var navLinks = navBar.getElementsByTagName("a");

    for (var i = 0; i < navLinks.length; i++) {
        navLinks[i].addEventListener("click", function() {
            navBar.classList.remove("active");
        });
    }
    document.addEventListener("click", function(event) {
        if (!navBar.contains(event.target) && !event.target.closest('.menu-icon')) {
            navBar.classList.remove("active");
        }
    });
});
