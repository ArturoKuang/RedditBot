import os
from llms import OpenAI
from agents import (
    ResearchAgent,
    AnalystAgent,
    WriterAgent,
    RedditAnalyzerAgent,
    SubredditDiscoveryAgent
)

def setup_llm():
    """Setup LLM with API key from environment"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    return OpenAI(api_key)

def test_research_agent(llm):
    """Test the ResearchAgent with a real query"""
    print("\n=== Testing ResearchAgent ===")
    agent = ResearchAgent("fake_key", llm)
    
    query = "What are the main challenges of implementing multi-agent systems?"
    print(f"Query: {query}")
    
    response = agent.research(query)
    print(f"Response:\n{response}")
    
    return response

def test_analyst_agent(llm, research_data):
    """Test the AnalystAgent with real research data"""
    print("\n=== Testing AnalystAgent ===")
    agent = AnalystAgent("fake_key", llm)
    
    print(f"Analyzing research data...")
    
    response = agent.analyze(research_data)
    print(f"Response:\n{response}")
    
    return response

def test_writer_agent(llm, research_data, analysis_data):
    """Test the WriterAgent with real research and analysis data"""
    print("\n=== Testing WriterAgent ===")
    agent = WriterAgent("fake_key", llm)
    
    print(f"Writing based on research and analysis...")
    
    response = agent.write(research_data, analysis_data)
    print(f"Response:\n{response}")
    
    return response

def test_reddit_analyzer_agent(llm):
    """Test the RedditAnalyzerAgent with example comments"""
    print("\n=== Testing RedditAnalyzerAgent ===")
    agent = RedditAnalyzerAgent("fake_key", llm)
    
    # Sample comments for testing
    sample_comments = [
        "I've been having issues with my GPU drivers crashing when playing newer games. Anyone else experiencing this?",
        "This game's performance is terrible even on high-end hardware. Developers need to fix their optimization!",
        "The new update completely broke my save file. Now I have to start over after 60 hours of gameplay. Thanks a lot.",
        "I'm getting constant crashes when trying to run this on Windows 11. Works fine on my Windows 10 machine though.",
        "The load times are insane even with an SSD. What's going on with this game?",
        "Can't believe they still haven't fixed the server issues. It's been two weeks since launch!",
        "Anyone else having frame drops when there are a lot of NPCs on screen?",
        "The UI is so cluttered and confusing. Why did they change it from the previous version?"
    ]
    
    print(f"Analyzing {len(sample_comments)} sample comments...")
    
    analysis = agent.analyze_comments(sample_comments)
    print(f"Analysis:\n{analysis}")
    
    summary = agent.summarize_findings(analysis)
    print(f"\nSummary:\n{summary}")
    
    return analysis, summary

def test_subreddit_discovery_agent(llm):
    """Test the SubredditDiscoveryAgent with a sample topic"""
    print("\n=== Testing SubredditDiscoveryAgent ===")
    agent = SubredditDiscoveryAgent("fake_key", llm)
    
    topic = "mechanical keyboards and custom keycaps"
    print(f"Topic: {topic}")
    
    # Test search term generation
    search_terms = agent.suggest_search_terms(topic)
    print(f"Suggested search terms:\n" + "\n".join(search_terms))
    
    # Sample subreddit data for testing
    sample_subreddits = [
        {
            'name': 'MechanicalKeyboards',
            'title': 'Mechanical Keyboards',
            'description': 'Home of mechanical keyboard enthusiasts and photos of keyboards.',
            'subscribers': 800000
        },
        {
            'name': 'CustomKeyboards',
            'title': 'Custom Keyboards',
            'description': 'A place to share your custom keyboard builds and get advice.',
            'subscribers': 150000
        },
        {
            'name': 'KeycapDesigners',
            'title': 'Keycap Designers',
            'description': 'For designers and enthusiasts of custom keycaps.',
            'subscribers': 50000
        },
        {
            'name': 'Keycaps',
            'title': 'Keycaps',
            'description': 'All about keycaps, artisans, group buys and more!',
            'subscribers': 70000
        },
        {
            'name': 'BuildAKeyboard',
            'title': 'Build A Keyboard',
            'description': 'Learn how to build your own mechanical keyboard from scratch.',
            'subscribers': 95000
        }
    ]
    
    analysis = agent.analyze_subreddits(topic, sample_subreddits)
    print(f"\nSubreddit Analysis:\n{analysis}")
    
    return search_terms, analysis

def main():
    print("Starting live agent tests with real API calls...")
    
    try:
        llm = setup_llm()
        
        # Test individual agents
        research_data = test_research_agent(llm)
        analysis_data = test_analyst_agent(llm, research_data)
        test_writer_agent(llm, research_data, analysis_data)
        test_reddit_analyzer_agent(llm)
        test_subreddit_discovery_agent(llm)
        
        print("\n=== All agent tests completed successfully ===")
        
    except Exception as e:
        print(f"Error during testing: {e}")

if __name__ == "__main__":
    main() 