from playwright.sync_api import sync_playwright, Request, Response


# Логирование запросов
def log_request(request: Request):
    print(f"Request: {request.url}")


# Логирование ответов
def log_response(response: Response):
    print(f"Response: {response.url, response.status}")


with sync_playwright() as playwright:
    # Открываем браузер и создаём новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Добавляем обработчики событий
    page.on("request", log_request)  # Запрос отправлен
    page.on("response", log_response)  # Ответ получен

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Задержка для завершения всех запросов
    page.wait_for_timeout(3000)

    # listener = lambda request: print(f"Request: {request.url}")
    #
    # page.on("request", listener)  # Добавляем обработчик
    # page.remove_listener("request", listener)  # Убираем обработчик
    #
    #
    # def log_specific_requests(request):
    #     if "googleapis.com" in request.url:
    #         print(f"Filtered request: {request.url}")
    #
    #
    # page.on("request", log_specific_requests)
    #
    #
    # def log_response_body(response):
    #     if response.ok:
    #         print(f"Response body: {response.body()}")  # Тело ответа
    #
    #
    # page.on("response", log_response_body)