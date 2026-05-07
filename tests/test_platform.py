import unittest
from content.book import Book
from content.article import Article
from content.poem import Poem
from users.regular import Regular
from users.premium import PremiumUser
from recommendation.genre import Genre
from recommendation.trending import Trend
from platform import ReadingPlatform
class TestContent(unittest.TestCase):
    def test_book_display(self):
        book = Book()
        self.assertEqual(book.display(), "Reading a book")
    def test_article_display(self):
        article = Article()
        self.assertEqual(article.display(), "Reading an article")
    def test_poem_display(self):
        poem = Poem()
        self.assertEqual(poem.display(), "Reading a poem")
class TestUsers(unittest.TestCase):
    def test_regular_user_read(self):
        user = Regular()
        result = user.read(Book())
        self.assertEqual(result, "Reading a book")
    def test_premium_user_read(self):
        user = PremiumUser()
        result = user.read(Book())
        self.assertIn("Premium", result)
class TestRecommendations(unittest.TestCase):
    def test_genre_recommendation_returns_dict(self):
        recommendation = Genre()
        result = recommendation.suggest()
        self.assertIsInstance(result, dict)
        self.assertIn("genre", result)
        self.assertIn("recommendation", result)
    def test_trend_recommendation_returns_dict(self):
        recommendation = Trend()
        result = recommendation.suggest()
        self.assertIsInstance(result, dict)
        self.assertIn("trending", result)
class TestPlatform(unittest.TestCase):
    def test_reading_platform_reads_content(self):
        user = PremiumUser()
        recommendation = Genre()
        platform = ReadingPlatform(user, recommendation)
        result = platform.read_content(Book())
        self.assertIn("Premium", result)
    def test_platform_history_updates(self):
        user = Regular()
        recommendation = Genre()
        platform = ReadingPlatform(user, recommendation)
        platform.read_content(Book())
        platform.read_content(Article())
        history = platform.get_history()
        self.assertEqual(history, ["Book", "Article"])
    def test_platform_get_recommendations(self):
        user = Regular()
        recommendation = Trend()
        platform = ReadingPlatform(user, recommendation)
        result = platform.get_recommendations()
        self.assertIsInstance(result, dict)
if __name__ == "__main__":
    unittest.main()