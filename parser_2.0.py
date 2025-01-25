from selenium import webdriver
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from browsermobproxy import Server
from mitmproxy import http, ctx, proxy, options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.addons import script
from selenium.webdriver.chrome.options import Options as ChromeOptions
from mitmproxy.addons import termlog
import threading
import random
import json
import os
import glob
import base64
import asyncio
import re
from bs4 import BeautifulSoup
import websockets


    # def response(self, flow: http.HTTPFlow):
    #     # Перехватываем ответ и выводим только URL
    #     with self.lock:
    #         print("==================== Response ====================")
    #         print(f"URL: {flow.request.url}")
    #         print("===================================================")

# class Addon:
#     def __init__(self):
#         self.lock = threading.Lock()

#     def request(self, flow: http.HTTPFlow):
#         # Проверяем, содержит ли URL текст "audioclip"
#         if "audioclip" in flow.request.url:
#             # Перехватываем запрос и выводим только URL
#             with self.lock:
#                 with open(f"C:\\Projects\\insta_parser\\pages\\audios.html",'w',encoding="utf-8") as file:
#                      file.write(f"URL: {flow.request.url}\n")
#                 # print("==================== Request =====================")
#                 # print(f"URL: {flow.request.url}")
#                 # print("===================================================")

# async def start_mitmproxy():
#     mitmproxy_options = options.Options(listen_host='127.0.0.1', listen_port=8080)
#     # mitmproxy_options.update(
#     #      console_eventlog_verbosity="error"
#     # )
#     m = DumpMaster(options=mitmproxy_options)
#     m.addons.add(Addon())
#     await asyncio.create_task(m.run())
    


# mitmproxy_thread = threading.Thread(target=lambda: asyncio.run(start_mitmproxy()))
# mitmproxy_thread.start()


# proxy = Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = "127.0.0.1:8080"
useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent=useragent={useragent.random}")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--ignore-certificate-errors")
# options.add_argument("--headless")
options.add_argument("--disable-javascript")
options.add_argument("--disable-features=PermissionsPolicy")
options.add_argument("--disable-features=SensorExtraClasses")
options.add_argument("--remote-debugging-port=9222")
options.set_capability("pageLoadStrategy", "eager")

# options.add_argument("--proxy-server=http://127.0.0.1:8080")



driver = webdriver.Chrome(options=options)





# async def get_network_responses():
#     async with websockets.connect('ws://127.0.0.1:9222/devtools/browser') as websocket:
#         # Отправляем запрос на получение списка доступных страниц
#         await websocket.send(json.dumps({"id": 1, "method": "Target.getTargets"}))
#         response = await websocket.recv()
#         targets = json.loads(response)['result']['targetInfos']

#         # Ищем ID страницы с загруженным URL
#         page_id = None
#         for target in targets:
#             if target['url'] == 'https://instagram.com/':
#                 page_id = target['targetId']
#                 break

#         if not page_id:
#             print("Страница Instagram не найдена")
#             return

#         # Отправляем запрос на подключение к странице
#         await websocket.send(json.dumps({"id": 2, "method": "Target.attachToTarget", "params": {"targetId": page_id, "flatten": True}}))
#         response = await websocket.recv()
#         session_id = json.loads(response)['result']['sessionId']

#         # Отправляем запрос на включение сбора сетевых данных
#         await websocket.send(json.dumps({"id": 3, "method": "Network.enable", "params": {}}))

#         # Ожидаем получение данных от страницы
#         while True:
#             response = await websocket.recv()
#             response_json = json.loads(response)
#             if 'method' in response_json:
#                 if response_json['method'] == 'Network.responseReceived':
#                     print(response_json['params']['response']['url'])
#             else:
#                 print(response_json)









driver.get('https://instagram.com/')
# asyncio.run(get_network_responses())
time.sleep(5)




try:
    button_ru = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Отклонить необязательные файлы cookie")]'))
    )
    print('отклоняем куки')
except: #TimeoutException:
    # button_ru = None  # Если элемент не найден, присваиваем None
     pass

try:
    button_eng = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Decline optional cookies")]'))
    )
    print('Нажимаем')
except: #TimeoutException:
    # button_eng = None  # Если элемент не найден, присваиваем None
    pass


# if button_ru or button_eng:
#     try: button_ru.click()
#     except: button_eng.click()


try:
    login = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Телефон, имя пользователя или эл. адрес"]'))
    )
    login.send_keys('usename')
    print('ввели логин')
except:
    login = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Phone number, username, or email"]'))
    )
    login.send_keys('username')

try:
    passwd= WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Пароль"]'))
    )
    passwd.send_keys('passwd')
    print('Ввели пароль')
except:
    passwd= WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Password"]'))
    )
    passwd.send_keys('passwd')

try:
    submit_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))
    )

    submit_button.click()
    time.sleep(10)
except:
    pass
try:
    direct_svg = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'svg[aria-label="Direct"]'))
    )
    direct_svg.click()
except:
    direct_svg.click()
finally:
     print("ERROR")

time.sleep(2)



try:
    button_not_now = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Не сейчас")]'))
    )
    button_not_now.click()

except TimeoutException:
    pass # Если элемент не найден, присваиваем None

elements = []  # Инициализируем список элементов
max_scroll_attempts = 2  # Максимальное количество попыток прокрутки
scroll_attempts = 0  # Счетчик попыток прокрутки

while scroll_attempts < max_scroll_attempts:
    # Прокрутите страницу к последнему элементу
    last_element = elements[-1] if elements else None
    if last_element:
        driver.execute_script("arguments[0].scrollIntoView();", last_element)
    else:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Ожидайте некоторое время, чтобы дать странице время загрузить новые элементы
    time.sleep(2)

    # Найдите все элементы с указанным классом
    new_elements = driver.find_elements(By.CSS_SELECTOR, '.x13dflua.x19991ni')

    # Проверьте, есть ли новые элементы, которых еще нет в списке
    new_elements = [element for element in new_elements if element not in elements]

    # Если есть новые элементы, добавьте их в список
    if new_elements:
        elements.extend(new_elements)
        scroll_attempts = 0  # Сброс счетчика, так как есть новые элементы
        print(f"Found {len(new_elements)} new elements.")
    else:
        scroll_attempts += 1  # Увеличение счетчика попыток, если новых элементов нет
        print(f"No new elements found. Scroll attempts: {scroll_attempts}")

    time.sleep(2)

for index, element in enumerate(elements):
    try:
        element.click()
    except:
        element.click()
    finally:
         element.click()
    time.sleep(2)

    # prev_div_elements = set()
    try:
        # hide_elements = WebDriverWait(driver, 10).until(
        #             EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.x78zum5.xdt5ytf[style*="height:"]'))
        #         )
                
        # prev_hide_elements = set()
        time.sleep(2)
        count=1
        prev_elements = []
        while True:
            try:
                all_elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class="x78zum5 xdt5ytf"]'))
                )
                if all_elements == prev_elements:
                    print("На странице больше нет новых элементов")
                    break

                prev_elements = all_elements[:]


                first = all_elements[0]
                driver.execute_script("arguments[0].scrollIntoView();", first)
                time.sleep(1)
                print('Прокрутка к первому скрытому сверху')

            except Exception as e:
                print('Ошибка:', e)
                break

        prev_elements=[]
        blocks=[]
        # while True:
        try:
                main_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.x1uipg7g.xu3j5b3.xol2nv.xlauuyb.x26u7qi.x19p7ews.x78zum5.xdt5ytf.x1iyjqo2.x6ikm8r.x10wlt62[role="grid"]'))
                )
                
                hide_elements = main_element.find_elements(By.CSS_SELECTOR, 'div.x13dflua.x19991ni')

                # hide_elements = WebDriverWait(driver, 10).until(
                #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.x78zum5.xdt5ytf'))
                # )
                
                for i in hide_elements:
                     outer = i.get_attribute("outerHTML")
                     blocks.append(outer)
                     driver.execute_script("arguments[0].scrollIntoView();", i)
                    #  driver.save_screenshot(f"C:\\Projects\\insta_parser\\imgs\\img_{count}.png")
                    #  count += 1
                     print('Прокрутка')
                with open(f"C:\\Projects\\insta_parser\\pages\\page_{index}.html",'w',encoding="utf-8") as file:
                    for block in blocks:
                          file.write(block + '\n')

                # first_hide_el = hide_elements[0]
                # el_index = hide_elements.index(first_hide_el)

                # if el_index + 1 < len(hide_elements):
                #     el_to_scroll = hide_elements[el_index + 1]
                #     driver.save_screenshot(f"C:\\Projects\\insta_parser\\imgs\\img_{count}.png")
                #     count += 1
                #     driver.execute_script("arguments[0].scrollIntoView();", el_to_scroll)
                #     print('Прокрутка')
                #     # Добавим небольшую задержку перед следующей проверкой
                #     time.sleep(1)
                # else:
                #     print("Дошли до конца")
                #     break

            # except Exception as e:
            #     print('Ошибка:', e)
            #     break


        # while True:
        #     try:
        #         # all_elements = WebDriverWait(driver, 10).until(
        #         #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class="x78zum5 xdt5ytf"]'))
        #         # )
                
        #         # visible_elements = []
        #         # for element in all_elements:
        #         #     if not element.get_attribute("style") or "height:" not in element.get_attribute("style"):
        #         #         visible_elements.append(element)
        #         hide_elements = WebDriverWait(driver, 10).until(
        #             EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.x78zum5.xdt5ytf'))
        #         )
        #         # print(hide_elements)
        #         # first_visible_element = visible_elements[0]
        #         # el_index = all_elements.index(first_visible_element)
        #         # print(el_index)
        #         # first_hide_element = all_elements[el_index - 1]
        #         first_hide_el=hide_elements[0]
        #         print(first_hide_el)
        #         el_index=hide_elements.index(first_hide_el)
        #         print(el_index)
        #         if el_index + 1 < len(hide_elements):
        #             el_to_scroll = hide_elements[el_index + 1]
        #             print(el_to_scroll)
        #             driver.save_screenshot(f"C:\\Projects\\insta_parser\\imgs\\img_{count}.png")
        #             count+=1
        #             driver.execute_script("arguments[0].scrollIntoView();", el_to_scroll)
        #             print('Прокрутка')
        #         else:
        #             print("Дошли до конца")
        #             break


        except Exception as e:
                print('Ошибка:', e)



    #     # Создаем объект soup и добавляем в него HTML-код всех блоков
    #     soup = BeautifulSoup('', 'html.parser')
    #     for content in blocks_content:
    #         soup.append(BeautifulSoup(content, 'html.parser'))

    #     # Записываем HTML содержимое в файл
    #     with open(f"C:\\Projects\\insta_parser\\pages\\blocks_{index}.html", "w", encoding='utf-8') as file:
    #         file.write(soup.prettify())

    #     source=driver.page_source

    #     filename = f'C:\\Projects\\insta_parser\\pages\\page_{index}.html'
    #     print('создали файл')
    #     with open(filename, 'w', encoding='utf-8') as file:
    #         file.write(source)
    #     with open(filename, 'r', encoding='utf-8') as file:
    #         source = file.read()

    #     # Создание объекта BeautifulSoup
    #     soup = BeautifulSoup(source, 'html.parser')

    #     # Удаление всех тегов <script>
    #     for script in soup.find_all('script'):
    #         script.extract()

    #     # Получение очищенного HTML-кода
    #     source_cleaned = str(soup)

    #     # Запись очищенного содержимого в файл
    #     with open(filename, 'w', encoding='utf-8') as file:
    #         file.write(source_cleaned)
    #     print('записали в файл')
    except:
        print('Не на той странице')
    
    time.sleep(2)


    # with open(f"C:\\Projects\\insta_parser\\pages\\page_{index}.html", "r", encoding="utf-8") as page_file:
    #     page_content = page_file.read()

    #     with open(f"C:\\Projects\\insta_parser\\pages\\blocks_{index}.html", "r", encoding="utf-8") as blocks_file:
    #         blocks_content = blocks_file.read()

    #     # Парсинг содержимого файлов с использованием BeautifulSoup
    #     page_soup = BeautifulSoup(page_content, "html.parser")
    #     blocks_soup = BeautifulSoup(blocks_content, "html.parser")

    #     # Находим и вырезаем блоки с атрибутом style из файла page
    #     page_blocks_with_style = page_soup.find_all("div", class_="x78zum5 xdt5ytf", style=True)
    #     for block in page_blocks_with_style:
    #         block.extract()

    #     # Находим блок, в который нужно вставить содержимое из blocks
    #     page_insertion_point = page_soup.find("div", class_="x1n2onr6")

    #     # Вставляем содержимое из blocks в page
    #     blocks_contents = blocks_soup.find_all("div", class_="x78zum5 xdt5ytf")
    #     for block in blocks_contents:
    #         page_insertion_point.append(block)

    #     # Сохранение обновленного содержимого файла page
    #     with open(f"C:\\Projects\\insta_parser\\pages\\page_{index}_updated.html", "w", encoding="utf-8") as output_file:
    #         output_file.write(str(page_soup))



directory_path = "C:\\Projects\\insta_parser\\tmp_pages"
file_pattern = os.path.join(directory_path, "page_*.html")




for file_path in glob.glob(file_pattern):
                    with open(file_path, "r", encoding='utf-8') as file:
                        soup = BeautifulSoup(file, "html.parser")
                        
                    meta_tag = soup.find('meta', attrs={"http-equiv": "content-type"})
                    if meta_tag and "windows-1251" in meta_tag['content']:
                        meta_tag['content'] = meta_tag['content'].replace("windows-1251", "utf-8")
                    
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(str(soup))


# directory_path = "C:\\Projects\\insta_parser\\tmp_pages"
# file_pattern = os.path.join(directory_path, "page_*.html")

# for file_path in glob.glob(file_pattern):
#             with open(file_path, "r", encoding='utf-8') as file:
#                 soup = BeautifulSoup(file, "html.parser")
                
#             meta_tag = soup.find('meta', attrs={"http-equiv": "content-type"})
#             if meta_tag and "windows-1251" in meta_tag['content']:
#                 meta_tag['content'] = meta_tag['content'].replace("windows-1251", "utf-8")
            
#             with open(file_path, "w", encoding="utf-8") as file:
#                 file.write(str(soup))


# try:
#     while True:
#         # Ожидайте, пока элементы с указанным классом станут видимыми и кликабельными
#         new_elements = WebDriverWait(driver, 20).until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.x13dflua.x19991ni'))
#         )

#         # Проверьте, есть ли хотя бы один новый элемент с таким классом
#         if new_elements:
#             print('dialogs founded')

#             # Добавим новые элементы в общий список
#             elements.extend(new_elements)

#             # Выполните клик на последнем элементе
#             last_element = new_elements[-1]
#             last_element.click()
#             time.sleep(5)
#         else:
#             print("elements 'x13dflua x19991ni' not founded")
#             break  # Если больше элементов не найдено, выход из цикла

# except Exception as e:
#     print(f"dialogs not founded {e}")
