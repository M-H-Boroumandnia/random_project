# random_project
user-research-agent-cli/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── setup.py                     # For CLI installation
├── config/
│   ├── __init__.py
│   ├── settings.py              # App configuration & API keys
│   └── prompts.py               # All LLM prompts and templates
├── src/
│   ├── __init__.py
│   ├── cli.py                   # Main CLI interface (Click/Typer)
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── core.py              # Main research agent logic
│   │   ├── conversation.py      # Individual conversation handler
│   │   ├── branching.py         # Dynamic conversation branching
│   │   ├── quality_scorer.py    # Conversation quality assessment
│   │   └── multi_session.py     # Multiple conversation orchestrator
│   ├── data/
│   │   ├── __init__.py
│   │   ├── models.py            # Pydantic data models
│   │   ├── storage.py           # File-based storage (JSON/CSV)
│   │   └── processor.py         # Data processing and analysis
│   ├── integrations/
│   │   ├── __init__.py
│   │   ├── llm_client.py        # OpenAI/Anthropic API wrapper
│   │   ├── platform_simulator.py # Mock platform API for user simulation
│   │   └── sentiment.py         # Sentiment analysis utilities
│   ├── reporting/
│   │   ├── __init__.py
│   │   ├── generator.py         # Report generation engine
│   │   ├── templates.py         # Report templates (text/markdown)
│   │   ├── charts.py            # ASCII/simple chart generation
│   │   └── exporters.py         # Export to various formats
│   └── utils/
│       ├── __init__.py
│       ├── display.py           # Rich console formatting
│       ├── progress.py          # Progress bars and status
│       └── validators.py        # Input validation
├── data/
│   ├── research_templates/
│   │   ├── customer_feedback.json
│   │   ├── product_research.json
│   │   └── user_experience.json
│   ├── mock_users/
│   │   ├── personas.json        # Different user archetypes
│   │   └── profiles.json        # Individual user profiles
│   └── outputs/                 # Runtime generated files
│       ├── conversations/       # Individual conversation logs
│       ├── reports/             # Generated reports
│       └── exports/             # Exported data
├── tests/
│   ├── __init__.py
│   ├── test_agent.py
│   ├── test_cli.py
│   ├── test_conversation.py
│   └── fixtures/
│       ├── sample_conversations.json
│       └── test_prompts.json
└── docs/
    ├── CLI_USAGE.md
    ├── DEMO_SCRIPT.md
    └── API_REFERENCE.md
