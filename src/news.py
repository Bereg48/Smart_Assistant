import requests
from bs4 import BeautifulSoup


def get_news():
    url = "https://ria.ru/"

    # Отправка запроса к указанной странице
    response = requests.get(url)

    # Проверка статуса ответа
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML-страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Используем CSS-селектор, чтобы найти заголовки новостей
        news_titles = soup.select(".cell-list__item-title")

        # Выводим последние 5 заголовков новостей
        for title in news_titles[:5]:
            print(title.text.strip())
    else:
        print("Ошибка при получении новостей")
