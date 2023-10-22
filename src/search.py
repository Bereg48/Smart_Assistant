import wikipediaapi
from bs4 import BeautifulSoup
from googlesearch import search
import wikipedia
import requests
from urllib.parse import quote

API_KEY = 'fd893fffc7e85e04ad69106ba6ab0383'


def wiki_search(query):
    """Метод wiki_search(query) используется для поиска информации на Википедии с использованием библиотеки wikipedia-api.
     Создаем объект wiki_wiki класса 'wikipediaapi.Википедия'. Указываем язык (в данном случае `ru` для русского)
     и формат извлечения (в данном случае `WIKI` для текстового формата). Устанавливаем user_agent,
     чтобы идентифицировать помощника. Далее метод page = wiki_wiki.page(query) для получения объекта страницы
     по переданному запросу query. """
    wiki_wiki = wikipediaapi.Wikipedia(
        language='ru',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent='Smart_Assistant'
    )

    page = wiki_wiki.page(query)

    try:
        if page.exists():
            return page.title, page.summary[0:500]
        else:
            return "Страница не найдена"
    except Exception as e:
        return "Ошибка при выполнении запроса: " + str(e)


def get_page_url(title):
    """Эта функция используется для получения URL-адреса статьи на Википедии по заданному заголовку."""
    try:
        page = wikipedia.page(title)
        page_url = page.url
        return page_url
    except wikipedia.exceptions.PageError:
        return "Страница с таким заголовком не найдена"
    except Exception as e:
        return "Ошибка при получении URL-адреса статьи: " + str(e)


def random_article():
    """Метод `random_article()` используется для получения случайной статьи
    с Википедии с помощью библиотеки `wikipedia`."""
    try:
        random_page = wikipedia.random(pages=1)
        random_title = random_page
        random_summary = wikipedia.summary(random_page)
        return random_title, random_summary
    except wikipedia.exceptions.DisambiguationError as e:
        return "Не удалось получить случайную статью: " + str(e)
    except Exception as e:
        return "Ошибка при получении случайной статьи: " + str(e)


def google_search(query, num_results=5):
    """Метод google_search(query, num_results=5) используется для выполнения поиска
    в Google с помощью библиотеки googlesearch-python."""
    try:
        results = []
        for url in search(query, num_results=num_results):
            results.append(url)

        if len(results) == 0:
            return "По вашему запросу ничего не найдено"
        else:
            return results
    except Exception as e:
        return "Ошибка при выполнении поиска в Google: " + str(e)


def search_yahoo(query):
    url = f"https://search.yahoo.com/search?p={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("div", {"class": "algo"})

    search_results = []
    for result in results:
        title = result.find("h3").text
        link = result.find("a")["href"]
        search_results.append({"title": title, "link": link})

    return search_results


def search_duckduckgo(query):
    """Метод search, принимает запрос пользователя и выполняет поиск на основе DuckDuckGo API.
    Отправляет запрос на поиск и возвращает краткое описание результата поиска и ссылку
    для получения более подробной информации."""
    try:
        encoded_query = quote(query)
        response = requests.get(f"https://api.duckduckgo.com",
                                params={"q": encoded_query,
                                        "format": "json"})
        results = response.json()

        if response.status_code != 200:
            return f"Ошибка при поиске: {results['message']}"

        abstract = results["AbstractText"]
        url = results["AbstractURL"]

        return f"{abstract}\n\nПодробнее: {url}"
    except Exception as e:
        return "Ошибка при поиске: " + str(e)


def get_weather(city):
    """Мето get_weather использует API погоды для получения текущей погоды в указанном городе.
    Она принимает аргумент `city`, который является названием города."""
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
        weather = response.json()

        if response.status_code != 200:
            return f"Ошибка при получении погоды: {weather['message']}"

        description = weather["weather"][0]["description"]
        temperature = weather["main"]["temp"]
        return f"Погода в городе {city}: {description}, температура: {temperature} градусов по Цельсию"
    except Exception as e:
        return "Ошибка при получении погоды: " + str(e)
