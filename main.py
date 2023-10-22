from termcolor import colored
from colorama import init, Fore, Back, Style

from src.news import get_news
from src.search import wiki_search, google_search, random_article, get_page_url, get_weather, \
    search_duckduckgo, search_yahoo
from src.speak import speak


def smart_assistant():
    """Метод smart_assistant() представляет собой основной цикл работы умного помощника. Он продолжается до тех пор,
    пока не будет дана команда "выход". Внутри цикла считывается пользовательский ввод с помощью функции input().
    Проверяем, с чего начинается пользовательский ввод, и выполняем соответствующие действия в зависимости от команды. """
    while True:
        user_input = input(Fore.YELLOW +
                           "1 - Поиск в Википедии: [запрос];\n"
                           "1.1 - Получить URL-адреса с Википедии: [запрос];\n"
                           "1.2 - Случайная статья с Википедии;\n"
                           "2 - Поиск в Google: [запрос];\n"
                           "3 - Поиск в Yahoo: [запрос];\n"
                           "4 - Поиск в Duckduckgo: [запрос];\n"
                           "5 - узнать 5 последних новостей;\n" + Back.BLACK +
                           "6 - погода на сегодня для города: [запрос];\n"
                           "выход - для завершения введите выход;\n"
                           )

        # Оформляем пользовательский ввод рамкой
        frame_top = "╔" + "═" * (len(user_input) + 2) + "╗"
        frame_middle = "║ " + user_input + " ║"
        frame_bottom = "╚" + "═" * (len(user_input) + 2) + "╝"

        print(colored(frame_top, "cyan"))
        print(colored(frame_middle, "cyan"))
        print(colored(frame_bottom, "cyan"))

        if user_input.startswith('Поиск в Википедии: '):
            query = user_input.split(':')[1].strip()
            result = wiki_search(query)
            print(result)
            speak(result)

        elif user_input.startswith('Получить URL-адреса с Википедии: '):
            title = user_input.split(':')[1].strip()
            result = get_page_url(title)
            print(result)
            speak(result)

        elif user_input.lower() == 'Случайная статья с Википедии':
            title, summary = random_article()
            print(f"Случайная статья с Википедии: {title}")
            print(summary)
            speak(f"Случайная статья с Википедии: {title}. {summary}")

        elif user_input.startswith('Поиск в Google:'):
            query = user_input.split(':')[1].strip()
            results = google_search(query)

            for i, url in enumerate(results):
                print(f"Результат #{i + 1}: {url}")
                speak(f"Результат #{i + 1}: {url}")

        elif user_input.startswith('Поиск в Yahoo: '):
            query = user_input.split(':')[1].strip()
            result = search_yahoo(query)
            print(result)
            speak(result)

        elif user_input.startswith('Поиск в Duckduckgo: '):
            query = user_input.split(':')[1].strip()
            result = search_duckduckgo(query)
            print(result)
            speak(result)

        elif user_input.lower() == 'узнать 5 последних новостей':
            get_news()

        elif user_input.startswith('погода на сегодня для города: '):
            city = user_input.split(':')[1].strip()
            result = get_weather(city)
            print(result)
            speak(result)

        elif user_input.lower() == 'выход':
            speak("До свидания!")
            break

        else:
            print("Неверная команда. Попробуйте еще раз.")
            speak("Неверная команда. Попробуйте еще раз.")


if __name__ == "__main__":
    smart_assistant()
