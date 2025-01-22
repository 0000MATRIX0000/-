import pygame
import time

# Тестовые данные для проверки производительности
test_positions = {
    "planshet": [(150, 765)],
    "bloknot": [(470, 835)],
    "nastolnaya_lampa": [(1120, 570)],
    "notebook": [(930, 660)],
    "monitor": [(700, 600)],
    "notebook2": [(1160, 720)],
    "switch": [(35, 620)],
    "ups": [(875, 790)],
    "router": [(1340, 740)],
    "keyboard": [(760, 600)],
    "monitor2": [(825, 500)],
    "kabelnaya_buhta": [(975, 730)],
    # Дополнительные позиции для увеличения нагрузки
    "item1": [(50, 50), (100, 100), (150, 150)],
    "item2": [(200, 200), (250, 250), (300, 300)],
    "item3": [(350, 350), (400, 400), (450, 450)],
    "item4": [(500, 500), (550, 550), (600, 600)],
    "item5": [(650, 650), (700, 700), (750, 750)],
}


def test_click_performance(item_positions):
    """
    Измеряет время обработки большого количества кликов по прямоугольным областям.

    :param item_positions: Словарь с координатами всех предметов.
    """
    start_time = time.time()

    for _ in range(1000):  # Симуляция 1000 кликов
        mouse_pos = (200, 200)  # Фиксированная позиция клика
        for positions in item_positions.values():
            for pos in positions:
                # Создаем прямоугольник вокруг позиции
                item_rect = pygame.Rect(pos[0], pos[1], 50, 50)
                if item_rect.collidepoint(mouse_pos):  # Проверка попадания клика
                    break

    elapsed_time = time.time() - start_time
    print(f"Время обработки 1000 кликов: {elapsed_time:.6f} секунд")


def test_rendering_performance(item_images, screen):
    """
    Измеряет время рендеринга большого количества кадров с изображениями.

    :param item_images: Словарь с тестовыми изображениями.
    :param screen: Поверхность экрана для отрисовки.
    """
    start_time = time.time()

    for _ in range(100):  # Симуляция отрисовки 100 кадров
        screen.fill((255, 255, 255))  # Очистка экрана белым цветом
        x_offset = 10

        for image in item_images.values():
            screen.blit(image, (x_offset, 10))  # Рисуем изображение на экране
            x_offset += 110  # Смещаем каждое изображение вправо

        pygame.display.flip()  # Обновление экрана

    elapsed_time = time.time() - start_time
    print(f"Время рендеринга 100 кадров: {elapsed_time:.6f} секунд")


def run_tests():
    """
    Запускает тесты производительности для проверки кликов и рендеринга.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Создаем окно с фиксированным размером

    # Генерация тестовых изображений
    test_images = {
        f"item{i}": pygame.Surface((100, 100))
        for i in range(10)  # Создаем 10 тестовых изображений
    }
    for img in test_images.values():
        img.fill((255, 0, 0))  # Заливаем изображения красным цветом

    # Запуск теста производительности кликов
    print("Тест производительности кликов:")
    test_click_performance(test_positions)

    # Запуск теста производительности рендеринга
    print("\nТест производительности рендеринга:")
    test_rendering_performance(test_images, screen)

    pygame.quit()


# Точка входа в программу
if __name__ == "__main__":
    run_tests()
