import streamlit as st
import sys
import os
from datetime import datetime

# Add agents to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'agents'))

from orchestrator import YouTubeContentOrchestrator

# Page config
st.set_page_config(
    page_title="YouTube AI Agent System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #FF0000;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = None
if 'package' not in st.session_state:
    st.session_state.package = None
if 'generated' not in st.session_state:
    st.session_state.generated = False

# Header
st.markdown('<div class="main-header">🎬 YouTube AI Agent System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Multi-Agent AI for Automated Content Creation</div>', unsafe_allow_html=True)

# Sidebar
# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Quick example topics FIRST (better UX)
    with st.expander("💡 Example Topics", expanded=False):
        st.caption("Click any example to auto-fill:")
        
        col1, col2 = st.columns(2)
        
        examples = [
            "ChatGPT tips",
            "AI productivity tools",
            "Notion AI guide",
            "AI for students",
            "Prompt engineering",
            "AI automation"
        ]
        
        for i, ex in enumerate(examples):
            with col1 if i % 2 == 0 else col2:
                if st.button(ex, key=f"ex_{i}", use_container_width=True):
                    st.session_state.example_topic = ex
    
    # Topic input
    default_topic = st.session_state.get('example_topic', '')
    topic = st.text_input(
        "📝 Video Topic",
        value=default_topic,
        placeholder="e.g., 'ChatGPT tips for beginners'",
        help="Enter the topic you want to create content about"
    )
    
    # Clear the example after using it
    if 'example_topic' in st.session_state and topic:
        del st.session_state.example_topic
    
    # Video length
    video_length = st.selectbox(
        "⏱️ Video Length",
        ["5-8 minutes", "8-10 minutes", "10-12 minutes", 
         "12-15 minutes", "15-20 minutes", "20+ minutes"],
        index=2
    )
    
    # Tone
    tone = st.selectbox(
        "🎭 Script Tone",
        ["educational", "entertaining", "professional"],
        help="Choose the style of your script"
    )
    
    # Options
    st.subheader("🔧 Options")
    
    include_seo = st.checkbox("Include SEO Optimization", value=True)
    generate_variations = st.checkbox(
        "Generate 3 Script Variations", 
        value=False,
        help="⚠️ Takes 4-5 minutes and costs ~$2"
    )
    
    st.divider()
    
    # Generate button
    generate_btn = st.button(
        "🚀 Generate Content Package",
        type="primary",
        use_container_width=True,
        disabled=not topic  # Disable if no topic
    )
    
    st.divider()
    
    # Info box with dynamic estimates
    info_box = st.container()
    with info_box:
        st.caption("📊 **Estimates:**")
        
        # Time estimate
        if generate_variations:
            st.caption("⏱️ Time: 4-5 minutes")
            cost_est = "$1.80-2.20" if include_seo else "$1.50-1.80"
        else:
            st.caption("⏱️ Time: 3-4 minutes")
            cost_est = "$0.60-0.80" if include_seo else "$0.45-0.60"
        
        st.caption(f"💰 Cost: {cost_est}")
        
        # Show what's included
        st.caption("\n✅ **Includes:**")
        st.caption("• Topic scoring")
        st.caption("• YouTube analysis")
        st.caption("• Market research")
        st.caption("• Content gaps")
        if generate_variations:
            st.caption("• 3 script variations")
        else:
            st.caption(f"• 1 script ({tone})")
        if include_seo:
            st.caption("• SEO metadata")

# Main content area
if generate_btn and topic:
    # Validate topic length
    if len(topic.strip()) < 3:
        st.error("❌ Topic too short! Please enter at least 3 characters.")
        st.stop()
    
    if len(topic) > 200:
        st.error("❌ Topic too long! Please keep it under 200 characters.")
        st.stop()
    # Initialize orchestrator if needed
    if st.session_state.orchestrator is None:
        with st.spinner("🚀 Initializing AI agents..."):
            try:
                st.session_state.orchestrator = YouTubeContentOrchestrator(track_costs=True)
                st.success("✅ All agents initialized!")
            except Exception as e:
                st.error(f"❌ Failed to initialize agents: {str(e)}")
                st.error("Please check your .env file has all API keys!")
                st.stop()
    
# Progress container
    with st.spinner(f"🤖 AI agents working on '{topic}'..."):
        progress_placeholder = st.empty()
        
        try:
            # Generate package
            if generate_variations:
                with progress_placeholder.container():
                    st.info("📝 Generating 3 script variations (Educational, Entertaining, Professional)...")
                    st.caption("⏳ This takes 4-5 minutes - agents are analyzing, researching, and writing!")
                
                package = st.session_state.orchestrator.create_package_with_variations(
                    topic=topic,
                    video_length=video_length,
                    include_seo=include_seo
                )
            else:
                with progress_placeholder.container():
                    progress_bar = st.progress(0)
                    status = st.empty()
                    
                    status.text("📊 Scoring topic opportunity...")
                    progress_bar.progress(16)
                    
                    status.text("📺 Analyzing YouTube competition...")
                    progress_bar.progress(33)
                    
                    status.text("🔬 Researching market trends...")
                    progress_bar.progress(50)
                    
                    status.text("🎯 Identifying content gaps...")
                    progress_bar.progress(66)
                    
                    status.text("✍️ Writing video script...")
                    progress_bar.progress(83)
                    
                    if include_seo:
                        status.text("🎯 Optimizing SEO...")
                
                package = st.session_state.orchestrator.create_content_package(
                    topic=topic,
                    video_length=video_length,
                    tone=tone,
                    include_seo=include_seo
                )
                
                progress_bar.progress(100)
                status.text("✅ Complete!")
            
            progress_placeholder.empty()
            
            # Check for errors
            if 'error' in package:
                st.error(f"❌ Generation failed: {package['error']}")
                st.error("💡 Try a different topic or check your API credits")
                st.stop()
            
            st.session_state.package = package
            st.session_state.generated = True
            
        except Exception as e:
            st.error(f"❌ Unexpected error: {str(e)}")
            st.exception(e)  # Show full traceback for debugging
            st.stop()

elif generate_btn:
    st.warning("⚠️ Please enter a video topic!")

# Display results
if st.session_state.generated and st.session_state.package:
    package = st.session_state.package
    
    # Success message
    st.success("🎉 Content package generated successfully!")
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        score = package['score']['total_score']
        st.metric("Opportunity Score", f"{score}/100")
    
    with col2:
        rec = package['score']['recommendation']
        if "STRONG" in rec:
            st.metric("Recommendation", "🟢 Strong")
        elif "GOOD" in rec:
            st.metric("Recommendation", "🟡 Good")
        else:
            st.metric("Recommendation", "🟠 Moderate")
    
    with col3:
        avg_views = package['score']['metrics']['avg_views']
        st.metric("Avg Competitor Views", avg_views)
    
    with col4:
        engagement = package['score']['metrics']['avg_engagement']
        st.metric("Avg Engagement", engagement)
    
    st.divider()
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Analysis", "🔍 Research", "🎯 Gaps", "✍️ Script", "🎯 SEO"
    ])
    
    with tab1:
        st.subheader("📊 YouTube Competition Analysis")
        st.text(package['youtube_analysis'])
    
    with tab2:
        st.subheader("🔍 Market Research & Trends")
        st.markdown(package['research'])
    
    with tab3:
        st.subheader("🎯 Content Gap Analysis")
        st.markdown(package['gaps'])
    
    with tab4:
        st.subheader("✍️ Video Script(s)")
        
        # Check if variations were generated
        if 'scripts' in package and isinstance(package.get('scripts'), dict):
            # Multiple scripts
            if 'educational' in package['scripts']:
                # Show variations in sub-tabs
                script_tab1, script_tab2, script_tab3, script_tab4 = st.tabs([
                    "📚 Educational", "🎭 Entertaining", "💼 Professional", "📊 Comparison"
                ])
                
                with script_tab1:
                    st.text_area(
                        "Educational Tone",
                        package['scripts']['educational'],
                        height=400
                    )
                    st.download_button(
                        "📥 Download Educational",
                        package['scripts']['educational'],
                        file_name=f"{topic.replace(' ', '_')}_educational.txt"
                    )
                
                with script_tab2:
                    st.text_area(
                        "Entertaining Tone",
                        package['scripts']['entertaining'],
                        height=400
                    )
                    st.download_button(
                        "📥 Download Entertaining",
                        package['scripts']['entertaining'],
                        file_name=f"{topic.replace(' ', '_')}_entertaining.txt"
                    )
                
                with script_tab3:
                    st.text_area(
                        "Professional Tone",
                        package['scripts']['professional'],
                        height=400
                    )
                    st.download_button(
                        "📥 Download Professional",
                        package['scripts']['professional'],
                        file_name=f"{topic.replace(' ', '_')}_professional.txt"
                    )
                
                with script_tab4:
                    if 'comparison' in package['scripts']:
                        st.markdown(package['scripts']['comparison'])
                    else:
                        st.info("Comparison not available")
            else:
                # Single script in scripts dict
                script_content = package['scripts'].get('main', str(package['scripts']))
                st.text_area("Script", script_content, height=400)
                st.download_button(
                    "📥 Download Script",
                    script_content,
                    file_name=f"{topic.replace(' ', '_')}_script.txt"
                )
        elif 'script' in package:
            # Single script (old format)
            st.text_area(
                "Script",
                package['script'],
                height=400,
                help="Copy this script for your video"
            )
            st.download_button(
                "📥 Download Script",
                package['script'],
                file_name=f"{topic.replace(' ', '_')}_script.txt",
                mime="text/plain"
            )
        else:
            st.warning("No script generated")
    
    with tab5:
        if package.get('seo'):
            st.subheader("🎯 SEO Metadata")
            st.text_area(
                "SEO Optimization",
                package['seo'],
                height=400,
                help="Use this for YouTube title, description, and tags"
            )
            
            # Download button
            st.download_button(
                "📥 Download SEO Metadata",
                package['seo'],
                file_name=f"{topic.replace(' ', '_')}_SEO.txt",
                mime="text/plain"
            )
        else:
            st.info("SEO optimization was not included in this package.")
    
    # Cost info
    if st.session_state.orchestrator and st.session_state.orchestrator.cost_tracker:
        st.divider()
        cost = st.session_state.orchestrator.cost_tracker.get_session_cost()
        st.caption(f"💰 Package cost: ${cost:.2f}")

else:
    # Welcome message when no content generated yet
    st.info("""
    👋 **Welcome to the YouTube AI Agent System!**
    
    Multi-agent AI system that automates YouTube content creation from idea to 
    production-ready script with SEO optimization.
    """)
    
    # Example topics
    st.subheader("💡 Example Topics to Try:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📊 Intelligence
        - Topic opportunity scoring
        - YouTube competition analysis
        - Market trend research
        - Content gap detection
        """)
    
    with col2:
        st.markdown("""
        ### ✍️ Content Creation
        - Production-ready scripts
        - 3 tone variations
        - Timestamps & B-roll
        - Engaging structure
        """)
    
    with col3:
        st.markdown("""
        ### 🎯 SEO Optimization
        - 3 title variations
        - Optimized descriptions
        - 15-20 tags
        - Thumbnail text ideas
        """)

        st.divider()

        # Quick stats
        st.subheader("⚡ Performance")
    
        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

        with metric_col1:
            st.metric("Generation Time", "3-4 min")
        with metric_col2:
            st.metric("Success Rate", "90%")
        with metric_col3:
            st.metric("Cost per Package", "$0.50")
        with metric_col4:
            st.metric("vs Industry Rate", "$1,500")
        st.divider()

        # How it works
        st.subheader("🔄 How It Works")
    
        st.markdown("""
        1. **Enter your topic** in the sidebar
        2. **Choose preferences** (length, tone, options)
        3. **Click generate** and wait 3-4 minutes
        4. **Get complete package** with analysis, script, and SEO
        5. **Download files** and start creating!
        """)
    
        st.success("💡 **Try the example topics in the sidebar to get started!**")

# Footer
st.divider()
st.caption("Built with ❤️ by Yash Jalan | Powered by GPT-4, LangChain, YouTube API")