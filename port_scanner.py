import socket

print("=" * 50)
print("         VERIFICADOR DE PORTAS")
print("=" * 50)

host = input("Insira o IP alvo: ")
port = int(input("Insira a Porta para verificar: "))

print("\nIniciando verificação da porta...")
print(f"Host selecionado: {host}")
print(f"Porta analisada: {port}")
print("Aguarde...\n")

def check_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # timeout de 2 segundos
        result = s.connect_ex((host, port))
        s.close()

        if result == 0:
            return True  # porta aberta
        else:
            return False  # porta fechada

    except socket.error:
        return False  # erro de conexão


# Testando
print("=" * 50)

if check_port(host, port):
    print(f"[+] Resultado: Porta {port} está ABERTA em {host}")
else:
    print(f"[-] Resultado: Porta {port} está FECHADA em {host}")

print("=" * 50)
print("Verificação finalizada.")