function handleSubmit(event) {
  event.preventDefault();

  const data = new FormData(event.target);
  const formJSON = Object.fromEntries(data.entries());

  // Display the result in the HTML
  const results = document.querySelector('.results pre');
  results.innerText = JSON.stringify(formJSON, null, 2);

  // Send the form data to the server
  fetch('/save-data', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(formJSON),
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
}

const form = document.querySelector('form');
form.addEventListener('submit', handleSubmit);