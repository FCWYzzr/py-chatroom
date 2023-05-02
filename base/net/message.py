from dataclasses import dataclass
from typing import TypeVar

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
        # todo 实现encode

    @staticmethod
    def decode(raw_message: bytes) -> "Message":
        """
        将数据包反序列化为信息
        """
        # todo 实现decode


