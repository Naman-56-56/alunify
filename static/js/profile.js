document.addEventListener('DOMContentLoaded', function() {
    // Edit Profile Button
    const editProfileBtn = document.querySelector('.edit-profile-btn');
    const editProfileModal = document.getElementById('edit-profile-modal');
    
    if (editProfileBtn && editProfileModal) {
        editProfileBtn.addEventListener('click', function() {
            editProfileModal.style.display = 'block';
        });
    }

    // Edit Profile Form Submission
    const editProfileForm = document.getElementById('edit-profile-form');
    
    if (editProfileForm) {
        editProfileForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form values
            const name = document.getElementById('edit-name').value;
            const title = document.getElementById('edit-title').value;
            const location = document.getElementById('edit-location').value;
            const about = document.getElementById('edit-about').value;
            
            // Update profile with new values
            document.getElementById('profile-name').textContent = name;
            document.getElementById('profile-title').textContent = title;
            document.getElementById('profile-location').textContent = location;
            document.getElementById('profile-about').textContent = about;
            
            // Close modal
            editProfileModal.style.display = 'none';
            
            // Show success message
            alert('Profile updated successfully!');
        });
    }

    // Alumni Directory Filtering
    const filterBtn = document.querySelector('.filter-btn');
    
    if (filterBtn) {
        filterBtn.addEventListener('click', function() {
            // In a real application, this would filter the alumni based on selected criteria
            // For demo purposes, we'll just show a message
            alert('Filtering functionality would be implemented here.');
            
            // Simulate loading alumni data
            const alumniGrid = document.querySelector('.alumni-grid');
            
            if (alumniGrid) {
                // Clear existing alumni
                alumniGrid.innerHTML = '';
                
                // Add sample alumni cards
                for (let i = 0; i < 6; i++) {
                    const alumniCard = document.createElement('div');
                    alumniCard.className = 'profile-card';
                    alumniCard.innerHTML = `
                        <div class="profile-header">
                            <div class="profile-avatar">
                                <img src="images/default-avatar.jpg" alt="Alumni">
                            </div>
                            <div class="profile-info">
                                <h3>Alumni Name ${i + 1}</h3>
                                <p>Class of ${2010 + i}, Computer Science</p>
                                <p>Software Engineer at Tech Company</p>
                                <p>San Francisco, CA</p>
                            </div>
                            <button class="btn secondary-btn">Connect</button>
                        </div>
                    `;
                    alumniGrid.appendChild(alumniCard);
                }
            }
        });
    }

    // Alumni Search
    const searchBtn = document.querySelector('.search-btn');
    
    if (searchBtn) {
        searchBtn.addEventListener('click', function() {
            const searchInput = document.getElementById('alumni-search');
            const searchResults = document.querySelector('.search-results');
            
            if (searchInput && searchResults) {
                const searchTerm = searchInput.value.trim();
                
                if (searchTerm === '') {
                    searchResults.innerHTML = '<p class="search-message">Enter a search term to find alumni</p>';
                    return;
                }
                
                // In a real application, this would search the alumni database
                // For demo purposes, we'll just show some sample results
                searchResults.innerHTML = `
                    <p>Search results for "${searchTerm}":</p>
                    <div class="alumni-grid">
                        <div class="profile-card">
                            <div class="profile-header">
                                <div class="profile-avatar">
                                    <img src="images/default-avatar.jpg" alt="Alumni">
                                </div>
                                <div class="profile-info">
                                    <h3>John ${searchTerm}</h3>
                                    <p>Class of 2015, Computer Science</p>
                                    <p>Software Engineer at Tech Company</p>
                                    <p>San Francisco, CA</p>
                                </div>
                                <button class="btn secondary-btn">Connect</button>
                            </div>
                        </div>
                        <div class="profile-card">
                            <div class="profile-header">
                                <div class="profile-avatar">
                                    <img src="images/default-avatar.jpg" alt="Alumni">
                                </div>
                                <div class="profile-info">
                                    <h3>Sarah ${searchTerm}</h3>
                                    <p>Class of 2018, Business</p>
                                    <p>Marketing Manager at Startup</p>
                                    <p>New York, NY</p>
                                </div>
                                <button class="btn secondary-btn">Connect</button>
                            </div>
                        </div>
                    </div>
                `;
            }
        });
    }

    // Add Experience Button
    const addExperienceBtn = document.querySelector('.add-item-btn');
    
    if (addExperienceBtn) {
        addExperienceBtn.addEventListener('click', function() {
            // In a real application, this would open a form to add new experience
            alert('Add experience functionality would be implemented here.');
        });
    }
});