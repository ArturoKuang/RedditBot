import openai
import json
from typing import Dict, List, Optional

from llms import BaseLLM


class BaseAgent:
    def __init__(self, api_key: str, llm: BaseLLM):
        self.conversation_history: List[Dict] = []
        self.llm = llm

    def _call_llm(self, messages: List[Dict]) -> str:
        try:
            return self.llm._call_llm(messages)
        except Exception as e:
            print(f"Error calling LLM: {e}")
            return ""


class ResearchAgent(BaseAgent):
    def __init__(self, api_key: str, llm: BaseLLM):
        super().__init__(api_key)
        self.system_prompt = """You are a research agent. Your role is to gather and provide 
        relevant information about a given topic. Focus on finding key facts and data points. 
        Be concise and accurate."""

    def research(self, query: str) -> str:
        messages = [
            self._format_message("system", self.system_prompt),
            self._format_message("user", query)
        ]
        return self._call_llm(messages)


class AnalystAgent(BaseAgent):
    def __init__(self, api_key: str, llm: BaseLLM):
        super().__init__(api_key)
        self.system_prompt = """You are an analysis agent. Your role is to analyze information 
        and identify patterns, insights, and conclusions. Be logical and thorough in your analysis."""

    def analyze(self, data: str) -> str:
        messages = [
            self._format_message("system", self.system_prompt),
            self._format_message(
                "user", f"Analyze the following information: {data}")
        ]
        return self._call_llm(messages)


class WriterAgent(BaseAgent):
    def __init__(self, api_key: str, llm: BaseLLM):
        super().__init__(api_key, llm)
        self.system_prompt = """You are a writer agent. Your role is to create well-structured, 
        engaging content based on provided information and analysis. Focus on clarity and coherence."""

    def write(self, research: str, analysis: str) -> str:
        prompt = f"""Based on the following research and analysis, create a well-structured report:
        
        Research: {research}
        
        Analysis: {analysis}"""

        messages = [
            self._format_message("system", self.system_prompt),
            self._format_message("user", prompt)
        ]
        return self._call_llm(messages)


class RedditAnalyzerAgent(BaseAgent):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.system_prompt = """You are a specialized agent for analyzing Reddit comments. 
        Your role is to:
        1. Identify common complaints, problems, and pain points
        2. Group similar issues together
        3. Determine the frequency and severity of each problem
        4. Extract any relevant context or user sentiment
        Be thorough in your analysis and format the output as a structured summary."""

    def analyze_comments(self, comments: List[str]) -> str:
        # Format comments for analysis
        formatted_comments = "\n".join(
            [f"Comment {i+1}: {comment}" for i, comment in enumerate(comments)])

        prompt = f"""Analyze the following Reddit comments and identify common complaints, 
        problems, and user pain points. Group similar issues together and note their frequency:

        {formatted_comments}

        Please structure your analysis as follows:
        1. Main Issues Identified (ordered by frequency)
        2. User Sentiment Analysis
        3. Context and Contributing Factors
        4. Notable Quotes or Examples"""

        messages = [
            self._format_message("system", self.system_prompt),
            self._format_message("user", prompt)
        ]
        return self._call_llm(messages)

    def summarize_findings(self, analysis: str) -> str:
        prompt = """Based on the analysis, provide a concise summary of the top 3-5 most 
        significant problems users are facing, including any patterns in user behavior or sentiment."""

        messages = [
            self._format_message("system", self.system_prompt),
            self._format_message("user", f"{analysis}\n\n{prompt}")
        ]
        return self._call_llm(messages)


class SubredditDiscoveryAgent(BaseAgent):
    def __init__(self, api_key: str, llm: BaseLLM):
        super().__init__(api_key, llm)
        self.system_prompt = """You are a specialized agent for discovering and analyzing relevant subreddits.
        Your role is to:
        1. Analyze subreddit descriptions and determine relevance to the user's interests
        2. Rank subreddits by relevance and quality
        3. Provide brief explanations of why each subreddit is relevant
        4. Filter out inappropriate or off-topic communities
        Be thorough in your analysis and focus on finding the most relevant communities."""

    def analyze_subreddits(self, query: str, subreddits: List[Dict]) -> str:
        formatted_subreddits = "\n".join([
            f"r/{sub['name']}: {sub['title']}\n"
            f"Description: {sub['description']}\n"
            f"Subscribers: {sub['subscribers']}\n"
            for sub in subreddits
        ])
        
        prompt = f"""Based on the user's interest in '{query}', analyze these subreddits and rank them by relevance:

        {formatted_subreddits}

        Please structure your analysis as follows:
        1. Most Relevant Communities (ordered by relevance)
        2. Why These Communities Are Relevant
        3. Additional Recommendations
        4. Communities to Avoid (if any)"""

        messages = [
            self._format_message("system", self.system_prompt),
            self._format_message("user", prompt)
        ]
        return self._call_llm(messages)

    def suggest_search_terms(self, topic: str) -> List[str]:
        """Generate relevant search terms for finding subreddits"""
        prompt = f"""Given the topic '{topic}', suggest 5-7 relevant search terms that would help find related subreddits.
        Consider different aspects and variations of the topic. Return only the search terms, one per line."""
        
        messages = [
            self._format_message("system", self.system_prompt),
            self._format_message("user", prompt)
        ]
        response = self._call_llm(messages)
        return [term.strip() for term in response.split('\n') if term.strip()]