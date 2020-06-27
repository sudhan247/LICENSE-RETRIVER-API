#Library used
import re
import requests
import json
from bs4 import BeautifulSoup, SoupStrainer
import lxml.html
def getdata(licenseno,dob):
    #URL's used for retrieval
    home_url = 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101'
    post_url = 'https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml'


    #Opening the home url
    r = requests.get(url=home_url)
    cookies = r.cookies
    soup = BeautifulSoup(r.text, 'html.parser')
    viewstate = soup.select('input[name="javax.faces.ViewState"]')[0]['value']

    
    #Finding the first button to check status
    i = 0
    for match in soup.find_all('button', id=re.compile("form_rcdl")):
        if i ==  0:
            button_id= match.get('id')
        i = 1
        

    #Preparing the data with the inputs given
    data = {
        'javax.faces.partial.ajax':'true',
        'javax.faces.source':button_id,
        'javax.faces.partial.execute':'@all',
        'javax.faces.partial.render': 'form_rcdl:pnl_show form_rcdl:pg_show form_rcdl:rcdl_pnl',
        button_id:button_id,
        'form_rcdl':'form_rcdl',
        "form_rcdl:tf_dlNO": licenseno,
        'form_rcdl:tf_dob_input': dob,
        'javax.faces.ViewState': viewstate,
    }


    #Retrieval of status with the available data
    r = requests.post(url=post_url, data=data, cookies=cookies)
    root = lxml.html.fromstring(r.text.encode())

    
    #Getting the table values
    data=root.xpath('//tr/td//text()')


    #Parsing the data and storing it in a dictionary details
    details=dict()


    #Solving the First table 'Details of Driving License' format
    topic='Details of Driving License'
    details[topic]=dict()
    for i in range(10):
        if i%2==0:
            key=data[i]
        else:
            value=' '.join(data[i].split())
            details[topic][key]=value


    #Solving the Second table 'Driving License Validity Details' format
    topic='Driving License Validity Details'

    ##Solving Non-Transport Format
    details[topic]=dict()
    details[topic][data[10]]=dict()
    details[topic][data[10]][data[11][:4]]=data[12]
    details[topic][data[10]][data[13][:2]]=data[14]

    ##Solving Transport Format
    details[topic][data[15]]=dict()
    details[topic][data[15]][data[16][:4]]=data[17]
    details[topic][data[15]][data[18][:2]]=data[19]

    ##Solving other fields
    details[topic][data[20]]=data[21]
    details[topic][data[22]]=data[23]


    #Solving the Third table 'Class of Vehicle Details' format
    topic='Class of Vehicle Details'
    details[topic]=dict()
    details[topic]["COV Category"]=[]
    details[topic]["Class Of Vehicle"]=[]
    details[topic]["COV Issue"]=[]
    data=data[24:]
    while(len(data)!=0):
        details[topic]["COV Category"].append(data[0])
        details[topic]["Class Of Vehicle"].append(data[1])
        details[topic]["COV Issue"].append(data[2])
        data=data[3:]

    
    #Converting created dict to json format
    result=json.dumps(details)
    return (result)


#Reading the license no and DOB

##SampleData
##licenseno='DL-0420110149646'
##dob='09-02-1976'

licenseno=input('Enter Driving License No:')
dob=input('Enter Date of Birth(DD-MM-YYYY Format):')
print('Result')
try:
    print(getdata(licenseno,dob))
except:
    print('Invalid Details')
