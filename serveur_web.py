import requests
def http_web(cible, port_ouvert):
   code  = None

   for port in port_ouvert:
       url = "http://" + cible + ":" + str(port) + "/"
       headers = {"User-Agent": "AWA-Network-Auditor/1.0"}
       print("URL : ",url)
       print("Cible Suivante : ",cible)

       try:
            print("==========================\n"
                        "WEB SERVER\n"
                  "============================")
            response = requests.get(url , headers=headers ,timeout=5)
            url = response.url
            code = response.status_code
            content = response.content.decode('utf-8')
            serveur = response.headers.get("server")
            temps = round(response.elapsed.total_seconds(),2)
            url_final = response.url
            print("URL : ",url)
            print("Code : ",code)
            #print("Content : ",content)
            print("Serveur : ",serveur)
            print("Response time : ",temps)
            print("URL_final : ",url_final)
            print("\n")
            #save_raport(cible,port_ouvert,code,serveur,url,content)
       except requests.exceptions.RequestException :
            print("Erreur de d'une requête HTTP\n")
            print("\n")