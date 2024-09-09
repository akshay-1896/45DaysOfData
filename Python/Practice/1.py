# st="hello @Welcome @to @upflairs."
#length
#print(st.replace("Welcome", "Come"))
# print(st.replace("upflairs", "Google"))
# print(st.capitalize())

# st1="Hello"
# st2="World"
# print(st1+st2)

# print(st.split(" "))
# print(st.split("@"))
# print(st.split(" @"))

# st3="    Hello"
# print(st3.strip())
# print(st.endswith("upflairs."))

#LIST

# ls = [2,3,4.5,"Hello", True, [2,4]]
# print(ls[-1])
# print(type(ls[-1]))
# a = ls[-1]
# print(a[1])

# 5 Write a Python program that calls an external command with different text color and style

import subprocess
from colorama import Fore,Style,init

init()

command = ["cmd","/c","dir"]

try:
    result = subprocess.run(command, capture_output=True, text = True, check= True)
    output = result.stdout.splitlines()
    print("Command Ouput: ")
    for line in output:
        if "Directory of" in line:
            print(Fore.LIGHTGREEN_EX + line + Style.RESET_ALL)
        elif "<DIR>" in line:
            print(Fore.MAGENTA + line + Style.RESET_ALL)
        else:
            print(Fore.WHITE + line + Style.RESET_ALL)
        
except subprocess.CalledProcessError as e:
    print(f"Error while running the command: {e}")














