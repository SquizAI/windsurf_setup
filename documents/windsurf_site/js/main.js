document.addEventListener('DOMContentLoaded', function() {
    // Load all components
    loadComponent('header', 'components/header.html');
    loadComponent('navigation', 'components/navigation.html');
    loadComponent('introduction', 'components/introduction.html');
    loadComponent('system-requirements', 'components/system-requirements.html');
    loadComponent('installation-process', 'components/installation-process.html');
    loadComponent('initial-setup', 'components/initial-setup.html');
    loadComponent('getting-started-cascade', 'components/getting-started-cascade.html');
    loadComponent('understanding-mcp', 'components/understanding-mcp.html');
    loadComponent('multiple-projects', 'components/multiple-projects.html');
    loadComponent('troubleshooting', 'components/troubleshooting.html');
    loadComponent('lesson-plan', 'components/lesson-plan.html');
    loadComponent('additional-resources', 'components/additional-resources.html');
    loadComponent('footer', 'components/footer.html');
    
    // Setup navigation highlighting
    setupNavigation();
    
    // Initialize back to top button
    initBackToTop();
    
    // Initialize dark mode toggle
    initDarkModeToggle();
});

// Function to load component content
function loadComponent(id, url) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById(id).innerHTML = html;
            // If this is the navigation component, set up after loading
            if (id === 'navigation') {
                setupNavigation();
            }
        })
        .catch(error => {
            console.error(`Error loading component ${id}:`, error);
            document.getElementById(id).innerHTML = `<div class="error">Failed to load ${id} component</div>`;
        });
}

// Function to setup navigation highlighting
function setupNavigation() {
    const nav = document.querySelector('.navigation');
    if (!nav) return;
    
    const navLinks = nav.querySelectorAll('a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Remove active class from all links
            navLinks.forEach(link => link.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // If it's a hash link, smooth scroll to the section
            if (this.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                const targetId = this.getAttribute('href').substring(1);
                const targetSection = document.getElementById(targetId);
                
                if (targetSection) {
                    window.scrollTo({
                        top: targetSection.offsetTop - 70, // Adjust for navbar height
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
    
    // Set active link based on current scroll position
    window.addEventListener('scroll', function() {
        let currentSection = '';
        const sections = document.querySelectorAll('section.section');
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (window.pageYOffset >= sectionTop - 100) {
                currentSection = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            const href = link.getAttribute('href');
            if (href === `#${currentSection}`) {
                link.classList.add('active');
            }
        });
    });
}

// Function to initialize back to top button
function initBackToTop() {
    const backToTopButton = document.createElement('a');
    backToTopButton.href = '#';
    backToTopButton.className = 'back-to-top';
    backToTopButton.innerHTML = '↑';
    document.body.appendChild(backToTopButton);
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopButton.classList.add('visible');
        } else {
            backToTopButton.classList.remove('visible');
        }
    });
    
    backToTopButton.addEventListener('click', function(e) {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Function to initialize dark mode toggle
function initDarkModeToggle() {
    // Create dark mode toggle button
    const darkModeToggle = document.createElement('button');
    darkModeToggle.innerHTML = '🌙';
    darkModeToggle.className = 'dark-mode-toggle btn';
    darkModeToggle.style.position = 'fixed';
    darkModeToggle.style.top = '1rem';
    darkModeToggle.style.right = '1rem';
    darkModeToggle.style.zIndex = '1000';
    document.body.appendChild(darkModeToggle);
    
    // Check for saved preference
    if (localStorage.getItem('darkMode') === 'enabled') {
        document.body.classList.add('dark-mode');
        darkModeToggle.innerHTML = '☀️';
    }
    
    // Toggle dark mode
    darkModeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        
        if (document.body.classList.contains('dark-mode')) {
            localStorage.setItem('darkMode', 'enabled');
            darkModeToggle.innerHTML = '☀️';
        } else {
            localStorage.setItem('darkMode', 'disabled');
            darkModeToggle.innerHTML = '🌙';
        }
    });
}
