const express = require('express');
const cors = require('cors');  // Add CORS middleware

const app = express();
const port = 3000;

app.use(cors()); // Enable CORS for all routes
// Parse JSON bodies
app.use(express.json());

let storedTabs = []; // In-memory storage for tabs data

// Endpoint to receive tab data
app.post('/receive-tabs', (req, res) => {
    storedTabs = req.body; // Store the received data
    console.log('Received tabs:', req.body);
    res.send({ status: 'success' });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

// Endpoint to serve tabs data to the webpage
app.get('/get-tabs', (req, res) => {
    res.json(storedTabs); // Send the stored tabs data
});