import enum
from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData

APPROPRIATE_Y_VALUE = -0.5

class RoadState(enum.Enum):
    bad = "Bad"
    ok = "OK"


def process_agent_data(
    agent_data: AgentData,
) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    # Implement it
    road_state = get_road_state(agent_data.accelerometer.y)
    return ProcessedAgentData(road_state=road_state, user_id=1, agent_data=agent_data)

def get_road_state(y: int) -> str:
    if y < APPROPRIATE_Y_VALUE:
        return RoadState.bad.value
    return RoadState.ok.value