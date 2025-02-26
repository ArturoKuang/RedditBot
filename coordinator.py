from agents import ResearchAgent, AnalystAgent, WriterAgent, RedditAnalyzerAgent, SubredditDiscoveryAgent
from reddit_utils import RedditScraper
from typing import Optional, List, Dict

class AgentCoordinator:
    def __init__(self, api_key: str, reddit_client_id: str, reddit_client_secret: str):
        self.researcher = ResearchAgent(api_key)
        self.analyst = AnalystAgent(api_key)
        self.writer = WriterAgent(api_key)
        self.reddit_analyzer = RedditAnalyzerAgent(api_key)
        self.reddit_scraper = RedditScraper(
            client_id=reddit_client_id,
            client_secret=reddit_client_secret,
            user_agent="RedditAnalyzerBot/1.0"
        )

    def analyze_reddit_complaints(self, 
                                subreddit: str, 
                                search_query: Optional[str] = None,
                                limit: int = 100) -> Dict:
        """
        Analyze complaints and problems from a subreddit
        """
        # Step 1: Gather comments
        if search_query:
            comments = self.reddit_scraper.search_subreddit_comments(
                subreddit, search_query, limit
            )
        else:
            comments = self.reddit_scraper.get_subreddit_comments(
                subreddit, limit=limit
            )

        # Step 2: Analyze comments for complaints and problems
        analysis = self.reddit_analyzer.analyze_comments(comments)
        
        # Step 3: Generate summary
        summary = self.reddit_analyzer.summarize_findings(analysis)
        
        # Step 4: Get additional insights from the analyst
        deeper_insights = self.analyst.analyze(
            f"Based on this analysis and summary of Reddit comments:\n\n"
            f"Analysis: {analysis}\n\n"
            f"Summary: {summary}\n\n"
            f"What additional patterns or insights can you identify?"
        )
        
        # Step 5: Generate final report
        final_report = self.writer.write(
            f"Reddit Analysis: {analysis}\nSummary: {summary}",
            deeper_insights
        )
        
        return {
            "raw_comments": comments,
            "detailed_analysis": analysis,
            "summary": summary,
            "insights": deeper_insights,
            "final_report": final_report
        } 

    def discover_subreddits(self, topic: str, limit: int = 25) -> Dict:
        """
        Find and analyze relevant subreddits for a given topic
        """
        # Initialize the discovery agent
        discovery_agent = SubredditDiscoveryAgent(self.api_key, self.llm)
        
        # Get search terms
        search_terms = discovery_agent.suggest_search_terms(topic)
        
        # Search for subreddits using each term
        all_subreddits = []
        seen_subreddits = set()
        
        for term in search_terms:
            results = self.reddit_scraper.search_subreddits(term, limit=limit)
            for sub in results:
                if sub['name'] not in seen_subreddits:
                    all_subreddits.append(sub)
                    seen_subreddits.add(sub['name'])
        
        # Analyze the found subreddits
        analysis = discovery_agent.analyze_subreddits(topic, all_subreddits)
        
        # Get additional insights
        deeper_insights = self.analyst.analyze(
            f"Based on this analysis of subreddits related to '{topic}':\n\n"
            f"{analysis}\n\n"
            "What additional patterns or insights can you identify about these communities?"
        )
        
        # Generate final report
        final_report = self.writer.write(
            f"Subreddit Discovery Analysis: {analysis}",
            deeper_insights
        )
        
        return {
            "search_terms_used": search_terms,
            "subreddits_found": all_subreddits,
            "analysis": analysis,
            "insights": deeper_insights,
            "final_report": final_report
        } 