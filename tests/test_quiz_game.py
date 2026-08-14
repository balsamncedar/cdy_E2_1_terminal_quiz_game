import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from game_session import GameSession
from quiz import Quiz
from quiz_game import QuizGame
from repository import QuizRepository


SEED_DATA = [
    {
        "question": "테스트 문제",
        "choices": ["하나", "둘", "셋", "넷"],
        "answer": 2,
    }
]


class QuizTest(unittest.TestCase):
    def test_quiz_validates_and_checks_answer(self):
        quiz = Quiz(" 문제 ", [" 1 ", "2", "3", "4"], 1)

        self.assertEqual("문제", quiz.question)
        self.assertTrue(quiz.check_answer(1))
        self.assertFalse(quiz.check_answer(2))

    def test_quiz_rejects_invalid_data(self):
        with self.assertRaises(ValueError):
            Quiz("", ["1", "2", "3", "4"], 1)
        with self.assertRaises(ValueError):
            Quiz("문제", ["1", "2"], 1)
        with self.assertRaises(ValueError):
            Quiz("문제", ["1", "2", "3", "4"], 5)


class RepositoryTest(unittest.TestCase):
    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp_directory.name)
        self.seed_path = self.directory / "seed.json"
        self.state_path = self.directory / "state.json"
        self.seed_path.write_text(
            json.dumps(SEED_DATA, ensure_ascii=False), encoding="utf-8"
        )

    def tearDown(self):
        self.temp_directory.cleanup()

    def test_missing_state_uses_seed_and_creates_state(self):
        repository = QuizRepository(self.seed_path, self.state_path)

        self.assertEqual(1, len(repository.quizzes))
        self.assertIsNone(repository.best_score)
        self.assertTrue(self.state_path.exists())

    def test_corrupt_state_is_recovered(self):
        self.state_path.write_text("{broken", encoding="utf-8")

        repository = QuizRepository(self.seed_path, self.state_path)

        self.assertEqual("테스트 문제", repository.quizzes[0].question)
        recovered = json.loads(self.state_path.read_text(encoding="utf-8"))
        self.assertEqual(SEED_DATA, recovered["quizzes"])

    def test_added_quiz_and_score_survive_reload(self):
        repository = QuizRepository(self.seed_path, self.state_path)
        self.assertTrue(repository.add_quiz("새 문제", ["가", "나", "다", "라"], 3))
        repository.best_score = 80.0
        repository.save_state()

        reloaded = QuizRepository(self.seed_path, self.state_path)

        self.assertEqual(2, len(reloaded.quizzes))
        self.assertEqual(80.0, reloaded.best_score)


class GameFlowTest(unittest.TestCase):
    def test_session_reprompts_invalid_answers(self):
        quiz = Quiz("문제", ["1", "2", "3", "4"], 2)
        session = GameSession([quiz])

        with patch("builtins.input", side_effect=["", "abc", "0", " 2 "]):
            score = session.start(lambda item: None)

        self.assertEqual(100.0, score)
        self.assertEqual(1, session.correct_count)

    def test_eof_safely_saves_and_exits(self):
        repository = unittest.mock.Mock()
        game = QuizGame(repository)

        with patch("builtins.input", side_effect=EOFError):
            game.run()

        repository.save_state.assert_called_once_with()

    def test_first_play_becomes_best_score(self):
        repository = unittest.mock.Mock()
        repository.quizzes = [Quiz("문제", ["1", "2", "3", "4"], 1)]
        repository.best_score = None
        game = QuizGame(repository)

        with patch("builtins.input", return_value="1"):
            game.play_quiz()

        self.assertEqual(100.0, repository.best_score)
        repository.save_state.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
