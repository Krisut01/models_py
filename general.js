const axios = require('axios');

const baseURL = 'http://localhost:5000';

// Function to get all books
async function getAllBooks() {
  try {
    const response = await axios.get(`${baseURL}/books`);
    return response.data;
  } catch (error) {
    console.error('Error fetching all books:', error.message);
    throw error;
  }
}

// Function to get book by ISBN
async function getBookByISBN(isbn) {
  try {
    const response = await axios.get(`${baseURL}/books/isbn/${isbn}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching book by ISBN:', error.message);
    throw error;
  }
}

// Function to get books by author
async function getBooksByAuthor(author) {
  try {
    const response = await axios.get(`${baseURL}/books/author/${encodeURIComponent(author)}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching books by author:', error.message);
    throw error;
  }
}

// Function to get books by title
async function getBooksByTitle(title) {
  try {
    const response = await axios.get(`${baseURL}/books/title/${encodeURIComponent(title)}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching books by title:', error.message);
    throw error;
  }
}

module.exports = {
  getAllBooks,
  getBookByISBN,
  getBooksByAuthor,
  getBooksByTitle
};
