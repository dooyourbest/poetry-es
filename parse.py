import sys
import json
from elasticsearch import Elasticsearch
es = Elasticsearch(['localhost:9200'])
file=open(sys.argv[1])
a=json.loads(file.read())
# print a[0]
i=1
for line in a:
    print line
    res = es.index(index="msg", doc_type='shijing', id=i, body=line)
    i+=1

