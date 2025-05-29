

## Key Components Overview

### Core Functionality
- **Agent System**: 
  - `agent/core.py` - Central research logic
  - `agent/branching.py` - Dynamic conversation flows
  - `agent/multi_session.py` - Concurrent conversation management

### Data Handling
- **Storage & Processing**:
  - `data/storage.py` - JSON/CSV persistence
  - `data/processor.py` - Analysis pipelines
- **Mock Data**:
  - Predefined user personas (`data/mock_users/`)
  - Research templates (`data/research_templates/`)

### Integrations
- `integrations/llm_client.py` - Unified LLM interface
- `integrations/platform_simulator.py` - Simulated user environments
- `integrations/sentiment.py` - Emotion analysis tools

### Reporting
- `reporting/generator.py` - Automated report creation
- `reporting/charts.py` - Visualization components
- Multiple export formats via `reporting/exporters.py`

### Utilities
- Rich console output (`utils/display.py`)
- Input validation (`utils/validators.py`)
- Progress tracking (`utils/progress.py`)

### Operational Files
- `setup.py` - CLI installation
- `config/settings.py` - API key management
- `config/prompts.py` - Prompt engineering templates

### Quality Assurance
- Test suite covering core components (`tests/`)
- Quality scoring mechanism (`agent/quality_scorer.py`)

### Documentation
- Usage guides (`docs/CLI_USAGE.md`)
- Demo scripts (`docs/DEMO_SCRIPT.md`)
