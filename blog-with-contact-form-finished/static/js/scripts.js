/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
* JavaScript snippet for handling the scroll behavior and navigation bar visibility.
*/

// Wait for the DOM content to be loaded before executing JavaScript
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0; // Initialize the scroll position
    const mainNav = document.getElementById('mainNav'); // Get the main navigation element
    const headerHeight = mainNav.clientHeight; // Get the height of the navigation bar

    // Listen for scroll events
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1; // Calculate the current scroll position

        // Check if scrolling up
        if (currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible'); // Make the navigation visible if scrolled up
            } else {
                mainNav.classList.remove('is-visible', 'is-fixed'); // Otherwise, remove visibility and fixed positioning classes
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove('is-visible'); // Remove visibility class if scrolling down
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed'); // Add fixed positioning class if scrolled down past header
            }
        }
        scrollPos = currentTop; // Update the scroll position
    });
});

