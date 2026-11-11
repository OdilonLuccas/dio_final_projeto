"""Login de laboratório — versão corrigida.

Mudanças em relação ao app.py:
1. Consulta parametrizada: a entrada da pessoa vira dado, nunca parte do SQL.
2. Senha guardada como hash com salt (scrypt), em vez de texto puro.
3. Comparação em tempo constante e mensagem de erro genérica.
Rode: python3 lab/app_corrigido.py
"""
import hashlib
import hmac
import os
import sqlite3


def gerar_hash(senha, salt):
    return hashlib.scrypt(senha.encode(), salt=salt, n=2**14, r=8, p=1)


def criar_banco():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE usuarios (usuario TEXT, salt BLOB, hash BLOB, perfil TEXT)"
    )
    for usuario, senha, perfil in [
        ("admin", "S3nh@Forte!2026", "administrador"),
        ("maria", "abc12345", "comum"),
    ]:
        salt = os.urandom(16)
        conn.execute(
            "INSERT INTO usuarios VALUES (?, ?, ?, ?)",
            (usuario, salt, gerar_hash(senha, salt), perfil),
        )
    conn.commit()
    return conn


def login(conn, usuario, senha):
    linha = conn.execute(
        "SELECT usuario, salt, hash, perfil FROM usuarios WHERE usuario = ?",
        (usuario,),
    ).fetchone()
    if linha is None:
        return None
    _, salt, hash_guardado, perfil = linha
    if hmac.compare_digest(gerar_hash(senha, salt), hash_guardado):
        return (linha[0], perfil)
    return None


if __name__ == "__main__":
    conn = criar_banco()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    resultado = login(conn, usuario, senha)
    if resultado:
        print(f"Bem-vindo, {resultado[0]} (perfil: {resultado[1]})")
    else:
        print("Usuário ou senha inválidos.")
