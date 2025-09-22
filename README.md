

### Создаём виртуальное окружение:
    python -m venv venv
- - - 
### Активируем виртуальное окружение:
    venv\scripts\activate
- - - 
### Устанавливаем все библиотеки 
    pip install -r .\requirements.txt
- - - 
### Запускаем команду создания проекта:
    py -m django startproject online_store
- - - 
### Переходим в директорию проекта:
    cd online_store

Здесь файл manage.py, который является точкой входа для управления проектом.

- - - 
### Также через консоль запустим следующую команду, которая создаст новое приложение news.
    py manage.py startapp core





---
admin
admin500
---










---

-- ОБЩИЕ ТАБЛИЦЫ --

Users: 
| user_id | name | email | password | role (buyer/seller) | created_at |

Products: 
| product_id | seller_id | name | description | price | currency | quantity | category_id | photos | created_at | is_active |

Categories:
| category_id | name | parent_category_id |

ProductPhotos:
| photo_id | product_id | photo_url | is_main |

-- ФИНАНСОВЫЕ ТАБЛИЦЫ --

Accounts: 
| account_id | user_id | balance | currency | created_at |

Transactions: 
| transaction_id | buyer_id | seller_id | order_id | amount | currency | status | created_at |

-- ПОКУПАТЕЛИ --

Orders:
| order_id | buyer_id | total_amount | status | created_at |

OrderItems:
| order_item_id | order_id | product_id | quantity | price_at_time |

Basket:
| basket_item_id | buyer_id | product_id | quantity | added_at |

-- ОТЗЫВЫ И РЕЙТИНГ --

Reviews:
| review_id | product_id | buyer_id | rating (1-5) | comment | created_at |

-- ПРОДАВЦЫ --

SellerProfiles:
| seller_id | user_id | company_name | description | rating | total_sales |







online_store/
│
├── core/                       # Общее ядро
│   ├── models.py              # User, Category
│   └── utils.py               # общие функции
│
├── products/                   # Товары
│   ├── models.py              # Product, ProductPhotos
│   ├── views.py               # каталог, детали товара
│   └── urls.py                # /products/
│
├── finance/                    # Финансы
│   ├── models.py              # Account, Transaction
│   ├── views.py               # баланс, история платежей
│   └── urls.py                # /finance/
│
├── customers/                  # Покупатели
│   ├── models.py              # Order, Basket, OrderItem
│   ├── views.py               # корзина, заказы
│   └── urls.py                # /cart/, /orders/
│
├── reviews/                    # Отзывы и рейтинг
│   ├── models.py              # Review
│   ├── views.py               # отзывы, оценки
│   └── urls.py                # /reviews/
│
├── sellers/                    # Продавцы
│   ├── models.py              # SellerProfile
│   ├── views.py               # управление товарами, статистика
│   └── urls.py                # /seller/
│
└── templates/
    ├── products/
    ├── customers/
    ├── sellers/
    ├── finance/
    └── flatpages/default.html  



Ключевые улучшения:
1. Убрал избыточные таблицы
Buyer и Seller не нужны как отдельные таблицы - достаточно поля role в Users

assess_product объединен с Comments в Reviews

2. Добавил важные поля
status для заказов и транзакций

created_at для временных меток

categories для организации товаров

order_items для истории заказов

3. Улучшил структуру
Отдельная таблица для фотографий товаров

Нормализация цен и валют

История заказов сохраняет цену на момент покупки
