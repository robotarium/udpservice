import asyncio
import socket
import struct
import json
import udpserver
import argparse
import messages

global ap_channel
ap_channel = 0

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("udp_ports", help="UDP port config file")
    parser.add_argument("host", help="UDP port config file")
    parser.add_argument("udp_port", help="UDP port config file")
    parser.add_argument("ssid", help="UDP port config file")
    parser.add_argument("passkey", help="UDP port config file")

    args = parser.parse_args()

    #host=socket.gethostbyname(args.host)

    try:
        f = open(args.udp_ports, 'r')
        udp_ports = json.load(f)
        f.close()
    except Exception as e:
        print(repr(e))
        return -1

    def handler(t, d, a):

        global ap_channel

        if(d[len(d)-1] == '\x00'):
            d = d[:len(d)-1]

        message = json.loads(d)

        print("Got message: " + repr(message) + "from ip: " + repr(a));

        try:
          if message["MAC"] in udp_ports:

              port_tuple = udp_ports[message["MAC"]]

              message_back = {
              "send_to" : port_tuple[0],
              "receive_on" : port_tuple[1],
              "host" : host,
              "ap" : args.ssid,
              "pass" : args.passkey,
              "cha" : (ap_channel+1),
              "msgType" : messages.MSG_HOST_IP}

              print("Assigning to channel: " + repr(ap_channel+1))

              print(message)

              print("UDP ports: %i %i" % tuple(port_tuple))

              print(message_back)

              ap_channel = (ap_channel + 5) % 15

              t.sendto(json.dumps(message_back).encode("UTF-8"), a)

          else:
              print("MAC address: " + repr(message["MAC"]) + " not registered")
        except Exception as e:
          pass

    udp_server = udpserver.UDPServerProtocol(args.udp_port, handler)
    udp_server.async_start()

    input('Press enter to quit')

    udp_server.stop()

    print("stopped successfully")

if __name__ == "__main__":
    main()
