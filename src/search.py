
import wikipediaapi
from googlesearch import search
import wikipedia


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