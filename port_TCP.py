import socket
import sys
def verfication_port(cible, portlists=[22,80,443,8080,8443,3307,21,53]):
    port_ouvert = []
    try:
        print("==========================\n"
                    " PORTS \n"
            "===============================")
        for port in portlists:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((cible, port))
            if result == 0:
                print("Port {} \t :OPEN".format(port))
                port_ouvert.append(port)
            else:
                print("Port {} \t :CLOSED".format(port))
            sock.close()
    except socket.error:
        print("Erreur de connexion")
        sys.exit()
    return port_ouvert