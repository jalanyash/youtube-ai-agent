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
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Topic input
    topic = st.text_input(
        "📝 Video Topic",
        placeholder="e.g., 'ChatGPT tips for beginners'",
        help="Enter the topic you want to create content about"
    )
    
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
        help="Takes longer but gives you 3 tone options"
    )
    
    st.divider()
    
    # Generate button
    generate_btn = st.button(
        "🚀 Generate Content Package",
        type="primary",
        use_container_width=True
    )
    
    st.divider()
    
    # Info
    st.caption("💡 **Estimated Time:**")
    if generate_variations:
        st.caption("4-5 minutes (3 scripts)")
    else:
        st.caption("3-4 minutes (1 script)")
    
    st.caption("💰 **Estimated Cost:**")
    if generate_variations and include_seo:
        st.caption("~$2.00")
    elif generate_variations:
        st.caption("~$1.50")
    elif include_seo:
        st.caption("~$0.70")
    else:
        st.caption("~$0.50")

# Main content area
if generate_btn and topic:
    # Initialize orchestrator if needed
    if st.session_state.orchestrator is None:
        with st.spinner("🚀 Initializing AI agents..."):
            st.session_state.orchestrator = YouTubeContentOrchestrator(track_costs=True)
        st.success("✅ All agents initialized!")
    
    # Progress container
    progress_container = st.container()
    
    with progress_container:
        st.subheader(f"🎬 Generating: {topic}")
        
        # Progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Generate package
            if generate_variations:
                status_text.text("📝 Generating 3 script variations...")
                progress_bar.progress(10)
                # This is complex - we'll simplify for now
                package = st.session_state.orchestrator.create_package_with_variations(
                    topic=topic,
                    video_length=video_length,
                    include_seo=include_seo
                )
            else:
                # Step-by-step with progress updates
                status_text.text("📊 Step 1/6: Scoring topic...")
                progress_bar.progress(16)
                
                package = st.session_state.orchestrator.create_content_package(
                    topic=topic,
                    video_length=video_length,
                    tone=tone,
                    include_seo=include_seo
                )
                
                progress_bar.progress(100)
                status_text.text("✅ Complete!")
            
            st.session_state.package = package
            st.session_state.generated = True
            
            # Clear progress
            progress_bar.empty()
            status_text.empty()
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
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
    
    This multi-agent system helps YouTube creators by:
    - 📊 Scoring content opportunities (0-100 scale)
    - 📺 Analyzing YouTube competition
    - 🔬 Researching market trends
    - 🎯 Identifying content gaps
    - ✍️ Generating production-ready scripts
    - 🎯 Optimizing SEO (titles, descriptions, tags)
    
    **Get started:**
    1. Enter your video topic in the sidebar
    2. Choose your preferences
    3. Click "Generate Content Package"
    4. Get complete package in 3-4 minutes!
    """)
    
    # Example topics
    st.subheader("💡 Example Topics to Try:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Popular:**
        - ChatGPT tips for beginners
        - AI productivity tools
        - Notion AI tutorial
        """)
    
    with col2:
        st.markdown("""
        **Trending:**
        - AI agents explained
        - Best AI apps 2024
        - Prompt engineering guide
        """)
    
    with col3:
        st.markdown("""
        **Niche:**
        - AI for content creators
        - Automation with AI
        - AI tools comparison
        """)

# Footer
st.divider()
st.caption("Built with ❤️ by Yash Jalan | Powered by GPT-4, LangChain, YouTube API")