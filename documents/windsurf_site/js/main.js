document.addEventListener('DOMContentLoaded', function() {
    // Load all components with loading indicators
    const components = [
        { id: 'header', url: 'components/header.html' },
        { id: 'navigation', url: 'components/navigation.html' },
        { id: 'introduction', url: 'components/introduction.html' },
        { id: 'system-requirements', url: 'components/system-requirements.html' },
        { id: 'installation-process', url: 'components/installation-process.html' },
        { id: 'initial-setup', url: 'components/initial-setup.html' },
        { id: 'getting-started-cascade', url: 'components/getting-started-cascade.html' },
        { id: 'understanding-mcp', url: 'components/understanding-mcp.html' },
        { id: 'multiple-projects', url: 'components/multiple-projects.html' },
        { id: 'github-guide', url: 'components/github-guide.html' },
        { id: 'netlify-guide', url: 'components/netlify-guide.html' },
        { id: 'workflow-guide', url: 'components/workflow-guide.html' },
        { id: 'windsurf-lesson', url: 'components/windsurf-lesson.html' },
        { id: 'troubleshooting', url: 'components/troubleshooting.html' },
        { id: 'lesson-plan', url: 'components/lesson-plan.html' },
        { id: 'additional-resources', url: 'components/additional-resources.html' },
        { id: 'footer', url: 'components/footer.html' }
    ];
    
    // Add loading indicators
    components.forEach(component => {
        const el = document.getElementById(component.id);
        if (el) {
            el.innerHTML = `<div class="loading-indicator">
                <div class="spinner"></div>
                <p>Loading ${component.id.replace(/-/g, ' ')}...</p>
            </div>`;
        }
    });
    
    // Load components with a slight delay between each for better performance
    let delay = 0;
    const delayIncrement = 100; // milliseconds between component loads
    
    components.forEach(component => {
        setTimeout(() => {
            loadComponent(component.id, component.url);
        }, delay);
        delay += delayIncrement;
    });
    
    // Initialize interactive elements after all components are loaded
    setTimeout(() => {
        setupTabInteractions();
        setupAccordions();
        setupInteractiveCards();
        enhanceCodeBlocks();
    }, delay + 500); // Additional delay to ensure components are loaded
});

// Function to load component content
function loadComponent(id, url) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(html => {
            const element = document.getElementById(id);
            if (element) {
                element.innerHTML = html;
                
                // Run specific initialization based on component type
                if (id === 'navigation') {
                    setupNavigation();
                } else if (id === 'installation-process') {
                    setupTabs();
                } else if (id === 'troubleshooting') {
                    setupAccordions();
                }
                
                // Check if this component has lazy-load images
                element.querySelectorAll('img[data-src]').forEach(img => {
                    // Set up intersection observer for lazy loading
                    const observer = new IntersectionObserver(entries => {
                        entries.forEach(entry => {
                            if (entry.isIntersecting) {
                                img.src = img.dataset.src;
                                observer.unobserve(img);
                            }
                        });
                    });
                    observer.observe(img);
                });
                
                // Add animation class after content is loaded
                element.classList.add('content-loaded');
            }
        })
        .catch(error => {
            console.error(`Error loading component ${id}:`, error);
            const element = document.getElementById(id);
            if (element) {
                element.innerHTML = `<div class="error-message">
                    <i class="fas fa-exclamation-triangle"></i>
                    <h3>Failed to load ${id.replace(/-/g, ' ')} component</h3>
                    <p>Please refresh the page and try again.</p>
                </div>`;
            }
        });
}

// Function to setup navigation highlighting
function setupNavigation() {
    const nav = document.querySelector('.navigation');
    if (!nav) return;
    
    const navLinks = nav.querySelectorAll('a');
    
    // Handle click events on navigation links
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
                    // Get the height of the navigation bar to offset the scroll position
                    const navHeight = nav.offsetHeight;
                    
                    window.scrollTo({
                        top: targetSection.offsetTop - navHeight - 20, // Additional 20px padding
                        behavior: 'smooth'
                    });
                    
                    // Update URL hash without scrolling
                    history.pushState(null, null, `#${targetId}`);
                }
            }
        });
    });
    
    // Set active link based on current scroll position
    function updateActiveNavLink() {
        let currentSection = '';
        const sections = document.querySelectorAll('section.section');
        const navHeight = nav.offsetHeight;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - navHeight - 100;
            const sectionBottom = sectionTop + section.offsetHeight;
            
            if (window.scrollY >= sectionTop && window.scrollY < sectionBottom) {
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
    }
    
    // Debounce function to limit how often the scroll event fires
    function debounce(func, wait) {
        let timeout;
        return function() {
            const context = this;
            const args = arguments;
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(context, args), wait);
        };
    }
    
    // Set up scroll event listener with debounce
    window.addEventListener('scroll', debounce(updateActiveNavLink, 50));
    
    // Run once on load to set initial active state
    updateActiveNavLink();
}

// Function to set up tabs
function setupTabs() {
    const tabContainers = document.querySelectorAll('.tab-buttons');
    
    tabContainers.forEach(container => {
        const buttons = container.querySelectorAll('.tab-button');
        const tabContent = container.nextElementSibling;
        
        if (!tabContent) return;
        
        const panes = tabContent.querySelectorAll('.tab-pane');
        
        buttons.forEach(button => {
            button.addEventListener('click', () => {
                // Remove active class from all buttons and panes
                buttons.forEach(btn => btn.classList.remove('active'));
                panes.forEach(pane => pane.classList.remove('active'));
                
                // Add active class to clicked button
                button.classList.add('active');
                
                // Show corresponding tab pane
                const tabId = button.getAttribute('data-tab');
                const pane = document.getElementById(tabId);
                if (pane) pane.classList.add('active');
            });
        });
    });
}

// Function to set up accordions
function setupAccordions() {
    const accordions = document.querySelectorAll('.issue-header');
    
    accordions.forEach(header => {
        header.addEventListener('click', () => {
            const content = header.nextElementSibling;
            const icon = header.querySelector('.toggle-icon');
            
            // Toggle the content display
            header.parentElement.classList.toggle('active');
            
            if (header.parentElement.classList.contains('active')) {
                if (icon) icon.textContent = '-';
            } else {
                if (icon) icon.textContent = '+';
            }
        });
    });
}

// Function to enhance interactive features of cards
function setupInteractiveCards() {
    // Add hover effect to cards
    const cards = document.querySelectorAll('.card, .feature-card, .resource-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.classList.add('card-hover');
        });
        
        card.addEventListener('mouseleave', () => {
            card.classList.remove('card-hover');
        });
    });
}

// Function to enhance code blocks
function enhanceCodeBlocks() {
    const codeBlocks = document.querySelectorAll('.code-block');
    
    codeBlocks.forEach(block => {
        // Add copy button
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-code-button';
        copyButton.innerHTML = '<i class="fas fa-copy"></i>';
        copyButton.title = 'Copy code';
        block.appendChild(copyButton);
        
        copyButton.addEventListener('click', () => {
            const code = block.textContent;
            navigator.clipboard.writeText(code)
                .then(() => {
                    copyButton.innerHTML = '<i class="fas fa-check"></i>';
                    setTimeout(() => {
                        copyButton.innerHTML = '<i class="fas fa-copy"></i>';
                    }, 2000);
                })
                .catch(err => {
                    console.error('Could not copy text: ', err);
                    copyButton.innerHTML = '<i class="fas fa-times"></i>';
                    setTimeout(() => {
                        copyButton.innerHTML = '<i class="fas fa-copy"></i>';
                    }, 2000);
                });
        });
    });
}

// Setup tab interactions if not part of installation-process
function setupTabInteractions() {
    document.querySelectorAll('.tab-buttons:not([data-initialized])').
        forEach(tabContainer => {
            setupTabs(tabContainer);
            tabContainer.setAttribute('data-initialized', 'true');
        });
}
