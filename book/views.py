from django.http import HttpResponse

def about_me(request):
    return HttpResponse(
        "<h1>Обо мне</h1>"
        "<p>Привет! Меня зовут Нурсултан. Я системный администратор и изучаю бэкенд-разработку на Python и Django.</p>"
    )

def my_favourite_writers(request):
    return HttpResponse(
        "<h1>Мои любимые писатели</h1>"
        "<ul>"
        "<li>Чингиз Айтматов</li>"
        "<li>Лев Толстой</li>"
        "<li>Федор Достоевский</li>"
        "</ul>"
    )

def sayings_of_great_poets(request):
    html_content = """
    <h1>Цитаты великих поэтов</h1>
    <hr>
    <div>
        <p><b>Чингиз Айтматов:</b> «Человеку в день порой нужно очень немного — чтобы просто выслушали.»</p>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Chinghiz_Aitmatov_1986.jpg/800px-Chinghiz_Aitmatov_1986.jpg" width="300" alt="Айтматов">
    </div>
    <br>
    <div>
        <p><b>Александр Пушкин:</b> «Любовь к родному пепелищу, любовь к отеческим гробам.»</p>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Oren_Pushkin.jpg/800px-Oren_Pushkin.jpg" width="300" alt="Пушкин">
    </div>
    """
    return HttpResponse(html_content)