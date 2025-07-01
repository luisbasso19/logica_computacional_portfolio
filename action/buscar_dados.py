from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

def captura_dados():
    options = Options()
    options.add_argument("--headless") #executa o navegador sem interface grafica
    options.add_argument("--disable-gpu") #desabilita a gpu, necessario para evitar erros de renderizacao
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36") #user agent informado para os sites, usado para evitar sistemas de bloqueio de automacao
    options.add_argument("--no-sandbox") #desabilita uma camada de segurança do chrome

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.accuweather.com/pt/br/s%C3%A3o-paulo/45881/current-weather/45881") #a pagina que uso para capturar os dados de previsao do tempo

    try:
        wait = WebDriverWait(driver, 10)

        try: #verifica se a pagina solicita confirmacao de cookies
            botao_ok = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cookie-consent-btn")))
            botao_ok.click()
        except:
            pass  # Se não encontrar, segue sem erro
        
        temp_element = driver.find_element(By.CSS_SELECTOR, "div.display-temp")#realiza a busca do elemento na pagina, usando a selecao por CSS
        temperatura = temp_element.text #captura o texto do elemento encontrado acima

        umidade_element = driver.find_element(By.XPATH, "//div[text()='Umidade']/following-sibling::div[1]")#realiza a busca usando o XPATH da pagina.
        umidade = umidade_element.text #captura o texto do elemento encontrado acima       

        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # captura e formata a data e hora atual

        #retorna um dicionario com os valores capturados da pagina
        return {
            "temperatura": temperatura,
            "umidade": umidade,
            "data_hora": data_hora,
            "erro": None
        }
    #trata algum eventual erro na captura, retornando para o usuario
    except Exception as e:
        return {"temperatura": None, "umidade": None, "data_hora": None, "erro": str(e)}
    #quando tudo estiver terminado ele fecha o navegador aberto
    finally:
        driver.quit()
