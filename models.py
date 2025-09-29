
from pydantic import BaseModel
from typing import Dict, Any, Optional

class AgentContext(BaseModel):
    """Shared context that passes between agents"""
    original_query: str
    extracted_data: Dict[str, Any] = {}
    processed_results: Dict[str, Any] = {}
    current_agent: str = ""
    next_agents: list = []