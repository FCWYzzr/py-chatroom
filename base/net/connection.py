from socket import socket, timeout
from constants import IP, Ports

from .constants import (
    IP, 
    Ports
    )

__all__ = [
    "Connection"
]

from typing import Optional

from .message import Message


class Connection:
    """
    socket用于实际的通讯
    """
    socket: socket

    def __init__(self):
        """
        不允许直接通过构造函数构造，
        必须使用open_client 或者 open_server
        """
        raise PermissionError("不允许直接通过构造函数构造")

    @classmethod
    def open_client(cls) -> "Connection":
        """
        构造一个客户端连接实例，
        :return: 新的Connection实例
        """
        connect_instance = object.__new__(cls)

        connect_instance.socket.bind((IP.CLIENT, Ports.CLIENT.value))
        connect_instance.socket.connect((IP.SERVER, Ports.SERVER.value))
        # 设置非阻塞
        connect_instance.socket.settimeout(0)

        return connect_instance

    @classmethod
    def open_from_server(cls, server_end: socket) -> "Connection":
        """
        利用服务器套接字连接所产生的服务端通讯套接字
        构造一个服务端连接实例，
        :return: 新的Connection实例
        """
        connect_instance = object.__new__(cls)

        return connect_instance

    def send_message(self, message: Message) -> None:
        self.socket.send(
            message.encode()
        )

    def read_message(self) -> Optional[Message]:
        try:
            raw_msg = self.socket.recv(1024)
            return Message.decode(raw_msg)
        except timeout:
            return None
