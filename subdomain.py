import requests
import sys
#a simple python code to get subdomains of a domain by scanning it
def getting_subdomains(domain):
    all_subdomain = []

    url = "https://crt.sh/?q=" + domain
    req = requests.get(url)
    if req.status_code == 200:
        data = req.text
        lines = data.split("<TD>")
        for line in lines:
            if domain + "</TD>" in line:
                line = line.replace("</TD", "")
                line = line.replace("\n" , "")
                if "<BR>" in line:
                    ff = line.split("<BR>")
                    for i in ff:
                        if i not in all_subdomain:
                            all_subdomain.append(i)
        for subdomain in all_subdomain:
            print(subdomain)

if __name__ == "__main__":
    domain = sys.argv[1]
    getting_subdomains(domain)
        
