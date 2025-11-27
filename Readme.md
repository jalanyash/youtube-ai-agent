# 🎬 YouTube AI Agent System

Multi-agent AI system that autonomously researches topics, analyzes competitor videos, generates production-ready scripts, and optimizes for SEO.

## 🚀 Live Demo
```bash
python orchestrator.py "Your Video Topic Here"
```

**Result:** Complete content package in 3-4 minutes!

---

## 🤖 Agent Architecture
```
YouTube Content AI System
├── YouTube Analyzer Agent
│   └── Analyzes top videos, engagement metrics
├── Research Agent (GPT-4)
│   └── Web search, trend analysis, gap detection
├── Topic Scorer
│   └── 4D scoring: demand, competition, engagement, trends
├── Script Writer Agent (GPT-4)
│   └── Generates scripts in 3 tones
├── SEO Agent (GPT-4)
│   └── Titles, descriptions, tags, thumbnails
└── Orchestrator
    └── Coordinates all agents seamlessly
```

---

## ✨ Features

- **Multi-Agent Coordination** - 5 specialized AI agents working together
- **Intelligent Scoring** - 4-dimensional opportunity analysis (0-100 scale)
- **Content Gap Detection** - GPT-4 identifies underserved topics
- **Script Variations** - Generate 3 tones: educational, entertaining, professional
- **SEO Optimization** - 3 title options, optimized descriptions, 15-20 tags
- **Automated Export** - Production-ready files in multiple formats
- **CLI Interface** - Professional command-line tool

---

## 🎯 What It Generates

**Input:** Any video topic

**Output (in 3-4 minutes):**
1. **Opportunity Score** (0-100) with recommendation
2. **YouTube Competition Analysis** - Top 5 videos, engagement data
3. **Market Research** - Current trends, popular subtopics, common questions
4. **Content Gap Analysis** - Specific opportunities identified
5. **Complete Video Script** - Ready to film (10-12 min)
6. **SEO Metadata** - 3 titles, description, tags, thumbnail text

---

## 💻 Tech Stack

- **Python 3.12**
- **LangChain** - Agent orchestration
- **OpenAI GPT-4-turbo** - Intelligence layer
- **YouTube Data API v3** - Video analytics
- **Tavily Search API** - Web research
- **Streamlit** (Coming soon - UI)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key
- YouTube Data API key
- Tavily API key

### Installation
```bash
# Clone repository
git clone https://github.com/jalanyash/youtube-ai-agent.git
cd youtube-ai-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env and add your API keys
```

### Usage

**Basic usage:**
```bash
python orchestrator.py "Your Video Topic"
```

**With options:**
```bash
# Choose tone
python orchestrator.py "AI Productivity" --tone entertaining

# Generate 3 script variations
python orchestrator.py "ChatGPT Tips" --variations

# Custom video length
python orchestrator.py "AI Tutorial" --length "15-20 minutes"

# Skip SEO
python orchestrator.py "Quick Topic" --no-seo

# Custom output folder
python orchestrator.py "My Topic" --output custom_folder
```

---

## 📊 Example Output
```
Score: 76/100 - 🟢 STRONG OPPORTUNITY
Files Generated:
  ✅ Complete analysis report
  ✅ Production-ready script
  ✅ SEO metadata (3 titles, description, tags)
  ✅ Structured metadata (JSON)
```

---

## 🎯 Use Cases

- **Content Creators** - Generate video ideas and scripts in minutes
- **Marketing Teams** - Research trending topics and competition
- **Agencies** - Scale content production for clients
- **Students** - Learn content strategy and SEO
- **Researchers** - Analyze YouTube trends and opportunities

---

## 📈 Project Status

**Version:** 1.0  
**Status:** Core pipeline complete! ✅  
**Progress:** Day 6/14 (43% complete)

**Completed:**
- ✅ All 5 AI agents operational
- ✅ Multi-agent orchestration
- ✅ CLI interface
- ✅ Export system

**Coming Soon:**
- 🚧 Streamlit web UI
- 🚧 Batch processing
- 🚧 Cloud deployment
- 🚧 API endpoints

---

## 💰 Cost Per Content Package

**API Costs:**
- YouTube Data API: **FREE** (10k quota/day)
- Tavily Search: **FREE** (1k/month free tier)
- OpenAI GPT-4: **~$0.50-0.75** per package

**Industry Comparison:**
- Your system: $0.75/package
- Content agency: $1,000-1,500/package
- **Savings: 2,000x cheaper!**

---

## 🏗️ Architecture Decisions

**Why not use LangChain Agents framework?**
- Better control over workflow
- Easier debugging
- Predictable costs
- Production-ready reliability

**Tech choices:**
- Direct API integration over heavy abstractions
- Modular agent design for maintainability
- Clear separation of concerns
- Optimized for Python 3.12

---

## 📝 Sample Output

See `output/` folder for examples of:
- Complete analysis reports
- Production-ready scripts (3 tones)
- SEO metadata packages
- Tone comparison analysis

---

## 🤝 Contributing

This is a portfolio project. Suggestions welcome!

---

## 📄 License

MIT License - See LICENSE file

---

## 👨‍💻 Author

**Yash Jalan**  
Master's Student | AI Engineer  
Building AI agent systems for real-world impact

- GitHub: [@jalanyash](https://github.com/jalanyash)
- Project: [youtube-ai-agent](https://github.com/jalanyash/youtube-ai-agent)

---

## 🙏 Acknowledgments

Built with:
- OpenAI GPT-4
- LangChain
- YouTube Data API v3
- Tavily Search API

---

**Built in 6 days | 26 hours | $7.50 in API costs**

Demonstrating: Multi-agent systems, LLM integration, production deployment