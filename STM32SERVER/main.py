# This Python file uses the following encoding: utf-8
# TCP server for data exchange between PC and microcontroller
# www.golenischev-electronics.ru

import socket
import time


if __name__ == "__main__":

    # открытие сокета, тип TCP (SOCK_STREAM)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # задание прослушиваемого порта сервера
    sock.bind(('', 10000))
    # прослушивание входящих соединений, максимум 1
    sock.listen(1)
    n = 1
    # бесконечный цикл
    while 1:
    # задание тайм-аута
        sock.settimeout(2)
    # конструкция try: ... except: для обработки исключений
        try:
    # приём входящего подключения
            conn, addr = sock.accept()
    # получение данных от клиента
            data = conn.recv(1024)
    # если не получены данные - закрытие соединения
            if not data:
                  conn.close()
                  break
            print (data)
    # конструкция для формирования ответа
            if n%2 == 1:
                   temp = "1"
            else:
                   temp = "0"
    # перевод данных для отправки в тип bytes
            data_send = temp.encode()
            print("Sending:",data_send)
    # передача данных клиенту
            conn.send(data_send)
    # закрытие соединения
            conn.close()
            n += 1
        except socket.timeout:
            print("Socket timeout")
    # закрытие сокета
    sock.close()

