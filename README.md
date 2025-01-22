Игра "Найди предметы"

Игра "Найди предметы" — это увлекательная игра на поиск предметов, где игрок выступает в роли администратора, решая задачи в различных сценах, таких как офис, серверная, и кабинет.

 Функционал
- Три уровня с уникальными сценами и списком предметов для поиска.
- Интерактивная панель для отслеживания прогресса.
- Система подсчета очков за найденные предметы.
- Таймер для измерения времени прохождения.
- Сохранение и отображение таблицы лидеров.

Установка
1. Убедитесь, что у вас установлен Python (3.7+).
2. Установите библиотеку Pygame:
   
   pip install pygame
  
3. Скачайте проект и перейдите в его директорию:
  
   git clone https://github.com/0000MATRIX0000.git
   
  ![image](https://github.com/user-attachments/assets/11f3e257-9f6a-4d9e-9124-cc4d6adfb06b)



Запуск игры
Для запуска игры выполните:

python main.py

Как играть
1. Запустите игру.
2. В главном меню:
   - Нажмите **ENTER** для начала игры.
   - Нажмите **L** для просмотра таблицы лидеров.
   - Нажмите **ESC**, чтобы выйти.
3. В каждой сцене ищите указанные предметы, кликая по ним.
4. По завершении всех уровней введите свое имя для записи результата в таблицу лидеров.
![image](https://github.com/user-attachments/assets/2e4432ea-474e-4be1-a53b-73d198ffa565)
Таблица лидеров
Игра сохраняет топ-10 результатов в файл `leaderboard.txt`. Очки начисляются за скорость и точность.

Структура проекта
- `main.py` — основной файл с логикой игры.
- `assets/` — папка с графическими ресурсами:
  - `background_office.png` — фон офиса.
  - `background_servernaya.png` — фон серверной.
  - `background_kabinet.png` — фон кабинета.
  - `menu_background.png` — фон меню.
  - `end_game_background.png` — фон экрана завершения игры.
  - Другие изображения для предметов.
- `leaderboard.txt` — файл для хранения таблицы лидеров.


Требования
- Python 3.7+
- Pygame 2.0+

