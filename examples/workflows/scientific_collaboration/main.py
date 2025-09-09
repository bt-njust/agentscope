# -*- coding: utf-8 -*-
"""Scientific collaboration scenario where two researchers discuss and select 
research topics based on their profiles and collaboration history."""
import asyncio
import os
from typing import Dict, List
from pydantic import BaseModel, Field

from agentscope.agent import ReActAgent
from agentscope.formatter import DashScopeMultiAgentFormatter
from agentscope.message import Msg
from agentscope.model import DashScopeChatModel
from agentscope.pipeline import MsgHub, sequential_pipeline


class ResearcherProfile(BaseModel):
    """Profile of a researcher including background and collaboration history."""
    
    name: str = Field(description="Researcher's name")
    age: int = Field(description="Researcher's age")
    field: str = Field(description="Primary research field")
    skills: List[str] = Field(description="List of technical skills")
    research_interests: List[str] = Field(description="Current research interests")
    recent_publications: List[str] = Field(description="Recent publication topics")
    collaboration_history: Dict[str, List[str]] = Field(
        description="History of collaboration with other researchers"
    )
    preferred_topics: List[str] = Field(description="Preferred research topics to explore")


class TopicSelection(BaseModel):
    """Structured output for selected research topic."""
    
    selected_topic: str = Field(description="The research topic both researchers agreed on")
    reasoning: str = Field(description="Rationale for selecting this topic")
    collaboration_potential: str = Field(
        description="Assessment of collaboration potential based on profiles"
    )
    next_steps: List[str] = Field(description="Proposed next steps for the research")


def create_researcher_agent(profile: ResearcherProfile) -> ReActAgent:
    """Create a researcher agent with specific profile and background."""
    
    # Build collaboration history text
    collab_text = ""
    if profile.collaboration_history:
        collab_text = "My past collaborations include:\n"
        for collaborator, topics in profile.collaboration_history.items():
            collab_text += f"- With {collaborator}: {', '.join(topics)}\n"
    
    sys_prompt = f"""You are Dr. {profile.name}, a {profile.age}-year-old researcher 
in {profile.field}. 

Your profile:
- Technical skills: {', '.join(profile.skills)}
- Research interests: {', '.join(profile.research_interests)}
- Recent publications: {', '.join(profile.recent_publications)}
- Preferred research topics: {', '.join(profile.preferred_topics)}

{collab_text}

You are participating in a research collaboration discussion to select a joint 
research topic. Be authentic to your background and consider:
1. How your expertise complements your collaborator's
2. Your past collaboration experience
3. Current research trends in your field
4. Feasibility and impact potential
5. Your genuine interest in the topic

Engage in a thoughtful, professional discussion while staying true to your 
research profile and experience."""

    return ReActAgent(
        name=f"Dr. {profile.name}",
        sys_prompt=sys_prompt,
        model=DashScopeChatModel(
            model_name="qwen-max",
            api_key=os.environ["DASHSCOPE_API_KEY"],
            stream=True,
        ),
        formatter=DashScopeMultiAgentFormatter(),
    )


def create_moderator_agent() -> ReActAgent:
    """Create a moderator agent to facilitate the discussion and make final decisions."""
    
    return ReActAgent(
        name="Research Facilitator",
        sys_prompt="""You are an experienced research facilitator helping two 
researchers collaborate on selecting a joint research topic. Your role is to:

1. Guide the discussion productively
2. Ensure both researchers' perspectives are heard
3. Help identify areas of mutual interest and complementary expertise
4. Synthesize their discussion into a concrete research topic selection
5. Assess the collaboration potential based on their profiles and discussion

Be objective, supportive, and focus on finding the best research topic that 
leverages both researchers' strengths.""",
        model=DashScopeChatModel(
            model_name="qwen-max",
            api_key=os.environ["DASHSCOPE_API_KEY"],
            stream=True,
        ),
        formatter=DashScopeMultiAgentFormatter(),
    )


async def run_scientific_collaboration() -> None:
    """Run the scientific collaboration workflow."""
    
    # Define researcher profiles
    researcher_1_profile = ResearcherProfile(
        name="Sarah Chen",
        age=35,
        field="Machine Learning",
        skills=["Deep Learning", "Neural Networks", "Computer Vision", "Python", "PyTorch"],
        research_interests=["AI Fairness", "Explainable AI", "Medical Image Analysis"],
        recent_publications=[
            "Bias Detection in Medical AI Systems",
            "Interpretable Deep Learning for Healthcare",
            "Fairness-Aware Neural Networks"
        ],
        collaboration_history={
            "Dr. James Liu": ["Healthcare AI Ethics", "Bias in Medical Imaging"],
            "Prof. Maria Santos": ["Explainable AI in Clinical Decision Making"]
        },
        preferred_topics=[
            "AI for Healthcare Equity",
            "Explainable Medical AI",
            "Bias Mitigation in Healthcare AI"
        ]
    )
    
    researcher_2_profile = ResearcherProfile(
        name="Michael Rodriguez",
        age=42,
        field="Biomedical Engineering",
        skills=["Signal Processing", "Medical Devices", "Data Analysis", "MATLAB", "R"],
        research_interests=["Biomedical Signal Processing", "Wearable Health Tech", "Telemedicine"],
        recent_publications=[
            "Advanced ECG Signal Analysis for Arrhythmia Detection",
            "Wearable Sensors for Remote Patient Monitoring",
            "Machine Learning in Biomedical Signal Processing"
        ],
        collaboration_history={
            "Dr. Lisa Wang": ["IoT Healthcare Devices", "Remote Monitoring Systems"],
            "Prof. Sarah Chen": ["ML Applications in Signal Processing"]  # Previous collaboration!
        },
        preferred_topics=[
            "AI-Powered Diagnostic Tools",
            "Smart Healthcare Monitoring",
            "Personalized Medicine Technology"
        ]
    )
    
    # Create researcher agents
    sarah = create_researcher_agent(researcher_1_profile)
    michael = create_researcher_agent(researcher_2_profile)
    facilitator = create_moderator_agent()
    
    print("=== Scientific Collaboration Session: Research Topic Selection ===\n")
    
    # Phase 1: Initial introductions and profile sharing
    print("📋 Phase 1: Researcher Introductions\n")
    
    async with MsgHub(
        participants=[sarah, michael],
        announcement=Msg(
            "system",
            "Welcome to this research collaboration session. Please introduce yourselves, "
            "share your current research focus, and mention any relevant past collaborations. "
            "This will help identify potential synergies for joint research.",
            "system",
        ),
    ) as hub:
        await sequential_pipeline([sarah, michael])
    
    # Phase 2: Topic brainstorming
    print("\n💡 Phase 2: Research Topic Brainstorming\n")
    
    async with MsgHub(
        participants=[sarah, michael],
        announcement=Msg(
            "system",
            "Now let's brainstorm potential research topics. Consider your complementary "
            "expertise, current research trends, and topics that could benefit from both "
            "of your backgrounds. Discuss what excites you and where you see opportunities "
            "for impactful collaboration.",
            "system",
        ),
    ) as hub:
        # Multiple rounds of discussion
        for round_num in range(3):
            print(f"  Round {round_num + 1} of brainstorming...")
            await sequential_pipeline([sarah, michael])
    
    # Phase 3: Topic evaluation and selection
    print("\n🎯 Phase 3: Topic Evaluation and Selection\n")
    
    async with MsgHub(
        participants=[sarah, michael],
        announcement=Msg(
            "system",
            "Based on your discussion, please now evaluate the proposed topics. "
            "Consider feasibility, impact potential, resource requirements, and "
            "how well each topic leverages both of your expertise. Work together "
            "to select the most promising research topic for collaboration.",
            "system",
        ),
    ) as hub:
        await sequential_pipeline([sarah, michael])
    
    # Phase 4: Facilitator synthesis and final recommendation
    print("\n📝 Phase 4: Research Facilitator Synthesis\n")
    
    final_decision = await facilitator(
        Msg(
            "user",
            "Based on the discussion between Dr. Sarah Chen and Dr. Michael Rodriguez, "
            "please synthesize their conversation and provide a structured recommendation "
            "for their joint research topic. Include the selected topic, reasoning, "
            "collaboration potential assessment, and suggested next steps.",
            "user",
        ),
        structured_model=TopicSelection,
    )
    
    print("\n" + "="*60)
    print("🎉 FINAL RESEARCH TOPIC SELECTION")
    print("="*60)
    
    if final_decision.metadata:
        selection = final_decision.metadata
        print(f"📊 Selected Topic: {selection.get('selected_topic', 'N/A')}")
        print(f"🔍 Reasoning: {selection.get('reasoning', 'N/A')}")
        print(f"🤝 Collaboration Potential: {selection.get('collaboration_potential', 'N/A')}")
        print("🎯 Next Steps:")
        next_steps = selection.get('next_steps', [])
        for i, step in enumerate(next_steps, 1):
            print(f"   {i}. {step}")
    else:
        print("⚠️  No structured output received from facilitator")
        print(f"💬 Facilitator's response: {final_decision.content}")
    
    print("\n" + "="*60)
    print("Research collaboration session completed successfully! 🎓")


if __name__ == "__main__":
    # Check for required environment variable
    if not os.environ.get("DASHSCOPE_API_KEY"):
        print("❌ Error: DASHSCOPE_API_KEY environment variable is required")
        print("Please set your DashScope API key before running this example.")
        exit(1)
    
    print("🚀 Starting Scientific Collaboration Workflow...\n")
    asyncio.run(run_scientific_collaboration())