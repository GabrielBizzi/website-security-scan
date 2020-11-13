def pesquisar_country( txt, posicao ):
    resultado = ""
    with open( 'sprint.txt', 'r' ) as a:
        for linha in a:
            if resultado == "":
                if txt in linha:
                    resultado = linha
                    res = resultado.split('= Country')[posicao].strip('\n')
                    return res;
        else: a.close()
    return None; 
def pesquisar_ip( txt, posicao ):
    resultado = ""
    with open( 'sprint.txt', 'r' ) as b:
        for linha in b:
            if resultado == "":
                if txt in linha:
                    resultado = linha
                    res = resultado.split('= IP')[posicao].strip('\n')
                    return res;
        else: b.close()
    return None; 
def pesquisar_servidor( txt, posicao ):
    resultado = ""
    with open( 'sprint.txt', 'r' ) as c:
        for linha in c:
            if resultado == "":
                if txt in linha:
                    resultado = linha
                    res = resultado.split('= HTTPServer')[posicao].strip('\n')
                    return res;
        else: c.close()
    return None; 
def pesquisar_script( txt, posicao ):
    resultado = ""
    with open( 'sprint.txt', 'r' ) as d:
        for linha in d:
            if resultado == "":
                if txt in linha:
                    resultado = linha
                    res = resultado.split('= Script')[posicao].strip('\n')
                    return res;
        else: d.close()
    return None; 
def pesquisar_title( txt, posicao ):
    resultado = ""
    with open( 'sprint.txt', 'r' ) as e:
        for linha in e:
            if resultado == "":
                if txt in linha:
                    resultado = linha
                    res = resultado.split('= Title')[posicao].strip('\n')
                    return res;
        else: e.close()
    return None;  
def pesquisar_erros_wordpress( txt, posicao ):
    resultado = ""
    with open( 'sprint.txt', 'r' ) as f:
        for linhas in f:
            if resultado == "":
                if txt in linhas:
                    resultado = linhas
                    res = resultado.split('[!] ')[posicao].strip('\n')
                    return res;
        else: f.close()
    return None;
def SSLv2( txt, posicao ):
    resultado = ""
    with open( 'sprint.txt', 'r' ) as f:
        for linhas in f:
            if resultado == "":
                if txt in linhas:
                    resultado = linhas
                    res = resultado.split('SSLv2 ')[posicao].strip('\n')
                    return res;
        else: f.close()
    return None;
def SSLv3( txt, posicao ):
    resultado = ""
    with open( 'sprint.txt', 'r' ) as f:
        for linhas in f:
            if resultado == "":
                if txt in linhas:
                    resultado = linhas
                    res = resultado.split('SSLv3 ')[posicao].strip('\n')
                    return res;
        else: f.close()
    return None;
def TLSv1_0( txt, posicao ):
    resultado = ""
    with open( 'sprint.txt', 'r' ) as f:
        for linhas in f:
            if resultado == "":
                if txt in linhas:
                    resultado = linhas
                    res = resultado.split('TLSv1.0 ')[posicao].strip('\n')
                    return res;
        else: f.close()
    return None;
def TLSv1_1( txt, posicao ):
    resultado = ""
    with open( 'sprint.txt', 'r' ) as f:
        for linhas in f:
            if resultado == "":
                if txt in linhas:
                    resultado = linhas
                    res = resultado.split('TLSv1.1 ')[posicao].strip('\n')
                    return res;
        else: f.close()
    return None;
def TLSv1_2( txt, posicao ):
    resultado = ""
    with open( 'sprint.txt', 'r' ) as f:
        for linhas in f:
            if resultado == "":
                if txt in linhas:
                    resultado = linhas
                    res = resultado.split('TLSv1.2 ')[posicao].strip('\n')
                    return res;
        else: f.close()
    return None;
def TLSv1_3( txt, posicao ):
    resultado = ""
    with open( 'sprint.txt', 'r' ) as f:
        for linhas in f:
            if resultado == "":
                if txt in linhas:
                    resultado = linhas
                    res = resultado.split('TLSv1.3 ')[posicao].strip('\n')
                    return res;
        else: f.close()
    return None;
#palavra = '[!] '
#with open('sprint.txt') as f:
    #alerts = f.read().count(palavra)
    #print(alerts)


#palavra = '(Medium)'
#with open('sprint.txt') as f:
    #ocorrencias = f.read().count(palavra)
    #print(ocorrencias)  

#palavra = '(Low)'
#with open ('sprint.txt') as f:
    #ocorrencias_b = f.read().count(palavra)
    #print(ocorrencias_b)

#palavra = '(High)'
#with open('sprint.txt') as f:
    #ocorrencias_c = f.read().count(palavra)
    #print(ocorrencias_c)
#palavra = '(Good)'
#with open('sprint.txt') as f:
    #ocorrencias_c = f.read().count(palavra)
    #print(ocorrencias_c)

#if ((ocorrencias > 4) & (ocorrencias_b > 0) & (ocorrencias_c <= 0)):
    #print('O site ta feio fi.')
#else:
    #pass