from content.book import Book
from content.article import Article
from content.poem import Poem
from users.regular import Regular
from users.premium import PremiumUser
from recommendation.genre import Genre
from recommendation.trending import Trend
from platform import ReadingPlatform
def main():
    contents = [Book(),Article(),Poem()]
    user = PremiumUser()
    recommendation = Genre()
    platform = ReadingPlatform(user,recommendation)
    print("----Reading----")
    for content in contents:
        print(platform.read_content(content))
    print("---- History ----")
    print(platform.get_history())
    print("---- Statistics ----")
    print(platform.get_statistics())
    print("---- Recommendations ----")
    print(platform.get_recommendations())
    platform.recommendation = Trend()
    print("---- Trending Recommendations ----")
    print(platform.get_recommendations())
if __name__ == "__main__":
    main()

