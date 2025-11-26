from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

class YouTubeAnalyzer:
    """Agent that analyzes YouTube videos and extracts insights"""
    
    def __init__(self):
        api_key = os.getenv('YOUTUBE_API_KEY')
        if not api_key:
            raise ValueError("YOUTUBE_API_KEY not found in environment")
        self.youtube = build('youtube', 'v3', developerKey=api_key)
    
    def search_videos(self, query, max_results=10):
        """Search for videos on a specific topic"""
        try:
            # Search for videos
            search_request = self.youtube.search().list(
                part="snippet",
                q=query,
                type="video",
                maxResults=max_results,
                order="viewCount",
                relevanceLanguage="en"
            )
            search_response = search_request.execute()
            
            videos = []
            video_ids = []
            
            # Extract video IDs
            for item in search_response.get('items', []):
                video_ids.append(item['id']['videoId'])
            
            # Get detailed statistics
            if video_ids:
                stats_request = self.youtube.videos().list(
                    part="statistics,contentDetails,snippet",
                    id=','.join(video_ids)
                )
                stats_response = stats_request.execute()
                
                for item in stats_response.get('items', []):
                    videos.append({
                        'video_id': item['id'],
                        'title': item['snippet']['title'],
                        'channel': item['snippet']['channelTitle'],
                        'description': item['snippet']['description'][:200],
                        'views': int(item['statistics'].get('viewCount', 0)),
                        'likes': int(item['statistics'].get('likeCount', 0)),
                        'comments': int(item['statistics'].get('commentCount', 0)),
                        'url': f"https://youtube.com/watch?v={item['id']}"
                    })
            
            return videos
            
        except Exception as e:
            print(f"Error searching videos: {str(e)}")
            return []
    
    def analyze_top_videos(self, query, top_n=5):
        """Analyze top performing videos on a topic"""
        print(f"\n🔍 Searching YouTube for: '{query}'...")
        
        videos = self.search_videos(query, max_results=10)
        
        if not videos:
            return "No videos found for this query."
        
        # Sort by views
        videos.sort(key=lambda x: x['views'], reverse=True)
        top_videos = videos[:top_n]
        
        # Create analysis
        analysis = f"📊 TOP {top_n} VIDEOS ANALYSIS FOR: '{query}'\n"
        analysis += "=" * 80 + "\n\n"
        
        total_views = sum(v['views'] for v in top_videos)
        avg_views = total_views // len(top_videos)
        
        for i, video in enumerate(top_videos, 1):
            engagement_rate = (video['likes'] / video['views'] * 100) if video['views'] > 0 else 0
            
            analysis += f"#{i} | {video['title']}\n"
            analysis += f"    Channel: {video['channel']}\n"
            analysis += f"    Views: {video['views']:,}\n"
            analysis += f"    Likes: {video['likes']:,} (Engagement: {engagement_rate:.2f}%)\n"
            analysis += f"    Comments: {video['comments']:,}\n"
            analysis += f"    URL: {video['url']}\n"
            analysis += f"    Preview: {video['description'][:150]}...\n"
            analysis += "-" * 80 + "\n"
        
        analysis += f"\n📈 INSIGHTS:\n"
        analysis += f"   • Total views across top {top_n}: {total_views:,}\n"
        analysis += f"   • Average views: {avg_views:,}\n"
        analysis += f"   • Most successful: {top_videos[0]['title'][:50]}...\n"
        
        return analysis


# Test function
def test_youtube_analyzer():
    """Test the YouTube Analyzer"""
    print("🧪 Testing YouTube Analyzer Agent...\n")
    
    analyzer = YouTubeAnalyzer()
    
    # Test with a topic
    test_topic = "AI agents tutorial"
    result = analyzer.analyze_top_videos(test_topic)
    
    print(result)
    print("\n✅ Test complete!")


if __name__ == "__main__":
    test_youtube_analyzer()