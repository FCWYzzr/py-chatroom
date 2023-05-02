from sqlite3 import *

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

        instance = object.__new__(cls)

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
            f"{col_name, col_type}"
            for col_name, col_type in
            zip(ColumnNames, ColumnTypes)
        )

        create_table_params = ','.join(create_table_params)

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS "
            f" {TableName} ",
            f"( {create_table_params} )"
        )
