from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

def captura_dados():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.accuweather.com/pt/br/s%C3%A3o-paulo/45881/current-weather/45881")

    try:
        wait = WebDriverWait(driver, 10)

        try:
            botao_ok = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cookie-consent-btn")))
            botao_ok.click()
        except:
            pass  # Se não encontrar, segue sem erro
        
        temp_element = driver.find_element(By.CSS_SELECTOR, "div.display-temp")
        temperatura = temp_element.text        

        umidade_element = driver.find_element(By.XPATH, "//div[text()='Umidade']/following-sibling::div[1]")
        umidade = umidade_element.text        

        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "temperatura": temperatura,
            "umidade": umidade,
            "data_hora": data_hora,
            "erro": None
        }

    except Exception as e:
        return {"temperatura": None, "umidade": None, "data_hora": None, "erro": str(e)}
    finally:
        driver.quit()
