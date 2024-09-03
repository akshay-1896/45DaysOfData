import socket
from datetime import datetime
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# target_ip = "192.168.1.70"  # connected with multiple persons
target_ip = "127.0.0.1"  # connected with single person
port_no = 2525
target_address = (target_ip,port_no)

# condition = True
# while condition:

while True:
    message = input("Write your message : ")
    live_datetime = datetime.now()
    msg = f'{message} | ({live_datetime})'
    encrypt_message = msg.encode('ascii')
    s.sendto(encrypt_message, target_address)
    
    if message == 'by':
        print("Chat ended!!")
        # with open(target_ip +'.txt', 'a+') as file:
        #     file.write(f"Akshay : {decrypted_reply}\n\n")
        break
    
    reply = s.recvfrom(100)
    # print(f"\n{reply}\n")
    # reply = (b'Hare Krishna', ('127.0.0.1', 57151))
    received_reply = reply[0]
    decrypted_reply = received_reply.decode('ascii')
    print(f"\nAkshay : {decrypted_reply}\n")
    
    with open(target_ip +'.txt', 'a+') as file:
        file.write(f"Akshay : {decrypted_reply}\n\n")
        file.close()

# reply = s.recvfrom(100)
# # print(f"\n{reply}\n")
# # reply = (b'Hare Krishna', ('127.0.0.1', 57151))
# received_reply = reply[0]
# decrypted_reply = received_reply.decode('ascii')
# print(f"\nAkshay : {decrypted_reply}\n")

# with open(target_ip +'.txt', 'a+') as file:
#     file.write(f"Akshay : {decrypted_reply}\n\n")
    
    














































