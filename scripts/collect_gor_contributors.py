#!/usr/bin/python3

import requests
import json

repos = [
    'awesome-gno', 
    'gno',
    'gno-by-example',
]

def write_to_file(repo,data):
    f = open('gor_contributors.txt', 'a')
    f.write(repo)
    f.write('\n\n') # formatting
    f.write('\n'.join(data))
    f.write('\n\n') # formatting
    f.close()

def get_contributors(repo):
    url = f'https://api.github.com/repos/gnolang/{repo}/pulls?state=closed'

    resp = requests.get(url)

    # Ensure the request was successful
    if resp.status_code == 200:
        data = resp.json()
        users = [item['user']['login'] for item in data]
        users_no_dupes = list(dict.fromkeys(users))
        write_to_file(repo,users_no_dupes)
    else:
        print(f"request failed with status code {resp.status_code}")

if __name__ == '__main__':
    print(f'[+] looping through {len(repos)} repos')
    for repo in repos:
        get_contributors(repo)
    print('[*] successfully fetched GoR contributors')
