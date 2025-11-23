# Secondshelf – Second-Hand Books Marketplace

## 📘 Description
Secondshelf is a Django-based e-commerce platform for buying and selling second-hand books. It allows users to:

- Browse and search books  
- Add books to wishlist or cart  
- Checkout per seller  
- Chat with sellers  
- Manage book listings (for sellers)  
- Admin management of users, books, and categories  

The platform aims to make books more affordable while providing an **easy-to-use marketplace** for students and readers.

---

## ✨ Features
- **User authentication & role-based access** (Buyer, Seller, Admin)  
- **Book listing** with search and category filters  
- **Wishlist & cart management**  
- **Multi-seller checkout**  
- **Buyer–seller chat system**  
- **Seller dashboard** for managing books  
- **Admin panel** for overseeing the platform  

---

## 🛠 Technologies Used
- **Backend:** Django  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Database:** SQLite / MySQL  
- **Payment Integration:** Stripe (test mode)  
- **Authentication:** Django Auth System  

---

## ⚙️ Installation

### Requirements
- Python 3.x  
- Django  
- pip  
- virtualenv  

### Steps

1. **Clone the repository**  
```bash
git clone <https://github.com/AamnaAamir/SecondShelfProj>
````

2. **Navigate to the project directory**

```bash
cd secondshelf
```

3. **Create a virtual environment**

```bash
python -m venv venv
```

4. **Activate the virtual environment**

```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

5. **Install dependencies**

```bash
pip install -r requirements.txt
```

6. **Apply database migrations**

```bash
python manage.py migrate
```

7. **Create a superuser for admin**

```bash
python manage.py createsuperuser
```

8. **Run the server**

```bash
python manage.py runserver
```

9. **Open the website in a browser**

```
http://127.0.0.1:8000
```

---

## 🖥 Usage

**Buyer:**

* Browse books, add to wishlist/cart
* Chat with sellers
* Checkout per seller

**Seller:**

* Add, edit, delete books
* Manage listings
* Chat with buyers

**Admin:**

* Manage users, books, categories
* Monitor chats and platform activity

---

## 🗄 Database Structure

**Tables:** User, Book, Category, CartItem, Wishlist, Message, Order, OrderItems

**Relationships:**

* User ↔ Book (Seller)
* User ↔ CartItem / Wishlist / Message
* Order ↔ OrderItems
* Book ↔ Category

---

## 👤 Author

* **Name:** Amna Amir
* **Email:** amnaamir0804@gmail.com

```
