import subprocess
import re
desired_computer_name = ""
def get_current_login_user(): # gets the user name of the curren user that is logged in
    p1 = subprocess.Popen(["powershell.exe", "whoami"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    who_am_i = p1.communicate()[0]
    user_name = re.split(r'\\r', (re.split(r'.\\\\', str(who_am_i))[1]))[0]
    print(f'{user_name} is currently logged in')

def find_office_language_pack():
    return

def rename_computer():
    return


get_current_login_user() #testing get_current_login_user function is working.
