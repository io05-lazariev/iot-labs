from pydantic import BaseModel
from app.entities.agent_data import AgentData


class ProcessedAgentData(BaseModel):
    road_state: str
    user_id: int
    agent_data: AgentData
