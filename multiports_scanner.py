import socket

print("=" * 50)
print("      BEM-VINDO AO PORT SCANNER")
print("=" * 50)

host = input("Insira o IP alvo: ")
port_inicial = int(input("Insira a Porta Inicial: "))
port_final = int(input("Insira a Porta Final: "))

print("\nIniciando varredura de portas...")
print(f"Host selecionado: {host}")
print(f"Faixa de portas: {port_inicial} até {port_final}")
print("\nAguarde enquanto o escaneamento é realizado...\n")

# Lista para guardar portas abertas
portas_abertas = []

def check_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((host, port))
        s.close()

        return result == 0

    except socket.error:
        return False


# Escaneando portas
for port in range(port_inicial, port_final + 1):

    if check_port(host, port):
        print(f"[+] Porta {port} aberta")
        portas_abertas.append(port)


# Resultado final
print("\n" + "=" * 50)
print("           RESULTADO FINAL")
print("=" * 50)

if portas_abertas:
    print("Portas abertas encontradas:")
    print(portas_abertas)
else:
    print("Nenhuma porta aberta foi encontrada.")

print("\nEscaneamento finalizado.")