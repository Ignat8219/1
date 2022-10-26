from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from config import url, login, password, name



browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url + 'login')
assert WebDriverWait(browser, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'form-control')))
browser.find_element(By.CSS_SELECTOR, 'input[id=email]').send_keys(login)
browser.find_element(By.CSS_SELECTOR, 'input[id=pass]').send_keys(password)
browser.find_element(By.CSS_SELECTOR, 'button[class*=btn-success]').click()
assert WebDriverWait(browser, 6).until(EC.url_to_be('https://petfriends.skillfactory.ru/all_pets'))
assert WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//h1'))).text == 'PetFriends'
browser.find_element(By.CSS_SELECTOR, 'a[class*=nav-link]').click()
assert WebDriverWait(browser, 6).until(EC.url_to_be('https://petfriends.skillfactory.ru/my_pets'))
assert WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//h2'))).text == name
browser.implicitly_wait(10)
pets_numb = browser.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1]

pets = browser.find_elements(By.XPATH, '//div[@id="all_my_pets"]')
images = browser.find_elements(By.CSS_SELECTOR, 'img')
counter = 0
pet_names = []
pet_uniq = []
for i in range(len(pets)):
    pets_list = pets[i].text.upper().split('\n')
pets_list = pets_list[1::2]
for i in range(len(images)):
    if images[i].get_attribute('src') == '':
        counter += 1
for pet in pets_list:
    assert len(pet.split(' ')) == 3
    pet_names.append(pet.split(' ')[0])
    if pet in pet_uniq:
        continue
    else:
        pet_uniq.append(pet)
assert int(pets_numb) == int(len(pets_list))
assert (round(((counter * 100) / int(pets_numb)))) <= 50
assert len(pet_names) == len(set(pet_names))
assert pets_list == pet_uniq
browser.quit()