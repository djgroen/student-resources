document.addEventListener('DOMContentLoaded', function () {
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const closeSidebar = document.getElementById('close-sidebar');

    // Function to open the sidebar
    function openSidebar() {
        sidebar.style.display = 'block'; // Show the sidebar
        setTimeout(() => {
            sidebar.classList.add('open'); // Add class to animate in
        }, 10); // Short delay for the CSS transition to take effect
    }

    // Function to close the sidebar
    function closeSidebarFunc() {
        sidebar.classList.remove('open'); // Remove class to animate out
        setTimeout(() => {
            sidebar.style.display = 'none'; // Hide after animation
        }, 300); // Match with CSS transition time
    }

    // Toggle sidebar visibility
    sidebarToggle.addEventListener('click', () => {
        if (sidebar.style.display === 'none' || sidebar.style.display === '') {
            openSidebar();
        } else {
            closeSidebarFunc();
        }
    });

    // Close sidebar with the close button
    closeSidebar.addEventListener('click', closeSidebarFunc);
});
