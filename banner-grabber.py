#!/usr/bin/python3

import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except socket.timeout:
        return "Connection timed out"
    except socket.error as err:
        return f"Socket error: {err}"
    except Exception as e:
        return str(e)

def main():
    print("Welcome, this is a simple banner grabbing tool")
    print("<------------------------------------------------------>")

    ip_addr = input("Please enter the IP address you want to scan: ")
    print("The IP you entered is:", ip_addr)
    print(type(ip_addr))

    port = int(input("Please enter the port number: "))
    print("The port you entered is:", port)

    banner = grab_banner(ip_addr, port)
    print(f"Banner for {ip_addr}:{port} is: {banner}")

if __name__ == "__main__":
    main()
