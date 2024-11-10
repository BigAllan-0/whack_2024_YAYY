const express = require('express');
const app = express();
const port = 3000;

// Parse JSON bodies
app.use(express.json());

// Endpoint to receive tab data
app.post('/receive-tabs', (req, res) => {
    console.log('Received tabs:', req.body);
    res.send({ status: 'success' });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

app.get('/receive-tabs', (req, res) => {
    res.send('This is the receive-tabs endpoint. Please use POST requests to send data.');
});
