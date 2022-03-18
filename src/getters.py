import requests
from bs4 import BeautifulSoup

def get_css_files(url):
    
    # Faz o Request ao URL e obtém objeto de resposta

    response=requests.get(url)
  
    # Etapa de parsing
    
    soup=BeautifulSoup(response.text, 'html.parser')
  
    # Encontra todos os hyperlinks presentes na webpage
    
    links=soup.find_all('link')

    i=0
    try:
        for link in links:
            # Aqui eu faço uma restrição para obter somente arquivos PDF
            if ('.css' in link.get('href')):
                i += 1
                factor = i
                print("Baixando arquivo: ", i)
  
                # Obtém objeto de resposta para o link

                print(link.get('href'))
                response = requests.get(url+link.get('href'))
                #response = requests.get(link.get('href'))
                
                # Escreve o conteúdo em arquivos PDF

                css=open("css_templates/file_"+str(factor)+".css", 'wb')
                css.write(response.content)
                css.close()
                print("Arquivo ", factor, " baixado")
        print("Todos os arquivos baixados com sucesso!")
    # Mensagem caso ocorram erros do tipo Runtime, TypeError, NameError
    except (RuntimeError, TypeError, NameError):
        print("Erro com algum link específico!")  

def get_js_files(url):
    
    # Faz o Request ao URL e obtém objeto de resposta

    response=requests.get(url)
  
    # Etapa de parsing
    
    soup=BeautifulSoup(response.text, 'html.parser')
  
    # Encontra todos os hyperlinks presentes na webpage
    
    links=soup.find_all('link')

    i=0
    try:
        for link in links:
            # Aqui eu faço uma restrição para obter somente arquivos PDF
            if ('.js' in link.get('href')):
                i += 1
                factor = i
                print("Baixando arquivo: ", i)
  
                # Obtém objeto de resposta para o link

                print(link.get('href'))
                response = requests.get(url+link.get('href'))
                #response = requests.get(link.get('href'))
                
                # Escreve o conteúdo em arquivos PDF

                js=open("js_templates/file_"+str(factor)+".txt", 'wb')
                js.write(response.content)
                js.close()
                print("Arquivo ", factor, " baixado")
        print("Todos os arquivos baixados com sucesso!")
    # Mensagem caso ocorram erros do tipo Runtime, TypeError, NameError
    except (RuntimeError, TypeError, NameError):
        print("Erro com algum link específico!")  
