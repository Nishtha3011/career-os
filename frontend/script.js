document.addEventListener('DOMContentLoaded', () => {
    const landingPage = document.getElementById('landing-page');
    const onboardingPage = document.getElementById('onboarding-page');
    const dashboardPage = document.getElementById('dashboard-page');

    const getStartedBtn = document.getElementById('get-started-btn');
    const onboardingForm = document.getElementById('onboarding-form');
    const targetRoleInput = document.getElementById('target-role');
    const displayTargetRole = document.getElementById('display-target-role');

    // Transition from Landing to Onboarding
    getStartedBtn.addEventListener('click', () => {
        landingPage.style.display = 'none';
        onboardingPage.style.display = 'flex';
    });

    // Handle Form Submission and Transition to Dashboard
    onboardingForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const target = targetRoleInput.value;

        // Update Dashboard with User Input
        if (target) {
            displayTargetRole.textContent = target;
        }

        onboardingPage.style.display = 'none';
        dashboardPage.style.display = 'grid';
        document.getElementById('particles-canvas').style.display = 'none';
    });
});
