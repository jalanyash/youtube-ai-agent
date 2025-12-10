import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'agents'))

from orchestrator import YouTubeContentOrchestrator
from datetime import datetime

class SystemTester:
    """Comprehensive test suite for YouTube AI Agent System"""
    
    def __init__(self):
        self.orchestrator = YouTubeContentOrchestrator(track_costs=True)
        self.test_results = []
    
    def test_topic(self, topic, expected_min_score=0):
        """
        Test a single topic
        
        Args:
            topic: Topic to test
            expected_min_score: Minimum expected score
            
        Returns:
            Test result dictionary
        """
        print(f"\n{'='*80}")
        print(f"🧪 Testing: {topic}")
        print('='*80)
        
        start_time = datetime.now()
        
        try:
            # Generate package (without SEO to save cost during testing)
            package = self.orchestrator.create_content_package(
                topic=topic,
                video_length="10-12 minutes",
                tone="educational",
                include_seo=False  # Skip SEO in tests to save money
            )
            
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            # Check for errors
            if 'error' in package:
                result = {
                    'topic': topic,
                    'status': 'FAILED',
                    'error': package['error'],
                    'duration': duration
                }
                print(f"❌ FAILED: {package['error']}")
            else:
                # Validate output
                score = package['score']['total_score']
                has_script = 'script' in package and len(package['script']) > 100
                has_research = 'research' in package and len(package['research']) > 100
                
                passed = (
                    score >= expected_min_score and
                    has_script and
                    has_research
                )
                
                result = {
                    'topic': topic,
                    'status': 'PASSED' if passed else 'WARNING',
                    'score': score,
                    'duration': duration,
                    'has_script': has_script,
                    'has_research': has_research
                }
                
                if passed:
                    print(f"✅ PASSED - Score: {score}/100, Duration: {duration:.1f}s")
                else:
                    print(f"⚠️ WARNING - Score: {score}/100 (expected >{expected_min_score})")
            
            self.test_results.append(result)
            return result
            
        except Exception as e:
            result = {
                'topic': topic,
                'status': 'ERROR',
                'error': str(e),
                'duration': 0
            }
            print(f"❌ ERROR: {str(e)}")
            self.test_results.append(result)
            return result
    
    def run_test_suite(self):
        """Run comprehensive test suite"""
        print("\n" + "="*80)
        print("🧪 RUNNING COMPREHENSIVE TEST SUITE")
        print("="*80)
        print("Testing various topics to ensure system reliability")
        print("Note: SEO skipped in tests to minimize costs")
        print("="*80 + "\n")
        
        # Test cases: diverse topics
        test_cases = [
            # Popular topics (should score high)
            ("ChatGPT tutorial for beginners", 50),
            ("AI productivity tools 2024", 40),
            
            # Niche topics (might score lower)
            ("Advanced prompt engineering techniques", 30),
            ("AI ethics in healthcare", 20),
            
            # Trending topics
            ("Best AI apps for students", 50),
            ("Notion AI complete guide", 40),
            
            # Edge cases
            ("AI", 0),  # Very short/broad
            ("How to use artificial intelligence machine learning deep learning", 0),  # Long
            
            # Different formats
            ("Top 10 AI tools", 30),
            ("AI vs Human: Who wins?", 20),
        ]
        
        print(f"📝 Testing {len(test_cases)} topics...\n")
        print("⏳ This will take 15-20 minutes (testing without SEO)\n")
        
        for i, (topic, min_score) in enumerate(test_cases, 1):
            print(f"\n--- Test {i}/{len(test_cases)} ---")
            self.test_topic(topic, min_score)
        
        # Generate summary
        self.print_summary()
    
    def print_summary(self):
        """Print test results summary"""
        print("\n" + "="*80)
        print("📊 TEST SUITE SUMMARY")
        print("="*80)
        
        passed = sum(1 for r in self.test_results if r['status'] == 'PASSED')
        failed = sum(1 for r in self.test_results if r['status'] == 'FAILED')
        errors = sum(1 for r in self.test_results if r['status'] == 'ERROR')
        warnings = sum(1 for r in self.test_results if r['status'] == 'WARNING')
        
        total = len(self.test_results)
        
        print(f"\nTotal Tests: {total}")
        print(f"✅ Passed: {passed}")
        print(f"⚠️ Warnings: {warnings}")
        print(f"❌ Failed: {failed}")
        print(f"🔥 Errors: {errors}")
        
        success_rate = (passed / total * 100) if total > 0 else 0
        print(f"\n📈 Success Rate: {success_rate:.1f}%")
        
        # Show avg duration
        durations = [r['duration'] for r in self.test_results if 'duration' in r]
        if durations:
            avg_duration = sum(durations) / len(durations)
            print(f"⏱️ Average Duration: {avg_duration:.1f}s")
        
        # Show cost
        if self.orchestrator.cost_tracker:
            total_cost = self.orchestrator.cost_tracker.get_session_cost()
            print(f"💰 Total Test Cost: ${total_cost:.2f}")
        
        # List any failures
        if failed > 0 or errors > 0:
            print(f"\n{'='*80}")
            print("🔍 FAILED/ERROR TESTS:")
            print('='*80)
            for r in self.test_results:
                if r['status'] in ['FAILED', 'ERROR']:
                    print(f"\n❌ {r['topic']}")
                    print(f"   Error: {r.get('error', 'Unknown')}")
        
        print("\n" + "="*80)
        
        if success_rate >= 80:
            print("🎉 EXCELLENT! System is robust!")
        elif success_rate >= 60:
            print("✅ GOOD! Minor issues to address")
        else:
            print("⚠️ NEEDS WORK! Several issues found")
        
        print("="*80 + "\n")


def main():
    """Run the test suite"""
    print("\n" + "="*80)
    print("🎬 YOUTUBE AI AGENT SYSTEM - TEST SUITE")
    print("="*80)
    print("Comprehensive testing to ensure system reliability")
    print("="*80 + "\n")
    
    tester = SystemTester()
    tester.run_test_suite()
    
    print("\n✅ Testing complete! Review results above.")


if __name__ == "__main__":
    main()