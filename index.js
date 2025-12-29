const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

// Import data
let books = require('./booksdb.js');
let users = require('./users.js');

const app = express();
const PORT = 5000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// JWT Secret (in production, use environment variable)
const JWT_SECRET = 'your-secret-key';

// Helper function to authenticate JWT token
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({ message: 'Access token required' });
  }

  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({ message: 'Invalid token' });
    }
    req.user = user;
    next();
  });
}

// Routes

// Get all books
app.get('/books', (req, res) => {
  res.status(200).json(books);
});

// Get book by ISBN
app.get('/books/isbn/:isbn', (req, res) => {
  const isbn = req.params.isbn;
  const book = Object.values(books).find(book => book.isbn === isbn);

  if (book) {
    res.status(200).json(book);
  } else {
    res.status(404).json({ message: 'Book not found' });
  }
});

// Get books by author
app.get('/books/author/:author', (req, res) => {
  const author = req.params.author.toLowerCase();
  const filteredBooks = Object.values(books).filter(book =>
    book.author.toLowerCase().includes(author)
  );

  res.status(200).json(filteredBooks);
});

// Get books by title
app.get('/books/title/:title', (req, res) => {
  const title = req.params.title.toLowerCase();
  const filteredBooks = Object.values(books).filter(book =>
    book.title.toLowerCase().includes(title)
  );

  res.status(200).json(filteredBooks);
});

// Get reviews for a book
app.get('/books/:isbn/review', (req, res) => {
  const isbn = req.params.isbn;
  const book = Object.values(books).find(book => book.isbn === isbn);

  if (book) {
    res.status(200).json(book.reviews || {});
  } else {
    res.status(404).json({ message: 'Book not found' });
  }
});

// Add or modify a review (requires authentication)
app.put('/books/:isbn/review', authenticateToken, (req, res) => {
  const isbn = req.params.isbn;
  const { review } = req.body;
  const username = req.user.username;

  const book = Object.values(books).find(book => book.isbn === isbn);

  if (!book) {
    return res.status(404).json({ message: 'Book not found' });
  }

  if (!book.reviews) {
    book.reviews = {};
  }

  book.reviews[username] = review;
  res.status(200).json({
    message: 'Review added/modified successfully',
    reviews: book.reviews
  });
});

// Delete a review (requires authentication)
app.delete('/books/:isbn/review', authenticateToken, (req, res) => {
  const isbn = req.params.isbn;
  const username = req.user.username;

  const book = Object.values(books).find(book => book.isbn === isbn);

  if (!book) {
    return res.status(404).json({ message: 'Book not found' });
  }

  if (book.reviews && book.reviews[username]) {
    delete book.reviews[username];
    res.status(200).json({
      message: 'Review deleted successfully',
      reviews: book.reviews
    });
  } else {
    res.status(404).json({ message: 'Review not found' });
  }
});

// User registration
app.post('/register', (req, res) => {
  const { username, password } = req.body;

  // Check if user already exists
  const existingUser = users.find(user => user.username === username);
  if (existingUser) {
    return res.status(400).json({ message: 'Username already exists' });
  }

  // Hash password
  const hashedPassword = bcrypt.hashSync(password, 8);

  // Create new user
  const newUser = {
    username,
    password: hashedPassword
  };

  users.push(newUser);

  res.status(201).json({ message: 'User registered successfully' });
});

// User login
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  // Find user
  const user = users.find(user => user.username === username);
  if (!user) {
    return res.status(401).json({ message: 'Invalid credentials' });
  }

  // Check password
  const passwordIsValid = bcrypt.compareSync(password, user.password);
  if (!passwordIsValid) {
    return res.status(401).json({ message: 'Invalid credentials' });
  }

  // Generate JWT token
  const token = jwt.sign({ username: user.username }, JWT_SECRET, {
    expiresIn: '24h'
  });

  res.status(200).json({
    message: 'Login successful',
    token: token
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app;
