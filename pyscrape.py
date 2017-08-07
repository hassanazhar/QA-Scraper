import lxml
from bs4 import BeautifulSoup as b
import urllib
import urllib.request

url="https://answers.yahoo.com/dir/index?sid=396545660"
page = urllib.request.urlopen(url).read()
html = b(page,'lxml')
##FINDS ALL QUESTIONS (MAX 20) ON PAGE AND PRINTS
links = html.findAll("a")

postcontainers = html.findAll("li",{"class":"ya-discover-tile ya-discover-tile-qn Bfc P-14 Bdbx-1g Bgc-w"})
numq=[]
numq = len(postcontainers)
questions =[]
for i in range(0,numq-1,):
    qcont2 = postcontainers[i]
    questions.append(qcont2.findAll("a",{"class":"Fz-14 Fw-b Clr-b Wow-bw title"}))
    #print(qcont2.findAll("a",{"class":"Fz-14 Fw-b Clr-b Wow-bw title"}))
print(questions)

##Returns Answers as well
qcont3 = html.findAll("div",{"class":"Clr-888 Fz-12 Lh-18"})
num2 = len(qcont3)
print(qcont3)
justlinks=[]
for anscont in qcont3:
    #justlinks = anscont.a["href"]
    justlinks.append(anscont.a["href"])
print(justlinks)
print(len(justlinks))
newurl=[]
for i in justlinks:
    newurl.append("https://answers.yahoo.com"+i)
print(newurl)

#url2="https://answers.yahoo.com/dir/index?sid=396545660"
#page = urllib.request.urlopen(url).read()
#html = b(page,'lxml')    
    #use href, append to yahoo.com, do a new urlopen.read, go to source
filename = "questions.csv"
f = open(filename,"w")
headers = "Yahoo Questions\n"
f.write(headers)
for i in questions:
    f.write('%s\n'% i)
f.close()


    
