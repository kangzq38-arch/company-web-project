import urllib.request

base_url = 'https://kangzq38-arch.github.io/company-web-project/'
routes = ['/', '/about', '/contact']

for path in routes:
    url = base_url.rstrip('/') + path
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
            print(f'✅ {url}  →  页面送达 (状态码 {resp.status})')
    except Exception as e:
        print(f'❌ {url}  →  完全无法访问: {e}')