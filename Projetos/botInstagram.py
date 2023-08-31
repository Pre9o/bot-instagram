import getpass
import json
import shutil
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

# Configurar as opções do Chrome para o modo headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Adicionar a opção headless
chrome_options.add_argument("--disable-gpu")  # Desativar aceleração de GPU (necessário para o modo headless)

# Inicializar o driver do Chrome com as opções configuradas
driver = webdriver.Chrome(options=chrome_options)

class Instagram:
    def __init__(self, username, password, username_for_scrape):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.bot = driver
        self.username_for_scrape = username_for_scrape
        self.login()
        
    def removeFiles(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        #remover todos os arquvios .json do diretorio
        for file in os.listdir(current_directory):
            if file.endswith(".json"):
                file_path = os.path.join(current_directory, file)
                os.remove(file_path)
                
        for file in os.listdir(current_directory):
            if file.endswith(".txt"):
                file_path = os.path.join(current_directory, file)
                os.remove(file_path)
             
        
    def selectData(self):     
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        script_file_path = os.path.join(current_directory, "script.js")
        
        default_file_type = ".json"
        current_file_type = default_file_type
        
        print("Selecione o arquivo que deseja visualizar: ")
        print("1 - JSON")
        print("2 - TXT")
        print("0 - Sair")
               
        while True:
            file_option = int(input("Digite a opção desejada: "))
            
            if file_option == 0:
                break
            
            elif file_option == 1:
                current_file_type = ".json"
                break
            
            elif file_option == 2:
                current_file_type = ".txt"
                break
            
            else:
                print("Opção inválida")          
            
        
        input_file_name = "data.json"
        input_file_path = os.path.join(current_directory, input_file_name)
                        
   
        if current_file_type == ".json":
            output_file_name = self.username_for_scrape + "followers.json"
            output_file_path = os.path.join(current_directory, output_file_name)
            
            with open(input_file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                
            followers = data.get('data', {}).get('followers', [])
            
            with open(output_file_path, "w", encoding="utf-8") as json_file:
                json.dump(followers, json_file, indent=2, ensure_ascii=False)
                
            print("Arquivo criado com sucesso")
            
        elif current_file_type == ".txt":
            output_file_name = self.username_for_scrape + "followers.txt"
            output_file_path = os.path.join(current_directory, output_file_name)
            
            with open(input_file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                
            followers = data.get('data', {}).get('followers', [])
            
            with open(output_file_path, "w", encoding="utf-8") as txt_file:
                for follower in followers:
                    txt_file.write(str(follower) + "\n")
                    
            print("Arquivo criado com sucesso")

        if current_file_type == ".json":
            output_file_name = self.username_for_scrape + "followings.json"
            output_file_path = os.path.join(current_directory, output_file_name)
            
            with open(input_file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                
            following = data.get('data', {}).get('followings', [])
            
            with open(output_file_path, "w", encoding="utf-8") as json_file:
                json.dump(following, json_file, indent=2, ensure_ascii=False)
                
            print("Arquivo criado com sucesso")
            
        elif current_file_type == ".txt":
            output_file_name = self.username_for_scrape + "followings.txt"
            output_file_path = os.path.join(current_directory, output_file_name)
            
            with open(input_file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                
            following = data.get('data', {}).get('followings', [])
            
            with open(output_file_path, "w", encoding="utf-8") as txt_file:
                for follower in following:
                    txt_file.write(str(follower) + "\n")
                    
            print("Arquivo criado com sucesso")
                    
        if current_file_type == ".json":
            output_file_name = self.username_for_scrape + "iDontFollowBack.json"
            output_file_path = os.path.join(current_directory, output_file_name)
            
            with open(input_file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                
            i_dont_follow_back = data.get('data', {}).get('iDontFollowBack', [])
            
            with open(output_file_path, "w", encoding="utf-8") as json_file:
                json.dump(i_dont_follow_back, json_file, indent=2, ensure_ascii=False)
                
            print("Arquivo criado com sucesso")
            
        elif current_file_type == ".txt":
            output_file_name = self.username_for_scrape + "iDontFollowBack.txt"
            output_file_path = os.path.join(current_directory, output_file_name)
            
            with open(input_file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                
            i_dont_follow_back = data.get('data', {}).get('iDontFollowBack', [])
            
            with open(output_file_path, "w", encoding="utf-8") as txt_file:
                for follower in i_dont_follow_back:
                    txt_file.write(str(follower) + "\n")
                    
            print("Arquivo criado com sucesso")
                    
        if current_file_type == ".json":
            output_file_name = self.username_for_scrape + "dontFollowMeBack.json"
            output_file_path = os.path.join(current_directory, output_file_name)
            
            with open(input_file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)

            dont_follow_me_back = data.get('data', {}).get('dontFollowMeBack', [])

            with open(output_file_path, "w", encoding="utf-8") as json_file:
                json.dump(dont_follow_me_back, json_file, indent=2, ensure_ascii=False)
                
            print("Arquivo criado com sucesso")
            
        elif current_file_type == ".txt":
            output_file_name = self.username_for_scrape + "dontFollowMeBack.txt"
            output_file_path = os.path.join(current_directory, output_file_name)
            
            with open(input_file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                
            dont_follow_me_back = data.get('data', {}).get('dontFollowMeBack', [])
            
            with open(output_file_path, "w", encoding="utf-8") as txt_file:
                for follower in dont_follow_me_back:
                    txt_file.write(str(follower) + "\n")
                    
            print("Arquivo criado com sucesso")
                                

        if current_file_type == ".json":
            print("O arquivo data.json contém todos os dados")
            
        elif current_file_type == ".txt":
            with open (input_file_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                
            #copiar tudo para um txt
            output_file_name = self.username_for_scrape + "data.txt"
            output_file_path = os.path.join(current_directory, output_file_name)
            
            with open(output_file_path, "w", encoding="utf-8") as txt_file:
                txt_file.write("Seguidores: \n")
                for follower in data.get('data', {}).get('followers', []):
                    txt_file.write(str(follower) + "\n")
                    
                txt_file.write("\nSeguindo: \n")
                for follower in data.get('data', {}).get('following', []):
                    txt_file.write(str(follower) + "\n")
                    
                txt_file.write("\nNão sigo de volta: \n")
                for follower in data.get('data', {}).get('iDontFollowBack', []):
                    txt_file.write(str(follower) + "\n")
                    
                txt_file.write("\nNão me segue de volta: \n")
                for follower in data.get('data', {}).get('dontFollowMeBack', []):
                    txt_file.write(str(follower) + "\n")
                    
            os.remove(input_file_path)
            print("Arquivo criado com sucesso")
            
        
        
        with open(script_file_path, "r") as js_file:
            js_code = js_file.read()
            js_code = js_code.replace(self.username_for_scrape, "cuardido")
            
        with open(script_file_path, "w") as js_file:
            js_file.write(js_code)          
        
                
                
    def moveData(self):
        # Especifique o caminho do arquivo original e o novo caminho de destino
        download_directory = os.path.join(os.path.expanduser("~"), "Downloads")
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        input_file_name = "data.json"
        input_file_path = os.path.join(download_directory, input_file_name)
        
        output_file_name = "data.json"
        output_file_path = os.path.join(current_directory, output_file_name)
        
        # Mova o arquivo para o novo caminho de destino
        shutil.move(input_file_path, output_file_path)
        
        self.selectData()
        
        
    def scrape(self):
        self.bot.get('https://www.instagram.com/' + self.username_for_scrape + '/')
        
        time.sleep(5)
        
        self.removeFiles()
        
        current_directory = os.path.dirname(os.path.abspath(__file__))
        input_file_name = "script.js"
        input_file_path = os.path.join(current_directory, input_file_name)
        
        with open(input_file_path, "r") as js_file:
            js_code = js_file.read()

        self.bot.execute_script(js_code)
        
        time.sleep(100)

        #fechar o driver
        self.bot.close()
        
        self.moveData()
        
    def login(self):
        self.bot.get(self.base_url)
        
        enter_username = WebDriverWait(self.bot, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'username')))
        
        enter_username.send_keys(self.username)
        
        enter_password = WebDriverWait(self.bot, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'password')))
        
        enter_password.send_keys(self.password)
        
        enter_password.send_keys(Keys.RETURN)
        
        time.sleep(5)
        
        self.scrape()
        
def main():
    username = input("Digite seu nome de usuário: ")
    password = getpass.getpass("Digite sua senha: ")
    
    username_for_scrape = input("Digite o nome de usuário que deseja fazer o scrape: ")
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    input_file_name = "script.js"
    input_file_path = os.path.join(current_directory, input_file_name)

    #modificar o arquivo script.js e colocar o nome de usuário que deseja fazer o scrape
    with open(input_file_path, "r") as js_file:
        js_code = js_file.read()
        js_code = js_code.replace("cuardido", username_for_scrape)
        
    with open(input_file_path, "w") as js_file:
        js_file.write(js_code)
        
    Instagram(username, password, username_for_scrape)
    
    with open(input_file_path, "r") as js_file:
        js_code = js_file.read()
        js_code = js_code.replace(username_for_scrape, "cuardido")
        
    with open(input_file_path, "w") as js_file:
        js_file.write(js_code)
    
main()