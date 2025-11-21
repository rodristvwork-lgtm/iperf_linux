import socket
import subprocess
def get_local_ip():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]         
    finally:
        s.close()
    return ip

def run_iperf(server_ip, duration, reverse, port):
    
    ip_address = get_local_ip()
    
    cmd = [
        "iperf3",
        "-c", server_ip,
        "-B", ip_address,
        "-t", str(duration),
        "-p", str(port),
        "-R" if reverse else "--get-server-output"
    ]
    print(cmd)
    subprocess.run(cmd, check=True)
   
if __name__ == "__main__":
    
    #run_iperf("178.215.228.109", 50, reverse = False, port= 9205)
    run_iperf("178.215.228.109", 10, reverse = False, port= 9206)

    