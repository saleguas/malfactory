#!/usr/bin/python3

import subprocess
import platform

had_error = False
red = '\033[31m'
green = '\033[92m'
rr = '\033[0m'  # reset
bold = '\033[01m'
p = platform.system()


def get_current_dir():
    save_location = str(subprocess.check_output(["pwd"]))
    # save directory to txt file in the simple-scan folder
    # delete this folder later in uninstaller.py
    folder = save_location.split("/")
    folder.remove("b'")  # this is needed to remove the first element in the list
    folder[len(folder) - 1] = folder[len(folder) - 1].split("\\")[0]  # removes the \n in the last element
    result = ""
    for i in folder:
        result += "/" + i
    return result


def save_folder_location(location, save_to_app_folder=True):
    # save to same directory location.txt for uninstaller and update files
    c = 0
    try:
        file1 = open(location + "/location.txt", "w")
        file1.write(location)
        file1.close()
        c += 1

        # save to app folder so main.py can locate the installation folder after getting separated
        if save_to_app_folder:
            file2 = open(location + "/mal-factory/location.txt", "w")
            file2.write(location)
            file2.close()
            c += 1

        print(green + "[+] location.txt created: " + str(c) + rr)

    except:
        print(red + bold + "[!] Error writing to file location.txt" + rr)
        had_error = True
        raise


try:
    # add modules u use here

    # subprocess.call("pip3 install curses",shell=True)
    # subprocess.call("pip3 install playsound, shell=True")

    # save location before file burst
    current_dir = get_current_dir()
    print(green + "[+] Detected location: \t" + current_dir + rr)
    save_folder_location(current_dir)
    subprocess.call("chmod 755 -R *", shell=True)

    if p == "Linux":
        subprocess.call("sudo mv mal-factory /usr/share", shell=True)  # folder
        print("[+] moved mal-factory folder to /usr/share")

        subprocess.call("sudo mv malfactory.desktop /usr/share/applications/", shell=True)  # .desktop file
        print("[+] moved desktop to /usr/share/applications")

        subprocess.call("sudo mv malfactory /usr/bin", shell=True)  # bash file
        print("[+] moved bash file to /usr/bin")
    else:
        subprocess.call("sudo mv mal-factory ~/Documents", shell=True)  # folder
        print("[+] moved mal-factory folder to ~/Documents")


except:
    had_error = True
    raise
finally:
    if had_error:
        print(red + bold + "[-] Setup Failed, an error stopped the setup process " + rr)
    else:
        print(green + bold + "[+] Setup is complete, no errors!" + rr)
