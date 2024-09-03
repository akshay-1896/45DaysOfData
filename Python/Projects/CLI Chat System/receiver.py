from datetime import datetime
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ip_address = "192.168.1.73"  # connected with multiple persons
ip_address = "127.0.0.1" #single person
port_no = 2525  # 0 - 65353 where 0 - 1023 reserved for TCP/IP Protocols

complete_address = (ip_address, port_no)

s.bind(complete_address)

print("Hey I am receiving your messages!!")
#cryptography dealing with encryption
count = 0
while True:
    count += 1
    message = s.recvfrom(100)  # buffer size == 100 characters
    # message = (b'Hare Krishna', ('127.0.0.1', 57151))
    # print(f"\n{message}\n")
    # print(type(message))
    sender_address = message[1][0]
    received_message = message[0]

    target_ip = message[1][0]
    target_port = message[1][1]
    target_address = (target_ip,target_port)
    
    decrypted_message = received_message.decode('ascii')
    print(f"\nShubham : {decrypted_message}\n")
    
    r_message = input("Write your message : ")
    live_datetime = datetime.now()
    reply = f'{r_message} | ({live_datetime})'
    reply_message = reply.encode('ascii')
    s.sendto(reply_message, target_address)

    if r_message == 'by':
        print("Chat ended!!")
        # with open(sender_address +'.txt', 'a+') as file:
        #     file.write(f"Shubham : {decrypted_message}\n\n")
        break
    
    if count == 1:
        print(f"count = {count}")
        with open(sender_address +'.txt', 'a') as file:
            file.write(f"Shubham : {decrypted_message}\n\n")
            file.close()
    else: 
        print(f"count = {count}")
        with open(sender_address +'.txt', 'a+') as file:
            file.write(f"Shubham : {decrypted_message}\n\n")
            file.close()
        
        
        
    
        

# --------------- send message from receiver side -----------------
# --------------- add date and time with current message ----------
# --------------- explore and create more features as in Ranjit sir github --------
