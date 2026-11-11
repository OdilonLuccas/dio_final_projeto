"""Login de laboratório — PROPOSITALMENTE VULNERÁVEL.

Use só em ambiente de estudo, na sua máquina. Não publique este código em produção.
Rode: python3 lab/app.py
"""
import sqlite3


def criar_banco():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE usuarios (usuario TEXT, senha TEXT, perfil TEXT)")
    conn.execute("INSERT INTO usuarios VALUES ('admin', 'S3nh@Forte!2026', 'administrador')")
    conn.execute("INSERT INTO usuarios VALUES ('maria', 'abc12345', 'comum')")
    conn.commit()
    return conn


def login(conn, usuario, senha):
    # A consulta é montada juntando o texto que a pessoa digitou.
    consulta = (
        "SELECT usuario, perfil FROM usuarios "
        "WHERE usuario = '" + usuario + "' AND senha = '" + senha + "'"
    )
    return conn.execute(consulta).fetchone()


if __name__ == "__main__":
    conn = criar_banco()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    resultado = login(conn, usuario, senha)
    if resultado:
        print(f"Bem-vindo, {resultado[0]} (perfil: {resultado[1]})")
    else:
        print("Usuário ou senha inválidos.")
