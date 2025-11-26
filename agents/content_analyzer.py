# from agents.youtube_analyzer import YouTubeAnalyzer
# from agents.research_agent import ResearchAgent
from youtube_analyzer import YouTubeAnalyzer
from research_agent import ResearchAgent
class ContentAnalyzer:
    """Combines YouTube analysis with web research for comprehensive insights"""
    
    def __init__(self):
        self.youtube = YouTubeAnalyzer()
        self.researcher = ResearchAgent()
    
    def analyze_content_opportunity(self, topic):
        """
        Analyze a topic from both YouTube and web research perspectives
        
        Args:
            topic: The topic to analyze
            
        Returns:
            Combined analysis with recommendations
        """
        print("\n" + "=" * 80)
        print(f"🎬 CONTENT OPPORTUNITY ANALYSIS: {topic}")
        print("=" * 80)
        
        # Step 1: YouTube Analysis
        print("\n📺 STEP 1: Analyzing YouTube Competition...")
        youtube_analysis = self.youtube.analyze_top_videos(topic)
        
        # Step 2: Web Research
        print("\n🔬 STEP 2: Researching Current Trends...")
        research_results = self.researcher.research_topic(topic)
        
        # Step 3: Combine insights
        print("\n💡 STEP 3: Generating Combined Report...")
        
        report = f"""
{'=' * 80}
📊 COMPREHENSIVE CONTENT ANALYSIS: {topic}
{'=' * 80}

📺 YOUTUBE COMPETITION ANALYSIS:
{'-' * 80}
{youtube_analysis}

{'=' * 80}

🔬 WEB RESEARCH & CURRENT TRENDS:
{'-' * 80}
{research_results}

{'=' * 80}

💡 CONTENT STRATEGY RECOMMENDATIONS:
{'-' * 80}

Based on the combined analysis above, here are actionable insights:

1. **Competition Level**: 
   - Check the view counts in the YouTube analysis
   - High views = proven demand for this topic

2. **Trending Angles**: 
   - Look at "Current Trends" in the research section
   - These are hot topics right now

3. **Content Gaps**: 
   - Compare YouTube top videos with research findings
   - Topics mentioned in research but missing from top videos = opportunity!

4. **Audience Questions**:
   - See "Common Questions" in research
   - Answer these questions = high engagement potential

5. **Timing**:
   - Recent developments = perfect timing for new content
   - Strike while the topic is hot!

{'=' * 80}
"""
        
        return report


# Test function
def test_content_analyzer():
    """Test the combined analyzer"""
    print("🧪 Testing Content Analyzer (YouTube + Research)...\n")
    
    analyzer = ContentAnalyzer()
    
    # Test topic
    topic = "ChatGPT for beginners"
    
    print(f"📝 Analyzing: {topic}")
    print("⏳ This will take 1-2 minutes (both agents working!)...\n")
    
    # Run full analysis
    full_report = analyzer.analyze_content_opportunity(topic)
    
    print(full_report)
    print("\n✅ Complete analysis done!")


if __name__ == "__main__":
    test_content_analyzer()