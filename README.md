Project Name

Secondshelf – Second-Hand Books Marketplace

Description

Secondshelf is a Django-based e-commerce platform for buying and selling second-hand books. It allows users to:

Browse and search books

Add books to wishlist or cart

Checkout per seller

Chat with sellers

Manage book listings (for sellers)

Admin management of users, books, and categories

The platform aims to make books more affordable while providing an easy-to-use marketplace for students and readers.

Features

User authentication and role-based access (Buyer, Seller, Admin)

Book listing with search and category filters

Wishlist and cart management

Multi-seller checkout

Buyer-seller chat system

Seller dashboard for managing books

Admin panel for overseeing the platform

Technologies Used

Backend: Django

Frontend: HTML, CSS, JavaScript, Bootstrap

Database: SQLite/MySQL

Payment Integration: Stripe (test mode)

Authentication: Django Auth System

Installation

Requirements: Python 3.x, Django, pip, virtualenv

Steps:

Clone the repository:

git clone <repository-url>


Navigate to the project directory:

cd secondshelf


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Create a superuser for admin:

python manage.py createsuperuser


Run the server:

python manage.py runserver


Open the website in a browser:

http://127.0.0.1:8000

Usage

Buyer: Browse books, add to wishlist/cart, chat with sellers, checkout

Seller: Add/edit/delete books, manage listings, chat with buyers

Admin: Manage users, books, categories, monitor chats

Database Structure

Tables: User, Book, Category, CartItem, Wishlist, Message, Order, OrderItems

Relationships:

User ↔ Book (Seller)

User ↔ CartItem / Wishlist / Messages

Order ↔ OrderItems

Book ↔ Category

Future Enhancements

Ratings and reviews for books and sellers

Order tracking system

Delivery partner integration

Mobile-friendly version

AI-based price suggestions

Author

Name: Amna Amir
Email: amnaamir0804@gmail.com
