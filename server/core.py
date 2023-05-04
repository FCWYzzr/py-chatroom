from socket import socket
from threading import Thread
from typing import NoReturn

from base import Message, IP, Ports, \
    IPAddress, Connection


class Server:
    __hub: socket
    __clients: dict[IPAddress, Connection]

    def __init__(self):
        skt = socket()

        # 绑定到IP和Port
        skt.bind((
            IP.SERVER,
            Ports.SERVER
        ))

        # 设定最大监听为5
        skt.listen(5)

        self.__hub = skt

    def launch(self):
        # 启用守护线程
        Thread(
            target=self.handle_connect_request,
            daemon=True
        ).start()

    def handle_connect_request(self) -> NoReturn:
        """
        守护线程任务： 处理连接请求
        """
        while True:
            skt, address = self.__hub.accept()

            self.__clients[address] = Connection.open_from_server(skt)

    def handle_new_message(self) -> NoReturn:
        """
        守护线程任务： 处理新消息
        """
        while True:
            client: Connection
            msg: Message

            for client in self.__clients.values():
                msg = client.read_message()
                if msg is not None:
                    self.proceed_message(msg)

    def proceed_message(self, msg: Message) -> None:
        # todo 实现新消息处理流程
        pass
