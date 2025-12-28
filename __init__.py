"""
AI Squad - Developer Agent with GitHub Integration

A Python application that provides an AI-powered Developer agent with
GitHub integration capabilities using LangChain.
"""

__version__ = "1.0.0"
__author__ = "Caio Bruno Vieira"

from .developer_agent import DeveloperAgent, create_developer_agent
from .config import Config

__all__ = [
    "DeveloperAgent",
    "create_developer_agent",
    "Config",
]
