import clickhouse_connect

if __name__ == '__main__':
    client = clickhouse_connect.get_client(
        host='k0tbyqcfqb.germanywestcentral.azure.clickhouse.cloud',
        user='default',
        password='password',
        secure=True
    )
    print("Result:", client.query("SELECT 1").result_set[0][0])

    # Первые 5 строк
    result = client.query("SELECT * FROM books_data LIMIT 5")
    for row in result.result_set:
        print(row)

    # товары дороже 20
    result = client.query("SELECT title, price FROM books_data WHERE price > 20")
    print("Товары дороже 20:")
    for row in result.result_set:
        print(row)

    # Топ-5
    result = client.query("""
            SELECT title, price
            FROM books_data
            ORDER BY price DESC
            LIMIT 5
        """)
    print("Топ-5 самых дорогих товаров:")
    for row in result.result_set:
        print(row)

# Товары с названием, начинающимся на 'Book'
result = client.query("""
    SELECT title, price
    FROM books_data
    WHERE title LIKE 'Book%'
    """)
print("Товары с названием, начинающимся на 'Book':")
for row in result.result_set:
    print(row)
