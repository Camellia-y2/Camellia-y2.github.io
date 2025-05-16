#!/usr/bin/env python3

"""
王俊凯粉丝网站 - 简易服务器启动脚本
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# 配置
PORT = 8000
DIRECTORY = Path(__file__).parent.absolute()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    print(f"王俊凯粉丝网站服务器启动中...")
    print(f"网站根目录: {DIRECTORY}")
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}/"
            print(f"服务器已启动! 请访问: {url}")
            print("(按 Ctrl+C 可以停止服务器)")
            
            # 自动在浏览器中打开网站
            webbrowser.open(url)
            
            # 保持服务器运行
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止，感谢使用!")
    except Exception as e:
        print(f"启动服务器时出错: {e}")

if __name__ == "__main__":
    main()
