Как я понял - суть задачи посмотреть как я организую код, поэтому я не реализовал так необходимые вещи тут: это валидация данных для handler's и асинхронное выполнение поставленных хэндлерам задач.

```
Сделать простую реализацию механизма sms хендлеров (или предложить свою реализацию).
Оба гейта отвечают в формате json
пример удачного ответа {'status': 'ok', 'phone': '79149009900'}
пример ошибки {'status': 'error', 'phone': '79149009900', 'error_code': ­3500, 'error_msg': 'Невозможно отправить сообщение указанному абоненту'}
Чтобы отправить смску необходимо отправить post запрос в api гейта Пример использования:
#get_handler фабрика, которая возвращает нам желаемый хендлер #handler_name может быть названием класса хендлера
sms_handler = get_handler(handler_name) sms_handler.send(user_data)
1) Реализовать функцию get_handler или предложить свой вариант
2) Сделать два простых хендлера, которые принимают сообщения по следующим адресам:
­ sms­центр http://smsc.ru/some­api/message/ #предположим, что оба эти адреса отвечают нам в формате, описанным выше
­ sms­траффик http://smstraffic.ru/super­api/message/
3) Механизм хендлеров должен иметь какой­то общий интерфейс и быть расширяем, добавление новых sms­гейтов не должно занимать больших усилий
4) Сделать логгирование отправки сообщений, можно хранить в бд (django orm)
```

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
