import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()
   # Переходим на страницу авторизации
   driver.get('https://petfriends.skillfactory.ru/login')


   yield driver
   time.sleep(5)
   driver.quit()



def test_show_all_pets(driver):
   # Вводим email
   driver.find_element(By.ID, 'email').send_keys('ioanpljnkv@mail.ru')
   # Ожидаем, что на странице появится поле ввода емайла
   assert WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'email')))
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys('iX3dh9eDEvtNf')
   # Ожидается что на странице появится поле ввода пароля и кнопка входа будет кликабельной
   assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "pass")))
   assert WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

   # Ищем на странице все фотографии, имена, породу (вид) и возраст питомцев:
   images = driver.find_elements(By.CSS_SELECTOR, '.card-img-top')
   names = driver.find_elements(By.CSS_SELECTOR, 'h5.card-title')
   descriptions = driver.find_elements(By.CSS_SELECTOR, 'p.card-text')

   # Проверяем, что на странице есть фотографии питомцев, имена, порода (вид) и возраст питомцев не пустые строки:
   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
   print(len(names))

def test_show_my_pets(driver):
   # Вводим email, пароль, открываем главную страницу сайта
   driver.find_element(By.ID, 'email').send_keys('ioanpljnkv@mail.ru')
   driver.find_element(By.ID, 'pass').send_keys('iX3dh9eDEvtNf')
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   #Настраиваем переменную явного ожидания:
   driver.implicitly_wait(3)
   assert driver.find_element(By.LINK_TEXT, "Мои питомцы")
   # Открываем страницу /my_pets.
   driver.find_element(By.LINK_TEXT, "Мои питомцы").click()


  # Ищем количество карточек и сравниваем со статистикой:
   cards = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr')
   statistics = driver.find_element(By.CSS_SELECTOR, 'div.task3 div')
   amount = statistics.text.split(': ')
   assert len(cards) == int(amount[1][0])

   # Ищем в теле таблицы все фотографии питомцев и проверяем, что количество питомцев с фото больше половины:
   images = driver.find_elements(By.CSS_SELECTOR, 'img')
   statistics = driver.find_element(By.CSS_SELECTOR, 'div.task3 div')
   amount = statistics.text.split(': ')
   count = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         count += 1
   assert count > (int(amount[1][0]) // 2)

   # Ищем все имена питомцев и проверяем их уникальность:
   names = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets table tbody tr')
   pet_name = []
   for i in range(len(names)):
      parts = names[i].text.split(' ')
      pet_name.append(parts[0])
   for i in range(len(pet_name) - 1):
      for j in range(i + 1, len(pet_name)):
         assert pet_name[i] != pet_name[j]
   print(pet_name)

   # Ищем в теле таблицы все породы питомцев:
   types = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets table tbody tr')
   my_pets_type = []
   for i in range(len(types)):
      parts = types[i].text.split(' ')
      my_pets_type.append(parts[1])
   print(my_pets_type)


      # assert wait.until(EC.visibility_of(type_my_pets[i]))

   # Ищем на странице /my_pets всю статистику пользователя,
   # и вычленяем из полученных данных количество питомцев пользователя:
   all_statistics = driver.find_element(By.CSS_SELECTOR, 'html > body > div > div > div').text.split("\n")
   statistics_pets = all_statistics[1].split(" ")
   pet_names = int(statistics_pets[-1])

   # Проверяем, что количество строк в таблице с моими питомцами равно общему количеству питомцев,
   # указанному в статистике пользователя:
   assert len(pet_name) ==  pet_names


   # Проверяем, что у всех питомцев есть имя:
   for i in range(len(names)):
      assert names[i].text != ''

   # Проверяем, что у всех питомцев есть порода:
   for i in range(len(types)):
      assert types[i].text != ''




   # Проверяем, что в списке нет повторяющихся питомцев:
   list_cards = []
   for i in range(len(cards)):
      list_data = cards[i].text.split("\n") # отделяем от данных питомца "х" удаления питомца
      list_cards.append(list_data[0]) # выбираем элемент с данными питомца и добавляем его в список
   set_cards = set(list_cards) # преобразовываем список в множество
   assert len(list_cards) == len(set_cards) # сравниваем длину списка и множества: без повторов должны совпасть





