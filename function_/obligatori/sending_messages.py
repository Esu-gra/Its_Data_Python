messages=["Ciao","Bello","mi piaci"]

def show_message():
    for i in messages:
        print (i)
      
show_message()


def send_messages():
    print(show_message())
    send_messages=[]
    for i in messages:
        send_messages.append(i)
    print(send_messages)

send_messages()
