from pathlib import Path
from urllib.parse import urljoin, urlsplit
import json, re, sys
from xml.sax.saxutils import escape
root=Path(__file__).resolve().parent
base=sys.argv[1].rstrip('/')+'/'
assert urlsplit(base).scheme=='https' and urlsplit(base).netloc, 'Provide the live HTTPS homepage URL.'
entries=[]
for page in sorted(root.glob('*.html')):
    url=base if page.name=='index.html' else urljoin(base,page.name)
    content=page.read_text()
    content=re.sub(r'<link[^>]*rel="canonical"[^>]*>','',content)
    content=content.replace('</head>','<link rel="canonical" href="'+url+'"></head>',1)
    def update(match):
        data=json.loads(match.group(1))
        def resolve(value):
            if isinstance(value,dict):
                return {key:(base+'#'+val.split('#',1)[1] if key=='@id' and isinstance(val,str) and '#' in val else resolve(val)) for key,val in value.items()}
            if isinstance(value,list): return [resolve(x) for x in value]
            return value
        data=resolve(data)
        data['@graph'][0]['url']=base
        data['@graph'][1]['url']=urljoin(base,'about.html')
        return '<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False,indent=2)+'</script>'
    content=re.sub(r'<script type="application/ld\+json">(.*?)</script>',update,content,flags=re.S)
    page.write_text(content)
    if page.name!='project-archive.html': entries.append(url)
xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('  <url><loc>'+escape(url)+'</loc></url>\n' for url in entries)+'</urlset>\n'
(root/'sitemap.xml').write_text(xml)
print('Configured canonical URLs, absolute structured-data IDs, and sitemap for',base)
