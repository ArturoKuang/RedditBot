from reddit_utils import RedditScraper
import os
from dotenv import load_dotenv
from typing import List

def print_separator():
    print("\n" + "="*50 + "\n")

def test_get_comments(scraper: RedditScraper, subreddit: str = "python") -> List[str]:
    print(f"Testing get_subreddit_comments for r/{subreddit}")
    try:
        comments = scraper.get_subreddit_comments(
            subreddit_name=subreddit,
            time_filter='day',  # Using 'day' for quicker testing
            limit=5  # Small limit for testing
        )
        print(f"Successfully retrieved {len(comments)} comments")
        
        # Print sample comments
        for i, comment in enumerate(comments[:2], 1):
            print(f"\nComment {i}:")
            print(f"{comment[:200]}...")  # First 200 chars
        
        return comments
    
    except Exception as e:
        print(f"Error in get_comments: {str(e)}")
        return []

def test_search_comments(scraper: RedditScraper, 
                        subreddit: str = "python", 
                        query: str = "django") -> List[str]:
    print(f"Testing search_subreddit_comments for r/{subreddit} with query '{query}'")
    try:
        comments = scraper.search_subreddit_comments(
            subreddit_name=subreddit,
            search_query=query,
            limit=5  # Small limit for testing
        )
        print(f"Successfully retrieved {len(comments)} comments")
        
        # Print sample comments
        for i, comment in enumerate(comments[:2], 1):
            print(f"\nComment {i}:")
            print(f"{comment[:200]}...")  # First 200 chars
            
        return comments
    
    except Exception as e:
        print(f"Error in search_comments: {str(e)}")
        return []
    
def test_get_subreddit_posts(scraper: RedditScraper, subreddit: str = "python") -> List[str]:
    print(f"Testing get_subreddit_posts for r/{subreddit}")
    try:
        posts = scraper.get_subreddit_posts(
            subreddit_name=subreddit,
            time_filter='day',  # Using 'day' for quicker testing
            limit=5  # Small limit for testing
        )
        print(f"Successfully retrieved {len(posts)} posts")
        
        # Print sample posts
        for i, post in enumerate(posts[:2], 1):
            print(f"\nPost {i}:")
            print(f"Title: {post['title']}")
            print(f"Author: {post['author']}")
            print(f"Score: {post['score']}")
            print(f"Comments: {post['num_comments']}")
            print(f"URL: {post['url']}")
            print(f"Content: {post['content'][:200]}...")
            
        return posts
    
    except Exception as e:
        print(f"Error in get_subreddit_posts: {str(e)}")
        return []

def main():
    # Load environment variables
    load_dotenv()
    
    # Get credentials from environment variables
    client_id = os.getenv('REDDIT_CLIENT_ID')
    client_secret = os.getenv('REDDIT_CLIENT_SECRET')
    
    if not client_id or not client_secret:
        print("Error: Reddit credentials not found in environment variables")
        print("Please create a .env file with REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET")
        return
    
    try:
        # Initialize the RedditScraper
        scraper = RedditScraper(
            client_id=client_id,
            client_secret=client_secret,
            user_agent="RedditAnalyzerBot/1.0"
        )
        
        # # Test 1: Get comments from Python subreddit
        # print_separator()
        # test_get_comments(scraper)
        
        # # Test 2: Search comments in Python subreddit
        # print_separator()
        # test_search_comments(scraper)
        
        # # Test 3: Try a different subreddit
        # print_separator()
        # test_get_comments(scraper, "programming")
        
        # # Test 4: Try a different search query
        # print_separator()
        # test_search_comments(scraper, "programming", "rust")

        print_separator()
        test_get_subreddit_posts(scraper)
        
        print("All tests completed!")
        
    except Exception as e:
        print(f"Fatal error during testing: {str(e)}")

if __name__ == "__main__":
    main() 