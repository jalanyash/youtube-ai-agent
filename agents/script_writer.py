from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class ScriptWriter:
    """Agent that writes YouTube video scripts based on research and analysis"""
    
    def __init__(self):
        # Use GPT-4 with higher temperature for creativity
        self.llm = ChatOpenAI(
            model="gpt-4-turbo-preview",
            temperature=0.7,  # Higher = more creative
            api_key=os.getenv('OPENAI_API_KEY')
        )
    
    def write_script(self, topic, youtube_analysis, research_data, gap_analysis, 
                     video_length="10-15 minutes", tone="educational"):
        """
        Generate a complete YouTube video script
        
        Args:
            topic: Video topic
            youtube_analysis: Data from YouTube Analyzer
            research_data: Research findings
            gap_analysis: Content gap analysis
            video_length: Target video length
            tone: Script tone (educational, entertaining, professional, casual)
            
        Returns:
            Complete formatted script
        """
        print(f"\n✍️ Writing script for: '{topic}'...")
        print(f"   Length: {video_length} | Tone: {tone}")
        
        # Create comprehensive prompt
        script_prompt = f"""You are an expert YouTube script writer who creates engaging, high-performing video scripts.

TOPIC: {topic}

TARGET LENGTH: {video_length}
TONE: {tone}

YOUTUBE COMPETITION ANALYSIS:
{youtube_analysis}

RESEARCH INSIGHTS:
{research_data}

CONTENT GAPS TO ADDRESS:
{gap_analysis}

Write a complete, production-ready YouTube video script with the following structure:

---
**HOOK (0:00-0:15)**
[First 10-15 seconds - CRITICAL for retention]
- Start with a surprising fact, bold statement, or compelling question
- Make viewers NEED to keep watching
- No intro fluff - get straight to value

**INTRODUCTION (0:15-1:00)**
- Briefly introduce yourself (if first-time viewers)
- Preview what viewers will learn
- Set expectations
- Build credibility on this topic

**MAIN CONTENT (Body - structured in clear sections)**
Section 1: [Title]
- Timestamp: [X:XX]
- Key points to cover
- [B-ROLL: Suggestion for visuals]
- Practical examples

Section 2: [Title]
- Timestamp: [X:XX]
- Key points
- [B-ROLL: Suggestion]
- Keep it engaging

[Continue for 3-5 sections based on video length]

**CALL TO ACTION (Before Outro)**
- Ask viewers to like/subscribe (make it genuine, not pushy)
- Mention next video or related content
- Encourage comments with a specific question

**OUTRO (Final 30 seconds)**
- Quick recap of main takeaways
- Thank viewers
- End screen prompt
---

IMPORTANT GUIDELINES:
1. Write conversationally - like talking to a friend, not reading an essay
2. Include specific examples and actionable advice
3. Address the content gaps identified in the analysis
4. Use short sentences and paragraphs for better pacing
5. Include [B-ROLL] suggestions where visuals would enhance understanding
6. Add [PAUSE] markers where natural breaks occur
7. Include approximate timestamps based on video length
8. Make it ENGAGING - YouTube viewers have short attention spans
9. Front-load value - don't save the best for last
10. End sections with transitions that maintain interest

Write the complete script now:"""

        try:
            print("\n🤖 Generating script with GPT-4...")
            
            messages = [
                {"role": "system", "content": "You are an expert YouTube script writer who creates engaging, viral-worthy video scripts."},
                {"role": "user", "content": script_prompt}
            ]
            
            response = self.llm.invoke(messages)
            script = response.content
            
            print("\n✅ Script generated successfully!")
            
            # Add metadata header
            script_with_metadata = f"""
{'='*80}
YOUTUBE VIDEO SCRIPT
{'='*80}
Topic: {topic}
Target Length: {video_length}
Tone: {tone}
Generated: {self._get_timestamp()}
{'='*80}

{script}

{'='*80}
END OF SCRIPT
{'='*80}
"""
            
            return script_with_metadata
            
        except Exception as e:
            print(f"\n❌ Script generation error: {str(e)}")
            return f"Script generation failed: {str(e)}"
    
    def write_multiple_variations(self, topic, youtube_analysis, research_data, 
                                   gap_analysis, video_length="10-15 minutes"):
        """
        Generate 3 script variations with different tones
        
        Args:
            Same as write_script but without tone parameter
            
        Returns:
            Dictionary with 3 script variations
        """
        print(f"\n📝 Generating 3 script variations for: '{topic}'...")
        
        tones = ["educational", "entertaining", "professional"]
        scripts = {}
        
        for i, tone in enumerate(tones, 1):
            print(f"\n{'='*60}")
            print(f"Variation {i}/3: {tone.upper()} tone")
            print('='*60)
            
            script = self.write_script(
                topic, youtube_analysis, research_data, 
                gap_analysis, video_length, tone
            )
            scripts[tone] = script
        
        return scripts
    
    def _get_timestamp(self):
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def save_script(self, script, topic, output_dir="scripts"):
        """
        Save script to a file
        
        Args:
            script: Script content
            topic: Topic name (for filename)
            output_dir: Directory to save to
            
        Returns:
            File path
        """
        import os
        from datetime import datetime
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Create safe filename
        safe_topic = topic.replace(" ", "_").replace("/", "-")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{safe_topic}_{timestamp}.txt"
        filepath = os.path.join(output_dir, filename)
        
        # Save script
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(script)
        
        print(f"\n💾 Script saved to: {filepath}")
        return filepath


# Test function
def test_script_writer():
    """Test the Script Writer Agent"""
    print("🧪 Testing Script Writer Agent...\n")
    print("="*80)
    
    writer = ScriptWriter()
    
    # Sample data (in real use, this comes from other agents)
    topic = "AI Tools for Productivity"
    
    youtube_analysis = """Top 5 videos average 6M views each.
Most successful approach: List-style format showing 5-10 tools.
High engagement on practical demos and real use cases."""
    
    research_data = """Trending: AI automation, personalized AI assistants.
Common questions: Which tools are best? How much do they cost?
Gap: Not enough content on limitations and privacy concerns."""
    
    gap_analysis = """High opportunity: AI tools for specific industries.
Underserved angle: Honest reviews including cons.
Trending: Ethical AI use in business."""
    
    print(f"📝 Topic: {topic}")
    print("⏳ This will take 60-90 seconds (GPT-4 is writing!)...\n")
    
    # Generate script
    script = writer.write_script(
        topic=topic,
        youtube_analysis=youtube_analysis,
        research_data=research_data,
        gap_analysis=gap_analysis,
        video_length="10-12 minutes",
        tone="educational"
    )
    
    print("\n" + "="*80)
    print("📄 GENERATED SCRIPT:")
    print("="*80)
    print(script)
    print("\n✅ Test complete!")


if __name__ == "__main__":
    test_script_writer()