import os
from coordinator import AgentCoordinator

def main():
    # Get API keys from environment variables
    openai_api_key = os.getenv("OPENAI_API_KEY")
    reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
    reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    
    if not all([openai_api_key, reddit_client_id, reddit_client_secret]):
        raise ValueError("Please set all required environment variables")

    coordinator = AgentCoordinator(
        api_key=openai_api_key,
        reddit_client_id=reddit_client_id,
        reddit_client_secret=reddit_client_secret
    )
    
    # Example: Analyze complaints in a specific subreddit
    results = coordinator.analyze_reddit_complaints(
        subreddit="techsupport",
        search_query="problem",
        limit=50
    )
    
    print("=== Reddit Analysis Results ===")
    print("\nSummary of Issues:")
    print(results["summary"])
    print("\nDetailed Analysis:")
    print(results["detailed_analysis"])
    print("\nAdditional Insights:")
    print(results["insights"])
    print("\nFinal Report:")
    print(results["final_report"])

    # Example: Find deal-hunting related subreddits
    results = coordinator.discover_subreddits(
        topic="deal finding and bargain hunting",
        limit=25
    )
    
    print("=== Subreddit Discovery Results ===")
    print("\nSearch Terms Used:")
    print("\n".join(results["search_terms_used"]))
    print("\nAnalysis:")
    print(results["analysis"])
    print("\nAdditional Insights:")
    print(results["insights"])
    print("\nFinal Report:")
    print(results["final_report"])

if __name__ == "__main__":
    main() 