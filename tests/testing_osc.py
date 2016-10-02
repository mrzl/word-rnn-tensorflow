import OSC
import threading

receive_address = ('localhost', 12001)
send_address = 'localhost', 12000

server = OSC.OSCServer(receive_address)
client = OSC.OSCClient()
client.connect(send_address)

server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()


def received(addr, tags, stuff, source):
    print(addr)

server.addMsgHandler('/get', received)

while True:
    input = raw_input('tell me: ')
    msg = OSC.OSCMessage('/get')
    msg.append(input)
    msg.append('233546')
    client.send(msg)