#!/usr/bin/env python3
"""Usage: build.py business.json OUTDIR"""
import json,sys,os,html
d=json.load(open(sys.argv[1]));out=sys.argv[2];os.makedirs(out,exist_ok=True)
t=open(os.path.join(os.path.dirname(__file__),'index.template.html')).read()
t=t.replace('__TITLE__',html.escape(d['name'])).replace('__DATA__',json.dumps(d).replace('</','<\\/'))
open(os.path.join(out,'index.html'),'w').write(t);json.dump(d,open(os.path.join(out,'business.json'),'w'),indent=2)
print('built',out)
