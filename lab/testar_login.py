"""Compara as duas versões do login com entradas de teste.

Roda só em memória, no seu computador. Rode: python3 lab/testar_login.py
"""
import app
import app_corrigido

CASOS = [
    ("login legítimo", "maria", "abc12345", True),
    ("senha errada", "maria", "errada", False),
    ("entrada com aspas simples", "maria' --", "qualquer", False),
    ("condição sempre verdadeira", "x", "' OR '1'='1", False),
]


def rodar(nome, modulo):
    print(f"\n=== {nome} ===")
    conn = modulo.criar_banco()
    falhas = 0
    for descricao, usuario, senha, esperado in CASOS:
        try:
            entrou = modulo.login(conn, usuario, senha) is not None
        except Exception as erro:  # a entrada pode quebrar a consulta
            print(f"[ERRO ] {descricao}: {type(erro).__name__}")
            falhas += 1
            continue
        ok = entrou == esperado
        falhas += 0 if ok else 1
        print(f"[{'OK   ' if ok else 'FALHA'}] {descricao}: entrou={entrou} (esperado={esperado})")
    print(f"Resultado: {falhas} problema(s)")
    return falhas


if __name__ == "__main__":
    rodar("app.py (vulnerável)", app)
    rodar("app_corrigido.py", app_corrigido)
