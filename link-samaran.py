import os
import requests

def shortener(link):
    api_url = f"https://tinyurl.com/api-create.php?url={link}"
    try:
        res = requests.get(api_url)
        if res.status_code == 200:
            return res.text
        else:
            return "Gagal memperpendek link."
    except Exception as e:
        return f"Error: {e}"

def main():
    os.system("clear")
    print("=== LINK SAMARAN TOOLS ===")
    original_link = input("Masukkan link asli: ")
    if not original_link.startswith("http"):
        original_link = "https://" + original_link

    print("\nSedang memproses...")
    short_link = shortener(original_link)
    print(f"\nLink samaran: {short_link}")

if __name__ == "__main__":
    main()
