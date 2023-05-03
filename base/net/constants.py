from enum import Enum
from socket import gethostname, gethostbyname

__all__ = [
    "Ports"
]


class Ports(Enum):
    """
    客户端/服务端的端口号是魔数，记为枚举常量
    """
    SERVER = 20120
    CLIENT = 20808


class IP(Enum):
    """
    服务端的IP是魔数，记为枚举常量
    """
    SERVER = 20120
    CLIENT = gethostbyname(gethostname())
