import requests

def analyser_headres(cible):

    print("=====================================\n"
                "SECURITY HEADERS\n"
          "=====================================")

    url = f"https://{cible}" if not cible.startswith("http") else cible
    headers_cles = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-XSS-Protection",
        "X-Content-Type-Options",
        "Strict-Transport-Security",
        "Referrer-Policy"
    ]
    #url = f"https://{cible}"
    try:
        response = requests.get(url, timeout=5)
        headers_serveur = response.headers

        for header in headers_cles:
            status = "PRESENT" if header in headers_serveur else "MISSING"
            print((f"{header:<28} : {status}"))
    except Exception:
        try:
            url_http = f"http://{cible}"
            response = requests.get(url_http, timeout=5)
            headers_recus = response.headers
            for header in headers_cles:
                status = "PRESENT" if header in headers_recus else "MISSING"
                print((f"{header:<28} : {status}"))
        except Exception:
            for header in headers_cles:
                print((f"{header:<28} : ERROR"))


