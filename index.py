import tkinter as tk
from tkinter import messagebox
import psycopg2

def create_tables():
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Category(
                category_id SERIAL PRIMARY KEY,
                Category_name VARCHAR(100)
            );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Animals(
                 animal_id SERIAL PRIMARY KEY,
                 Animal_name VARCHAR(100),
                 category_id SERIAL,
                 FOREIGN KEY (category_id) REFERENCES Category(category_id)
            );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
                product_id SERIAL PRIMARY KEY,
                Product_name VARCHAR(100),
                animal_id SERIAL,
                FOREIGN KEY (animal_id) REFERENCES Animals(animal_id)
            );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Vitamins(
                vitamin_id SERIAL PRIMARY KEY,
                Vitamin_name VARCHAR(100),
                Vitamin_price NUMERIC,
                product_id SERIAL,
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Pharmacy(
                pharmacy_id SERIAL PRIMARY KEY,
                Pharmacy_name VARCHAR(100),
                Pharmacy_price NUMERIC,
                product_id SERIAL,
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Food(
                food_id SERIAL PRIMARY KEY,
                Food_name VARCHAR(100),
                Food_price NUMERIC,
                product_id SERIAL,
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Toys(
                toys_id SERIAL PRIMARY KEY,
                Toys_name VARCHAR(100),
                Toys_price NUMERIC,
                product_id SERIAL,
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Care_products(
                cr_id SERIAL PRIMARY KEY,
                Care_products_name VARCHAR(100),
                Care_products_price NUMERIC,
                product_id SERIAL,
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Collars(
                collars_id SERIAL PRIMARY KEY,
                Collars_name VARCHAR(100),
                Collars_description TEXT,
                Collars_price NUMERIC,
                product_id SERIAL,
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Bowls_feeders(
                bf_id SERIAL PRIMARY KEY,
                Bowls_feeders_name VARCHAR(100),
                Bowls_feeders_description TEXT,
                Bowls_feeders_price NUMERIC,
                product_id SERIAL,
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Clothes(
                clothes_id SERIAL PRIMARY KEY,
                clothes_name VARCHAR(100),
                clothes_description TEXT,
                clothes_price NUMERIC,
                product_id SERIAL,
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Beds_kennels(
                Beds_kennels_id SERIAL PRIMARY KEY,
                Beds_kennels_name VARCHAR(100),
                Beds_kennels_description TEXT,
                Beds_kennels_price NUMERIC,
                product_id SERIAL,
                FOREIGN KEY (product_id) REFERENCES Products(product_id)
            );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Orders(
                orders_id SERIAL PRIMARY KEY         
            );
        """)

        con.commit()
        messagebox.showinfo("Успех", "Таблицы успешно созданы!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка: {e}")

def show_animals_buttons():
    animals_frame = tk.Frame(root)
    animals_frame.pack()

    animal_buttons = [
        ("Собака", lambda: show_products_buttons("Собака")),
        ("Кошка", lambda: show_products_buttons("Кошка")),
        ("Попугай", lambda: show_products_buttons("Попугай")),
        ("Кролик", lambda: show_products_buttons("Кролик")),
    ]

    for animal, command in animal_buttons:
        button = tk.Button(animals_frame, text=animal, command=command)
        button.pack(pady=10, side=tk.RIGHT)

def show_products_buttons(animal):
    products_frame = tk.Frame(root)
    products_frame.pack()

    product_buttons = [
        ("Витамины", lambda: add_to_cart(animal, "Витамины")),
        ("Фармаси", lambda: add_to_cart(animal, "Фармаси")),
        ("Корм", lambda: add_to_cart(animal, "Корм")),
        ("Игрушки", lambda: add_to_cart(animal, "Игрушки")),
        ("Уходовые товары", lambda: add_to_cart(animal, "Уходовые товары")),
        ("Ошейники", lambda: add_to_cart(animal, "Ошейники")),
        ("Миски", lambda: add_to_cart(animal, "Миски")),
        ("Кровати", lambda: add_to_cart(animal, "Кровати")),
    ]

    for product, command in product_buttons:
        button = tk.Button(products_frame, text=product, command=command)
        button.pack(pady=10, side=tk.RIGHT)

def add_to_cart(animal, product):
    cart.append((animal, product))
    messagebox.showinfo("Добавлено в корзину", f"{product} для {animal} добавлено в корзину!")
    print("Successful!!")
    show_cart()

def show_cart():
    cart_frame = tk.Frame(root)
    cart_frame.pack()

    cart_label = tk.Label(cart_frame, text="Корзина")
    cart_label.pack()

    for item in cart:
        item_label = tk.Label(cart_frame, text=f"{item[1]} для {item[0]}")
        item_label.pack()

    return_to_shopping_button = tk.Button(cart_frame, text="Вернуться к покупкам", command=show_animals_buttons)
    return_to_shopping_button.pack(pady=10, side=tk.RIGHT)

if __name__ == "__main__":
    con = psycopg2.connect(
        host='localhost',
        database='SUBD',
        user='postgres',
        password='123',
        port='5432'
    )
    cursor = con.cursor()

    root = tk.Tk()
    root.title("Магазин для животных")

    create_tables_button = tk.Button(root, text="Создать таблицы", command=create_tables)
    create_tables_button.pack(pady=10, side=tk.RIGHT)

    cart = []  # Здесь хранятся товары в корзине

    show_animals_buttons()

    root.mainloop()
