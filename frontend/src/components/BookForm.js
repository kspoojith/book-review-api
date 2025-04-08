import React, { useState } from 'react';

function BookForm() {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [description, setDescription] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch('/books/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title: title,
        author: author,
        description: description,
      }),
    })
      .then((res) => {
        if (res.ok) {
          setMessage('Book added successfully!');
          setTitle('');
          setAuthor('');
          setDescription('');
        } else {
          setMessage('Failed to add book.');
        }
      })
      .catch(() => {
        setMessage('Error connecting to backend.');
      });
  };

  return (
    <div>
      <h2>Add a Book</h2>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title: </label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Author: </label>
          <input
            type="text"
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Description: </label>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          ></textarea>
        </div>
        <button type="submit">Add Book</button>
      </form>
    </div>
  );
}

export default BookForm;
