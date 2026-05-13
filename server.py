import http.server
import os
import urllib.parse

FALLBACK_FILE = 'index.html'
PORT = 8000

class SPAHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        clean_path = parsed_path.path

        # 如果请求的是一个真实存在的文件（比如 .css .js .png），就正常发送
        if os.path.exists('.' + clean_path) and os.path.isfile('.' + clean_path):
            super().do_GET()
        else:
            # 否则，一律返回 index.html，让里面的 JS 来处理路由
            self.path = '/' + FALLBACK_FILE
            super().do_GET()

if __name__ == '__main__':
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, SPAHandler)
    print(f'✅ 本地测试网站已启动！请在浏览器打开 http://localhost:{PORT}')
    httpd.serve_forever()