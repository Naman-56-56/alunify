document.addEventListener('DOMContentLoaded', function() {
    // Event Registration
    const registerBtns = document.querySelectorAll('.event-btn');
    
    if (registerBtns.length > 0) {
        registerBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                const eventTitle = this.closest('.event-details').querySelector('h3').textContent;
                
                // In a real application, this would register the user for the event
                alert(`You have successfully registered for "${eventTitle}"`);
                
                // Update the My Events tab
                updateMyEvents(eventTitle);
            });
        });
    }

    // Function to update My Events tab
    function updateMyEvents(eventTitle) {
        const myEventsTab = document.getElementById('my-events');
        
        if (myEventsTab) {
            // Remove empty state if it exists
            const emptyState = myEventsTab.querySelector('.my-events-empty');
            if (emptyState) {
                emptyState.remove();
            }
            
            // Create events list if it doesn't exist
            let eventsList = myEventsTab.querySelector('.events-list');
            if (!eventsList) {
                eventsList = document.createElement('div');
                eventsList.className = 'events-list';
                myEventsTab.appendChild(eventsList);
            }
            
            // Add the new event
            const eventCard = document.createElement('div');
            eventCard.className = 'event-card';
            eventCard.innerHTML = `
                <div class="event-date">
                    <span class="day">15</span>
                    <span class="month">May</span>
                </div>
                <div class="event-details">
                    <h3>${eventTitle}</h3>
                    <p class="event-meta">
                        <span class="event-time">10:00 AM - 5:00 PM</span>
                        <span class="event-location">Main Campus, Grand Hall</span>
                    </p>
                    <div class="event-actions">
                        <button class="btn secondary-btn">Cancel Registration</button>
                        <button class="btn secondary-btn">Add to Calendar</button>
                    </div>
                </div>
            `;
            eventsList.appendChild(eventCard);
            
            // Add event listener to cancel registration button
            const cancelBtn = eventCard.querySelector('.secondary-btn');
            if (cancelBtn) {
                cancelBtn.addEventListener('click', function() {
                    // In a real application, this would cancel the registration
                    alert(`You have cancelled your registration for "${eventTitle}"`);
                    eventCard.remove();
                    
                    // If no more events, show empty state
                    if (eventsList.children.length === 0) {
                        myEventsTab.innerHTML = `
                            <div class="my-events-empty">
                                <img src="images/calendar-icon.svg" alt="Calendar" class="empty-icon">
                                <h3>No Registered Events</h3>
                                <p>You haven't registered for any upcoming events yet.</p>
                                <button class="btn primary-btn">Browse Events</button>
                            </div>
                        `;
                    }
                });
            }
        }
    }

    // Event Proposal
    const proposeEventBtn = document.getElementById('propose-event-btn');
    const eventProposalModal = document.getElementById('event-proposal-modal');
    
    if (proposeEventBtn && eventProposalModal) {
        proposeEventBtn.addEventListener('click', function() {
            eventProposalModal.style.display = 'block';
        });
    }

    // Event Proposal Form Submission
    const eventProposalForm = document.getElementById('event-proposal-form');
    
    if (eventProposalForm) {
        eventProposalForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // In a real application, this would submit the proposal to the server
            alert('Your event proposal has been submitted successfully!');
            
            // Close modal and reset form
            eventProposalModal.style.display = 'none';
            eventProposalForm.reset();
        });
    }

    // Event Filtering
    const filterBtn = document.querySelector('.filter-btn');
    
    if (filterBtn) {
        filterBtn.addEventListener('click', function() {
            // Get filter values
            const eventType = document.getElementById('event-type').value;
            const eventLocation = document.getElementById('event-location').value;
            const eventDate = document.getElementById('event-date').value;
            
            // In a real application, this would filter events based on selected criteria
            alert(`Filtering events by: Type=${eventType}, Location=${eventLocation}, Date=${eventDate}`);
            
            // For demo purposes, we'll just show a loading message
            const eventsTab = document.getElementById('upcoming-events');
            if (eventsTab) {
                const eventsList = eventsTab.querySelector('.events-list');
                if (eventsList) {
                    eventsList.innerHTML = '<p class="search-message">Filtering events...</p>';
                    
                    // Simulate loading delay
                    setTimeout(() => {
                        // Restore original events (in a real app, this would show filtered results)
                        eventsList.innerHTML = document.querySelector('.events-list').innerHTML;
                    }, 1000);
                }
            }
        });
    }

    // Pagination
    const paginationBtns = document.querySelectorAll('.pagination-btn');
    
    if (paginationBtns.length > 0) {
        paginationBtns.forEach(btn => {
            if (!btn.disabled) {
                btn.addEventListener('click', function() {
                    // In a real application, this would load the next/previous page of events
                    alert('Pagination functionality would be implemented here.');
                });
            }
        });
    }
});