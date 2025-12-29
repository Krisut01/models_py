# Express Bookstore API

This is a complete Express.js application for an online bookstore, built for the Coursera final project. The application provides a REST API with the following features:

## Features Implemented

### Book Management
- **GET /books**: Retrieve all available books
- **GET /books/isbn/:isbn**: Search books by ISBN
- **GET /books/author/:author**: Search books by author name
- **GET /books/title/:title**: Search books by title

### User Authentication
- **POST /register**: Register new users
- **POST /login**: User login with JWT token generation

### Review Management
- **GET /books/:isbn/reviews**: Get reviews for a specific book
- **POST /books/:isbn/reviews**: Add/modify reviews (requires authentication)
- **DELETE /books/:isbn/reviews**: Delete user's own review (requires authentication)

## Project Structure

- `index.js`: Main Express server file
- `booksdb.js`: Books data store
- `users.js`: User data store
- `general.js`: Axios-based helper functions for book retrieval
- `package.json`: Project dependencies and scripts

## Dependencies

- `express`: Web framework
- `body-parser`: Request body parsing
- `cors`: Cross-origin resource sharing
- `jsonwebtoken`: JWT token handling
- `bcryptjs`: Password hashing
- `axios`: HTTP client for general.js functions

## Running the Application

1. Install dependencies: `npm install`
2. Start the server: `npm start` or `node index.js`
3. Server runs on http://localhost:5000

## API Testing

All endpoints have been tested and the cURL commands with responses are saved in the following files:
- `githubrepo`: GitHub repository fork command
- `getallbooks`: Get all books
- `getbooksbyISBN`: Get book by ISBN
- `getbooksbyauthor`: Get books by author
- `getbooksbytitle`: Get books by title
- `getbookreview`: Get book reviews
- `register`: User registration
- `login`: User login
- `reviewadded`: Add/modify review
- `deletereview`: Delete review

## Data Source

Books data is stored in `booksdb.js` with sample book entries including ISBN, title, author, and reviews.
