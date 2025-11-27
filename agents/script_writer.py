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
                                   gap_analysis, video_length="10-12 minutes"):
        """
        Generate 3 script variations with different tones
        
        Args:
            Same as write_script but without tone parameter
            
        Returns:
            Dictionary with 3 script variations + comparison
        """
        print(f"\n📝 Generating 3 script variations for: '{topic}'...")
        print(f"   This will take 3-4 minutes...\n")
        
        tones = {
            "educational": "Clear, informative, teaching-focused. Like a knowledgeable professor.",
            "entertaining": "Fun, energetic, personality-driven. Like a friend sharing cool stuff.",
            "professional": "Polished, authoritative, business-like. Like an industry expert."
        }
        
        scripts = {}
        
        for i, (tone, description) in enumerate(tones.items(), 1):
            print(f"\n{'='*70}")
            print(f"📝 Variation {i}/3: {tone.upper()} ({description})")
            print('='*70)
            
            script = self.write_script(
                topic, youtube_analysis, research_data, 
                gap_analysis, video_length, tone
            )
            scripts[tone] = script
        
        # Generate comparison
        print(f"\n{'='*70}")
        print(f"📊 Generating Comparison Analysis...")
        print('='*70)
        
        comparison = self._compare_script_variations(scripts, topic)
        scripts['comparison'] = comparison
        
        print("\n✅ All variations and comparison generated!")
        
        return scripts
    
    def _compare_script_variations(self, scripts, topic):
        """
        Compare script variations and recommend best approach
        
        Args:
            scripts: Dictionary of scripts by tone
            topic: Topic name
            
        Returns:
            Comparison analysis
        """
        comparison_prompt = f"""You are a YouTube content strategist analyzing different script approaches.

TOPIC: {topic}

I have 3 script variations:
1. EDUCATIONAL TONE
2. ENTERTAINING TONE
3. PROFESSIONAL TONE

Based on the topic and typical YouTube audience preferences, provide:

1. **RECOMMENDED TONE** (which one is best for this topic and why)
   - Consider: topic type, target audience, competition style, engagement potential

2. **TONE COMPARISON**
   - Educational: Best for [scenarios] | Pros | Cons
   - Entertaining: Best for [scenarios] | Pros | Cons
   - Professional: Best for [scenarios] | Pros | Cons

3. **HYBRID APPROACH** (optional)
   - Suggest mixing elements from different tones if beneficial

4. **FINAL VERDICT**
   - Which script to use for maximum views and engagement
   - Any modifications to make it even better

Be specific and practical. Consider what works on YouTube."""

        try:
            messages = [
                {"role": "system", "content": "You are an expert YouTube content strategist."},
                {"role": "user", "content": comparison_prompt}
            ]
            
            response = self.llm.invoke(messages)
            comparison = response.content
            
            # Format comparison
            formatted_comparison = f"""
{'='*80}
SCRIPT VARIATION COMPARISON ANALYSIS
{'='*80}
Topic: {topic}
Variations Analyzed: Educational, Entertaining, Professional
{'='*80}

{comparison}

{'='*80}
END OF COMPARISON
{'='*80}
"""
            
            return formatted_comparison
            
        except Exception as e:
            print(f"\n❌ Comparison error: {str(e)}")
            return "Comparison analysis unavailable."
    
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
    """Test the Script Writer Agent with variations"""
    print("🧪 Testing Script Writer Agent with Variations...\n")
    print("="*80)
    
    writer = ScriptWriter()
    
    # Sample data
    topic = "Best AI Tools for Students"
    
    youtube_analysis = """Top videos average 8M views.
Successful format: List-style with practical demos.
High engagement on real student testimonials."""
    
    research_data = """Trending: AI note-taking, study assistants.
Common questions: Are they free? Do they work offline?
Gap: Not enough content on budget options."""
    
    gap_analysis = """High opportunity: AI tools under $10/month.
Underserved: Privacy-focused AI tools for students.
Trending: AI for exam preparation."""
    
    print(f"📝 Topic: {topic}")
    print("⏳ Generating 3 script variations...")
    print("   This will take 3-4 minutes (GPT-4 writing 3 scripts!)\n")
    
    # Generate all variations
    variations = writer.write_multiple_variations(
        topic=topic,
        youtube_analysis=youtube_analysis,
        research_data=research_data,
        gap_analysis=gap_analysis,
        video_length="10-12 minutes"
    )
    
    # Display comparison
    print("\n" + "="*80)
    print("📊 COMPARISON ANALYSIS:")
    print("="*80)
    print(variations['comparison'])
    
    # Show snippet of each script
    print("\n" + "="*80)
    print("📄 SCRIPT PREVIEWS:")
    print("="*80)
    
    for tone in ['educational', 'entertaining', 'professional']:
        print(f"\n{tone.upper()} TONE (first 300 chars):")
        print("-" * 70)
        # Find the hook in the script
        script = variations[tone]
        hook_start = script.find("**HOOK")
        if hook_start != -1:
            preview = script[hook_start:hook_start+300]
            print(preview + "...")
        else:
            print(script[:300] + "...")
    
    print("\n✅ All variations generated successfully!")


if __name__ == "__main__":
    test_script_writer()