/**
 * JavaScript functionality for quick match results page
 */
document.addEventListener('DOMContentLoaded', function() {
    // Add viewport meta tag if it doesn't exist
    if (!document.querySelector('meta[name="viewport"]')) {
        var meta = document.createElement('meta');
        meta.name = 'viewport';
        meta.content = 'width=device-width, initial-scale=1, maximum-scale=1';
        document.head.appendChild(meta);
    }

    // Focus on opponent select when page loads with a default player
    const opponentSelect = document.getElementById('opponent');
    if (opponentSelect) {
        setTimeout(function() {
            opponentSelect.focus();
        }, 300);
    }

    // Initialize any tooltip components
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    if (typeof bootstrap !== 'undefined') {
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
});
