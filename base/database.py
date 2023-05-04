from sqlite3 import *

from .net import Message

__all__ = [
    "TableName",
    "ColumnNames",
    "ColumnTypes",
    "DatabaseManager"
]

TableName: str = "messages"
ColumnNames: tuple[str, str, str] = (
    "index",
    "sender",
    "content"
)
ColumnTypes: tuple[str, str, str] = (
    "INTEGER",
    "TEXT",
    "TEXT"
)


class DatabaseManagerSingleton:
    __connection: Connection

    def __init__(self):
        raise PermissionError("单例类不允许通过构造函数构造")

    def __new__(cls):
        instance: DatabaseManagerSingleton

        instance = super().__new__(cls)

        instance.__connection = Connection(
            "local_storage.db"
        )

        instance.__initialize()
        return instance

    def __initialize(self):
        cursor = self.__connection.cursor()

        create_table_params = [
            "id INTEGER PRIMARY KEY AUTOINCREMENT"
        ]

        create_table_params.extend(
            f"{col_name} {col_type}"
            for col_name, col_type in
            zip(ColumnNames, ColumnTypes)
        )

        create_table_params = ','.join(create_table_params)

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS "
            f" {TableName} ",
            f"( {create_table_params} )"
        )

        cursor.close()
        self.__connection.commit()

    def insert(self, message: Message) -> None:
        self.__connection.execute(
            f"INSERT INTO TABLE {TableName} " +
            str(ColumnNames) +
            str(message.values())
        )
        self.__connection.commit()

    def query(self, msg_index: int) -> list[tuple[int, str, str]]:
        cur = self.__connection.cursor()

        cur.execute(
            f"SELECT * FROM {TableName} "
            f"WHERE {ColumnNames[0]} = {msg_index}"
        )

        return cur.fetchall()


DatabaseManager = DatabaseManagerSingleton.__new__(DatabaseManagerSingleton)
