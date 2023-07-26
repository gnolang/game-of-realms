#!/usr/bin/env python3

import requests

repos = [
    'awesome-gno', 
    'gno',
    'gno-by-example',
]

def write_to_file(repo, data, counter):
    f = open('gor_contributors.txt', 'a')

    if counter == 0:
        f.write(f'game of realms contributor list')
        counter += 1

    f.write(f'===============\r{repo}\r===============')
    f.write('\n\n') # formatting
    f.write('\n'.join(data))
    f.write('\n\n') # formatting
    f.close()

def get_contributors(repo, counter):
    url = f'https://api.github.com/repos/gnolang/{repo}/pulls?state=closed&page=1'

    resp = requests.get(url)

    users = []
    users_no_dupes = []

    if resp.status_code == 200:
        data = resp.json()
 
        # pagination
        while 'next' in resp.links.keys():
            resp = requests.get(resp.links['next']['url'])
            data.extend(resp.json())
            users = [item['user']['login'] for item in data]
            users_no_dupes = list(dict.fromkeys(users))
    else:
        print(f"request failed with status code {resp.status_code}")

    # final operation
    write_to_file(repo, users_no_dupes, counter)

if __name__ == '__main__':
    counter = 0
    print(f'[+] collecting GoR contributors across {len(repos)} repos')
    for repo in repos:
        get_contributors(repo, counter)
    print(f'[*] successfully collected GoR contributors')
