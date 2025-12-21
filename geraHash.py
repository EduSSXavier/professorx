import hashlib

def gerar_sha256(texto):
    # Codifica a string para bytes (SHA-256 trabalha com bytes)
    texto_bytes = texto.encode('utf-8')
    
    # Cria o objeto hash SHA-256
    sha256_hash = hashlib.sha256()
    
    # Atualiza o hash com os bytes da string
    sha256_hash.update(texto_bytes)
    
    # Retorna o hash em hexadecimal
    return sha256_hash.hexdigest()

def main():
    print("=== Gerador de Hash SHA-256 ===\n")
    
    # Solicita a string do usuário
    entrada = input("Digite a string que deseja transformar em hash SHA-256: ")
    
    # Gera o hash
    hash_resultado = gerar_sha256(entrada)
    
    # Exibe o resultado
    print("\nString original:", entrada)
    print("Hash SHA-256:   ", hash_resultado)

# Executa o programa
if __name__ == "__main__":
    main()