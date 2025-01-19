import pandas as pd
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

error_url = []
service_directory = "path/to/chromedriver.exe"

def crawl(url, download_dir):


    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": download_dir,  # Set the download directory
        "download.prompt_for_download": False,      # Disable download prompt
        "download.directory_upgrade": True,         # Automatically upgrade the directory
        "safebrowsing.enabled": True                # Enable safe browsing
    }

    options.add_experimental_option("prefs", prefs)


    service = Service(service_directory)
    driver = webdriver.Chrome(service=service, options=options)

    # driver.get("https://jakarta.bps.go.id/id/statistics-table/2/MzczIzI=/curah-hujan-di-stasiun-kemayoran-menurut-bulan--mm-.html")
    driver.get(url)

    wait = WebDriverWait(driver, 20)
    try:
        # image_wbs = driver.find_element(By.CSS_SELECTOR, 'div > img[alt="WBS"]')
        tutup_button = driver.find_element(By.XPATH, '//*[@id="headlessui-dialog-panel-:rl:"]/div[2]/button')
        tutup_button.click()

        year_data = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class="max-sm:hidden"] > button')))

        for x in year_data:
            x.click()

            choose_download_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="h-full"] > button[data-headlessui-state]')))
            choose_download_button.click()

            xlsx_download_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="p-1"] > button:nth-child(1)')))
            xlsx_download_button.click()

            # This timeout needed to makesure downloaded file has downloaded successfully
            time.sleep(5.0) # you can change above 2.0 seconds
    except:
        error_url.append(url)
    finally:
        driver.quit() 


def main():
    df = pd.read_csv("test.csv")
    curr_dir = os.getcwd()
    for _, row in df.iterrows():
        tmp_dir = f'{curr_dir}\\{row["provinsi"]}\\{row["stasiun"]}'
        if not os.path.exists(tmp_dir):
            os.makedirs(os.path.join(row["provinsi"],row["stasiun"]))
        crawl(row["link"], tmp_dir)

main() 
