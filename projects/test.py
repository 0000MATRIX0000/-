import unittest
import os
from main import save_leaderboard, load_leaderboard


class TestLeaderboardFunctions(unittest.TestCase):
    def setUp(self):
        self.test_leaderboard_file = "test_leaderboard.txt"
        self.sample_entries = [
            "Player1: 500 очков, 30 сек",
            "Player2: 300 очков, 40 сек"
        ]

    def tearDown(self):
        # Удаляем файл после тестов
        if os.path.exists(self.test_leaderboard_file):
            os.remove(self.test_leaderboard_file)

    def test_save_leaderboard(self):
        save_leaderboard(self.sample_entries, self.test_leaderboard_file)
        self.assertTrue(os.path.exists(self.test_leaderboard_file))  # Файл должен быть создан
        with open(self.test_leaderboard_file, "r") as f:
            lines = f.read().splitlines()
        self.assertEqual(lines, self.sample_entries)  # Содержимое файла должно совпадать

    def test_load_leaderboard(self):
        with open(self.test_leaderboard_file, "w") as f:
            f.write("\n".join(self.sample_entries))
        loaded_entries = load_leaderboard(self.test_leaderboard_file)
        self.assertEqual(loaded_entries, self.sample_entries)  # Проверка загруженных данных


if __name__ == "__main__":
    unittest.main()
