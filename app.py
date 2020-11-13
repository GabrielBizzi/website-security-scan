# -*- coding: utf-8 -*-
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from platform import python_version 
from tkinter import * 
from subprocess import call 
import subprocess 
import logging 
import time 
from requests import get
from socket import *
from subprocess import check_output
import os
import re

from searchLog import *

token = ('–api-token Rw4mlsKSOvuYfTsUvoIeHyuutL8cutdspWT4xApuvOs')

ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

ds = SupervisedDataSet(2, 1)

god = ('>=90')

medium = ('>=51 & <=89')

bad = ('<=50')

ds.addSample((0.8, 0.4), (0.7))
ds.addSample((0.5, 0.7), (0.5))
ds.addSample((1.0, 0.8), (0.95))

nn = buildNetwork(2, 4, 1, bias=True)

trainer = BackpropTrainer(nn, ds)

p = subprocess.Popen("python --version", stdout=subprocess.PIPE, shell=True) 

(output, err) = p.communicate() 

 
homeDir = str(os.getcwd())                           
logFile= ("sprint.txt")

logger = logging.getLogger("sprint")  
logger.setLevel(logging.INFO)         
                                         
logger_handler = logging.FileHandler(logFile, mode='w')
logger_handler.setLevel(logging.INFO)
 
logger_formatter = logging.Formatter('')
 
logger_handler.setFormatter(logger_formatter)
  
logger.addHandler(logger_handler)
 
logger.info('Anne iniciada.')

p_status = p.wait()

if (output=='Python ', python_version()):    
    class Aplication:
        def __init__(self, master=None):            
            self.widget1 = Frame(master)            
            self.widget1["pady"] = 90            
            self.fontePadrao = ("Arial", "10")            
            self.primeiroContainer = Frame(master)           
            self.primeiroContainer["pady"] = 30            
            self.primeiroContainer.pack()

            self.segundoContainer = Frame(master)            
            self.segundoContainer["padx"] = 50            
            self.segundoContainer.pack()

            self.terceiroContainer = Frame(master)            
            self.terceiroContainer["padx"] = 20            
            self.terceiroContainer.pack()

            self.quartoContainer = Frame(master)            
            self.quartoContainer["padx"] = 20            
            self.quartoContainer.pack()

            self.titulo = Label(self.primeiroContainer, text="Anne")            
            self.titulo["font"] = ("Arial", "42", "bold")    
            self.titulo["pady"] = 20               
            self.titulo.pack()

            self.sub_titulo = Label(self.primeiroContainer, text="Intelligence Artificial Security Scanner Web", fg="#aeaeae") 
            self.sub_titulo["pady"] = 6          
            self.sub_titulo["font"] = ("Arial", "14", "")          
            self.sub_titulo.pack()

            self.sub_text = Label(self.primeiroContainer, text="Through artificial intelligence technologym we can have knowledge beyond superficiality, knowledge that revolutionizes the world.", fg="#adadad") 
            self.sub_text["pady"] = 16        
            self.sub_text["font"] = ("Arial", "10", "")          
            self.sub_text.pack()

            #Url:

            #self.urlLabel = Label(self.segundoContainer, text="Url: ", font=self.fontePadrao)            
            #self.urlLabel.pack(side=LEFT)
        
            #end Url:

            self.url = Entry(self.segundoContainer)            
            self.url["width"] = 30  
            self.url["font"] = self.fontePadrao            
            self.url.pack(side=LEFT)

            self.aut = Button(self.quartoContainer, bg="#ba007c", fg="#ddd")            
            self.aut["text"] = "Scan URL"
            self.aut["font"] = ("Calibri", "8")            
            self.aut["width"] = 14  
            self.aut.pack(side=LEFT)

            self.aut_two = Button(self.quartoContainer, bg="#071525", fg="#ddd")            
            self.aut_two["text"] = "About Us"
            self.aut_two["font"] = ("Calibri", "8")            
            self.aut_two["width"] = 14  
            self.aut_two.pack(side=RIGHT)

            self.aut["command"] = self.aut_url            
            self.aut.pack()

            self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)            
            self.mensagem.pack()

            #self.info = Label(self.primeiroContainer, text="Lorem ipsum dolor sit amer, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
            #self.info.pack(side=LEFT)
        def aut_url(self):        

            url = str(self.url.get()) #comando para puxar a variavel da input
            time.sleep(3.5)
            ip_url = gethostbyname(url) #captando Ip do site
            debug_url = str(ip_url) #ip do site
            logger.warning(debug_url)

            #checar palavra no log
            check_scan = str(subprocess.check_output(['whatweb', '-a', '3', '-v', url ]))
            time.sleep(3.5)
            details_whatweb_scan = (ansi_escape.sub('', check_scan)).replace(',','\n=')
            logger.warning(details_whatweb_scan)
            time.sleep(3.5)

            search = '[ WordPress ]'
            WordPress_found='Continue'
            WordPress_not_found='Skip this step'
            def check():
                datafile = file('sprint.txt')
                for line in datafile:
                    if search in line:
                        found = True
                        break
                    else:
                        found = False
                return found

            if check():
                print WordPress_found
                time.sleep(3.5)
                check_wp_scan = str(subprocess.check_output(['wpscan', '--url', url, '--enumerate', 'u,ap', token]))
                time.sleep(3.5)
                details_wordpress_scan = (ansi_escape.sub('', check_wp_scan))
                logger.warning(details_wordpress_scan)
                time.sleep(3.5)
            else:
                print WordPress_not_found
                pass

            ssl_compatibility = str('<https://'+url+'/>')
            search = (ssl_compatibility)
            Have_SSL='Continue'
            dont_Have_SSL='Skip this step'
            def check_quickurl():
                datafile = file('sprint.txt')
                for line in datafile:
                    if search in line:
                        found = True
                        break
                    else:
                        found = False
                return found
            def check():
                datafile = file('sprint.txt')
                for line in datafile:
                    if search in line:
                        found = True
                        break
                    else:
                        found = False
                return found

            if check():
                print Have_SSL
                time.sleep(3.5)
                check_ssl = str(subprocess.check_output(['sslscan', '--show-certificate', 'https://'+url]))
                time.sleep(3.5)
                details_sslscan_check = (ansi_escape.sub('', check_ssl))
                logger.warning(details_sslscan_check)
                time.sleep(3.5)
                check_ssl_conection_http = str(subprocess.check_output(['sslscan', '--http', 'https://'+url]))
                time.sleep(3.5)
                details_sslscan_two_check_conection = (ansi_escape.sub('', check_ssl_conection_http))
                logger.warning(details_sslscan_two_check_conection)
                time.sleep(3.5)
                check_ssl_conection_regular = str(subprocess.check_output(['sslyze', '--regular', 'https://'+url]))
                time.sleep(3.5)
                details_sslyze_scan = (ansi_escape.sub('', check_ssl_conection_regular))
                logger.warning(details_sslyze_scan)
                time.sleep(3.5)
            else:
                print dont_Have_SSL
                pass
            if check_quickurl():
                print Have_SSL
                time.sleep(3.5)
                check_url = str(subprocess.check_output(['bash', '/usr/share/zaproxy/zap.sh', '-cmd', '-quickurl', 'https://'+url, '-quickprogress']))
                time.sleep(3.5)
                details_zap_advanced_scan = (ansi_escape.sub('', check_url))
                logger.warning(details_zap_advanced_scan)
                time.sleep(3.5)
            else:
                print dont_Have_SSL
                pass
            
            print pesquisar_country( 'Country', 1 )
            print pesquisar_ip('IP', 1)
            print pesquisar_servidor('HTTPServer', 1)
            print pesquisar_script('Script',1)
            print pesquisar_title('Title',1)
            print SSLv2('SSLv2', 1)
            print SSLv3('SSLv3', 1)
            print TLSv1_0('TLSv1_0', 1)
            print TLSv1_1('TLSv1_1', 1)
            print TLSv1_2('TLSv1_2', 1)
            print TLSv1_3('TLSv1_3', 1)

            palavra = '[!] '
            with open('sprint.txt') as f:
                alerts = f.read().count(palavra)
                print('Tem %i alertas no seu site.'%(alerts))
                  

            palavra = '(Medium)'
            with open('sprint.txt') as f:
                ocorrencias = f.read().count(palavra)
                print('Tem %i alertas no seu site'%(correncias))  

            palavra = '(Low)'
            with open ('sprint.txt') as f:
                ocorrencias_b = f.read().count(palavra)
                print(ocorrencias_b)

            palavra = '(High)'
            with open('sprint.txt') as f:
                ocorrencias_c = f.read().count(palavra)
                print(ocorrencias_c)
            palavra = '(Good)'
            with open('sprint.txt') as f:
                ocorrencias_c = f.read().count(palavra)
                print(ocorrencias_c)

    root = Tk()    
    root.title('Anne: Intelligence Aritificial For Security Web')
    root.geometry("1024x576")
    root.resizable(0, 0)
    image=PhotoImage(file="src/bk.png")
    image=image.subsample(1,1)
    labelimage = Label(image=image)
    labelimage.place(x=0, y=0, relwidth=1.0, relheight=1.0)
    Aplication(root)    
    root.mainloop()

else:    
    subprocess.Popen("sudo apt-get install python2.7", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo apt-get install idle-python2.7", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo apt-get update", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo apt-get install -y w3af", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo apt-get update", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo apt-get install -y python-pip", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo pip install --upgrade pip", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo apt-get install liballegro4-dev", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo pip install beautifulsoup4", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo apt-get install zaproxy", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo gem install zapr", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo apt-get -y install npm libyaml-dev libxslt1-dev libxml2-dev", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo pip install pyClamd==0.4.0 PyGithub==1.21.0 GitPython==2.1.15 pybloomfiltermmap==0.3.14 phply==0.9.1 nltk==3.0.1 tblib==0.2.0 pdfminer==20140328 futures==3.2.0 pyOpenSSL==18.0.0 ndg-httpsclient==0.4.0 lxml==3.4.4 scapy==2.4.0 guess-language==0.2 cluster==1.1.1b3 msgpack==0.5.6 python-ntlm==1.0.1 halberd==0.2.4 darts.util.lru==0.5 Jinja2==2.10 vulndb==0.1.1 markdown==2.6.1 psutil==5.4.8 ds-store==1.1.2 termcolor==1.1.0 mitmproxy==0.13 ruamel.ordereddict==0.4.8 Flask==0.10.1 PyYAML==3.12 tldextract==1.7.2 pebble==4.3.8 acora==2.1 esmre==0.3.1 diff-match-patch==20121119 bravado-core==5.15.0 lz4==1.1.0 vulners==1.3.0 ipaddresses==0.0.2", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo apt-get install snapd", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("sudo apt-get install -y git", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("pip install pybrain", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("pip install scipy", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("pip install matploib", stdout=subprocess.PIPE, shell=True)
    subprocess.Popen("pip install reportlab", stdout=subprocess.PIPE, shell=True)
 