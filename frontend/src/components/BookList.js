import React, { useEffect, useState } from 'react';

function BookList() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch('/books/')
      .then(response => response.json())
      .then(data => setBooks(data));
  }, []);

  return (
    <ul>
      {books.map(book => (
        <li key={book.id}>{book.title} by {book.author}</li>
      ))}
    </ul>
  );
}

export default BookList;
