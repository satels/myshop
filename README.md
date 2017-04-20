Как я понял - суть задачи посмотреть как я организую код, поэтому я не реализовал так необходимые вещи тут: это валидация данных для handler's и асинхронное выполнение поставленных хэндлерам задач

# myshop:

   Url: http://yourlocalmachine:8020/complete/

# Сборка:

    time docker build -t myshop .

# Запуск сервера:

    cp local.example.yml local.yml

    docker-compose up runserver

# Запуск тестов:

    cp local.example.yml local.yml

    docker-compose up runtests
