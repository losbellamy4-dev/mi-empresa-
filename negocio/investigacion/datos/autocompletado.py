import json,urllib.parse,urllib.request,sys,time
def sug(q,gl="es"):
    u="https://suggestqueries.google.com/complete/search?client=firefox&hl=es&gl=%s&q=%s"%(gl,urllib.parse.quote(q))
    try:
        return json.loads(urllib.request.urlopen(u,timeout=15).read().decode("utf-8","ignore"))[1]
    except Exception as e: return ["ERR "+str(e)]
out={}
for pre in sys.argv[1:]:
    for gl in ["es"]:
        r=sug(pre,gl); out[f"{pre}|{gl}"]=r; time.sleep(0.4)
print(json.dumps(out,ensure_ascii=False,indent=1))
