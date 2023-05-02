from socket import socket

__all__ = [
    "Connection"
]

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

        # todo 实现客户端连接实例

        return connect_instance

    @classmethod
    def open_from_server(cls, server_end: socket) -> "Connection":
        """
        利用服务器套接字连接所产生的服务端通讯套接字
        构造一个服务端连接实例，
        :return: 新的Connection实例
        """
        connect_instance = object.__new__(cls)

        connect_instance.socket = server_end

        return connect_instance

    def send_message(self, message: Message) -> None:
        self.socket.send(
            message.encode()
        )
