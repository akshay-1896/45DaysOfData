// Custom JS

// Example: Smooth scrolling for internal links
$('a.nav-link').on('click', function(event) {
    if (this.hash !== "") {
        event.preventDefault();
        var hash = this.hash;
        $('html, body').animate({
            scrollTop: $(hash).offset().top
        }, 800, function(){
            window.location.hash = hash;
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var projectsButton = document.getElementById('projectsButton');

    projectsButton.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default anchor link behavior

        var targetElement = document.getElementById('projects');
        var targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;
        var offset = 75; // Adjust this value based on your needs

        window.scrollTo({
            top: targetPosition - offset,
            behavior: 'smooth'
        });
    });
});