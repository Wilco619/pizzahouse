create DATABASE pizzahouse;
use pizzahouse;
CREATE TABLE services (
    id INT PRIMARY KEY AUTO_INCREMENT,
    image VARCHAR(255),
    title VARCHAR(255),
    subtitle VARCHAR(255),
    serviceId INT
);


CREATE TABLE blogs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    main_image VARCHAR(255),
    other_images TEXT,
    date DATE  DEFAULT CURRENT_DATE,
    title VARCHAR(255),
    subtitle VARCHAR(255),
    body TEXT,
    blogId INT,
    author VARCHAR(255)
);
CREATE TABLE item (
    id INT PRIMARY KEY AUTO_INCREMENT,
    image VARCHAR(255),
    name VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2),
    itemId INT,
    cat VARCHAR(255)
);

INSERT INTO blogs (main_image, other_images, date_, title, subtitle, body, blogId, author) VALUES ('https://example.com/main_image.jpg', 'https://example.com/other_image_1.jpg,https://example.com/other_image_2.jpg', '2022-04-16', 'My Blog Post', 'A Brief Summary', 'Lorem ipsum dolor sit amet.', 1, 'John Doe');
``
