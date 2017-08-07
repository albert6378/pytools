#coding=utf-8

import threading
import urllib2;
from bs4 import BeautifulSoup;
import random;
import gzip;
import StringIO;
import os;


def xicidaili(useragents,returnlist,start=1,end=10):
    for i in range(start,end):
        iplisturl = "http://www.xicidaili.com/nn/" + str(i)
        print iplisturl + u':页面采集中..';
        try:
            req = urllib2.Request(iplisturl)
            req.add_header("User-Agent", random.choice(useragents))
            res = urllib2.urlopen(req, timeout=20)
            # 解决gzip压缩 start
            headers = res.info()
            content = res.read()
            if ('Content-Encoding' in headers and headers['Content-Encoding']) or \
                    ('content-encoding' in headers and headers['content-encoding']):
                data = StringIO.StringIO(content)
                gz = gzip.GzipFile(fileobj=data)
                content = gz.read()
                gz.close()
                # 解决gzip压缩 end
            soup = BeautifulSoup(content, 'html.parser')
            ips = soup.findAll('tr')
            for x in range(1, len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")
                if (str(tds[5].contents[0]) == 'HTTP'):
                    ip_temp = str(tds[1].contents[0]) + ':' + str(tds[2].contents[0])
                    returnlist.append(ip_temp);
            print iplisturl + u':页面采集完成';
        except Exception, e:
            print iplisturl + u':页面采集失败';

def kuaidaili(useragents,returnlist,start=1,end=10):
    for i in range(start, end):
        iplisturl = "http://www.kuaidaili.com/free/inha/" + str(i) + "/"
        print iplisturl + u':页面采集中..';
        try:
            req = urllib2.Request(iplisturl)
            req.add_header("User-Agent", random.choice(useragents))
            req.add_header("Host", "www.kuaidaili.com")
            # req.add_header("Connection", "close")
            # req.add_header("Referer", "http://www.baidu.com")
            res = urllib2.urlopen(req, timeout=20)
            # 解决gzip压缩 start
            headers = res.info()
            content = res.read()
            if ('Content-Encoding' in headers and headers['Content-Encoding']) or \
                    ('content-encoding' in headers and headers['content-encoding']):
                data = StringIO.StringIO(content)
                gz = gzip.GzipFile(fileobj=data)
                content = gz.read()
                gz.close()
            # 解决gzip压缩 end
            soup = BeautifulSoup(content, "html.parser")
            ips = soup.findAll('tr')
            for x in range(1, len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")
                if (str(tds[3].contents[0]) == 'HTTP'):
                    ip_temp = str(tds[0].contents[0]) + ':' + str(tds[1].contents[0])
                    returnlist.append(ip_temp);
            print iplisturl + u':页面采集完成';
        except Exception, e:
            print iplisturl + u':页面采集失败';

def youdaili(useragents,returnlist):
    iplisturl = "http://www.youdaili.net/Daili/http/"
    print iplisturl + u':页面采集中..';
    try:
        req = urllib2.Request(iplisturl)
        req.add_header("User-Agent",random.choice(useragents))
        req.add_header("Host", "www.youdaili.net")
        req.add_header("Connection", "close")
        res = urllib2.urlopen(req, timeout=20)
        #解决gzip压缩 start
        headers = res.info()
        content = res.read()
        if ('Content-Encoding' in headers and headers['Content-Encoding']) or \
           ('content-encoding' in headers and headers['content-encoding']):
            data = StringIO.StringIO(content)
            gz = gzip.GzipFile(fileobj=data)
            content = gz.read()
            gz.close()
        # 解决gzip压缩 end
        soup = BeautifulSoup(content, "html.parser")
        adiv=soup.findAll('div', {'class': 'chunlist'})
        href=adiv[0].find("a").attrs['href']
        if href:
            req = urllib2.Request(href)
            req.add_header("User-Agent", random.choice(useragents))
            req.add_header("Host", "www.youdaili.net")
            req.add_header("Connection", "close")
            res = urllib2.urlopen(req, timeout=20)
            # 解决gzip压缩 start
            headers = res.info()
            content = res.read()
            if ('Content-Encoding' in headers and headers['Content-Encoding']) or \
                    ('content-encoding' in headers and headers['content-encoding']):
                data = StringIO.StringIO(content)
                gz = gzip.GzipFile(fileobj=data)
                content = gz.read()
                gz.close()
            # 解决gzip压缩 end
            soup = BeautifulSoup(content, "html.parser")
            contentdiv = soup.findAll('div', {'class': 'content'})
            contentp=contentdiv[0].findAll('p')
            for x in range(1,len(contentp)):
               text=contentp[x].text
               position=text.find('@')
               ip_temp=text[0:position]
               if ip_temp:
                  returnlist.append(ip_temp);
        print iplisturl + u':页面采集完成';
    except Exception, e:
        print iplisturl + u':页面采集失败';

def data5u(useragents,returnlist):
    iplisturl = "http://www.data5u.com/free/gngn/index.shtml"
    print iplisturl + u':页面采集中..';
    try:
        req = urllib2.Request(iplisturl)
        req.add_header("User-Agent",random.choice(useragents))
        req.add_header("Host", "www.data5u.com")
        req.add_header("Cookie",'auth=2815ffcc0824b1647d8e97515d8c0ac9; UM_distinctid=15c9b35a7aab6-00a58639c4f985-323f5c0f-13c680-15c9b35a7abdde; JSESSIONID=138EB15BD92BD2CD8BF955053EFEC9B8; Hm_lvt_3406180e5d656c4789c6c08b08bf68c2=1497404195,1497434158,1497488208,1497834959; Hm_lpvt_3406180e5d656c4789c6c08b08bf68c2=1497834959; CNZZDATA1260383977=904410821-1497251971-null%7C1497831815')
        # req.add_header("Connection", "close")
        res = urllib2.urlopen(req, timeout=20)
        #解决gzip压缩 start
        headers = res.info()
        content = res.read()
        if ('Content-Encoding' in headers and headers['Content-Encoding']) or \
           ('content-encoding' in headers and headers['content-encoding']):
            data = StringIO.StringIO(content)
            gz = gzip.GzipFile(fileobj=data)
            content = gz.read()
            gz.close()
        # 解决gzip压缩 end;
        soup = BeautifulSoup(content, "html.parser")
        contentdiv = soup.findAll('ul', {'class': 'l2'})
        for x in range(1,len(contentdiv)):
          ip = contentdiv[x]
          tds = ip.findAll("li")
          ip_temp =str(tds[0].contents[0])+':'+str(tds[1].contents[0])
          returnlist.append(ip_temp );
        print iplisturl + u':页面采集完成';
    except Exception, e:
        print iplisturl + u':页面采集失败';

def validateip(useragents):
    url = "http://ip.chinaz.com/getip.aspx"
    with open("proxy", "r") as f:
        lines = f.readlines()
    with open("proxy", "w") as f_w:
        for line in lines:
            ip =line.strip("\n")
            if ip.strip():
                try:
                    # 下面是模拟浏览器进行访问
                    req = urllib2.Request(url)
                    req.add_header("User-Agent", random.choice(useragents))
                    req.add_header("Host", "ip.chinaz.com")
                    req.add_header("Connection", "close")
                    # 下面是使用ip代理进行访问
                    proxy_handler = urllib2.ProxyHandler({"http": ip})
                    opener = urllib2.build_opener(proxy_handler, urllib2.HTTPHandler)
                    urllib2.install_opener(opener)
                    try:
                        html = urllib2.urlopen(req, timeout=20).read()
                        if (html.find('address') != -1):
                            f_w.write(ip+'\n')
                            print u'代理IP:' + ip + u' 有效'
                        else:
                            print u'代理IP:' + ip + u' 已经失效'
                            continue
                    except Exception, e:
                        print u'代理IP:' + ip + u'已经失效'
                        continue
                except Exception, e:
                    print ip + u'未知错误'
                    continue
            else:
                continue
    print u'IP校验完成'

returnlist = []
useragents = [
    {'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    {'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
    {'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
    {'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},
    {'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},
    {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
    {'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
    {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},
    {'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},
    {'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'},
    {'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
]
threads = []
t1 = threading.Thread(target=xicidaili,args=(useragents,returnlist,1,3))
threads.append(t1)
t2 = threading.Thread(target=kuaidaili,args=(useragents,returnlist,1,3))
threads.append(t2)
t3 = threading.Thread(target=youdaili,args=(useragents,returnlist,))
threads.append(t3)
t4 = threading.Thread(target=data5u,args=(useragents,returnlist,))
threads.append(t4)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print u'IP采集完成'
    f = open("proxy", "w")
    for proxy in returnlist:
        f.write(proxy + "\n")
    f.close()
    # 验证IP是否可用
    # validateip(useragents);
    os.system("pause")