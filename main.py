import requests
import re

if __name__ == '__main__':

  post_addr = "https://itouch.cycu.edu.tw/active_system/quary/s_grade.jsp"

#構造header
  post_header={
      'Host': 'itouch.cycu.edu.tw',
      'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
      'Accept-Encoding': 'gzip, deflate, br',
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-Requested-With':'XMLHttpRequest',
      'Referer':'https://itouch.cycu.edu.tw/i3/s_web/2_1.jsp',
      'Content-Length': '65',

      'Cookie':'JSESSIONID=XXXXXX;',
      'Connection':'keep-alive'
  }

#構造登陸信息
  post_data={'domain':'CYCU',
             'enablemacauth':'0',
             'password':'XXXX',
             'username':'XXXX'
            }
#發送post請求，獲取response
  response = requests.post(post_addr,data=post_data,headers=post_header)

#處理response信息
  pattern = re.compile('<tr.*?bgcolor="#33FFFF".*?</td>.*?</td>.*?</td>.*?<font size="2">(.*?)</font>.*?</td>.*?</td>.*?<font size="2">(.*?)</font>.*?</td>.*?</td>.*?</td>.*?</td>.*?</td>.*?</tr>', re.S)
  grades = re.findall(pattern, response.text)

  for grade in grades :
      print('課程名稱：' + grade[0] + '成績：' + grade[1])
