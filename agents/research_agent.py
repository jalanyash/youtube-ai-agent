from langchain_openai import ChatOpenAI
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

class ResearchAgent:
    """Agent that conducts web research on topics for YouTube content creation"""
    
    def __init__(self):
        # Initialize GPT-4
        self.llm = ChatOpenAI(
            model="gpt-4-turbo-preview",
            temperature=0.3,
            api_key=os.getenv('OPENAI_API_KEY')
        )
        
        # Initialize Tavily client directly
        self.tavily = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))
    
    def search_web(self, query):
        """Search the web using Tavily"""
        try:
            print(f"   🔍 Searching: {query}")
            response = self.tavily.search(query=query, max_results=5)
            return response.get('results', [])
        except Exception as e:
            print(f"   ❌ Search error: {str(e)}")
            return []
    
    def research_topic(self, topic):
        """
        Research a topic using web search and AI analysis
        
        Args:
            topic: The topic to research
            
        Returns:
            Comprehensive research summary
        """
        print(f"\n🔬 Starting research on: '{topic}'...")
        
        # Step 1: Search the web
        print("\n📡 Step 1: Searching the web...")
        queries = [
            f"{topic} trends 2024",
            f"{topic} tutorial popular",
            f"{topic} recent developments"
        ]
        
        all_results = []
        for query in queries:
            results = self.search_web(query)
            all_results.extend(results)
        
        if not all_results:
            return "No search results found. Please check your Tavily API key."
        
        # Step 2: Compile search findings
        print("\n📊 Step 2: Compiling findings...")
        search_summary = "WEB SEARCH FINDINGS:\n\n"
        for i, result in enumerate(all_results[:10], 1):
            search_summary += f"{i}. {result.get('title', 'No title')}\n"
            search_summary += f"   {result.get('content', '')[:200]}...\n"
            search_summary += f"   Source: {result.get('url', 'No URL')}\n\n"
        
        # Step 3: Analyze with GPT-4
        print("\n🤖 Step 3: Analyzing with GPT-4...")
        
        analysis_prompt = f"""You are an expert research assistant for YouTube content creators.

I've gathered web search results about: {topic}

Here are the search findings:
{search_summary}

Based on these findings, provide a comprehensive research summary with:

1. **Current Trends**: What's trending right now?
2. **Popular Subtopics**: What specific angles are people interested in?
3. **Common Questions**: What questions do people have?
4. **Recent Developments**: Any news or updates in the last 30 days?
5. **Content Opportunities**: Gaps or angles not well-covered yet

Be specific, actionable, and format clearly with sections."""

        try:
            messages = [
                {"role": "system", "content": "You are an expert research assistant for YouTube creators."},
                {"role": "user", "content": analysis_prompt}
            ]
            
            response = self.llm.invoke(messages)
            analysis = response.content
            
            print("\n✅ Research complete!")
            return analysis
            
        except Exception as e:
            print(f"\n❌ GPT-4 Error: {str(e)}")
            return f"Analysis failed: {str(e)}\n\nRaw search results:\n{search_summary}"

    def analyze_content_gaps(self, topic, youtube_data):
            """
            Analyze content gaps by comparing YouTube videos with web research
            
            Args:
                topic: The topic being analyzed
                youtube_data: YouTube analysis results
                
            Returns:
                Structured gap analysis with opportunities
            """
            print(f"\n🔍 Analyzing content gaps for: '{topic}'...")
            
            # First, do research
            research = self.research_topic(topic)
            
            # Then analyze gaps with GPT-4
            print("\n💡 Identifying opportunities...")
            
            gap_analysis_prompt = f"""You are a content strategy expert analyzing opportunities for YouTube creators.

    TOPIC: {topic}

    YOUTUBE COMPETITION DATA:
    {youtube_data}

    WEB RESEARCH INSIGHTS:
    {research}

    Based on this information, identify specific content gaps and opportunities:

    1. **HIGH OPPORTUNITY TOPICS** (3-5 topics):
    - Topics that are trending in research but few/no videos in top results
    - Format: Topic name | Why it's an opportunity | Estimated difficulty

    2. **UNDERSERVED ANGLES** (3-5 angles):
    - Popular topics but specific angles not well covered
    - Format: Angle | Gap description | Potential views

    3. **TRENDING BUT LOW COMPETITION** (2-3 topics):
    - Recent developments with minimal video coverage
    - Format: Topic | Trend signal | Competition level

    4. **CONTENT IMPROVEMENT OPPORTUNITIES** (2-3):
    - Topics with high views but room for better content
    - Format: What's missing | How to improve | Why it'll win

    Be specific, actionable, and data-driven. Focus on opportunities that can realistically get views."""

            try:
                messages = [
                    {"role": "system", "content": "You are an expert content strategist for YouTube creators."},
                    {"role": "user", "content": gap_analysis_prompt}
                ]
                
                response = self.llm.invoke(messages)
                gap_analysis = response.content
                
                print("\n✅ Gap analysis complete!")
                return gap_analysis
                
            except Exception as e:
                print(f"\n❌ Gap analysis error: {str(e)}")
                return "Gap analysis failed. Using basic research data."
            


# Test function
def test_research_agent():
    """Test the Research Agent"""
    print("🧪 Testing Research Agent...\n")
    print("=" * 80)
    
    researcher = ResearchAgent()
    
    # Test topic
    test_topic = "AI agents for small business"
    
    print(f"\n📝 Topic: {test_topic}")
    print("⏳ This will take 30-60 seconds...\n")
    
    # Run research
    research_results = researcher.research_topic(test_topic)
    
    print("\n" + "=" * 80)
    print("📊 RESEARCH RESULTS:")
    print("=" * 80)
    print(research_results)
    print("\n" + "=" * 80)
    print("✅ Test complete!")


if __name__ == "__main__":
    test_research_agent()