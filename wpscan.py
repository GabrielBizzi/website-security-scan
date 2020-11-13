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
from collections import Counter

token = '–api-token Rw4mlsKSOvuYfTsUvoIeHyuutL8cutdspWT4xApuvOs'

check_wp_scan = str(subprocess.check_output(['wpscan', '--url', url, '--enumerate', 'u,ap', token]))
time.sleep(3.5)
details_wordpress_scan = (ansi_escape.sub('', check_wp_scan))
logger.warning(details_wordpress_scan)
time.sleep(3.5)

check_scan = str(subprocess.check_output(['whatweb', '-a', '3', '-v', url ]))
time.sleep(3.5)
details_whatweb_scan = (ansi_escape.sub('', check_scan)).replace(',','\n=')
logger.warning(details_whatweb_scan)
time.sleep(3.5)

check = str(subprocess.check_output(['nikto', '-h', 'scanme.nmap.org']))    
time.sleep(3.5)
details_nikto_scan = (ansi_escape.sub('', check))
logger.warning(details_nikto_scan)
time.sleep(3.5)

check_ssl = str(subprocess.check_output(['sslscan', '--show-certificate', url]))
time.sleep(3.5)
details_sslscan_check = (ansi_escape.sub('', check_ssl))
logger.warning(details_sslscan_check)
time.sleep(3.5)

#check_ssl_nc = str(subprocess.check_output(['sslscan', '--no-colour', url]))

check_ssl_conection_http = str(subprocess.check_output(['sslscan', '--http', url]))
time.sleep(3.5)
details_sslscan_two_check_conection = (ansi_escape.sub('', check_ssl_conection_http))
logger.warning(details_sslscan_two_check_conection)
time.sleep(3.5)

check_ssl_conection_regular = str(subprocess.check_output(['sslyze', '--regular', url]))
time.sleep(3.5)
details_sslyze_scan = (ansi_escape.sub('', check_ssl_conection_regular))
logger.warning(details_sslyze_scan)
time.sleep(3.5)

scan_site = str(subprocess.check_output(['sqliv', '-t', url]))
time.sleep(3.5)
details_sqliv_scan = (ansi_escape.sub('', scan_site))
logger.warning(details_sqliv_scan)
time.sleep(3.5)

#check_sql_injection = str(subprocess.check_output(['sqliv', '-d', url,]))

check_url = str(subprocess.check_output(['bash', '/usr/share/zaproxy/zap.sh', '-cmd', '-quickurl', url, '-quickprogress']))
time.sleep(3.5)
details_zap_advanced_scan = (ansi_escape.sub('', check_url))
logger.warning(details_zap_advanced_scan)
time.sleep(3.5)

def frequencia(texto):
    frequencia_por_palavra = [texto.count(p) for p in texto]
    return dict(zip(texto, frequencia_por_palavra))

def popularidade(texto, palavras):
    dFrequencia = frequencia(texto)
    return dict((k, dFrequencia[k]) for k in palavras if k in dFrequencia)

print(popularidade(open('sprint.txt', 'r').read().split(), ['<riskdesc>Low', '(Medium)</riskdesc>', '<riskdesc>Medium', '(Low)</riskdesc>']))

palavra = '(Medium)'
with open('sprint.txt') as f:
    ocorrencias = f.read().count(palavra)
print(ocorrencias) # num de vezes que a palavra aparece


{'''

Fundo vermelho: cifra NULL (sem criptografia)

Vermelho: cifra quebrada (<= 40 bits), protocolo quebrado (SSLv2 ou SSLv3) ou algoritmo de assinatura de certificado quebrado (MD5)

Amarelo: cifra fraca (<= 56 bits ou RC4) ou algoritmo de assinatura de certificado fraco (SHA-1)

Roxo: cifra anônima (ADH ou AECDH)

'''}