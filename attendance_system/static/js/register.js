document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registrationForm');
    const faceUpload = document.querySelector('.face-upload');
    const faceUploadLabel = document.querySelector('.face-upload-label');

    // Update file upload label when file is selected
    faceUpload.addEventListener('change', function(e) {
        const fileName = e.target.files[0]?.name;
        if (fileName) {
            faceUploadLabel.textContent = `Selected: ${fileName}`;
        } else {
            faceUploadLabel.textContent = 'Upload Photo for Face Recognition';
        }
    });

    // Form submission handler
    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        const formData = new FormData(form);
        
        try {
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (response.ok) {
                // Show success message and redirect to login
                alert('Registration successful! Please login.');
                window.location.href = '/login';
            } else {
                // Show error message
                alert(data.error || 'Registration failed. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again later.');
        }
    });
});
