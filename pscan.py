import socket
import threading
import concurrent.futures
import argparse

open_ports = set()
barrier = threading.Barrier(2)  # Adjust the number as needed

def scan_port(host, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))

            if result == 0:
                open_ports.add(port)
                try:
                    banner = sock.recv(1024).decode().strip()
                    print(f"\033[32m[+] Port {port} is open - Service: {banner}\033[0m")
                except:
                    print(f"\033[32m[+] Port {port} is open\033[0m")
    except:
        pass
    finally:
        barrier.wait()  # Signal that this thread is done

def scan_ports_range(host, port_range, timeout, max_threads):
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(scan_port, host, port, timeout) for port in port_range]
        concurrent.futures.wait(futures)

    barrier.wait()  # Wait for all threads to finish

    print(f"\n\033[36m[+] Total open ports found: {len(open_ports)}\033[0m")

def main():
    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("host", help="Host to scan")
    parser.add_argument("-p", "--ports", metavar="PORT_RANGE", default="1-1024",
                        help="Range of ports to scan (e.g., 1-1024)")
    parser.add_argument("-t", "--timeout", type=float, default=1,
                        help="Timeout for each port scan (in seconds)")
    parser.add_argument("-c", "--concurrency", type=int, default=10,
                        help="Maximum number of concurrent threads")
    args = parser.parse_args()

    try:
        ip = socket.gethostbyname(args.host)
        print(f"\033[35m[+] Scanning host: {ip}\033[0m")
        port_range = range(*map(int, args.ports.split("-")))
        scan_ports_range(ip, port_range, args.timeout, args.concurrency)
    except (socket.gaierror, ValueError):
        print("\033[31m[!] Invalid host or port range.\033[0m")

if __name__ == "__main__":
    main()
