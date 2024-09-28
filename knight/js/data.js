function submitData() {
    const email = document.getElementById('email').value;
    const state = document.getElementById('state').value;

    if (email && state) {
        // Here you can use AJAX or Fetch API to send the data to your backend
        // This is a mock example, assuming you have a backend API set up
        fetch('YOUR_BACKEND_API_ENDPOINT', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: email, state: state }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            alert('Data submitted successfully!');
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('There was an error submitting your data.');
        });
    } else {
        alert('Please fill in both fields.');
    }
}
