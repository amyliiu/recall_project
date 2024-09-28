const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

// Serve the HTML form
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'popup.html'));
});

// Handle form submission
app.post('/submit', (req, res) => {
    const { email, address } = req.body;

    // Create the data object
    const userData = {
        email,
        address,
    };

    // Specify the path for the JSON file
    const dataFilePath = path.join(__dirname, 'data.json');

    // Read existing data
    fs.readFile(dataFilePath, 'utf8', (err, data) => {
        let jsonData = [];
        if (!err && data) {
            jsonData = JSON.parse(data);
        }

        // Add new data to the array
        jsonData.push(userData);

        // Write the updated data back to the file
        fs.writeFile(dataFilePath, JSON.stringify(jsonData, null, 2), (err) => {
            if (err) {
                console.error(err);
                return res.status(500).send('Error saving data.');
            }
            res.send('Thanks for submitting! Your data has been saved.');
        });
    });
});

// Start the server
app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
