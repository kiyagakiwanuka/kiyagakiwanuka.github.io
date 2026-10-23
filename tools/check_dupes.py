"""Check every project detail page for duplicated sentences across sections.
Usage: python3 tools/check_dupes.py [base_url_or_local_dir]"""
import re,sys,os,time,html,glob,urllib.request
from itertools import combinations
base=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
paths=sorted(["projects-detail/"+os.path.basename(f) for f in glob.glob(R+"/projects-detail/*.html")]+[f[len(R)+1:] for f in glob.glob(R+"/projects/*/index.html")])
def get(p):
    if base.startswith("http"):
        return urllib.request.urlopen(urllib.request.Request(f"{base.rstrip('/')}/{p}?nocache={time.time()}",headers={"Cache-Control":"no-cache"})).read().decode()
    return open(os.path.join(base,p)).read()
norm=lambda s:re.sub(r"\s+"," ",re.sub(r"[^\w\s]"," ",html.unescape(re.sub("<[^>]+>"," ",s)).lower())).strip()
STOP=set("a an the and or of to in on for by with from at as is are was were be it its this that these those their his her into than then so such can may how what which who do does across over between before after each".split())
W=lambda s:set(norm(s).split())-STOP
total=0
for p in paths:
    a=get(p); a=a[a.find("<article"):]
    parts=re.split(r'<h2[^>]*>',a)[1:]
    secs=[]
    for x in parts:
        name=norm(x.split("</h2>")[0]); body=x.split("</h2>",1)[1]
        if 'class="tags"' in body[:40] or "tag" in body[:30]: continue  # skip tag lists
        sents=[s for s in re.split(r"(?<=[.!?])\s+|</p>|</li>",body) if len(norm(s).split())>=5]
        secs.append((name,sents))
    issues=[]
    for (n1,s1),(n2,s2) in combinations(secs,2):
        for x in s1:
            for y in s2:
                a1,b1=norm(x),norm(y); wa,wb=W(x),W(y)
                if a1==b1 or (len(a1)>25 and a1 in b1) or (len(b1)>25 and b1 in a1) or (len(wa&wb)>=4 and len(wa&wb)/max(1,min(len(wa),len(wb)))>0.6):
                    issues.append(f"  [{n1}] vs [{n2}]: {a1[:80]}")
    total+=len(issues)
    print(("DUP " if issues else "ok  ")+p); [print(i) for i in issues]
print("TOTAL DUPLICATES:",total); sys.exit(1 if total else 0)
