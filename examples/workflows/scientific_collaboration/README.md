# Scientific Collaboration Workflow

This example demonstrates how to use AgentScope to simulate a scientific collaboration scenario where two researchers with different backgrounds discuss and select a joint research topic based on their profiles and collaboration history.

## Overview

The workflow simulates a realistic research collaboration session with:

- **Two Researcher Agents**: Each with detailed profiles including age, field, skills, research interests, recent publications, collaboration history, and preferred topics
- **Research Facilitator Agent**: An experienced moderator who guides the discussion and synthesizes the final topic selection
- **Structured Decision Making**: Uses Pydantic models for structured output of the final research topic selection

## Scenario Description

### Researcher Profiles

**Dr. Sarah Chen (35 years old)**
- Field: Machine Learning
- Skills: Deep Learning, Neural Networks, Computer Vision, Python, PyTorch
- Research Interests: AI Fairness, Explainable AI, Medical Image Analysis
- Recent Publications: Focus on bias detection and interpretable AI in healthcare
- Past Collaborations: Healthcare AI ethics and explainable AI projects

**Dr. Michael Rodriguez (42 years old)**
- Field: Biomedical Engineering  
- Skills: Signal Processing, Medical Devices, Data Analysis, MATLAB, R
- Research Interests: Biomedical Signal Processing, Wearable Health Tech, Telemedicine
- Recent Publications: ECG analysis, wearable sensors, ML in biomedical signals
- Past Collaborations: IoT healthcare devices and has previously worked with Dr. Chen

## Workflow Phases

### Phase 1: Researcher Introductions
- Each researcher introduces themselves
- Share current research focus and past collaborations
- Identify potential synergies

### Phase 2: Research Topic Brainstorming
- Multiple rounds of brainstorming sessions
- Discussion of complementary expertise
- Exploration of research opportunities

### Phase 3: Topic Evaluation and Selection
- Evaluate proposed topics for feasibility and impact
- Consider resource requirements and expertise alignment
- Collaborative selection of the most promising topic

### Phase 4: Facilitator Synthesis
- Research facilitator synthesizes the discussion
- Provides structured recommendation with:
  - Selected research topic
  - Reasoning for selection
  - Collaboration potential assessment
  - Suggested next steps

## Prerequisites

### Environment Setup

1. **DashScope API Key**: You need a valid DashScope API key from Alibaba Cloud
   ```bash
   export DASHSCOPE_API_KEY="your_api_key_here"
   ```

2. **AgentScope Installation**: Ensure AgentScope is installed
   ```bash
   pip install -e .  # from the repository root
   ```

## Usage

### Running the Example

```bash
cd examples/workflows/scientific_collaboration
python main.py
```

### Expected Output

The script will produce a structured conversation showing:

1. **Introductory Phase**: Researchers sharing their backgrounds
2. **Brainstorming Phase**: Multiple rounds of topic exploration
3. **Selection Phase**: Collaborative evaluation and decision making
4. **Final Recommendation**: Structured output with:
   - Selected research topic
   - Detailed reasoning
   - Collaboration potential assessment
   - Concrete next steps

### Example Output Structure

```
🎉 FINAL RESEARCH TOPIC SELECTION
============================================================
📊 Selected Topic: AI-Powered Wearable Health Monitoring for Healthcare Equity
🔍 Reasoning: Combines Sarah's AI fairness expertise with Michael's biomedical engineering background...
🤝 Collaboration Potential: Excellent synergy between AI/ML and biomedical engineering expertise...
🎯 Next Steps:
   1. Literature review on current wearable health monitoring systems
   2. Identify specific healthcare equity challenges to address
   3. Design preliminary system architecture
   ...
```

## Customization

### Modifying Researcher Profiles

You can customize the researcher profiles by modifying the `ResearcherProfile` objects in `main.py`:

```python
researcher_profile = ResearcherProfile(
    name="Your Name",
    age=30,
    field="Your Field",
    skills=["Skill1", "Skill2"],
    research_interests=["Interest1", "Interest2"],
    recent_publications=["Publication1", "Publication2"],
    collaboration_history={"Collaborator": ["Topic1", "Topic2"]},
    preferred_topics=["Topic1", "Topic2"]
)
```

### Adding More Researchers

The framework supports multiple researchers. Simply create additional profiles and add them to the conversation flow.

### Modifying the Workflow

You can adjust the workflow by:
- Changing the number of brainstorming rounds
- Adding additional phases (e.g., funding discussion, timeline planning)
- Modifying the facilitator's synthesis criteria
- Adding structured outputs for intermediate phases

## Technical Details

### Key Components

- **ReActAgent**: Core agent implementation with reasoning capabilities
- **DashScopeMultiAgentFormatter**: Handles multi-agent conversation formatting
- **MsgHub**: Manages message broadcasting between participants
- **Pydantic Models**: Ensure structured data handling for profiles and outputs
- **Sequential Pipeline**: Orchestrates turn-based conversations

### Model Configuration

The example uses:
- **Model**: `qwen-max` (DashScope's advanced model)
- **Streaming**: Enabled for real-time conversation flow
- **Structured Output**: Pydantic model validation for final recommendations

## Educational Value

This example demonstrates:

1. **Complex Agent Profiles**: How to create agents with rich, realistic backgrounds
2. **Multi-Phase Workflows**: Structured conversation management
3. **Collaborative Decision Making**: Agents working together toward a common goal
4. **Historical Context**: How past experiences influence current decisions
5. **Structured Outputs**: Converting natural conversation to actionable recommendations
6. **Domain Expertise**: Authentic representation of academic collaboration

## Potential Extensions

- **Grant Proposal Generation**: Extend to generate research proposals
- **Timeline Planning**: Add project timeline and milestone discussion
- **Resource Allocation**: Include budget and resource planning phases
- **Literature Review**: Integrate automated literature search and analysis
- **Peer Review Simulation**: Simulate peer review of the selected topic