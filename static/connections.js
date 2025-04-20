/*
 * Connections Page JavaScript
 * Handles tab switching and other connection page functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    // Tab switching functionality
    const tabButtons = document.querySelectorAll('.connections-tabs .tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Get the tab ID from data attribute
            const tabId = this.getAttribute('data-tab');
            
            // Remove active class from all buttons and tabs
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to current button and tab
            this.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });

    // Connection request buttons
    const acceptButtons = document.querySelectorAll('.connection-actions .primary-btn');
    const declineButtons = document.querySelectorAll('.connection-actions .secondary-btn');
    
    acceptButtons.forEach(button => {
        button.addEventListener('click', function() {
            const card = this.closest('.connection-card');
            // Add a success message
            const message = document.createElement('div');
            message.classList.add('connection-message', 'success');
            message.textContent = 'Connection accepted!';
            
            // Replace the action buttons with the message
            const actionsDiv = this.parentNode;
            actionsDiv.innerHTML = '';
            actionsDiv.appendChild(message);
            
            // Animate the card
            card.classList.add('accepted');
            
            // You would typically make an AJAX call to the server here
            // to accept the connection request
        });
    });
    
    declineButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (button.textContent === 'Decline') {
                const card = this.closest('.connection-card');
                // Confirm before declining
                if (confirm('Are you sure you want to decline this connection request?')) {
                    // Add a declined message
                    const message = document.createElement('div');
                    message.classList.add('connection-message');
                    message.textContent = 'Request declined';
                    
                    // Replace the action buttons with the message
                    const actionsDiv = this.parentNode;
                    actionsDiv.innerHTML = '';
                    actionsDiv.appendChild(message);
                    
                    // Fade out the card
                    card.style.opacity = '0.6';
                    
                    // You would typically make an AJAX call to the server here
                    // to decline the connection request
                }
            }
        });
    });
    
    // Filter functionality
    const filterBtn = document.querySelector('.filter-btn');
    if (filterBtn) {
        filterBtn.addEventListener('click', function() {
            // This would typically trigger an AJAX request to filter results
            // For demo purposes, we'll just show a loading state
            filterBtn.textContent = 'Loading...';
            setTimeout(() => {
                filterBtn.textContent = 'Apply Filters';
                alert('Filters applied! This would reload the connections with filters applied.');
            }, 1000);
        });
    }
}); 