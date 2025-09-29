from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.utils import new_agent_text_message
from agents.weather_agent import logger
import google.generativeai as genai
from config.settings import MODEL

class FlightAgent(AgentExecutor):
    def __init__(self, next_agent=None):
        super().__init__()
        self.name = "FlightAgent"
        self.next_agent = next_agent

    async def execute(self, request: RequestContext):
        context = request.agent_context
        context.current_agent = "flight_agent"
        query = context.original_query

        logger.info(f"FlightAgent received: {query}")

        prompt = f"Extract origin and destination as IATA codes from: '{query}'. Return JSON with origin and destination."
        response = genai.GenerativeModel(MODEL).generate_content(prompt)
        flight_info = response.text.strip()

        context.processed_results["flights"] = flight_info

        if self.next_agent:
            return await self.next_agent.execute(request)
        return new_agent_text_message(flight_info)

    async def cancel(self, request: RequestContext):
        return new_agent_text_message("Flight request cancelled.")


flight_agent = FlightAgent()
