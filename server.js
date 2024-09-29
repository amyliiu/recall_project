const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Serve static files (HTML, CSS, JS) from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Endpoint to handle form submission and save to a JSON file
app.post('/save-data', (req, res) => {
  const formData = req.body; // formData will contain 'email' and 'state'

  // Write form data to a JSON file
  fs.writeFile('email.json', JSON.stringify(formData, null, 2), (err) => {
    if (err) {
      console.error('Error writing file:', err);
      return res.status(500).json({ message: 'Failed to save data' });
    }
    res.json({ message: 'Data saved successfully!' });
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
