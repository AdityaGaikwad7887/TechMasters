document.addEventListener('DOMContentLoaded', function () {
    const signupForm = document.getElementById('signup-form');
    const submitButton = document.getElementById('submit-btn');

    signupForm.addEventListener('submit', function (event) {
        event.preventDefault();
        // Assuming successful sign-up, proceed to the next page
        window.open('nextPage.html', '_blank');
    });
});


