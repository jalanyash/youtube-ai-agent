import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Add agents to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'agents'))

from agents.youtube_analyzer import YouTubeAnalyzer
from agents.research_agent import ResearchAgent
from agents.topic_scorer import TopicScorer
from agents.script_writer import ScriptWriter
from agents.seo_agent import SEOAgent

load_dotenv()

class YouTubeContentOrchestrator:
    """
    Main orchestrator that coordinates all AI agents for YouTube content creation
    
    This is the central brain that manages:
    - YouTube Analyzer (video data)
    - Research Agent (web trends)
    - Topic Scorer (opportunity scoring)
    - Script Writer (content generation)
    - SEO Agent (optimization)
    """
    
    def __init__(self):
        """Initialize all agents"""
        print("🚀 Initializing YouTube Content AI Agent System...")
        print("="*80)
        
        try:
            self.youtube_analyzer = YouTubeAnalyzer()
            print("✅ YouTube Analyzer initialized")
            
            self.researcher = ResearchAgent()
            print("✅ Research Agent initialized")
            
            self.scorer = TopicScorer()
            print("✅ Topic Scorer initialized")
            
            self.script_writer = ScriptWriter()
            print("✅ Script Writer initialized")
            
            self.seo_agent = SEOAgent()
            print("✅ SEO Agent initialized")
            
            print("="*80)
            print("🎉 All agents ready!\n")
            
        except Exception as e:
            print(f"\n❌ Initialization error: {str(e)}")
            raise
    
    def create_content_package(self, topic, video_length="10-12 minutes", 
                               tone="educational", include_seo=True):
        """
        Create complete content package with single script
        
        Args:
            topic: Video topic
            video_length: Target video length
            tone: Script tone (educational, entertaining, professional)
            include_seo: Whether to generate SEO metadata
            
        Returns:
            Complete content package dictionary
        """
        print("\n" + "="*80)
        print(f"🎬 CREATING CONTENT PACKAGE: {topic}")
        print("="*80)
        print(f"Length: {video_length} | Tone: {tone} | SEO: {include_seo}")
        print("="*80 + "\n")
        
        package = {
            'topic': topic,
            'timestamp': datetime.now().isoformat(),
            'settings': {
                'video_length': video_length,
                'tone': tone,
                'include_seo': include_seo
            }
        }
        
        try:
            # Step 1: Score Topic
            print("📊 [1/6] Scoring Topic Opportunity...")
            score_data = self.scorer.score_topic(topic)
            package['score'] = score_data
            print(f"    ✅ Score: {score_data['total_score']}/100 - {score_data['recommendation']}")
            
            # Step 2: YouTube Analysis
            print("\n📺 [2/6] Analyzing YouTube Competition...")
            youtube_analysis = self.youtube_analyzer.analyze_top_videos(topic)
            package['youtube_analysis'] = youtube_analysis
            print("    ✅ Analyzed top 5 videos")
            
            # Step 3: Market Research
            print("\n🔬 [3/6] Conducting Market Research...")
            research_data = self.researcher.research_topic(topic)
            package['research'] = research_data
            print("    ✅ Research complete")
            
            # Step 4: Content Gaps
            print("\n🎯 [4/6] Identifying Content Gaps...")
            gap_analysis = self.researcher.analyze_content_gaps(topic, youtube_analysis)
            package['gaps'] = gap_analysis
            print("    ✅ Gaps identified")
            
            # Step 5: Script Generation
            print("\n✍️ [5/6] Writing Video Script...")
            script = self.script_writer.write_script(
                topic, youtube_analysis, research_data, 
                gap_analysis, video_length, tone
            )
            package['script'] = script
            print("    ✅ Script generated")
            
            # Step 6: SEO Optimization (optional)
            if include_seo:
                print("\n🎯 [6/6] Optimizing SEO Metadata...")
                seo_metadata = self.seo_agent.optimize_metadata(
                    topic, script, youtube_analysis, research_data
                )
                package['seo'] = seo_metadata
                print("    ✅ SEO optimized")
            else:
                print("\n⏭️ [6/6] Skipping SEO (not requested)")
                package['seo'] = None
            
            print("\n" + "="*80)
            print("🎉 CONTENT PACKAGE COMPLETE!")
            print("="*80)
            
            return package
            
        except Exception as e:
            print(f"\n❌ Error during content generation: {str(e)}")
            package['error'] = str(e)
            return package
    
    def create_package_with_variations(self, topic, video_length="10-12 minutes", 
                                        include_seo=True):
        """
        Create content package with 3 script variations
        
        Args:
            topic: Video topic
            video_length: Target length
            include_seo: Whether to include SEO
            
        Returns:
            Package with 3 scripts + comparison
        """
        print("\n" + "="*80)
        print(f"🎬 CREATING PACKAGE WITH VARIATIONS: {topic}")
        print("="*80)
        print(f"Length: {video_length} | Variations: 3 tones | SEO: {include_seo}")
        print("="*80 + "\n")
        
        package = {
            'topic': topic,
            'timestamp': datetime.now().isoformat(),
            'settings': {
                'video_length': video_length,
                'variations': True,
                'include_seo': include_seo
            }
        }
        
        try:
            # Steps 1-4: Same as single package
            print("📊 [1/6] Scoring Topic...")
            score_data = self.scorer.score_topic(topic)
            package['score'] = score_data
            print(f"    ✅ Score: {score_data['total_score']}/100")
            
            print("\n📺 [2/6] Analyzing YouTube...")
            youtube_analysis = self.youtube_analyzer.analyze_top_videos(topic)
            package['youtube_analysis'] = youtube_analysis
            print("    ✅ Complete")
            
            print("\n🔬 [3/6] Researching Market...")
            research_data = self.researcher.research_topic(topic)
            package['research'] = research_data
            print("    ✅ Complete")
            
            print("\n🎯 [4/6] Finding Gaps...")
            gap_analysis = self.researcher.analyze_content_gaps(topic, youtube_analysis)
            package['gaps'] = gap_analysis
            print("    ✅ Complete")
            
            # Step 5: Generate 3 script variations
            print("\n✍️ [5/6] Writing 3 Script Variations...")
            print("    This will take 3-4 minutes...")
            script_variations = self.script_writer.write_multiple_variations(
                topic, youtube_analysis, research_data, 
                gap_analysis, video_length
            )
            package['scripts'] = script_variations
            print("    ✅ All variations complete")
            
            # Step 6: SEO (based on entertaining script)
            if include_seo:
                print("\n🎯 [6/6] Optimizing SEO...")
                main_script = script_variations.get('entertaining', 
                             script_variations.get('educational', ''))
                seo_metadata = self.seo_agent.optimize_metadata(
                    topic, main_script, youtube_analysis, research_data
                )
                package['seo'] = seo_metadata
                print("    ✅ SEO complete")
            else:
                package['seo'] = None
            
            print("\n" + "="*80)
            print("🎉 COMPLETE PACKAGE WITH VARIATIONS READY!")
            print("="*80)
            
            return package
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            package['error'] = str(e)
            return package
    
    def export_package(self, package, output_dir="output"):
        """
        Export content package to files
        
        Args:
            package: Content package dictionary
            output_dir: Output directory
            
        Returns:
            Dictionary with file paths
        """
        import json
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        safe_topic = package['topic'].replace(" ", "_").replace("/", "-")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        files = {}
        
        # 1. Save summary report
        report_file = os.path.join(output_dir, f"{safe_topic}_REPORT_{timestamp}.md")
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(f"# Content Package: {package['topic']}\n\n")
            f.write(f"**Generated:** {package['timestamp']}\n")
            f.write(f"**Score:** {package['score']['total_score']}/100\n")
            f.write(f"**Recommendation:** {package['score']['recommendation']}\n\n")
            f.write("---\n\n")
            
            if 'youtube_analysis' in package:
                f.write(f"## YouTube Analysis\n\n{package['youtube_analysis']}\n\n")
            if 'research' in package:
                f.write(f"## Research\n\n{package['research']}\n\n")
            if 'gaps' in package:
                f.write(f"## Content Gaps\n\n{package['gaps']}\n\n")
        
        files['report'] = report_file
        print(f"   ✅ Report: {os.path.basename(report_file)}")
        
        # 2. Save scripts
        if 'scripts' in package and isinstance(package['scripts'], dict):
            # Multiple variations
            if 'educational' in package['scripts']:
                for tone in ['educational', 'entertaining', 'professional']:
                    if tone in package['scripts']:
                        script_file = os.path.join(output_dir, f"{safe_topic}_script_{tone}_{timestamp}.txt")
                        with open(script_file, 'w', encoding='utf-8') as f:
                            f.write(package['scripts'][tone])
                        files[f'script_{tone}'] = script_file
                        print(f"   ✅ {tone.capitalize()} script saved")
                
                # Save comparison
                if 'comparison' in package['scripts']:
                    comp_file = os.path.join(output_dir, f"{safe_topic}_comparison_{timestamp}.txt")
                    with open(comp_file, 'w', encoding='utf-8') as f:
                        f.write(package['scripts']['comparison'])
                    files['comparison'] = comp_file
                    print(f"   ✅ Comparison saved")
        elif 'script' in package:
            # Single script
            script_file = os.path.join(output_dir, f"{safe_topic}_script_{timestamp}.txt")
            with open(script_file, 'w', encoding='utf-8') as f:
                f.write(package['script'])
            files['script'] = script_file
            print(f"   ✅ Script saved")
        
        # 3. Save SEO metadata
        if package.get('seo'):
            seo_file = os.path.join(output_dir, f"{safe_topic}_SEO_{timestamp}.txt")
            with open(seo_file, 'w', encoding='utf-8') as f:
                f.write(package['seo'])
            files['seo'] = seo_file
            print(f"   ✅ SEO metadata saved")
        
        # 4. Save metadata JSON
        meta_file = os.path.join(output_dir, f"{safe_topic}_metadata_{timestamp}.json")
        metadata = {
            'topic': package['topic'],
            'score': package['score']['total_score'],
            'recommendation': package['score']['recommendation'],
            'settings': package['settings'],
            'timestamp': package['timestamp'],
            'files_generated': list(files.keys())
        }
        with open(meta_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        files['metadata'] = meta_file
        print(f"   ✅ Metadata saved")
        
        print(f"\n📁 Exported {len(files)} files to '{output_dir}/'")
        
        return files
    
    def get_system_status(self):
        """Get status of all agents"""
        status = {
            'system': 'YouTube Content AI Agent System',
            'version': '1.0',
            'agents': {
                'youtube_analyzer': 'Ready' if self.youtube_analyzer else 'Error',
                'researcher': 'Ready' if self.researcher else 'Error',
                'scorer': 'Ready' if self.scorer else 'Error',
                'script_writer': 'Ready' if self.script_writer else 'Error',
                'seo_agent': 'Ready' if self.seo_agent else 'Error'
            },
            'capabilities': [
                'Topic opportunity scoring',
                'YouTube competition analysis',
                'Market research & trends',
                'Content gap detection',
                'Script generation (3 tones)',
                'SEO optimization',
                'Automated export'
            ]
        }
        return status


def main():
    """Main CLI interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='YouTube Content AI Agent System - Automated content creation'
    )
    parser.add_argument('topic', type=str, help='Video topic')
    parser.add_argument('--length', type=str, default='10-12 minutes',
                       help='Video length (default: 10-12 minutes)')
    parser.add_argument('--tone', type=str, default='educational',
                       choices=['educational', 'entertaining', 'professional'],
                       help='Script tone')
    parser.add_argument('--variations', action='store_true',
                       help='Generate 3 script variations')
    parser.add_argument('--no-seo', action='store_true',
                       help='Skip SEO generation')
    parser.add_argument('--output', type=str, default='output',
                       help='Output directory')
    
    args = parser.parse_args()
    
    print("\n" + "="*80)
    print("🎬 YOUTUBE CONTENT AI AGENT SYSTEM")
    print("="*80)
    print(f"Topic: {args.topic}")
    print(f"Length: {args.length}")
    print(f"Tone: {args.tone}")
    print(f"Variations: {'Yes (3 scripts)' if args.variations else 'No (1 script)'}")
    print(f"SEO: {'No' if args.no_seo else 'Yes'}")
    print("="*80 + "\n")
    
    # Initialize
    orchestrator = YouTubeContentOrchestrator()
    
    # Generate package
    if args.variations:
        package = orchestrator.create_package_with_variations(
            topic=args.topic,
            video_length=args.length,
            include_seo=not args.no_seo
        )
    else:
        package = orchestrator.create_content_package(
            topic=args.topic,
            video_length=args.length,
            tone=args.tone,
            include_seo=not args.no_seo
        )
    
    # Export
    if 'error' not in package:
        print("\n💾 Exporting package...")
        files = orchestrator.export_package(package, args.output)
        
        print("\n" + "="*80)
        print("✅ SUCCESS!")
        print("="*80)
        print(f"Topic: {package['topic']}")
        print(f"Score: {package['score']['total_score']}/100")
        print(f"Files: {len(files)} files in '{args.output}/'")
        print("\n🎉 Your content package is ready!")
    else:
        print(f"\n❌ Error: {package['error']}")


if __name__ == "__main__":
    main()