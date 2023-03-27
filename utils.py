import os

def get_pid(name):
    list = os.popen('frida-ps -Uai').read().split("\n")
    
    for ele in list:
        if name in ele:
            pid = ""
            while ele[0] == ' ': ele = ele[1:]
            while ele[0] != ' ':
                pid += ele[0]
                ele = ele[1:]
            if pid == "-":
                raise ValueError("Does not active : " + name)
            return int(pid, 10)

    raise ValueError("No process name " + name)

