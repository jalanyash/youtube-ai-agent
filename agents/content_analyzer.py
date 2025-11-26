from youtube_analyzer import YouTubeAnalyzer
from research_agent import ResearchAgent
from topic_scorer import TopicScorer

class ContentAnalyzer:
    """Enhanced content analyzer with gap detection and scoring"""
    
    def __init__(self):
        self.youtube = YouTubeAnalyzer()
        self.researcher = ResearchAgent()
        self.scorer = TopicScorer()
    
    def analyze_content_opportunity(self, topic):
        """
        Comprehensive content opportunity analysis
        
        Args:
            topic: The topic to analyze
            
        Returns:
            Complete analysis with scoring, gaps, and recommendations
        """
        print("\n" + "=" * 80)
        print(f"🎬 COMPREHENSIVE CONTENT ANALYSIS: {topic}")
        print("=" * 80)
        
        # Step 1: Score the topic
        print("\n📊 STEP 1: Scoring Topic Opportunity...")
        score_data = self.scorer.score_topic(topic)
        
        # Step 2: YouTube Analysis
        print("\n📺 STEP 2: Analyzing YouTube Competition...")
        youtube_analysis = self.youtube.analyze_top_videos(topic)
        
        # Step 3: Research + Gap Analysis
        print("\n🔬 STEP 3: Research & Gap Analysis...")
        research_results = self.researcher.research_topic(topic)
        gap_analysis = self.researcher.analyze_content_gaps(topic, youtube_analysis)
        
        # Step 4: Generate final report
        print("\n💡 STEP 4: Generating Final Report...")
        
        report = f"""
{'=' * 80}
📊 CONTENT OPPORTUNITY REPORT: {topic}
{'=' * 80}

🎯 OPPORTUNITY SCORE: {score_data['total_score']}/100
{score_data['recommendation']}
Confidence Level: {score_data['confidence']}

📈 SCORE BREAKDOWN:
   • Demand Score: {score_data['breakdown']['demand_score']}/100
   • Competition Score: {score_data['breakdown']['competition_score']}/100
   • Engagement Score: {score_data['breakdown']['engagement_score']}/100
   • Trend Score: {score_data['breakdown']['trend_score']}/100

📊 KEY METRICS:
   • Average Views: {score_data['metrics']['avg_views']}
   • Top Video Views: {score_data['metrics']['top_video_views']}
   • Average Engagement: {score_data['metrics']['avg_engagement']}
   • Videos Analyzed: {score_data['metrics']['videos_analyzed']}

{'=' * 80}

📺 YOUTUBE COMPETITION ANALYSIS:
{'-' * 80}
{youtube_analysis}

{'=' * 80}

🔬 MARKET RESEARCH & TRENDS:
{'-' * 80}
{research_results}

{'=' * 80}

🎯 CONTENT GAP ANALYSIS:
{'-' * 80}
{gap_analysis}

{'=' * 80}

✅ FINAL RECOMMENDATIONS:

1. **Should You Create This Content?**
   {self._get_creation_advice(score_data['total_score'])}

2. **Best Approach:**
   {self._get_approach_advice(score_data)}

3. **Success Factors:**
   - Create content better than top 5 competitors
   - Focus on gaps identified in analysis
   - Leverage trending angles from research
   - Aim for {score_data['metrics']['avg_engagement']} engagement rate

4. **Estimated Potential:**
   - Target views: {self._estimate_views(score_data)}
   - Time to rank: {self._estimate_ranking_time(score_data)}
   - Competition level: {self._get_competition_level(score_data)}

{'=' * 80}
"""
        
        return report
    
    def _get_creation_advice(self, score):
        """Get advice based on score"""
        if score >= 75:
            return "✅ YES! Strong opportunity. Create ASAP while topic is hot."
        elif score >= 60:
            return "🟡 MAYBE. Good opportunity if you have a unique angle."
        elif score >= 45:
            return "⚠️ PROCEED WITH CAUTION. Need strong differentiation."
        else:
            return "❌ NOT RECOMMENDED. Consider different topic or wait for better timing."
    
    def _get_approach_advice(self, score_data):
        """Get approach recommendations"""
        comp_score = score_data['breakdown']['competition_score']
        
        if comp_score >= 80:
            return "Low competition - focus on quality fundamentals and SEO"
        elif comp_score >= 60:
            return "Medium competition - need unique angle or better production"
        elif comp_score >= 40:
            return "High competition - must differentiate significantly"
        else:
            return "Very high competition - only proceed if you can create best-in-class content"
    
    def _estimate_views(self, score_data):
        """Estimate potential views"""
        avg_views = int(score_data['metrics']['avg_views'].replace(',', ''))
        score = score_data['total_score']
        
        if score >= 75:
            return f"{avg_views * 0.3:,.0f} - {avg_views * 0.5:,.0f} (30-50% of average)"
        elif score >= 60:
            return f"{avg_views * 0.15:,.0f} - {avg_views * 0.30:,.0f} (15-30% of average)"
        else:
            return f"{avg_views * 0.05:,.0f} - {avg_views * 0.15:,.0f} (5-15% of average)"
    
    def _estimate_ranking_time(self, score_data):
        """Estimate time to rank"""
        comp_score = score_data['breakdown']['competition_score']
        
        if comp_score >= 80:
            return "1-2 weeks"
        elif comp_score >= 60:
            return "2-4 weeks"
        elif comp_score >= 40:
            return "1-2 months"
        else:
            return "2-3 months or more"
    
    def _get_competition_level(self, score_data):
        """Get competition level description"""
        comp_score = score_data['breakdown']['competition_score']
        
        if comp_score >= 80:
            return "LOW - Great for beginners"
        elif comp_score >= 60:
            return "MEDIUM - Achievable with quality content"
        elif comp_score >= 40:
            return "HIGH - Challenging but possible"
        else:
            return "VERY HIGH - Extremely difficult"
    
    def compare_topics(self, topics):
        """
        Compare multiple topics and recommend the best one
        
        Args:
            topics: List of topic strings
            
        Returns:
            Comparison report
        """
        print("\n" + "=" * 80)
        print(f"🔬 COMPARING {len(topics)} CONTENT IDEAS")
        print("=" * 80)
        
        scores = self.scorer.compare_topics(topics)
        
        print(f"\n🏆 RECOMMENDED TOPIC: {scores[0]['topic']}")
        print(f"   Score: {scores[0]['total_score']}/100")
        print(f"   {scores[0]['recommendation']}")
        
        return scores


# Test function
def test_enhanced_analyzer():
    """Test the enhanced content analyzer"""
    print("🧪 Testing Enhanced Content Analyzer...\n")
    
    analyzer = ContentAnalyzer()
    
    # Test 1: Single topic analysis
    topic = "AI tools for productivity"
    
    print(f"📝 Analyzing: {topic}")
    print("⏳ This will take 2-3 minutes (comprehensive analysis)...\n")
    
    report = analyzer.analyze_content_opportunity(topic)
    
    print(report)
    print("\n✅ Analysis complete!")


if __name__ == "__main__":
    test_enhanced_analyzer()