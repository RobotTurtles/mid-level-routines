import socket

def GetCurrentAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 0))  # connecting to a UDP address doesn't send packets
    local_ip_address = s.getsockname()[0]

    return  local_ip_address

def GetTurtleName():
    turtle_name = socket.gethostname()

    return  turtle_name