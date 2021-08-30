def show_message(msgs):
    for msg in msgs:
        print(msg)

msgs = ['lalala', 'lalala1', 'lala']
show_message(msgs)

# 8-10, 8-11
sent_messages = []
mms = msgs[:]
def send_messages(send, sents):
    while send:
        mmsg = send.pop()
        print(mmsg)
        sents.append(mmsg)

send_messages(mms, sent_messages)
print(f"original archive msgs list: {msgs}")
print(f"original copied msgs list popped in the function: {mms}")
print(f"sent message list: {sent_messages}")



