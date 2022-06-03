import subprocess
def get_current_login_user(): # gets the user name of the curren user that is logged in
    import subprocess
    import re
    p1 = subprocess.Popen(["powershell.exe", "whoami"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    who_am_i = p1.communicate()[0]
    user_name = re.split(r'\\r', (re.split(r'.\\\\', str(who_am_i))[1]))[0]
    return user_name
