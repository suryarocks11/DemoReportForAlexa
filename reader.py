import urllib
data = ""
g_url ="https://storage.googleapis.com/demo_report_for_dev/report.txt"
import urllib.request

with urllib.request.urlopen(g_url) as url:
    data = url.read()
    # I'm guessing this would output the html source code ?
    data = data.decode()
    print(data)    
#gsutil -h "Cache-Control:no-cache, max-age=0" gs://demo_report_for_dev/report.txt

#gsutil setmeta -r -h "Cache-control:public, max-age=0" gs://demo_report_for_dev/report.txt