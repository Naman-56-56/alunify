document.addEventListener('DOMContentLoaded', function() {
  // Add theme switcher to the body
  addThemeSwitcher();
  
  // Initialize theme from localStorage or default
  initializeTheme();
  
  // Mobile Navigation
  const hamburger = document.querySelector('.hamburger');
  const navLinks = document.querySelector('.nav-links');
  
  hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      navLinks.classList.toggle('active');
  });
  
  // Close mobile menu when clicking on a link
  document.querySelectorAll('.nav-links li a').forEach(link => {
      link.addEventListener('click', () => {
          hamburger.classList.remove('active');
          navLinks.classList.remove('active');
      });
  });
  
  // Header scroll effect
  const header = document.querySelector('header');
  window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
          header.classList.add('scrolled');
      } else {
          header.classList.remove('scrolled');
      }
  });
  
  // Back to top button
  const backToTop = document.querySelector('.back-to-top');
  window.addEventListener('scroll', () => {
      if (window.scrollY > 500) {
          backToTop.classList.add('active');
      } else {
          backToTop.classList.remove('active');
      }
  });
  
  backToTop.addEventListener('click', () => {
      window.scrollTo({
          top: 0,
          behavior: 'smooth'
      });
  });
  
  // Playground tabs
  const playgroundTabs = document.querySelectorAll('.playground-tab');
  const playgroundPanels = document.querySelectorAll('.playground-panel');
  
  playgroundTabs.forEach(tab => {
      tab.addEventListener('click', () => {
          const target = tab.dataset.tab;
          
          // Remove active class from all tabs and panels
          playgroundTabs.forEach(t => t.classList.remove('active'));
          playgroundPanels.forEach(p => p.classList.remove('active'));
          
          // Add active class to clicked tab and corresponding panel
          tab.classList.add('active');
          document.getElementById(`${target}-panel`).classList.add('active');
      });
  });
  
  // Testimonial slider
  const testimonialTrack = document.querySelector('.testimonials-track');
  const testimonials = document.querySelectorAll('.testimonial');
  const testimonialDots = document.querySelectorAll('.testimonial-dot');
  const prevTestimonial = document.querySelector('.prev-testimonial');
  const nextTestimonial = document.querySelector('.next-testimonial');
  
  let currentTestimonial = 0;
  const testimonialCount = testimonials.length;
  
  function updateTestimonialSlider() {
      testimonialTrack.style.transform = `translateX(-${currentTestimonial * 100}%)`;
      
      // Update dots
      testimonialDots.forEach((dot, index) => {
          dot.classList.toggle('active', index === currentTestimonial);
      });
  }
  
  prevTestimonial.addEventListener('click', () => {
      currentTestimonial = (currentTestimonial - 1 + testimonialCount) % testimonialCount;
      updateTestimonialSlider();
  });
  
  nextTestimonial.addEventListener('click', () => {
      currentTestimonial = (currentTestimonial + 1) % testimonialCount;
      updateTestimonialSlider();
  });
  
  testimonialDots.forEach((dot, index) => {
      dot.addEventListener('click', () => {
          currentTestimonial = index;
          updateTestimonialSlider();
      });
  });
  
  // Auto-advance testimonials
  setInterval(() => {
      currentTestimonial = (currentTestimonial + 1) % testimonialCount;
      updateTestimonialSlider();
  }, 5000);
  
  // Pricing toggle
  const pricingToggle = document.querySelector('.pricing-toggle-switch');
  const pricingToggleTexts = document.querySelectorAll('.pricing-toggle-text');
  const monthlyPrices = document.querySelectorAll('.pricing-price.monthly');
  const yearlyPrices = document.querySelectorAll('.pricing-price.yearly');
  
  pricingToggle.addEventListener('click', () => {
      pricingToggle.classList.toggle('yearly');
      pricingToggleTexts.forEach(text => text.classList.toggle('active'));
      
      if (pricingToggle.classList.contains('yearly')) {
          monthlyPrices.forEach(price => price.style.display = 'none');
          yearlyPrices.forEach(price => price.style.display = 'block');
      } else {
          monthlyPrices.forEach(price => price.style.display = 'block');
          yearlyPrices.forEach(price => price.style.display = 'none');
      }
  });
  
  // Initialize pricing toggle
  pricingToggleTexts[0].classList.add('active');
  
  // Calculator functionality
  const mentorHoursSlider = document.getElementById('mentor-hours');
  const mentorHoursValue = document.getElementById('mentor-hours-value');
  const donationAmountSlider = document.getElementById('donation-amount');
  const donationAmountValue = document.getElementById('donation-amount-value');
  const jobOppsSlider = document.getElementById('job-opps');
  const jobOppsValue = document.getElementById('job-opps-value');
  const eventsAttendedSlider = document.getElementById('events-attended');
  const eventsAttendedValue = document.getElementById('events-attended-value');
  
  const studentsImpacted = document.getElementById('students-impacted');
  const scholarshipContribution = document.getElementById('scholarship-contribution');
  const careerOpportunities = document.getElementById('career-opportunities');
  const networkStrength = document.getElementById('network-strength');
  
  function updateCalculator() {
      const mentorHours = parseInt(mentorHoursSlider.value);
      const donationAmount = parseInt(donationAmountSlider.value);
      const jobOpps = parseInt(jobOppsSlider.value);
      const eventsAttended = parseInt(eventsAttendedSlider.value);
      
      // Update display values
      mentorHoursValue.textContent = mentorHours;
      donationAmountValue.textContent = donationAmount;
      jobOppsValue.textContent = jobOpps;
      eventsAttendedValue.textContent = eventsAttended;
      
      // Calculate impact
      const impactedStudentsCount = mentorHours * 3 + Math.floor(donationAmount / 100) + jobOpps * 3 + eventsAttended;
      const scholarshipAmount = Math.floor(donationAmount * 0.5);
      const careerOppCount = jobOpps * 3 + Math.floor(mentorHours / 2);
      
      let strengthLevel = 'Low';
      const totalPoints = mentorHours + (donationAmount / 100) + (jobOpps * 2) + eventsAttended;
      
      if (totalPoints > 30) {
          strengthLevel = 'Exceptional';
      } else if (totalPoints > 20) {
          strengthLevel = 'Very Strong';
      } else if (totalPoints > 10) {
          strengthLevel = 'Strong';
      } else if (totalPoints > 5) {
          strengthLevel = 'Moderate';
      }
      
      // Update result values
      studentsImpacted.textContent = impactedStudentsCount;
      scholarshipContribution.textContent = scholarshipAmount;
      careerOpportunities.textContent = careerOppCount;
      networkStrength.textContent = strengthLevel;
  }
  
  // Add event listeners to sliders
  mentorHoursSlider.addEventListener('input', updateCalculator);
  donationAmountSlider.addEventListener('input', updateCalculator);
  jobOppsSlider.addEventListener('input', updateCalculator);
  eventsAttendedSlider.addEventListener('input', updateCalculator);
  
  // Initialize calculator
  updateCalculator();
  
  // Particles animation
  createParticles();
  
  // Initialize AOS (if you want to add it)
  if (typeof AOS !== 'undefined') {
      AOS.init({
          duration: 800,
          easing: 'ease-in-out',
          once: true
      });
  }
});

// Theme Switcher Functions
function addThemeSwitcher() {
  const themeSwitcher = document.createElement('div');
  themeSwitcher.className = 'theme-switcher';
  
  const themes = [
      { name: 'default', label: 'Blue' },
      { name: 'dark', label: 'Dark' },
      { name: 'purple', label: 'Purple' },
      { name: 'green', label: 'Green' },
      { name: 'amber', label: 'Amber' }
  ];
  
  themes.forEach(theme => {
      const themeOption = document.createElement('div');
      themeOption.className = 'theme-option';
      themeOption.dataset.theme = theme.name;
      themeOption.title = theme.label;
      
      themeOption.addEventListener('click', () => {
          setTheme(theme.name);
          
          // Update active state
          document.querySelectorAll('.theme-option').forEach(option => {
              option.classList.remove('active');
          });
          themeOption.classList.add('active');
      });
      
      themeSwitcher.appendChild(themeOption);
  });
  
  document.body.appendChild(themeSwitcher);
}

function initializeTheme() {
  const savedTheme = localStorage.getItem('alumni-theme') || 'default';
  setTheme(savedTheme);
  
  // Set active state on the correct theme option
  const activeOption = document.querySelector(`.theme-option[data-theme="${savedTheme}"]`);
  if (activeOption) {
      activeOption.classList.add('active');
  }
}

function setTheme(themeName) {
  // Add transition class to body for smooth theme change
  document.body.classList.add('theme-transition');
  
  // Remove all theme attributes
  document.body.removeAttribute('data-theme');
  
  // Add the selected theme attribute
  if (themeName !== 'default') {
      document.body.setAttribute('data-theme', themeName);
  }
  
  // Save theme preference
  localStorage.setItem('alumni-theme', themeName);
  
  // Remove transition class after transition completes
  setTimeout(() => {
      document.body.classList.remove('theme-transition');
  }, 500);
}

// Create particles for hero section
function createParticles() {
  const particlesContainer = document.getElementById('particles');
  if (!particlesContainer) return;
  
  const particleCount = 50;
  
  for (let i = 0; i < particleCount; i++) {
      const particle = document.createElement('div');
      particle.className = 'particle';
      
      // Random position
      const posX = Math.random() * 100;
      const posY = Math.random() * 100;
      
      // Random size
      const size = Math.random() * 5 + 1;
      
      // Random opacity
      const opacity = Math.random() * 0.5 + 0.1;
      
      // Random animation duration
      const duration = Math.random() * 20 + 10;
      
      // Apply styles
      particle.style.cssText = `
          position: absolute;
          top: ${posY}%;
          left: ${posX}%;
          width: ${size}px;
          height: ${size}px;
          background-color: var(--primary-color);
          border-radius: 50%;
          opacity: ${opacity};
          animation: float ${duration}s infinite ease-in-out;
          animation-delay: ${Math.random() * 5}s;
      `;
      
      particlesContainer.appendChild(particle);
  }
}