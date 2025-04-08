document.addEventListener('DOMContentLoaded', function () {
    // Datos ficticios para libros
    const books = [
        { title: 'El Gran Gatsby', author: 'F. Scott Fitzgerald', image: 'images/libro1.jpeg' },
        { title: 'Cien Años de Soledad', author: 'Gabriel García Márquez', image: 'images/libro2.jpeg' },
        { title: 'Don Quijote de la Mancha', author: 'Miguel de Cervantes', image: 'images/libro3.jpg' }
    ];

    // Función para cargar libros
    function loadBooks() {
        const booksList = document.getElementById('books-list');
        books.forEach(book => {
            booksList.innerHTML += `
                <div class="book">
                    <img src="${book.image}" alt="${book.title}">
                    <h3>${book.title}</h3>
                    <p>Autor: ${book.author}</p>
                </div>
            `;
        });
    }

    // Cargar libros cuando la página se carga
    if (document.getElementById('books-list')) {
        loadBooks();
    }
});


document.addEventListener('DOMContentLoaded', function () {
    // Datos ficticios para libros
    const books = [
        { title: 'El Gran Gatsby', author: 'F. Scott Fitzgerald', image: 'images/libro1.jpeg' },
        { title: 'Cien Años de Soledad', author: 'Gabriel García Márquez', image: 'images/libro2.jpeg' },
        { title: 'Don Quijote de la Mancha', author: 'Miguel de Cervantes', image: 'images/libro3.jpg' }
    ];

    // Datos ficticios para autores
    const authors = [
        { name: 'F. Scott Fitzgerald' },
        { name: 'Gabriel García Márquez' },
        { name: 'Miguel de Cervantes' }
    ];

    // Función para cargar libros
    function loadBooks() {
        const booksList = document.getElementById('books-list');
        books.forEach(book => {
            booksList.innerHTML += `
                <div>
                    <img src="${book.image}" alt="${book.title}">
                    <h3>${book.title}</h3>
                    <p>Autor: ${book.author}</p>
                </div>
            `;
        });
    }

    // Función para cargar autores
    function loadAuthors() {
        const authorsList = document.getElementById('authors-list');
        authors.forEach(author => {
            authorsList.innerHTML += `<p>${author.name}</p>`;
        });
    }

    // Cargar libros y autores cuando la página se carga
    if (document.getElementById('books-list')) {
        loadBooks();
    }
    if (document.getElementById('authors-list')) {
        loadAuthors();
    }

    // Manejo del formulario de contacto
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function (event) {
            event.preventDefault();
            alert('Mensaje enviado con éxito');
            contactForm.reset();
        });
    }
});