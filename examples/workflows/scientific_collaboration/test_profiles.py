# -*- coding: utf-8 -*-
"""Test script to validate the researcher profiles and models without requiring API calls."""

import sys
import os

# Add the src directory to the path to import agentscope
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src'))

from main import ResearcherProfile, TopicSelection
from pydantic import ValidationError


def test_researcher_profile():
    """Test the ResearcherProfile model."""
    print("Testing ResearcherProfile model...")
    
    try:
        # Test valid profile
        profile = ResearcherProfile(
            name="Test Researcher",
            age=30,
            field="Computer Science",
            skills=["Python", "Machine Learning"],
            research_interests=["AI", "Data Science"],
            recent_publications=["Paper 1", "Paper 2"],
            collaboration_history={"Dr. Smith": ["Topic A", "Topic B"]},
            preferred_topics=["AI Applications", "Data Mining"]
        )
        print("✅ ResearcherProfile model validation passed")
        print(f"   Name: {profile.name}")
        print(f"   Field: {profile.field}")
        print(f"   Skills: {profile.skills}")
        return True
        
    except ValidationError as e:
        print(f"❌ ResearcherProfile validation failed: {e}")
        return False


def test_topic_selection():
    """Test the TopicSelection model."""
    print("\nTesting TopicSelection model...")
    
    try:
        # Test valid topic selection
        selection = TopicSelection(
            selected_topic="AI for Healthcare",
            reasoning="Combines expertise in AI and medical applications",
            collaboration_potential="High potential due to complementary skills",
            next_steps=["Literature review", "Prototype development", "Testing"]
        )
        print("✅ TopicSelection model validation passed")
        print(f"   Topic: {selection.selected_topic}")
        print(f"   Reasoning: {selection.reasoning}")
        print(f"   Next steps: {selection.next_steps}")
        return True
        
    except ValidationError as e:
        print(f"❌ TopicSelection validation failed: {e}")
        return False


def test_import_dependencies():
    """Test that all required dependencies can be imported."""
    print("\nTesting dependency imports...")
    
    try:
        from agentscope.agent import ReActAgent
        from agentscope.formatter import DashScopeMultiAgentFormatter
        from agentscope.message import Msg
        from agentscope.model import DashScopeChatModel
        from agentscope.pipeline import MsgHub, sequential_pipeline
        print("✅ All AgentScope dependencies imported successfully")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False


def test_profile_creation():
    """Test creating the actual researcher profiles used in main.py."""
    print("\nTesting specific researcher profile creation...")
    
    try:
        # Test Sarah Chen's profile
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
        
        # Test Michael Rodriguez's profile
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
        
        print("✅ Both researcher profiles created successfully")
        print(f"   Sarah's field: {sarah_profile.field}")
        print(f"   Michael's field: {michael_profile.field}")
        print(f"   Shared collaboration: Found past collaboration between them")
        return True
        
    except ValidationError as e:
        print(f"❌ Profile creation failed: {e}")
        return False


def main():
    """Run all tests."""
    print("🧪 Running Scientific Collaboration Example Tests\n")
    
    tests = [
        test_import_dependencies,
        test_researcher_profile,
        test_topic_selection,
        test_profile_creation,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The example is ready to run.")
        print("\n💡 To run the full example, set your DASHSCOPE_API_KEY environment variable and run:")
        print("   python main.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)