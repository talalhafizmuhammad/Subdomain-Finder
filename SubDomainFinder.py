import requests
import sys

def fetch_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        res = requests.get(url, timeout=15)
        res.raise_for_status()
        data = res.json()
        subdomains = {sub.strip()
                      for entry in data
                      for sub in entry.get('name_value', '').split('\n')
                      if domain in sub}
        return sorted(subdomains)
    except Exception as e:
        print(f"[!] Error: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python subfinder.py <domain>")
        sys.exit(1)

    domain = sys.argv[1].replace("http://", "").replace("https://", "").strip("/")
    subs = fetch_subdomains(domain)

    if subs:
        print(f"\n[+] Subdomains for {domain}:\n")
        print("\n".join(subs))
    else:
        print("[!] No subdomains found.")
