import sqlite3
from pathlib import Path

FILE_NAME = 'database.db'
DIR_NAME = Path(__file__).parent
VESTIMENTA_TABLE_NAME = 'vestimenta_table'
MARCA_TABLE_NAME = 'marca_table'
USO_TABLE_NAME = 'uso_table'
TECIDO_TABLE_NAME = 'tecido_table'
LAVAGEM_TABLE_NAME = 'lavagem_table'
TIPO_VESTIMENTA_TABLE_NAME = 'tipo_vestimenta_table'
TIPO_USO_TABLE_NAME = 'tipo_uso_table'
TIPO_LAVAGEM_TABLE_NAME = 'tipo_lavagem_table'
VESTIMENTA_USO_TABLE_NAME = 'vestimenta_uso_table'
VESTIMENTA_TECIDO_TABLE_NAME = 'vestimenta_tecido_table'
VESTIMENTA_LAVAGEM_TABLE_NAME = 'vestimenta_lavagem_table'
TECIDO_TIPO_LAVAGEM_TABLE_NAME = 'tecido_tipo_lavagem_table'


def create_tables():
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {TIPO_USO_TABLE_NAME}"
        "("
        "id_tipo_uso INTEGER PRIMARY KEY AUTOINCREMENT,"
        "descricao_tipo_uso TEXT,"
        "data_inclusao TEXT"
        ")"
    )

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {TIPO_VESTIMENTA_TABLE_NAME}"
        "("
        "id_tipo_vestimenta INTEGER PRIMARY KEY AUTOINCREMENT,"
        "nome_tipo_vestimenta TEXT,"
        "quantidade_tipo_vestimenta INTEGER"
        ")"
    )

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {TIPO_LAVAGEM_TABLE_NAME}"
        "("
        "id_tipo_lavagem INTEGER PRIMARY KEY AUTOINCREMENT,"
        "descricao_tipo_lavagem TEXT,"
        "data_inclusao INTEGER"
        ")"
    )

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {TECIDO_TABLE_NAME}"
        "("
        "id_tecido INTEGER PRIMARY KEY AUTOINCREMENT,"
        "nome_tecido TEXT,"
        "descricao_tecido TEXT,"
        "data_inclusao TEXT"
        ")"
    )

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {MARCA_TABLE_NAME}"
        "("
        "id_marca INTEGER PRIMARY KEY AUTOINCREMENT,"
        "nome_marca TEXT,"
        "data_inclusao TEXT"
        ")"
    )

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {USO_TABLE_NAME}"
        "("
        "id_uso INTEGER PRIMARY KEY AUTOINCREMENT,"
        "data_uso TEXT,"
        "id_tipo_uso INTEGER,"
        f"FOREIGN KEY(id_tipo_uso) REFERENCES {TIPO_USO_TABLE_NAME}(id_tipo_uso)"
        ")"
    )

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {LAVAGEM_TABLE_NAME}"
        "("
        "id_lavagem INTEGER PRIMARY KEY AUTOINCREMENT,"
        "data_lavagem TEXT,"
        "id_tipo_lavagem INTEGER,"
        f"FOREIGN KEY(id_tipo_lavagem) REFERENCES {TIPO_LAVAGEM_TABLE_NAME}(id_tipo_lavagem)"
        ")"
    )

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {VESTIMENTA_TABLE_NAME}"
        "("
        "id_vestimenta INTEGER PRIMARY KEY AUTOINCREMENT,"
        "cor TEXT,"
        "data_aquisicao TEXT,"
        "indicador_vestimenta_em_uso NUMERIC,"
        "id_tipo_vestimenta INTEGER,"
        "id_marca INTEGER,"
        f"FOREIGN KEY(id_tipo_vestimenta) REFERENCES {TIPO_VESTIMENTA_TABLE_NAME}(id_tipo_vestimenta),"
        f"FOREIGN KEY(id_marca) REFERENCES {MARCA_TABLE_NAME}(id_marca)"
        ")"
    )

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {VESTIMENTA_USO_TABLE_NAME}"
        "("
        "id_uso INTEGER,"
        "id_vestimenta INTEGER,"
        "PRIMARY KEY(id_uso, id_vestimenta)"
        f"FOREIGN KEY(id_uso) REFERENCES {USO_TABLE_NAME}(id_uso),"
        f"FOREIGN KEY(id_vestimenta) REFERENCES {VESTIMENTA_TABLE_NAME}(id_vestimenta)"
        ")"
    )

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {VESTIMENTA_TECIDO_TABLE_NAME}"
        "("
        "id_tecido INTEGER,"
        "id_vestimenta INTEGER,"
        "PRIMARY KEY(id_tecido, id_vestimenta)"
        f"FOREIGN KEY(id_tecido) REFERENCES {TECIDO_TABLE_NAME}(id_tecido),"
        f"FOREIGN KEY(id_vestimenta) REFERENCES {VESTIMENTA_TABLE_NAME}(id_vestimenta)"
        ")"
    )

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {VESTIMENTA_LAVAGEM_TABLE_NAME}"
        "("
        "id_lavagem INTEGER,"
        "id_vestimenta INTEGER,"
        "PRIMARY KEY(id_lavagem, id_vestimenta)"
        f"FOREIGN KEY(id_lavagem) REFERENCES {LAVAGEM_TABLE_NAME}(id_lavagem),"
        f"FOREIGN KEY(id_vestimenta) REFERENCES {VESTIMENTA_TABLE_NAME}(id_vestimenta)"
        ")"
    )

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {TECIDO_TIPO_LAVAGEM_TABLE_NAME}"
        "("
        "id_tecido INTEGER,"
        "id_tipo_lavagem INTEGER,"
        "PRIMARY KEY(id_tecido, id_tipo_lavagem)"
        f"FOREIGN KEY(id_tecido) REFERENCES {TECIDO_TABLE_NAME}(id_tecido),"
        f"FOREIGN KEY(id_tipo_lavagem) REFERENCES {TIPO_LAVAGEM_TABLE_NAME}(id_tipo_lavagem)"
        ")"
    )
    cursor.close()
    conn.close()


create_tables()

