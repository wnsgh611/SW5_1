# -*- coding:utf-8 -*-
__author__ = 'JunoJunho'
#Simple Session Open

import urllib
import urllib2

def find_User_Name(url_body):
    student = "연수생"
    mentor = "멘토"
    #Hangul = 3 bytes
    if url_body.find(student) > -1 :
        stu_index = url_body.find(student)
        ret_str = url_body[stu_index : stu_index + 22]
    else:
        mentor_index = url_body.find(mentor)
        ret_str = url_body[mentor_index: mentor_index + 19]
    return ret_str



cookie_url = "http://new.swmaestro.kr/operate/myInfor/login.do"

login_url = 'http://new.swmaestro.kr/operate/loginAction.do'
login_form={'returnUrl' : '',
  'remember' : '',
  'username' : 'wnsgh611',
  'loginPassword' : '5357kjh',
  'x' : 0,
  'y' : 0
}
login_req = urllib.urlencode(login_form)


cookie_req = urllib2.Request(cookie_url)
cookie_response = urllib2.urlopen(cookie_url)
cookie = cookie_response.headers.get('Set-Cookie')

login_req = urllib2.Request(login_url,login_req)
login_response = urllib2.urlopen(login_req)
#print login_response.headers
#print login_response.read()

login_body = login_response.read()
if login_body.find('<strong>로그인을 ') > 0:
    print "Fail"
else:
    print "##Login Success##"
    print find_User_Name(login_body)
#page = login_response.read()

#print "##### BODY #####\n"
#print page