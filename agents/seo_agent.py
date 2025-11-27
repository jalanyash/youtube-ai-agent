from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class SEOAgent:
    """Agent that optimizes YouTube video metadata for SEO"""
    
    def __init__(self):
        # Use GPT-4 for creative SEO optimization
        self.llm = ChatOpenAI(
            model="gpt-4-turbo-preview",
            temperature=0.5,  # Balanced creativity and focus
            api_key=os.getenv('OPENAI_API_KEY')
        )
    
    def optimize_metadata(self, topic, script, youtube_analysis, research_data):
        """
        Generate complete SEO-optimized metadata for YouTube video
        
        Args:
            topic: Video topic
            script: Video script content
            youtube_analysis: Competitor analysis
            research_data: Market research
            
        Returns:
            Dictionary with titles, description, tags, thumbnail text
        """
        print(f"\n🎯 Optimizing SEO for: '{topic}'...")
        
        # Create comprehensive SEO prompt
        seo_prompt = f"""You are a YouTube SEO expert who optimizes video metadata for maximum views and discoverability.

TOPIC: {topic}

VIDEO SCRIPT:
{script[:2000]}...

COMPETITOR ANALYSIS:
{youtube_analysis}

MARKET RESEARCH:
{research_data[:1000]}...

Generate complete SEO-optimized metadata:

---
## 1. TITLES (3 Variations)

**Title A: Clickability-Focused** (50-60 characters)
- Curiosity-driven, makes viewers want to click
- Uses power words, numbers, or questions
- Example format: "This [X] Changed Everything (You Won't Believe #3)"

**Title B: Keyword-Rich** (50-60 characters)
- Front-loads main keywords for SEO
- Clear value proposition
- Example format: "[Main Keyword]: Complete Guide to [Benefit]"

**Title C: Emotional Hook** (50-60 characters)
- Triggers emotion (surprise, urgency, FOMO)
- Personal or relatable angle
- Example format: "I Tried [X] For 30 Days - Here's What Happened"

---
## 2. DESCRIPTION (First 150 chars crucial!)

**Above the Fold (First 2-3 lines):**
[Hook that makes viewers want to read more + main keywords]

**Main Body:**
- Brief video overview with keywords
- What viewers will learn (3-5 bullet points)
- Call to action (like, subscribe, comment)

**Timestamps:**
0:00 - Introduction
[X:XX] - [Section name]
[Continue for main sections...]

**Resources & Links:**
[Placeholder for relevant links]

**Social/Contact:**
[Placeholder for social media]

**Hashtags:**
#[Tag1] #[Tag2] #[Tag3]

---
## 3. TAGS (15-20 tags)

**Primary Tags (5-7):**
[Main topic keywords, exact match phrases]

**Secondary Tags (5-7):**
[Related topics, broader keywords]

**Long-tail Tags (5-6):**
[Specific phrases, questions people search]

---
## 4. THUMBNAIL TEXT (3-5 word options)

**Option 1:** [Bold, attention-grabbing]
**Option 2:** [Question or number-based]
**Option 3:** [Benefit-focused]

---
## 5. SEO NOTES

**Primary Keyword:** [Main keyword to optimize for]
**Search Volume:** [High/Medium/Low based on research]
**Competition:** [Easy/Medium/Hard based on analysis]
**Recommendation:** [Best practices for this specific video]

---

IMPORTANT:
- Keep titles under 60 characters (mobile optimization)
- Front-load keywords in title and description
- Use exact match keywords from competitor analysis
- Include timestamps for better SEO
- Balance clickability with honesty (no clickbait lies)
- Consider YouTube's algorithm preferences (watch time, CTR)"""

        try:
            print("\n🤖 Generating SEO metadata with GPT-4...")
            
            messages = [
                {"role": "system", "content": "You are an expert YouTube SEO specialist who maximizes video discoverability and views."},
                {"role": "user", "content": seo_prompt}
            ]
            
            response = self.llm.invoke(messages)
            seo_content = response.content
            
            print("\n✅ SEO metadata generated!")
            
            # Format the output
            formatted_output = f"""
{'='*80}
SEO-OPTIMIZED METADATA
{'='*80}
Topic: {topic}
Generated for YouTube optimization
{'='*80}

{seo_content}

{'='*80}
END OF SEO METADATA
{'='*80}
"""
            
            return formatted_output
            
        except Exception as e:
            print(f"\n❌ SEO generation error: {str(e)}")
            return f"SEO generation failed: {str(e)}"
    
    def generate_quick_seo(self, topic, script_snippet):
        """
        Quick SEO generation without full analysis (faster, cheaper)
        
        Args:
            topic: Video topic
            script_snippet: First part of script
            
        Returns:
            Basic SEO metadata
        """
        print(f"\n⚡ Generating quick SEO for: '{topic}'...")
        
        quick_prompt = f"""Generate YouTube SEO metadata for: {topic}

Script preview: {script_snippet[:500]}

Provide:
1. One optimized title (50-60 chars)
2. Brief description (2-3 sentences)
3. 10 tags
4. One thumbnail text idea

Keep it concise and SEO-focused."""

        try:
            messages = [
                {"role": "system", "content": "You are a YouTube SEO expert."},
                {"role": "user", "content": quick_prompt}
            ]
            
            response = self.llm.invoke(messages)
            return response.content
            
        except Exception as e:
            return f"Quick SEO failed: {str(e)}"


# Test function
def test_seo_agent():
    """Test the SEO Agent"""
    print("🧪 Testing SEO Agent...\n")
    print("="*80)
    
    agent = SEOAgent()
    
    # Sample data
    topic = "ChatGPT Tips for Beginners"
    
    script = """
**HOOK (0:00-0:15)**
Did you know that the right ChatGPT prompt can 10x your productivity? 
Stay tuned to learn the secrets!

**INTRODUCTION (0:15-1:00)**
Hey everyone! Today we're diving into ChatGPT tips that will change 
how you work...
"""
    
    youtube_analysis = """Top videos average 5M views.
Successful titles use numbers and "secrets" angle.
High engagement on practical tips format."""
    
    research_data = """Trending: ChatGPT productivity hacks, prompt engineering.
Common searches: "ChatGPT tips", "how to use ChatGPT better"
High demand for beginner-friendly content."""
    
    print(f"📝 Topic: {topic}")
    print("⏳ This will take 30-60 seconds...\n")
    
    # Generate SEO metadata
    seo_metadata = agent.optimize_metadata(
        topic=topic,
        script=script,
        youtube_analysis=youtube_analysis,
        research_data=research_data
    )
    
    print("\n" + "="*80)
    print("🎯 SEO METADATA:")
    print("="*80)
    print(seo_metadata)
    
    print("\n✅ Test complete!")


if __name__ == "__main__":
    test_seo_agent()