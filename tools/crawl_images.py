"""mkspedal.com을 돌며 이미지 주소를 모아 .github/mks-images.tsv 로 저장합니다 (Actions에서 실행).
열: 페이지 URL, 이미지 URL, alt / 파일 설명"""
import re, sys, time, urllib.request, urllib.parse
from html.parser import HTMLParser

STARTS = ['https://www.mkspedal.com/', 'https://www.mkspedal.com/en/', 'https://mkspedal.com/']
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
MAX = 150

class P(HTMLParser):
    def __init__(s): super().__init__(); s.links=[]; s.imgs=[]
    def handle_starttag(s, t, a):
        a = dict(a)
        if t == 'a' and a.get('href'): s.links.append(a['href'])
        if t in ('img', 'source'):
            for k in ('src', 'data-src', 'data-lazy-src', 'data-original'):
                if a.get(k): s.imgs.append((a[k], a.get('alt', '')))
            for k in ('srcset', 'data-srcset'):
                if a.get(k):
                    best = a[k].split(',')[-1].strip().split(' ')[0]
                    if best: s.imgs.append((best, a.get('alt', '')))
        if t == 'meta' and a.get('property') in ('og:image',) and a.get('content'):
            s.imgs.append((a['content'], 'og:image'))
    def handle_data(s, d): pass

def get(u):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': UA}), timeout=20)
    if 'html' not in r.headers.get('Content-Type', ''): return None, r.geturl()
    return r.read().decode('utf-8', 'replace'), r.geturl()

seen, queue, rows, hosts = set(), list(STARTS), [], set()
log = []
while queue and len(seen) < MAX:
    u = queue.pop(0).split('#')[0]
    if u in seen: continue
    seen.add(u)
    try:
        html, final = get(u)
    except Exception as e:
        log.append(f'ERR {u} {e}'); continue
    hosts.add(urllib.parse.urlparse(final).netloc)
    log.append(f'OK  {u} -> {final}')
    if not html: continue
    p = P(); p.feed(html)
    # 인라인 CSS background-image도 수집
    for m in re.findall(r'url\((["\']?)([^)"\']+\.(?:jpe?g|png|webp))\1\)', html, re.I):
        p.imgs.append((m[1], 'css-bg'))
    for src, alt in p.imgs:
        full = urllib.parse.urljoin(final, src)
        if re.search(r'\.(jpe?g|png|webp)(\?|$)', full, re.I):
            rows.append((final, full, alt.replace('\t', ' ').replace('\n', ' ')))
    for h in p.links:
        full = urllib.parse.urljoin(final, h).split('#')[0]
        pu = urllib.parse.urlparse(full)
        if pu.scheme.startswith('http') and pu.netloc.replace('www.', '') in {x.replace('www.', '') for x in hosts | {'mkspedal.com'}} \
           and not re.search(r'\.(jpe?g|png|webp|gif|pdf|zip|css|js)$', pu.path, re.I) and full not in seen:
            queue.append(full)
    time.sleep(0.3)

uniq, out = set(), []
for r in rows:
    if r[1] in uniq: continue
    uniq.add(r[1]); out.append('\t'.join(r))
open('.github/mks-images.tsv', 'w').write('\n'.join(out) + '\n')
open('.github/mks-crawl.log', 'w').write('\n'.join(log) + '\n')
print(len(seen), 'pages,', len(out), 'images')
