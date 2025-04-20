document.addEventListener('DOMContentLoaded', function() {
    // Theme variables
    const THEMES = {
      LIGHT: 'theme-light',
      DARK: 'theme-dark',
      BLUE: 'theme-blue',
      GREEN: 'theme-green',
      PURPLE: 'theme-purple',
      HIGH_CONTRAST: 'theme-high-contrast'
    };
    
    // Get theme elements
    const themeToggle = document.querySelector('.theme-toggle');
    const themeOptions = document.querySelectorAll('.theme-option');
    
    // Check for saved theme preference or use default
    const savedTheme = localStorage.getItem('alumni-theme') || THEMES.LIGHT;
    const savedMode = localStorage.getItem('alumni-mode') || 'light';
    
    // Apply saved theme
    applyTheme(savedTheme);
    applyMode(savedMode);
    
    // Toggle between light and dark mode
    if (themeToggle) {
      themeToggle.addEventListener('click', function() {
        const currentMode = document.body.classList.contains(THEMES.DARK) ? 'light' : 'dark';
        applyMode(currentMode);
        localStorage.setItem('alumni-mode', currentMode);
      });
    }
    
    // Theme option selection
    if (themeOptions) {
      themeOptions.forEach(option => {
        // Mark the active theme
        if (option.dataset.theme === savedTheme) {
          option.classList.add('active');
        }
        
        option.addEventListener('click', function() {
          const selectedTheme = this.dataset.theme;
          
          // Update active state
          themeOptions.forEach(opt => opt.classList.remove('active'));
          this.classList.add('active');
          
          // Apply and save theme
          applyTheme(selectedTheme);
          localStorage.setItem('alumni-theme', selectedTheme);
        });
      });
    }
    
    // Function to apply theme
    function applyTheme(theme) {
      // Remove all theme classes
      Object.values(THEMES).forEach(themeClass => {
        if (themeClass !== THEMES.DARK && themeClass !== THEMES.LIGHT) {
          document.body.classList.remove(themeClass);
        }
      });
      
      // Add selected theme class
      if (theme !== THEMES.LIGHT) {
        document.body.classList.add(theme);
      }
    }
    
    // Function to apply light/dark mode
    function applyMode(mode) {
      if (mode === 'dark') {
        document.body.classList.add(THEMES.DARK);
      } else {
        document.body.classList.remove(THEMES.DARK);
      }
    }
  });