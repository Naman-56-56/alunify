document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const nav = document.querySelector('nav');
    
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', function() {
            nav.style.display = nav.style.display === 'block' ? 'none' : 'block';
            mobileMenuBtn.classList.toggle('active');
        });
    }

    // Modal Functionality
    const loginBtn = document.querySelector('.login-btn');
    const signupBtn = document.querySelector('.signup-btn');
    const loginModal = document.getElementById('login-modal');
    const signupModal = document.getElementById('signup-modal');
    const closeModalBtns = document.querySelectorAll('.close-modal');
    const showSignupBtn = document.getElementById('show-signup');
    const showLoginBtn = document.getElementById('show-login');

    // Open login modal
    if (loginBtn && loginModal) {
        loginBtn.addEventListener('click', function() {
            loginModal.style.display = 'block';
        });
    }

    // Open signup modal
    if (signupBtn && signupModal) {
        signupBtn.addEventListener('click', function() {
            signupModal.style.display = 'block';
        });
    }

    // Close modals
    if (closeModalBtns) {
        closeModalBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                if (loginModal) loginModal.style.display = 'none';
                if (signupModal) signupModal.style.display = 'none';
                const eventProposalModal = document.getElementById('event-proposal-modal');
                if (eventProposalModal) eventProposalModal.style.display = 'none';
                const editProfileModal = document.getElementById('edit-profile-modal');
                if (editProfileModal) editProfileModal.style.display = 'none';
            });
        });
    }

    // Switch between login and signup modals
    if (showSignupBtn && signupModal && loginModal) {
        showSignupBtn.addEventListener('click', function(e) {
            e.preventDefault();
            loginModal.style.display = 'none';
            signupModal.style.display = 'block';
        });
    }

    if (showLoginBtn && loginModal && signupModal) {
        showLoginBtn.addEventListener('click', function(e) {
            e.preventDefault();
            signupModal.style.display = 'none';
            loginModal.style.display = 'block';
        });
    }

    // Close modals when clicking outside
    window.addEventListener('click', function(e) {
        if (loginModal && e.target === loginModal) {
            loginModal.style.display = 'none';
        }
        if (signupModal && e.target === signupModal) {
            signupModal.style.display = 'none';
        }
        const eventProposalModal = document.getElementById('event-proposal-modal');
        if (eventProposalModal && e.target === eventProposalModal) {
            eventProposalModal.style.display = 'none';
        }
        const editProfileModal = document.getElementById('edit-profile-modal');
        if (editProfileModal && e.target === editProfileModal) {
            editProfileModal.style.display = 'none';
        }
    });

    // Form Submissions
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');
    const newsletterForm = document.querySelector('.newsletter-form');

    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            // Simulate login - in a real app, this would send data to a server
            alert('Login functionality would be implemented here.');
            loginModal.style.display = 'none';
        });
    }

    if (signupForm) {
        signupForm.addEventListener('submit', function(e) {
            e.preventDefault();
            // Simulate signup - in a real app, this would send data to a server
            alert('Signup functionality would be implemented here.');
            signupModal.style.display = 'none';
        });
    }

    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('input[type="email"]');
            if (emailInput && emailInput.value) {
                // Simulate newsletter subscription
                alert(`Thank you for subscribing with ${emailInput.value}!`);
                emailInput.value = '';
            }
        });
    }

    // Testimonial Slider
    const testimonialCards = document.querySelectorAll('.testimonial-card');
    const dots = document.querySelectorAll('.dot');
    const prevBtn = document.getElementById('prev-testimonial');
    const nextBtn = document.getElementById('next-testimonial');
    
    if (testimonialCards.length > 0 && dots.length > 0) {
        let currentTestimonial = 0;

        // Function to show a specific testimonial
        function showTestimonial(index) {
            testimonialCards.forEach(card => card.classList.remove('active'));
            dots.forEach(dot => dot.classList.remove('active'));
            
            testimonialCards[index].classList.add('active');
            dots[index].classList.add('active');
            currentTestimonial = index;
        }

        // Event listeners for dots
        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => showTestimonial(index));
        });

        // Event listeners for prev/next buttons
        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                let newIndex = currentTestimonial - 1;
                if (newIndex < 0) newIndex = testimonialCards.length - 1;
                showTestimonial(newIndex);
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                let newIndex = currentTestimonial + 1;
                if (newIndex >= testimonialCards.length) newIndex = 0;
                showTestimonial(newIndex);
            });
        }

        // Auto-rotate testimonials
        setInterval(() => {
            if (nextBtn) {
                let newIndex = currentTestimonial + 1;
                if (newIndex >= testimonialCards.length) newIndex = 0;
                showTestimonial(newIndex);
            }
        }, 5000);
    }

    // Tab functionality
    const tabBtns = document.querySelectorAll('.tab-btn');
    
    if (tabBtns.length > 0) {
        tabBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                const tabId = this.getAttribute('data-tab');
                
                // Remove active class from all tabs and contents
                document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
                document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
                
                // Add active class to clicked tab and corresponding content
                this.classList.add('active');
                document.getElementById(tabId).classList.add('active');
            });
        });
    }
});