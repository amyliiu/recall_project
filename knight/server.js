const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Path to the JSON file
const jsonFilePath = path.join(__dirname, 'data.json');

// Endpoint to handle form submissions
app.post('/submit', (req, res) => {
    const newData = req.body;

    // Read the existing JSON file
    fs.readFile(jsonFilePath, 'utf8', (err, data) => {
        if (err) {
            // If the file doesn't exist, start with an empty array
            if (err.code === 'ENOENT') {
                data = '[]';
            } else {
                return res.status(500).send('Error reading data');
            }
        }

        // Parse existing data
        let jsonData = JSON.parse(data);

        // Append new data
        jsonData.push(newData);

        // Write updated data back to the file
        fs.writeFile(jsonFilePath, JSON.stringify(jsonData, null, 2), (err) => {
            if (err) {
                return res.status(500).send('Error saving data');
            }
            res.send('Data saved successfully!');
        });
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
