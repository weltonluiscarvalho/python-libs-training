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

def insert_tecido_tipo_lavagem(id_tecido, id_tipo_lavagem):
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {TECIDO_TIPO_LAVAGEM_TABLE_NAME}(id_tecido, id_tipo_lavagem) "
        f"VALUES({id_tecido}, {id_tipo_lavagem})"
    )
    conn.commit()

    cursor.close()
    conn.close()

def insert_vestimenta_lavagem(id_vestimenta, id_lavagem):
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {VESTIMENTA_LAVAGEM_TABLE_NAME}(id_vestimenta, id_lavagem) "
        f"VALUES({id_vestimenta}, {id_lavagem})"
    )
    conn.commit()

    cursor.close()
    conn.close()

def insert_vestimenta_tecido(id_vestimenta, id_tecido):
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {VESTIMENTA_TECIDO_TABLE_NAME}(id_vestimenta, id_tecido) "
        f"VALUES({id_vestimenta}, {id_tecido})"
    )
    conn.commit()

    cursor.close()
    conn.close()

def insert_vestimenta_uso(id_uso, id_vestimenta):
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {VESTIMENTA_USO_TABLE_NAME}(id_uso, id_vestimenta) "
        f"VALUES({id_uso}, {id_vestimenta})"
    )
    conn.commit()

    cursor.close()
    conn.close()

def insert_vestimenta(cor, data_aquisicao, indicador_vestimenta_em_uso, id_tipo_vestimenta, id_marca):
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {VESTIMENTA_TABLE_NAME}(cor, data_aquisicao, indicador_vestimenta_em_uso, id_tipo_vestimenta, id_marca) "
        f"VALUES('{cor}', '{data_aquisicao}', {indicador_vestimenta_em_uso}, {id_tipo_vestimenta}, {id_marca})"
    )
    conn.commit()

    cursor.close()
    conn.close()

def insert_uso(data_uso, id_tipo_uso):
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {USO_TABLE_NAME}(data_uso, id_tipo_uso) "
        f"VALUES('{data_uso}', {id_tipo_uso})"
    )
    conn.commit()

    cursor.close()
    conn.close()

def insert_lavagem(data_lavagem, id_tipo_lavagem):
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {LAVAGEM_TABLE_NAME}(data_lavagem, id_tipo_lavagem) "
        f"VALUES('{data_lavagem}', {id_tipo_lavagem})"
    )
    conn.commit()

    cursor.close()
    conn.close()

def insert_tecido(nome_tecido, descricao_tecido, data_inclusao):
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {TECIDO_TABLE_NAME}(nome_tecido, descricao_tecido, data_inclusao) "
        f"VALUES('{nome_tecido}', '{descricao_tecido}', '{data_inclusao}')"
    )
    conn.commit()

    cursor.close()
    conn.close()

def insert_tipo_vestimenta(nome_tipo_vestimenta, quantidade_tipo_vestimenta):
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {TIPO_VESTIMENTA_TABLE_NAME}(nome_tipo_vestimenta, quantidade_tipo_vestimenta) "
        f"VALUES('{nome_tipo_vestimenta}', {quantidade_tipo_vestimenta})"
    )
    conn.commit()

    cursor.close()
    conn.close()

def insert_tipo_lavagem(descricao, data_inclusao):
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {TIPO_LAVAGEM_TABLE_NAME}(descricao_tipo_lavagem, data_inclusao) VALUES('{descricao}', '{data_inclusao}')"
    )
    conn.commit()

    cursor.close()
    conn.close()

def insert_marca(nome, data):
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {MARCA_TABLE_NAME}(nome_marca, data_inclusao) VALUES('{nome}', '{data}')"
    )
    conn.commit()

    cursor.close()
    conn.close()

def insert_tipo_uso(descricao, data):
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO {TIPO_USO_TABLE_NAME}(descricao_tipo_uso, data_inclusao) VALUES('{descricao}', '{data}')"
    )
    conn.commit()

    cursor.close()
    conn.close()

def list_tipo_uso():
    conn = sqlite3.connect(DIR_NAME / FILE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        f"SELECT * FROM {TIPO_USO_TABLE_NAME}"
    )

    resultado = cursor.fetchall()
    print(resultado)
    conn.commit()

    cursor.close()
    conn.close()

    return resultado



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
# insert_marca("adidas", "02/08/2025")
# insert_tipo_uso("Dormir", "02/08/2025")
# insert_tipo_lavagem("Na Maquina", "02/08/2025")
# insert_tipo_vestimenta("Camisa", 5)
# insert_tecido("Algodao", "Tecido firme e de facil lavagem", "03/08/2025")
# insert_lavagem("03/08/2025", 1)
# insert_uso("03/08/2025", 1)
# insert_vestimenta("preto", "03/08/2025", 1, 1, 1)
# insert_vestimenta_uso(1, 2)
# insert_vestimenta_tecido(1, 1)
# insert_vestimenta_lavagem(1, 1)
# insert_tecido_tipo_lavagem(1, 1)
