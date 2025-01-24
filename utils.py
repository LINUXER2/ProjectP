import socket


# 获取本机ip地址
def get_ip_addr():
    global s, ip
    try:
        # 创建一个UDP套接字
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # 尝试连接到一个公共的IP地址和端口
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        print("localIP:", ip)
        s.close()
    return ip


if __name__ == '__main__':
    get_ip_addr()
