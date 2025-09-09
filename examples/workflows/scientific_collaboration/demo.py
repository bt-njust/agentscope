# -*- coding: utf-8 -*-
"""Demo script to showcase the scientific collaboration workflow structure without API calls."""

import sys
import os
from datetime import datetime

# Add the src directory to the path to import agentscope
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src'))

from main import ResearcherProfile, TopicSelection


def simulate_conversation():
    """Simulate the conversation flow with mock responses."""
    
    print("🚀 Scientific Collaboration Workflow Demo")
    print("=" * 60)
    print(f"Demo run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Create the researcher profiles
    sarah_profile = ResearcherProfile(
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
    
    michael_profile = ResearcherProfile(
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
            "Prof. Sarah Chen": ["ML Applications in Signal Processing"]
        },
        preferred_topics=[
            "AI-Powered Diagnostic Tools",
            "Smart Healthcare Monitoring",
            "Personalized Medicine Technology"
        ]
    )
    
    print("\n📋 RESEARCHER PROFILES")
    print("-" * 40)
    print(f"🔬 Dr. {sarah_profile.name} ({sarah_profile.age} years)")
    print(f"   Field: {sarah_profile.field}")
    print(f"   Key Skills: {', '.join(sarah_profile.skills[:3])}...")
    print(f"   Research Interests: {', '.join(sarah_profile.research_interests)}")
    print(f"   Recent Publications: {len(sarah_profile.recent_publications)} papers")
    
    print(f"\n🔬 Dr. {michael_profile.name} ({michael_profile.age} years)")
    print(f"   Field: {michael_profile.field}")
    print(f"   Key Skills: {', '.join(michael_profile.skills[:3])}...")
    print(f"   Research Interests: {', '.join(michael_profile.research_interests)}")
    print(f"   Recent Publications: {len(michael_profile.recent_publications)} papers")
    
    # Show collaboration history
    print(f"\n🤝 PAST COLLABORATION")
    print("-" * 40)
    shared_collab = "Prof. Sarah Chen" in michael_profile.collaboration_history
    if shared_collab:
        topics = michael_profile.collaboration_history["Prof. Sarah Chen"]
        print(f"✅ Previous collaboration found!")
        print(f"   Topics: {', '.join(topics)}")
    else:
        print("❌ No previous direct collaboration")
    
    # Simulate workflow phases
    print(f"\n💡 SIMULATED WORKFLOW PHASES")
    print("-" * 40)
    
    phases = [
        ("📋 Phase 1: Researcher Introductions", "Sharing backgrounds and expertise"),
        ("💡 Phase 2: Research Topic Brainstorming", "Exploring collaborative opportunities"),
        ("🎯 Phase 3: Topic Evaluation and Selection", "Assessing feasibility and impact"),
        ("📝 Phase 4: Research Facilitator Synthesis", "Final recommendation and next steps")
    ]
    
    for phase_name, description in phases:
        print(f"\n{phase_name}")
        print(f"   {description}")
    
    # Create a mock final selection
    mock_selection = TopicSelection(
        selected_topic="AI-Enhanced Wearable Health Monitoring for Personalized Healthcare",
        reasoning="This topic perfectly combines Dr. Chen's expertise in AI fairness and explainable AI with Dr. Rodriguez's background in biomedical signal processing and wearable technology. Their previous collaboration on ML applications in signal processing provides a solid foundation.",
        collaboration_potential="Excellent synergy potential. Dr. Chen's work on bias detection in medical AI systems complements Dr. Rodriguez's experience with wearable sensors and remote monitoring. Together they can address both technical innovation and ethical considerations in healthcare AI.",
        next_steps=[
            "Conduct comprehensive literature review on current wearable health AI systems",
            "Identify specific healthcare equity challenges in current monitoring technologies",
            "Design preliminary system architecture combining AI fairness with signal processing",
            "Develop prototype focusing on bias detection in health monitoring algorithms",
            "Plan user studies with diverse patient populations",
            "Prepare grant proposal for NIH or NSF funding"
        ]
    )
    
    print(f"\n🎉 MOCK FINAL SELECTION")
    print("=" * 60)
    print(f"📊 Selected Topic:")
    print(f"   {mock_selection.selected_topic}")
    print(f"\n🔍 Reasoning:")
    print(f"   {mock_selection.reasoning}")
    print(f"\n🤝 Collaboration Potential:")
    print(f"   {mock_selection.collaboration_potential}")
    print(f"\n🎯 Next Steps:")
    for i, step in enumerate(mock_selection.next_steps, 1):
        print(f"   {i}. {step}")
    
    print("\n" + "=" * 60)
    print("✅ Demo completed successfully!")
    print("\n💡 To run the actual workflow with real AI agents:")
    print("   1. Set your DASHSCOPE_API_KEY environment variable")
    print("   2. Run: python main.py")
    print("\n📚 For more information, see README.md")


def show_technical_details():
    """Show technical implementation details."""
    
    print(f"\n🔧 TECHNICAL IMPLEMENTATION DETAILS")
    print("-" * 40)
    
    details = [
        ("🤖 Agent Framework", "AgentScope with ReActAgent"),
        ("🧠 LLM Model", "DashScope qwen-max"),
        ("💬 Communication", "MsgHub for multi-agent coordination"),
        ("📊 Data Structure", "Pydantic models for type safety"),
        ("🔄 Workflow", "Sequential pipeline with async support"),
        ("📝 Output Format", "Structured JSON with validation"),
        ("🎯 Customization", "Easily configurable profiles and phases")
    ]
    
    for feature, description in details:
        print(f"{feature}: {description}")
    
    print(f"\n📈 WORKFLOW SCALABILITY")
    print("-" * 40)
    print("✅ Support for multiple researchers (2+ agents)")
    print("✅ Customizable conversation phases")
    print("✅ Structured decision-making process")
    print("✅ Rich agent profiles with history")
    print("✅ Extensible for other collaboration scenarios")


if __name__ == "__main__":
    simulate_conversation()
    show_technical_details()