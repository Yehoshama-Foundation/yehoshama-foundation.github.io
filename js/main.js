document.addEventListener('DOMContentLoaded', () => {
    // Set current year in footer
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // Smooth scrolling for navigation links (exclude dropdown toggle)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        // Skip dropdown toggle links
        if (anchor.parentElement && anchor.parentElement.classList.contains('has-dropdown')) return;

        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetEl = document.querySelector(targetId);
            if (targetEl) {
                targetEl.scrollIntoView({
                    behavior: 'smooth'
                });
                history.pushState(null, null, targetId);
            }

            // Close any open dropdowns when navigating
            document.querySelectorAll('.has-dropdown').forEach(el => {
                el.classList.remove('dropdown-open');
            });
        });
    });

    // Dropdown menu toggle via click
    document.querySelectorAll('.has-dropdown > a').forEach(toggle => {
        toggle.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();

            const parent = this.parentElement;
            const isOpen = parent.classList.contains('dropdown-open');

            // Close all dropdowns
            document.querySelectorAll('.has-dropdown').forEach(el => {
                el.classList.remove('dropdown-open');
            });

            // Toggle this one
            if (!isOpen) {
                parent.classList.add('dropdown-open');
            }
        });
    });

    // Close dropdown when clicking anywhere outside
    document.addEventListener('click', function (e) {
        if (!e.target.closest('.has-dropdown')) {
            document.querySelectorAll('.has-dropdown').forEach(el => {
                el.classList.remove('dropdown-open');
            });
        }
    });

    // Close dropdown when clicking a link inside it
    document.querySelectorAll('.dropdown-menu a').forEach(link => {
        link.addEventListener('click', function () {
            document.querySelectorAll('.has-dropdown').forEach(el => {
                el.classList.remove('dropdown-open');
            });
        });
    });
});

