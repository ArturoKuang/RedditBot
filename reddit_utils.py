import praw
from typing import List, Dict
from datetime import datetime, timedelta
import re

class RedditScraper:
    def __init__(self, client_id: str, client_secret: str, user_agent: str):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def get_subreddit_comments(self, 
                             subreddit_name: str, 
                             time_filter: str = 'week',
                             limit: int = 100) -> List[str]:
        """
        Fetch comments from a subreddit
        """
        subreddit = self.reddit.subreddit(subreddit_name)
        comments = []
        
        for submission in subreddit.top(time_filter=time_filter, limit=25):
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list()[:limit]:
                if comment.body and len(comment.body.split()) > 5:  # Filter out very short comments
                    comments.append(comment.body)
                if len(comments) >= limit:
                    break
            if len(comments) >= limit:
                break
                
        return comments

    def search_subreddit_comments(self, 
                                subreddit_name: str, 
                                search_query: str,
                                limit: int = 100) -> List[str]:
        """
        Search for specific topics in subreddit comments
        """
        subreddit = self.reddit.subreddit(subreddit_name)
        comments = []
        
        for submission in subreddit.search(search_query, time_filter='month', limit=25):
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list()[:limit]:
                if comment.body and len(comment.body.split()) > 5:
                    comments.append(comment.body)
                if len(comments) >= limit:
                    break
            if len(comments) >= limit:
                break
                
        return comments 
    
    def get_subreddit_posts(self, 
                           subreddit_name: str, 
                           time_filter: str = 'week', 
                           limit: int = 100) -> List[Dict]:
        """
        Fetch posts from a subreddit
        """
        subreddit = self.reddit.subreddit(subreddit_name)
        posts = []
        
        for submission in subreddit.top(time_filter=time_filter, limit=25):
            posts.append({
                'title': submission.title,
                'author': submission.author.name,
                'score': submission.score,
                'num_comments': submission.num_comments,
                'url': submission.url,
                'content': submission.selftext[:200] + '...' if len(submission.selftext) > 200 else submission.selftext
            })
            if len(posts) >= limit:
                break
                
        return posts

    def search_subreddits(self, query: str, limit: int = 25) -> List[Dict]:
        """
        Search for subreddits matching the query
        """
        subreddits = []
        for subreddit in self.reddit.subreddits.search(query, limit=limit):
            subreddits.append({
                'name': subreddit.display_name,
                'title': subreddit.title,
                'description': subreddit.public_description,
                'subscribers': subreddit.subscribers,
                'created_utc': subreddit.created_utc,
                'over18': subreddit.over18,
                'url': f"https://reddit.com{subreddit.url}"
            })
        return subreddits

    def get_related_subreddits(self, subreddit_name: str) -> List[str]:
        """
        Get related subreddits from sidebar and wiki
        """
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            # Get sidebar text
            related = []
            
            # Check sidebar
            if hasattr(subreddit, 'description'):
                sidebar = subreddit.description
                # Find subreddit mentions in sidebar (r/subreddit format)
                related.extend(re.findall(r'/r/([a-zA-Z0-9_]+)', sidebar))
                
            # Check wiki pages if available
            try:
                wiki = subreddit.wiki['related']
                related.extend(re.findall(r'/r/([a-zA-Z0-9_]+)', wiki.content_md))
            except:
                pass
                
            return list(set(related))  # Remove duplicates
        except:
            return []