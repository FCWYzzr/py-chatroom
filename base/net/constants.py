from enum import Enum

__all__ = [
    "Ports"
]


class Ports(Enum):
    """
    客户端/服务端的端口号是魔数，记为枚举常量
    """
    SERVER = 20120
    CLIENT = 20808
