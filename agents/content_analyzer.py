from youtube_analyzer import YouTubeAnalyzer
from research_agent import ResearchAgent
from topic_scorer import TopicScorer
from script_writer import ScriptWriter
from seo_agent import SEOAgent

class ContentAnalyzer:
    """Enhanced content analyzer with gap detection and scoring"""
    
    def __init__(self):
        self.youtube = YouTubeAnalyzer()
        self.researcher = ResearchAgent()
        self.scorer = TopicScorer()
    
    def generate_full_content_package(self, topic, video_length="10-12 minutes", 
                                       tone="educational"):
        """
        Generate complete content package: analysis + script
        
        Args:
            topic: Video topic
            video_length: Target length
            tone: Script tone
            
        Returns:
            Dictionary with analysis and script
        """
        print("\n" + "=" * 80)
        print(f"🎬 GENERATING COMPLETE CONTENT PACKAGE: {topic}")
        print("=" * 80)
        
        # Initialize script writer
        writer = ScriptWriter()
        
        # Step 1: Score the topic
        print("\n📊 STEP 1/5: Scoring Topic Opportunity...")
        score_data = self.scorer.score_topic(topic)
        
        # Step 2: YouTube Analysis
        print("\n📺 STEP 2/5: Analyzing YouTube Competition...")
        youtube_analysis = self.youtube.analyze_top_videos(topic)
        
        # Step 3: Research
        print("\n🔬 STEP 3/5: Conducting Market Research...")
        research_results = self.researcher.research_topic(topic)
        
        # Step 4: Gap Analysis
        print("\n🎯 STEP 4/5: Identifying Content Gaps...")
        gap_analysis = self.researcher.analyze_content_gaps(topic, youtube_analysis)
        
        # Step 5: Generate Script
        print("\n✍️ STEP 5/5: Writing Video Script...")
        script = writer.write_script(
            topic=topic,
            youtube_analysis=youtube_analysis,
            research_data=research_results,
            gap_analysis=gap_analysis,
            video_length=video_length,
            tone=tone
        )
        
        print("\n🎉 COMPLETE PACKAGE GENERATED!")
        
        # Combine everything
        package = {
            'topic': topic,
            'score': score_data,
            'youtube_analysis': youtube_analysis,
            'research': research_results,
            'gaps': gap_analysis,
            'script': script,
            'metadata': {
                'video_length': video_length,
                'tone': tone,
                'recommendation': score_data['recommendation']
            }
        }
        
        return package
    
    def generate_complete_package(self, topic, video_length="10-12 minutes", 
                                   include_variations=False):
        """
        Generate the ULTIMATE content package: analysis + scripts + SEO
        
        Args:
            topic: Video topic
            video_length: Target length
            include_variations: If True, generates 3 script variations
            
        Returns:
            Complete package with everything
        """
        print("\n" + "=" * 80)
        print(f"🚀 GENERATING ULTIMATE CONTENT PACKAGE: {topic}")
        print("=" * 80)
        
        # Initialize all agents
        from script_writer import ScriptWriter
        writer = ScriptWriter()
        seo_optimizer = SEOAgent()
        
        # Step 1: Score
        print("\n📊 STEP 1/6: Scoring Topic...")
        score_data = self.scorer.score_topic(topic)
        
        # Step 2: YouTube Analysis
        print("\n📺 STEP 2/6: Analyzing YouTube Competition...")
        youtube_analysis = self.youtube.analyze_top_videos(topic)
        
        # Step 3: Research
        print("\n🔬 STEP 3/6: Conducting Research...")
        research_results = self.researcher.research_topic(topic)
        
        # Step 4: Gap Analysis
        print("\n🎯 STEP 4/6: Identifying Content Gaps...")
        gap_analysis = self.researcher.analyze_content_gaps(topic, youtube_analysis)
        
        # Step 5: Scripts
        if include_variations:
            print("\n✍️ STEP 5/6: Writing Script Variations (3 tones)...")
            scripts = writer.write_multiple_variations(
                topic, youtube_analysis, research_results, 
                gap_analysis, video_length
            )
            main_script = scripts['entertaining']  # Use entertaining for SEO
        else:
            print("\n✍️ STEP 5/6: Writing Script (single tone)...")
            main_script = writer.write_script(
                topic, youtube_analysis, research_results, 
                gap_analysis, video_length, "educational"
            )
            scripts = None
        
        # Step 6: SEO Optimization
        print("\n🎯 STEP 6/6: Optimizing SEO Metadata...")
        seo_metadata = seo_optimizer.optimize_metadata(
            topic=topic,
            script=main_script,
            youtube_analysis=youtube_analysis,
            research_data=research_results
        )
        
        print("\n🎉 ULTIMATE PACKAGE COMPLETE!")
        
        # Package everything
        package = {
            'topic': topic,
            'score': score_data,
            'youtube_analysis': youtube_analysis,
            'research': research_results,
            'gaps': gap_analysis,
            'scripts': scripts if include_variations else {'main': main_script},
            'seo': seo_metadata,
            'metadata': {
                'video_length': video_length,
                'has_variations': include_variations,
                'recommendation': score_data['recommendation']
            }
        }
        
        return package
    

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
    
    def generate_content_package_with_variations(self, topic, video_length="10-12 minutes"):
        """
        Generate complete content package with script variations
        
        Args:
            topic: Video topic
            video_length: Target length
            
        Returns:
            Dictionary with analysis and 3 script variations
        """
        print("\n" + "=" * 80)
        print(f"🎬 GENERATING COMPLETE PACKAGE WITH VARIATIONS: {topic}")
        print("=" * 80)
        
        # Initialize script writer
        from script_writer import ScriptWriter
        writer = ScriptWriter()
        
        # Step 1: Score the topic
        print("\n📊 STEP 1/5: Scoring Topic Opportunity...")
        score_data = self.scorer.score_topic(topic)
        
        # Step 2: YouTube Analysis
        print("\n📺 STEP 2/5: Analyzing YouTube Competition...")
        youtube_analysis = self.youtube.analyze_top_videos(topic)
        
        # Step 3: Research
        print("\n🔬 STEP 3/5: Conducting Market Research...")
        research_results = self.researcher.research_topic(topic)
        
        # Step 4: Gap Analysis
        print("\n🎯 STEP 4/5: Identifying Content Gaps...")
        gap_analysis = self.researcher.analyze_content_gaps(topic, youtube_analysis)
        
        # Step 5: Generate Script Variations
        print("\n✍️ STEP 5/5: Writing Script Variations...")
        print("   Generating 3 different tones: Educational, Entertaining, Professional")
        
        script_variations = writer.write_multiple_variations(
            topic=topic,
            youtube_analysis=youtube_analysis,
            research_data=research_results,
            gap_analysis=gap_analysis,
            video_length=video_length
        )
        
        print("\n🎉 COMPLETE PACKAGE WITH VARIATIONS GENERATED!")
        
        # Combine everything
        package = {
            'topic': topic,
            'score': score_data,
            'youtube_analysis': youtube_analysis,
            'research': research_results,
            'gaps': gap_analysis,
            'script_variations': script_variations,
            'metadata': {
                'video_length': video_length,
                'variations': ['educational', 'entertaining', 'professional'],
                'recommendation': score_data['recommendation']
            }
        }
        
        return package
    
    def export_content_package(self, package, output_dir="output"):
        """
        Export complete content package to files
        
        Args:
            package: Content package dictionary
            output_dir: Directory to save files
            
        Returns:
            Dictionary with file paths
        """
        import os
        import json
        from datetime import datetime
        
        # Create output directory
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        safe_topic = package['topic'].replace(" ", "_").replace("/", "-")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        files = {}
        
        # 1. Save full report (markdown)
        report_file = os.path.join(output_dir, f"{safe_topic}_report_{timestamp}.md")
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(f"# Content Analysis Report: {package['topic']}\n\n")
            f.write(f"**Generated:** {timestamp}\n\n")
            f.write(f"## Score: {package['score']['total_score']}/100\n\n")
            f.write(f"**Recommendation:** {package['score']['recommendation']}\n\n")
            f.write(f"---\n\n")
            f.write(f"## YouTube Analysis\n\n{package['youtube_analysis']}\n\n")
            f.write(f"---\n\n")
            f.write(f"## Market Research\n\n{package['research']}\n\n")
            f.write(f"---\n\n")
            f.write(f"## Content Gaps\n\n{package['gaps']}\n\n")
        files['report'] = report_file
        
        # 2. Save script separately
        script_file = os.path.join(output_dir, f"{safe_topic}_script_{timestamp}.txt")
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(package['script'])
        files['script'] = script_file
        
        # 3. Save metadata as JSON
        metadata_file = os.path.join(output_dir, f"{safe_topic}_metadata_{timestamp}.json")
        metadata = {
            'topic': package['topic'],
            'score': package['score']['total_score'],
            'recommendation': package['score']['recommendation'],
            'video_length': package['metadata']['video_length'],
            'tone': package['metadata']['tone'],
            'generated': timestamp
        }
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        files['metadata'] = metadata_file
        
        print(f"\n📁 Content package exported to '{output_dir}/':")
        print(f"   - Report: {os.path.basename(report_file)}")
        print(f"   - Script: {os.path.basename(script_file)}")
        print(f"   - Metadata: {os.path.basename(metadata_file)}")
        
        return files

    def export_package_with_variations(self, package, output_dir="output"):
        """
        Export package with all script variations
        
        Args:
            package: Content package with variations
            output_dir: Directory to save files
            
        Returns:
            Dictionary with file paths
        """
        import os
        import json
        from datetime import datetime
        
        # Create output directory
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        safe_topic = package['topic'].replace(" ", "_").replace("/", "-")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        files = {}
        
        # 1. Save analysis report
        report_file = os.path.join(output_dir, f"{safe_topic}_analysis_{timestamp}.md")
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(f"# Content Analysis: {package['topic']}\n\n")
            f.write(f"**Score:** {package['score']['total_score']}/100\n\n")
            f.write(f"**Recommendation:** {package['score']['recommendation']}\n\n")
            f.write(f"---\n\n## YouTube Analysis\n\n{package['youtube_analysis']}\n\n")
            f.write(f"---\n\n## Research\n\n{package['research']}\n\n")
            f.write(f"---\n\n## Content Gaps\n\n{package['gaps']}\n\n")
        files['analysis'] = report_file
        
        # 2. Save comparison
        comparison_file = os.path.join(output_dir, f"{safe_topic}_comparison_{timestamp}.txt")
        with open(comparison_file, 'w', encoding='utf-8') as f:
            f.write(package['script_variations']['comparison'])
        files['comparison'] = comparison_file
        
        # 3. Save each script variation
        for tone in ['educational', 'entertaining', 'professional']:
            script_file = os.path.join(output_dir, f"{safe_topic}_script_{tone}_{timestamp}.txt")
            with open(script_file, 'w', encoding='utf-8') as f:
                f.write(package['script_variations'][tone])
            files[f'script_{tone}'] = script_file
        
        # 4. Save metadata
        metadata_file = os.path.join(output_dir, f"{safe_topic}_metadata_{timestamp}.json")
        metadata = {
            'topic': package['topic'],
            'score': package['score']['total_score'],
            'recommendation': package['score']['recommendation'],
            'video_length': package['metadata']['video_length'],
            'variations_generated': package['metadata']['variations'],
            'generated': timestamp
        }
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        files['metadata'] = metadata_file
        
        print(f"\n📁 Complete package exported to '{output_dir}/':")
        print(f"   - Analysis Report: {os.path.basename(report_file)}")
        print(f"   - Tone Comparison: {os.path.basename(comparison_file)}")
        print(f"   - Educational Script: {os.path.basename(files['script_educational'])}")
        print(f"   - Entertaining Script: {os.path.basename(files['script_entertaining'])}")
        print(f"   - Professional Script: {os.path.basename(files['script_professional'])}")
        print(f"   - Metadata: {os.path.basename(metadata_file)}")
        
        return files
    
    def export_ultimate_package(self, package, output_dir="output"):
        """
        Export the complete ultimate package
        
        Args:
            package: Ultimate content package
            output_dir: Output directory
            
        Returns:
            File paths dictionary
        """
        import os
        import json
        from datetime import datetime
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        safe_topic = package['topic'].replace(" ", "_").replace("/", "-")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        files = {}
        
        # 1. Complete analysis report
        report_file = os.path.join(output_dir, f"{safe_topic}_FULL_REPORT_{timestamp}.md")
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(f"# COMPLETE CONTENT PACKAGE: {package['topic']}\n\n")
            f.write(f"**Score:** {package['score']['total_score']}/100\n")
            f.write(f"**Recommendation:** {package['score']['recommendation']}\n\n")
            f.write(f"---\n\n## YouTube Analysis\n\n{package['youtube_analysis']}\n\n")
            f.write(f"---\n\n## Market Research\n\n{package['research']}\n\n")
            f.write(f"---\n\n## Content Gaps\n\n{package['gaps']}\n\n")
        files['report'] = report_file
        
        # 2. Scripts
        if package['metadata']['has_variations']:
            # Multiple scripts
            for tone in ['educational', 'entertaining', 'professional']:
                if tone in package['scripts']:
                    script_file = os.path.join(output_dir, f"{safe_topic}_script_{tone}_{timestamp}.txt")
                    with open(script_file, 'w', encoding='utf-8') as f:
                        f.write(package['scripts'][tone])
                    files[f'script_{tone}'] = script_file
            
            # Comparison
            if 'comparison' in package['scripts']:
                comp_file = os.path.join(output_dir, f"{safe_topic}_comparison_{timestamp}.txt")
                with open(comp_file, 'w', encoding='utf-8') as f:
                    f.write(package['scripts']['comparison'])
                files['comparison'] = comp_file
        else:
            # Single script
            script_file = os.path.join(output_dir, f"{safe_topic}_script_{timestamp}.txt")
            with open(script_file, 'w', encoding='utf-8') as f:
                f.write(package['scripts']['main'])
            files['script'] = script_file
        
        # 3. SEO Metadata
        seo_file = os.path.join(output_dir, f"{safe_topic}_SEO_{timestamp}.txt")
        with open(seo_file, 'w', encoding='utf-8') as f:
            f.write(package['seo'])
        files['seo'] = seo_file
        
        # 4. Metadata JSON
        meta_file = os.path.join(output_dir, f"{safe_topic}_metadata_{timestamp}.json")
        metadata = {
            'topic': package['topic'],
            'score': package['score']['total_score'],
            'recommendation': package['score']['recommendation'],
            'video_length': package['metadata']['video_length'],
            'has_variations': package['metadata']['has_variations'],
            'generated': timestamp
        }
        with open(meta_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        files['metadata'] = meta_file
        
        print(f"\n📁 Ultimate package exported to '{output_dir}/':")
        for key, filepath in files.items():
            print(f"   - {key}: {os.path.basename(filepath)}")
        
        return files

# Test function
# Test function
def test_enhanced_analyzer():
    """Test the enhanced content analyzer"""
    print("🧪 Testing Enhanced Content Analyzer with Script Generation...\n")
    
    analyzer = ContentAnalyzer()
    
    # Test: Full content package
    topic = "ChatGPT tips for beginners"
    
    print(f"📝 Generating complete content package for: {topic}")
    print("⏳ This will take 3-4 minutes (comprehensive process)...\n")
    
    package = analyzer.generate_full_content_package(
        topic=topic,
        video_length="10-12 minutes",
        tone="educational"
    )
    
    # Display results
    print("\n" + "="*80)
    print("📊 CONTENT PACKAGE SUMMARY")
    print("="*80)
    print(f"Topic: {package['topic']}")
    print(f"Score: {package['score']['total_score']}/100")
    print(f"Recommendation: {package['score']['recommendation']}")
    print(f"Video Length: {package['metadata']['video_length']}")
    print(f"Tone: {package['metadata']['tone']}")
    print("="*80)
    
    print("\n📄 GENERATED SCRIPT:")
    print(package['script'])

    # Export the package
    print("\n💾 Exporting content package...")
    files = analyzer.export_content_package(package)
    
    print("\n✅ Complete package generated successfully!")


# if __name__ == "__main__":
#     test_enhanced_analyzer()


def test_variations():
    """Quick test for variations feature"""
    print("🧪 Testing Variations Feature...\n")
    
    analyzer = ContentAnalyzer()
    
    topic = "Notion AI tutorial"
    
    print(f"📝 Topic: {topic}")
    print("⏳ Generating package with 3 script variations...")
    print("   This will take 4-5 minutes...\n")
    
    package = analyzer.generate_content_package_with_variations(topic)
    
    # Show summary
    print("\n" + "="*80)
    print("📊 PACKAGE SUMMARY")
    print("="*80)
    print(f"Topic: {package['topic']}")
    print(f"Score: {package['score']['total_score']}/100")
    print(f"Variations: {', '.join(package['metadata']['variations'])}")
    
    # Show comparison snippet
    print("\n📊 RECOMMENDATION (from GPT-4):")
    comparison = package['script_variations']['comparison']
    # Extract just the recommended tone section
    if "RECOMMENDED TONE" in comparison:
        start = comparison.find("RECOMMENDED TONE")
        end = comparison.find("### TONE COMPARISON")
        if end > start:
            print(comparison[start:end])
    
    # Export everything
    print("\n💾 Exporting all files...")
    files = analyzer.export_package_with_variations(package)
    
    print("\n✅ Test complete! Check the output folder.")

def test_ultimate_package():
    """Test the ultimate complete package with SEO"""
    print("🧪 Testing ULTIMATE Content Package (Analysis + Script + SEO)...\n")
    
    analyzer = ContentAnalyzer()
    
    topic = "Productivity Apps for Students"
    
    print(f"📝 Topic: {topic}")
    print("⏳ Generating complete package...")
    print("   This will take 3-4 minutes...\n")
    
    # Generate ultimate package (single script + SEO)
    package = analyzer.generate_complete_package(
        topic=topic,
        video_length="10-12 minutes",
        include_variations=False  # Set True for 3 scripts
    )
    
    # Display summary
    print("\n" + "="*80)
    print("📊 ULTIMATE PACKAGE SUMMARY")
    print("="*80)
    print(f"Topic: {package['topic']}")
    print(f"Score: {package['score']['total_score']}/100")
    print(f"Script Variations: {'Yes (3)' if package['metadata']['has_variations'] else 'No (1)'}")
    print(f"SEO Included: Yes")
    print("="*80)
    
    # Show SEO snippet
    print("\n🎯 SEO METADATA (preview):")
    seo_preview = package['seo'][:500]
    print(seo_preview + "...\n")
    
    # Export
    print("💾 Exporting complete package...")
    files = analyzer.export_ultimate_package(package)
    
    print("\n✅ Ultimate package complete! Check output folder.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "variations":
            test_variations()
        elif sys.argv[1] == "ultimate":
            test_ultimate_package()
        else:
            test_enhanced_analyzer()
    else:
        test_enhanced_analyzer()