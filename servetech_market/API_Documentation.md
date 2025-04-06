
**Explanation:**

- The **README.md** file provides an overview of the project, structure, setup instructions, and best practices regarding Git.  





# API Documentation for ServeTech Market

This document describes the API endpoints, HTTP methods, URL examples, and a short description for each.

## Base URL

`https://servetch.com/`

## Endpoints

| **Endpoint**         | **HTTP Method** | **URL Example**                        | **Description**                                                         |
|----------------------|-----------------|----------------------------------------|-------------------------------------------------------------------------|
| **Authentication**   |                 |                                        |                                                                         |
| Register             | POST            | `https://servetch.com/register/`       | Registers a new user (customer or manager).                             |
| Login                | POST            | `https://servetch.com/login/`          | Logs in a user and returns a session or token.                          |
| Logout               | POST            | `https://servetch.com/logout/`         | Logs out the user.                                                      |
| **Customers**        |                 |                                        |                                                                         |
| List Customers       | GET             | `https://servetch.com/customers/`      | Retrieves a list of customers (manager/admin access only).              |
| Create Customer      | POST            | `https://servetch.com/customers/`      | Creates a new customer record.                                          |
| Retrieve Customer    | GET             | `https://servetch.com/customers/1/`    | Retrieves details for customer with ID 1.                               |
| Update Customer      | PUT/PATCH       | `https://servetch.com/customers/1/`    | Updates details for customer with ID 1.                                 |
| Delete Customer      | DELETE          | `https://servetch.com/customers/1/`    | Deletes the customer record with ID 1.                                  |
| **Products**         |                 |                                        |                                                                         |
| List Products        | GET             | `https://servetch.com/products/`       | Retrieves a list of products, optionally filtered/paginated.            |
| Create Product       | POST            | `https://servetch.com/products/`       | Creates a new product (manager/admin only).                             |
| Retrieve Product     | GET             | `https://servetch.com/products/1/`     | Retrieves details for product with ID 1.                                |
| Update Product       | PUT/PATCH       | `https://servetch.com/products/1/`     | Updates details for product with ID 1.                                  |
| Delete Product       | DELETE          | `https://servetch.com/products/1/`     | Deletes the product with ID 1.                                          |
| **Categories**       |                 |                                        |                                                                         |
| List Categories      | GET             | `https://servetch.com/categories/`     | Retrieves a list of product categories.                                 |
| Create Category      | POST            | `https://servetch.com/categories/`     | Creates a new category (manager/admin only).                            |
| Retrieve Category    | GET             | `https://servetch.com/categories/1/`   | Retrieves details for category with ID 1.                               |
| Update Category      | PUT/PATCH       | `https://servetch.com/categories/1/`   | Updates details for category with ID 1.                                 |
| Delete Category      | DELETE          | `https://servetch.com/categories/1/`   | Deletes the category with ID 1.                                         |
| **Orders**           |                 |                                        |                                                                         |
| List Orders          | GET             | `https://servetch.com/orders/`         | Retrieves orders (admin sees all; customers see their own orders).      |
| Create Order         | POST            | `https://servetch.com/orders/`         | Creates a new order.                                                    |
| Retrieve Order       | GET             | `https://servetch.com/orders/1/`       | Retrieves details for order with ID 1.                                  |
| Update Order         | PUT/PATCH       | `https://servetch.com/orders/1/`       | Updates order details (e.g., order status).                             |
| Delete Order         | DELETE          | `https://servetch.com/orders/1/`       | Cancels or deletes the order with ID 1.                                 |
| **Order Items**      |                 |                                        |                                                                         |
| Add Order Item       | POST            | `https://servetch.com/orders/1/items/`  | Adds an item to order with ID 1.                                        |
| List Order Items     | GET             | `https://servetch.com/orders/1/items/`  | Lists all items in order with ID 1.                                     |
| Retrieve Order Item  | GET             | `https://servetch.com/orders/1/items/1/`| Retrieves details for order item with ID 1 in order with ID 1.            |
| Update Order Item    | PUT/PATCH       | `https://servetch.com/orders/1/items/1/`| Updates the order item with ID 1 in order with ID 1.                     |
| Delete Order Item    | DELETE          | `https://servetch.com/orders/1/items/1/`| Removes the order item with ID 1 from order with ID 1.                    |

## Usage
these endpoints will be used to manage user authentication, customers, products, categories, orders, and order items. Authentication is required for creating, updating, and deleting resources; public endpoints are used for listing and retrieving details.
