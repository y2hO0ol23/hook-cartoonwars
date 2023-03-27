import frida
import utils

print("[*] Starting to hook")

#TARGET = "com.gamevil.cartoonwars.one.global"
TARGET = "com.gamevil.cartoonwars.two.global"

print("[*] Target : " + TARGET)

try:
    PID = utils.get_pid(TARGET)
except Exception as err:
    print('[!]', err)
    exit(1)

print("[*] Found pid : %d"%PID)

session = frida.get_usb_device().attach(PID)

js_code = "".join(open('./hook.js','r').readlines())
script = session.create_script(js_code)

script.load()
agent = script.exports

print('[*] Hook start!')

G = 0
S = 1

while True:
    try:
        exec(input('> '))
    except frida.InvalidOperationError:
        print('[!] target destroyed.')
        break
    except KeyboardInterrupt as e:
        print()
        break
    except Exception as e:
        print(e)

print('[*] Hook end!')