// Theme Switcher
document.addEventListener('DOMContentLoaded', function() {
    // Get theme from localStorage or use default
    const savedTheme = localStorage.getItem('theme') || 'theme-dark';
    document.documentElement.className = savedTheme;
    
    // Apply high-contrast enhancements if that's the selected theme
    if (savedTheme === 'theme-high-contrast') {
        enhanceHighContrastSelects();
    }
    
    const themeToggle = document.querySelector('.theme-toggle');
    const themeSelector = document.querySelector('.theme-selector');
    const themeOptions = document.querySelectorAll('.theme-option');
    
    // Toggle theme selector
    themeToggle.addEventListener('click', function() {
        themeSelector.classList.toggle('active');
    });
    
    // Close theme selector when clicking outside
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.theme-switcher')) {
            themeSelector.classList.remove('active');
        }
    });
    
    // Theme option selection
    themeOptions.forEach(option => {
        option.addEventListener('click', function() {
            const theme = this.getAttribute('data-theme');
            document.documentElement.className = theme;
            localStorage.setItem('theme', theme);
            themeSelector.classList.remove('active');
            
            // Apply high-contrast enhancements if high-contrast theme is selected
            if (theme === 'theme-high-contrast') {
                enhanceHighContrastSelects();
            }
        });
    });
    
    // Function to enhance select elements for high-contrast theme
    function enhanceHighContrastSelects() {
        const selectElements = document.querySelectorAll('select');
        selectElements.forEach(select => {
            // Set direct styles to ensure visibility
            select.style.backgroundColor = '#4d4d4d';
            select.style.color = 'white';
            select.style.border = '2px solid #ffff00';
            
            // Add a class that we can target with CSS
            select.classList.add('high-contrast-enhanced');
            
            // Add event listener to set option colors when dropdown opens
            select.addEventListener('mousedown', function() {
                setTimeout(() => {
                    const options = this.querySelectorAll('option');
                    options.forEach(option => {
                        option.style.backgroundColor = '#3d3d3d';
                        option.style.color = 'white';
                    });
                }, 10);
            });
        });
    }
    
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mainNav = document.getElementById('main-nav');
    
    mobileMenuBtn.addEventListener('click', function() {
        this.classList.toggle('open');
        mainNav.classList.toggle('open');
    });
    
    // Testimonial Slider
    const testimonialTrack = document.querySelector('.testimonial-track');
    const testimonialCards = document.querySelectorAll('.testimonial-card');
    const dots = document.querySelectorAll('.dot');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    let currentIndex = 0;
    const cardWidth = 100; // 100%
    
    // Initialize testimonial slider
    function updateSlider() {
        testimonialTrack.style.transform = `translateX(-${currentIndex * cardWidth}%)`;
        
        // Update active dot
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });
    }
    
    // Next button click
    nextBtn.addEventListener('click', function() {
        currentIndex = (currentIndex + 1) % testimonialCards.length;
        updateSlider();
    });
    
    // Previous button click
    prevBtn.addEventListener('click', function() {
        currentIndex = (currentIndex - 1 + testimonialCards.length) % testimonialCards.length;
        updateSlider();
    });
    
    // Dot navigation
    dots.forEach((dot, index) => {
        dot.addEventListener('click', function() {
            currentIndex = index;
            updateSlider();
        });
    });
    
    // Auto slide every 5 seconds
    setInterval(function() {
        currentIndex = (currentIndex + 1) % testimonialCards.length;
        updateSlider();
    }, 5000);
    
    // Modal functionality
    const loginModal = document.getElementById('login-modal');
    const signupModal = document.getElementById('signup-modal');
    const closeModalBtns = document.querySelectorAll('.close-modal');
    const switchToSignup = document.getElementById('switch-to-signup');
    const switchToLogin = document.getElementById('switch-to-login');
    
    // Login and signup buttons are now direct links that navigate to other pages
    // No need for event listeners to open modals
    
    // Close modals
    closeModalBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            loginModal.classList.remove('active');
            signupModal.classList.remove('active');
        });
    });
    
    // Switch between modals
    switchToSignup.addEventListener('click', function(e) {
        e.preventDefault();
        loginModal.classList.remove('active');
        signupModal.classList.add('active');
    });
    
    switchToLogin.addEventListener('click', function(e) {
        e.preventDefault();
        signupModal.classList.remove('active');
        loginModal.classList.add('active');
    });
    
    // Close modal when clicking outside
    window.addEventListener('click', function(event) {
        if (event.target === loginModal) {
            loginModal.classList.remove('active');
        }
        if (event.target === signupModal) {
            signupModal.classList.remove('active');
        }
    });
    
    // Animate stats counter
    const statNumbers = document.querySelectorAll('.stat-number');
    
    // Check if element is in viewport
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
    
    // Animate counter
    function animateCounter(element) {
        const target = parseInt(element.getAttribute('data-count'));
        const duration = 2000; // 2 seconds
        const step = target / (duration / 16); // 60fps
        let current = 0;
        
        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                element.textContent = target.toLocaleString() + '+';
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(current).toLocaleString() + '+';
            }
        }, 16);
    }
    
    // Start animation when scrolled into view
    function checkScroll() {
        statNumbers.forEach(stat => {
            if (isInViewport(stat) && !stat.classList.contains('animated')) {
                animateCounter(stat);
                stat.classList.add('animated');
            }
        });
    }
    
    // Check on scroll and initial load
    window.addEventListener('scroll', checkScroll);
    checkScroll();
    
    // Form submissions
    const newsletterForm = document.querySelector('.newsletter-form');
    
    // Login and signup forms are now handled by Django on separate pages
    
    newsletterForm.addEventListener('submit', function(e) {
        e.preventDefault();
        // Simulate newsletter subscription
        const emailInput = this.querySelector('input[type="email"]');
        alert(`Thank you for subscribing with ${emailInput.value}!`);
        emailInput.value = '';
    });
});