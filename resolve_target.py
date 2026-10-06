import socket

def resolve_targe(cible):
    print("=========== DNS =========")
    try:
        ip = socket.gethostbyname(cible)
        print("Domaine : ", cible)
        print("Adress IP : ", ip)
        print("=========================")
    except socket.gaierror:
        print("[!] Imossible de résoudre le domaine")