import pygame
import sys
import os

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 1440, 1005  # Размеры игрового окна
PANEL_HEIGHT = 120  # Высота панели, где отображаются изображения предметов
FPS = 60  # Частота кадров
WHITE = (255, 255, 255)  # Цвета для отрисовки
BLACK = (0, 0, 0)
FONT_COLOR = (50, 50, 200)
LEADERBOARD_FILE = "leaderboard.txt"  # Файл для таблицы лидеров

# Инициализация экрана и шрифтов
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Администратор в деле!")
font = pygame.font.Font(None, 36)

# Таймер и очки
clock = pygame.time.Clock()
timer = 0  # Счетчик времени в секундах
score = 0  # Начальное количество очков

# Локация предметов для трех сцен
# Каждая сцена содержит список предметов и их координаты
items_to_find_scene1 = ["planshet", "bloknot", "nastolnaya_lampa", "notebook"]
item_positions_scene1 = {
    "notebook": [(930, 660)],
    "bloknot": [(470, 835)],
    "nastolnaya_lampa": [(1120, 570)],
    "planshet": [(150, 765)]
}

items_to_find_scene2 = ["monitor", "notebook2", "switch", "ups"]
item_positions_scene2 = {
    "monitor": [(700, 600)],
    "notebook2": [(1160, 720)],
    "switch": [(35, 620)],
    "ups": [(875, 790)]
}

items_to_find_scene3 = ["router", "keyboard", "monitor2", "kabelnaya_buhta"]
item_positions_scene3 = {
    "router": [(1340, 740)],
    "keyboard": [(760, 600)],
    "monitor2": [(825, 500)],
    "kabelnaya_buhta": [(975, 730)]
}

# Загрузка изображений фонов для всех сцен
# Изображения масштабируются, чтобы соответствовать размеру экрана
background_image_scene1 = pygame.image.load("assets/background_office.png")
background_image_scene1 = pygame.transform.scale(
    background_image_scene1, (WIDTH, HEIGHT - PANEL_HEIGHT)
)

background_image_scene2 = pygame.image.load("assets/background_servernaya.png")
background_image_scene2 = pygame.transform.scale(
    background_image_scene2, (WIDTH, HEIGHT - PANEL_HEIGHT)
)

background_image_scene3 = pygame.image.load("assets/background_kabinet.png")
background_image_scene3 = pygame.transform.scale(
    background_image_scene3, (WIDTH, HEIGHT - PANEL_HEIGHT)
)

# Загрузка изображений интерфейса
menu_background = pygame.image.load("assets/menu_background.png")
menu_background = pygame.transform.scale(menu_background, (WIDTH, HEIGHT))

end_game_background = pygame.image.load("assets/end_game_background.png")
end_game_background = pygame.transform.scale(end_game_background, (WIDTH, HEIGHT))

# Загрузка и масштабирование изображений предметов
item_images_scene1 = {
    "planshet": pygame.image.load("assets/planshet.png"),
    "bloknot": pygame.image.load("assets/bloknot.png"),
    "nastolnaya_lampa": pygame.image.load("assets/nastolnaya_lampa.png"),
    "notebook": pygame.image.load("assets/notebook.png"),
}

item_images_scene2 = {
    "monitor": pygame.image.load("assets/monitor.png"),
    "notebook2": pygame.image.load("assets/notebook2.png"),
    "switch": pygame.image.load("assets/switch.png"),
    "ups": pygame.image.load("assets/ups.png"),
}

item_images_scene3 = {
    "router": pygame.image.load("assets/router.png"),
    "keyboard": pygame.image.load("assets/keyboard.png"),
    "monitor2": pygame.image.load("assets/monitor2.png"),
    "kabelnaya_buhta": pygame.image.load("assets/kabelnaya_buhta.png"),
}

# Преобразование изображений для панели предметов
panel_images_scene1 = {
    key: pygame.transform.scale(image, (100, 100)) for key, image in item_images_scene1.items()
}
panel_images_scene2 = {
    key: pygame.transform.scale(image, (100, 100)) for key, image in item_images_scene2.items()
}
panel_images_scene3 = {
    key: pygame.transform.scale(image, (100, 100)) for key, image in item_images_scene3.items()
}

# Функция загрузки таблицы лидеров
def load_leaderboard(file_path="leaderboard.txt"):
    """
       Загружает данные таблицы лидеров из файла.
       Возвращает список сохраненных результатов предыдущих игр.
       """
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

# Функция сохранения таблицы лидеров
def save_leaderboard(entries, file_path="leaderboard.txt"):
    """
    Сохраняет результат игры в файл таблицы лидеров.
    """
    with open(file_path, "w") as f:
        for entry in entries:
            f.write(entry + "\n")

# Главное меню игры
def main_menu():
    """
    Отображает главное меню игры.
    Пользователь может начать игру, посмотреть таблицу лидеров или выйти.
    """
    while True:
        # Отображение фона меню
        screen.blit(menu_background, (0, 0))

        # Отображение текста меню
        title_text = font.render("Администратор в деле!", True, FONT_COLOR)
        start_text = font.render("Нажмите ENTER, чтобы начать игру", True, WHITE)
        leaderboard_text = font.render("Нажмите L, чтобы посмотреть таблицу лидеров", True, WHITE)
        exit_text = font.render("Нажмите ESC, чтобы выйти", True, WHITE)

        # Позиционирование текста
        screen.blit(title_text, ((WIDTH - title_text.get_width()) // 2, HEIGHT // 3))
        screen.blit(start_text, ((WIDTH - start_text.get_width()) // 2, HEIGHT // 2))
        screen.blit(leaderboard_text, ((WIDTH - leaderboard_text.get_width()) // 2, HEIGHT // 2 + 50))
        screen.blit(exit_text, ((WIDTH - exit_text.get_width()) // 2, HEIGHT // 2 + 100))

        pygame.display.flip()

        # Обработка событий в меню
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Закрытие окна
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # Обработка нажатий клавиш
                if event.key == pygame.K_RETURN:  # Начать игру
                    return
                if event.key == pygame.K_l:  # Показать таблицу лидеров
                    show_leaderboard()
                if event.key == pygame.K_ESCAPE:  # Выход из игры
                    pygame.quit()
                    sys.exit()

# Отображение таблицы лидеров
def show_leaderboard():
    """
    Отображает таблицу лидеров, загруженную из файла.
    Пользователь может вернуться в главное меню.
    """
    entries = load_leaderboard()
    while True:
        screen.fill(WHITE)

        # Заголовок таблицы
        title_text = font.render("Таблица лидеров", True, BLACK)
        screen.blit(title_text, ((WIDTH - title_text.get_width()) // 2, 50))

        # Вывод записей таблицы
        y_offset = 150
        for entry in entries:
            entry_text = font.render(entry, True, BLACK)
            screen.blit(entry_text, (100, y_offset))
            y_offset += 40

        # Инструкция выхода
        exit_text = font.render("Нажмите ESC, чтобы вернуться в меню", True, BLACK)
        screen.blit(exit_text, ((WIDTH - exit_text.get_width()) // 2, HEIGHT - 100))

        pygame.display.flip()

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return  # Вернуться в главное меню

# Игровая сцена
def game_scene(background_image, item_positions, items_to_find, panel_images):
    """
    Основная логика игровой сцены. Игрок ищет предметы на изображении.
    :param background_image: Фон сцены.
    :param item_positions: Координаты предметов.
    :param items_to_find: Список предметов, которые нужно найти.
    :param panel_images: Изображения предметов для панели.
    """
    global timer, score
    found_items = []  # Список найденных предметов
    running = True

    while running:
        # Отображение фона и панели
        screen.fill(WHITE)
        screen.blit(background_image, (0, PANEL_HEIGHT))

        # Обновление времени
        timer += clock.tick(FPS) / 1000

        # Отрисовка панели с предметами
        pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, PANEL_HEIGHT))

        # Отображение предметов на панели
        x_offset = 10
        for item, image in panel_images.items():
            if item in found_items:  # Если предмет найден, подсветить
                overlay = pygame.Surface((100, 100), pygame.SRCALPHA)
                overlay.fill((0, 255, 0, 128))  # Зеленая подсветка
                screen.blit(overlay, (x_offset, 10))
            screen.blit(image, (x_offset, 10))
            x_offset += 110

        # Отображение таймера и очков
        timer_text = font.render(f"Время: {int(timer)} сек", True, BLACK)
        score_text = font.render(f"Очки: {score}", True, BLACK)
        screen.blit(timer_text, (WIDTH - 200, 10))
        screen.blit(score_text, (WIDTH - 200, 50))

        pygame.display.flip()

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Закрытие окна
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Клик мыши
                mouse_pos = pygame.mouse.get_pos()
                for item, positions in item_positions.items():
                    if item not in found_items:  # Если предмет не найден
                        for pos in positions:
                            item_rect = pygame.Rect(pos[0], pos[1], 50, 50)
                            if item_rect.collidepoint(mouse_pos):  # Проверка попадания
                                found_items.append(item)  # Добавить в найденные
                                score += 100  # Начислить очки
                                break

        # Проверка окончания сцены
        if len(found_items) == len(items_to_find):  # Все предметы найдены
            running = False

# Финальное сообщение и таблица лидеров
def leaderboard():
    """
    Отображение экрана завершения игры и сохранение результата в таблице лидеров.
    """
    global timer, score
    input_active = True
    player_name = ""

    while input_active:
        screen.blit(end_game_background, (0, 0))

        # Отображение информации о завершении игры
        title_text = font.render("Игра завершена!", True, WHITE)
        name_text = font.render(f"Введите ваше имя: {player_name}", True, WHITE)
        score_text = font.render(f"Очки: {score}, Время: {int(timer)} сек", True, WHITE)

        screen.blit(title_text, ((WIDTH - title_text.get_width()) // 2, HEIGHT // 4))
        screen.blit(name_text, ((WIDTH - name_text.get_width()) // 2, HEIGHT // 2))
        screen.blit(score_text, ((WIDTH - score_text.get_width()) // 2, HEIGHT // 2 + 50))

        pygame.display.flip()

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and player_name:  # Сохранить имя
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:  # Удалить символ
                    player_name = player_name[:-1]
                else:  # Добавить символ
                    player_name += event.unicode

    # Сохранение результата
    entry = f"{player_name}: {score} очков, {int(timer)} сек"
    entries = load_leaderboard()
    entries.append(entry)
    entries = sorted(entries, key=lambda x: int(x.split(",")[1].split()[0]))  # Сортировка
    save_leaderboard(entries[:10])  # Сохранение топ-10 записей

# Основной цикл игры
main_menu()
game_scene(background_image_scene1, item_positions_scene1, items_to_find_scene1, panel_images_scene1)
game_scene(background_image_scene2, item_positions_scene2, items_to_find_scene2, panel_images_scene2)
game_scene(background_image_scene3, item_positions_scene3, items_to_find_scene3, panel_images_scene3)
leaderboard()
pygame.quit()
