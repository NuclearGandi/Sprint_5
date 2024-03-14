from selenium import webdriver
from selenium.webdriver.common.by import By

# функция для инициализации браузера
def init_browser():
    driver = webdriver.Chrome()
    return driver


# функция для проверки успешной регистрации
def test_successful_registration():
    driver = init_browser()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # вводим данные для регистрации
    driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()
    search = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input")
    search.send_keys("daniilbogach")
    search_e = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input")
    search_e.send_keys("daniilbogach5111@mail.ru")
    search_p = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input")
    search_p.send_keys("79021311564h")

    # нажимаем на кнопку "зарегистрироваться"
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p/a").click()

    # проверяем, что успешно зарегистрировались и перешли в личный кабинет
    assert "Stellar Burgers" in driver.title

    driver.quit()


# функция для проверки ошибки при некорректном пароле
def test_incorrect_password():
    driver = init_browser()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()
    search = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input")
    search.send_keys("daniilbogach")
    search_e = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input")
    search_e.send_keys("daniilbogach5111@mail.ru")
    search_p = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input")
    search_p.send_keys("790")

    # нажимаем на кнопку "зарегистрироваться"
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()

    # проверяем, что появилась ошибка при некорректном пароле
    assert "Некорректный пароль" in driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p").text

    driver.quit()


# функция для проверки входа в аккаунт
def test_login():
    driver = init_browser()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # нажимаем на кнопку "вход в аккаунт" на главной
    driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()

    # нажимаем на кнопку "зарегистрироваться" в форме регистрации
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()

    # нажимаем на кнопку "войти" в форме восстановления пароля
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p/a").click()

    # нажимаем на кнопку "забыли пароль?" в форме восстановления пароля
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[2]/a").click()

    driver.quit()


# функция для проверки перехода в личный кабинет
def test_go_to_personal_account():
    driver = init_browser()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # нажимаем на ссылку "личный кабинет"
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()

    # нажимаем на логотип бургеров
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/div/a/svg").click()

    driver.quit()


# функция для проверки перехода в конструктор из личного кабинета
def test_go_to_constructor_from_personal_account():
    driver = init_browser()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # нажимаем на кнопку "конструктор"
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p").click()

    # нажимаем на ссылку "личный кабинет"
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()

    # нажимаем на логотип stellar burgers
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/div/a/svg").click()

    driver.quit()


# функция для проверки выхода из аккаунта
def test_logout():
    driver = init_browser()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # нажимаем на ссылку "личный кабинет"
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()

    # нажимаем на кнопку "выход"
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button").click()

    driver.quit()
# Функция для проверки переходов к разделам в конструкторе
def test_constructor_sections():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем на ссылку "Конструктор"
    driver.find_element(By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p").click()
    # Переходим к разделу "Булки"
    driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[1]/span").click()
    # Переходим к разделу "Соусы"
    driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]/span").click()
    # Переходим к разделу "Начинки"
    driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]/span").click()

    driver.quit()

test_successful_registration()
test_incorrect_password()
test_login()
test_go_to_personal_account()
test_go_to_constructor_from_personal_account()
test_logout()
test_constructor_sections()