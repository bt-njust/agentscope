# Scientific Collaboration Example - Usage Instructions

## Quick Start

To test the scientific collaboration example:

### 1. Set Environment Variables
```bash
export DASHSCOPE_API_KEY="your_dashscope_api_key_here"
```

### 2. Navigate to Example Directory
```bash
cd examples/workflows/scientific_collaboration
```

### 3. Run the Example
```bash
python main.py
```

### 4. View Demo (No API Key Required)
```bash
python demo.py
```

### 5. Run Tests
```bash
python test_profiles.py
```

## Expected Workflow Output

The script will simulate a realistic research collaboration session:

1. **Introduction Phase**: Researchers share their backgrounds
2. **Brainstorming Phase**: Multiple rounds of topic exploration  
3. **Selection Phase**: Collaborative evaluation and decision making
4. **Synthesis Phase**: Structured final recommendation

## Example Scenario

**Dr. Sarah Chen** (ML expert) and **Dr. Michael Rodriguez** (Biomedical Engineering expert) collaborate to select a research topic, leveraging their:

- Previous collaboration history
- Complementary expertise 
- Research interests and skills
- Recent publications
- Preferred research directions

The facilitator guides them to select an optimal research topic with structured output including reasoning, next steps, and collaboration assessment.

## Customization Options

- Modify researcher profiles in `main.py`
- Adjust conversation phases and rounds
- Change the facilitator's evaluation criteria
- Add more researchers to the conversation
- Extend to other collaboration scenarios

## Files Structure

- `main.py` - Core implementation
- `README.md` - Detailed documentation
- `demo.py` - Mock demonstration 
- `test_profiles.py` - Validation tests
- `USAGE.md` - This usage guide

## Technical Requirements

- Python 3.10+
- AgentScope framework
- DashScope API access
- Internet connection for API calls