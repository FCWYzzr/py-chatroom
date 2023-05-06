from dataclasses import dataclass
from typing import TypeVar
from socket import socket

__all__ = [
    "IPAddress",
    "Message"
]


IPAddress = TypeVar("IPAddress", bound=str)


@dataclass
class Message:
    index: int
    sender: IPAddress
    content: str

    def encode(self) -> bytes:
        """
        将本信息序列化为可传输的数据包
        """
        index_bytes = self.index.to_bytes(4, byteorder = 'big')
        sender_bytes = socket.inet_aton(self.IPAddress)
        ret_packet = index_bytes + sender_bytes + self.content.encode('utf-8')
        return ret_packet

    @staticmethod
    def decode(raw_message: bytes) -> "Message":
        """
        将数据包反序列化为信息
        """
        raw_index = int.from_bytes(raw_message[:4], byteorder='big')
        raw_sender = socket.inet_ntoa(raw_message[4:8])
        raw_content = raw_message[8:].decode('utf-8')
        return Message(raw_index, raw_sender, raw_content)

    def values(self):
        return (
            self.index,
            repr(self.sender),
            repr(self.content)
        )
