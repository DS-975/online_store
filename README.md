

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

BuyerProfiles

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
│   ├── models.py              # Users, Categories
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


- - -


models - core настройка 







- - -
- - -
- - - 
## GIT
    
### Перейти на другую ветку
- - -
## 1. Переключиться на существующую ветку
### Посмотреть все ветки
    git branch -a
### Переключиться на другую ветку
    git checkout имя_ветки
### Или (более современный способ)
    git switch имя_ветки

- - -

## 2. Создать и перейти на новую ветку
### Создать новую ветку и перейти на неё
    `git checkout -b` новая_ветка
### Или
    git switch -c новая_ветка

- - -

## 3. Добавить изменения и сделать коммит
### Добавить все изменения
    git add .
### Или добавить конкретные файлы
    git add имя_файла.py
### Сделать коммит
    git commit -m "Описание изменений"

- - -

## 4. Запушить ветку в GitHub
### Первый пуш новой ветки:
#### Установить upstream и запушить
    git push -u origin имя_ветки
#### Последующие пуши (после установки upstream):
    git push

- - -

## 5. Полный рабочий процесс
### 1. Проверить текущую ветку
    git status
    git branch
### 2. Перейти на нужную ветку или создать новую
    git checkout existing_branch
### или
    git checkout -b new_feature_branch
### 3. Внести изменения в код
### ... работа с файлами ...
### 4. Добавить изменения в staging area
    git add .
### 5. Сделать коммит
    git commit -m "Добавлена новая функциональность"
### 6. Запушить в GitHub
    git push -u origin new_feature_branch  # для новой ветки
### или
    git push                               # для существующей ветки

- - -

## 6. Полезные команды для работы с ветками
### Посмотреть разницу между ветками
    git diff main..имя_ветки
### Обновить локальную ветку с GitHub
    git pull origin имя_ветки
### Удалить локальную ветку
    git branch -d имя_ветки
### Удалить ветку на GitHub
    git push origin --delete имя_ветки

- - -

## 7. Пример реального сценария
### Создаем новую ветку для фичи
    git checkout -b feature/user-authentication
### Работаем над кодом...
### Добавляем файлы
    git add .
### Коммитим изменения
    git commit -m "Добавлена аутентификация пользователя"
### Пушим в GitHub (первый раз)
    git push -u origin feature/user-authentication
### Продолжаем работать... делаем еще изменения
    git add .
    git commit -m "Добавлена валидация пароля"
    git push  # уже без -u, так как upstream установлен

- - -

## 8. Если ветка уже существует на GitHub
### Получить все ветки с сервера
    git fetch --all
### Переключиться на существующую ветку
    git checkout имя_ветки
### Обновить локальную ветку
    git pull origin имя_ветки

- - -

## 9. Настройка upstream для существующей ветки
### Если upstream не установлен
    git branch --set-upstream-to=origin/имя_ветки имя_ветки

Важные моменты:
Всегда делайте git pull перед началом работы, чтобы получить свежие изменения

Используйте понятные имена веток: feature/название, bugfix/описание, hotfix/срочное-исправление

Первый push требует флаг -u для установки upstream

Последующие push можно делать просто git push
- - - 

## Merge (слияние) - рекомендуется
### 1. Переключитесь на ветку master
    git checkout master
### 2. Получите последние изменения
    git pull origin master
### 3. Выполните слияние
    git merge ds
### Если есть конфликты, разрешите их
#### Редактируйте файлы с конфликтами, затем:
    git add .
    git commit -m "Разрешение конфликтов при слиянии ds в master"
### 5. Отправьте изменения в удаленный репозиторий
    git push origin master