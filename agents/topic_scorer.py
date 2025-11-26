from youtube_analyzer import YouTubeAnalyzer
from research_agent import ResearchAgent

class TopicScorer:
    """Scores topics based on opportunity, competition, and trends"""
    
    def __init__(self):
        self.youtube = YouTubeAnalyzer()
        self.researcher = ResearchAgent()
    
    def score_topic(self, topic):
        """
        Score a topic on multiple factors
        
        Args:
            topic: Topic to score
            
        Returns:
            Dictionary with scores and analysis
        """
        print(f"\n📊 Scoring topic: '{topic}'...")
        
        # Get YouTube data
        print("\n1️⃣ Analyzing YouTube competition...")
        videos = self.youtube.search_videos(topic, max_results=10)
        
        if not videos:
            return {
                'topic': topic,
                'error': 'No YouTube data found',
                'total_score': 0
            }
        
        # Calculate metrics
        avg_views = sum(v['views'] for v in videos) / len(videos)
        top_video_views = max(v['views'] for v in videos)
        avg_engagement = sum((v['likes'] / v['views'] * 100) if v['views'] > 0 else 0 for v in videos) / len(videos)
        
        # Scoring system (0-100 for each)
        
        # 1. Demand Score (based on views)
        if avg_views > 5_000_000:
            demand_score = 100
        elif avg_views > 1_000_000:
            demand_score = 80
        elif avg_views > 500_000:
            demand_score = 60
        elif avg_views > 100_000:
            demand_score = 40
        else:
            demand_score = 20
        
        # 2. Competition Score (inverse - lower competition = higher score)
        if top_video_views > 10_000_000:
            competition_score = 20  # Very high competition
        elif top_video_views > 5_000_000:
            competition_score = 40
        elif top_video_views > 1_000_000:
            competition_score = 60
        elif top_video_views > 500_000:
            competition_score = 80
        else:
            competition_score = 100  # Low competition
        
        # 3. Engagement Score
        if avg_engagement > 3:
            engagement_score = 100
        elif avg_engagement > 2:
            engagement_score = 80
        elif avg_engagement > 1.5:
            engagement_score = 60
        elif avg_engagement > 1:
            engagement_score = 40
        else:
            engagement_score = 20
        
        # 4. Trend Score (from web research)
        print("\n2️⃣ Checking trend signals...")
        search_results = self.researcher.search_web(f"{topic} trends 2024")
        
        # Simple trend detection based on result count and recency
        if len(search_results) >= 5:
            trend_score = 80
        elif len(search_results) >= 3:
            trend_score = 60
        else:
            trend_score = 40
        
        # Calculate weighted total score
        total_score = (
            demand_score * 0.30 +      # 30% weight on demand
            competition_score * 0.25 + # 25% weight on competition (inverse)
            engagement_score * 0.25 +  # 25% weight on engagement
            trend_score * 0.20         # 20% weight on trends
        )
        
        # Determine recommendation
        if total_score >= 75:
            recommendation = "🟢 STRONG OPPORTUNITY - Create content ASAP!"
            confidence = "High"
        elif total_score >= 60:
            recommendation = "🟡 GOOD OPPORTUNITY - Worth considering"
            confidence = "Medium-High"
        elif total_score >= 45:
            recommendation = "🟠 MODERATE - Needs unique angle"
            confidence = "Medium"
        else:
            recommendation = "🔴 CHALLENGING - High competition or low demand"
            confidence = "Low"
        
        print("\n✅ Scoring complete!")
        
        return {
            'topic': topic,
            'total_score': round(total_score, 1),
            'recommendation': recommendation,
            'confidence': confidence,
            'breakdown': {
                'demand_score': demand_score,
                'competition_score': competition_score,
                'engagement_score': engagement_score,
                'trend_score': trend_score
            },
            'metrics': {
                'avg_views': f"{avg_views:,.0f}",
                'top_video_views': f"{top_video_views:,.0f}",
                'avg_engagement': f"{avg_engagement:.2f}%",
                'videos_analyzed': len(videos)
            }
        }
    
    def compare_topics(self, topics):
        """
        Score and compare multiple topics
        
        Args:
            topics: List of topics to compare
            
        Returns:
            Ranked list of topics with scores
        """
        print(f"\n🔬 Comparing {len(topics)} topics...\n")
        
        scores = []
        for i, topic in enumerate(topics, 1):
            print(f"\n{'='*60}")
            print(f"Analyzing {i}/{len(topics)}: {topic}")
            print('='*60)
            
            score = self.score_topic(topic)
            scores.append(score)
        
        # Sort by total score (descending)
        scores.sort(key=lambda x: x.get('total_score', 0), reverse=True)
        
        # Create comparison report
        print("\n" + "="*80)
        print("📊 TOPIC COMPARISON REPORT")
        print("="*80 + "\n")
        
        for i, score in enumerate(scores, 1):
            print(f"#{i} | {score['topic']}")
            print(f"    Score: {score['total_score']}/100")
            print(f"    {score['recommendation']}")
            print(f"    Confidence: {score['confidence']}")
            print(f"    Views: {score['metrics']['avg_views']} avg")
            print("-"*80)
        
        print(f"\n🏆 WINNER: {scores[0]['topic']} (Score: {scores[0]['total_score']}/100)")
        print("="*80 + "\n")
        
        return scores


# Test function
def test_topic_scorer():
    """Test the topic scoring system"""
    print("🧪 Testing Topic Scorer...\n")
    
    scorer = TopicScorer()
    
    # Test single topic
    print("\n" + "="*80)
    print("TEST 1: Single Topic Scoring")
    print("="*80)
    
    result = scorer.score_topic("AI agents for business")
    
    print(f"\n📊 SCORE BREAKDOWN:")
    print(f"   Topic: {result['topic']}")
    print(f"   Total Score: {result['total_score']}/100")
    print(f"   Recommendation: {result['recommendation']}")
    print(f"   Confidence: {result['confidence']}")
    print(f"\n   Component Scores:")
    for key, value in result['breakdown'].items():
        print(f"   - {key}: {value}/100")
    
    # Test multiple topics
    print("\n\n" + "="*80)
    print("TEST 2: Comparing Multiple Topics")
    print("="*80)
    
    topics_to_compare = [
        "ChatGPT tutorial",
        "AI automation tools",
        "Machine learning basics"
    ]
    
    comparison = scorer.compare_topics(topics_to_compare)
    
    print("\n✅ All tests complete!")


if __name__ == "__main__":
    test_topic_scorer()