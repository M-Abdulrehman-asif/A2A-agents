from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.utils import new_agent_text_message
from models import AgentContext
import logging
import google.generativeai as genai
from config.settings import GEMINI_API_KEY, MODEL

logger = logging.getLogger(__name__)
genai.configure(api_key=GEMINI_API_KEY)


class WeatherAgent(AgentExecutor):
    def __init__(self, next_agent=None):
        super().__init__()
        self.name = "WeatherAgent"
        self.next_agent = next_agent

    async def execute(self, request: RequestContext):
        if not hasattr(request, "agent_context"):
            request.agent_context = AgentContext(original_query=request.input_text)

        context = request.agent_context
        context.current_agent = "weather_agent"

        query = context.original_query
        logger.info(f"WeatherAgent received: {query}")

        prompt = f"Extract the city from: '{query}'. Then give me fake but realistic weather in JSON."
        response = genai.GenerativeModel(MODEL).generate_content(prompt)
        result = response.text.strip()

        context.processed_results["weather"] = result

        if self.next_agent:
            return await self.next_agent.execute(request)
        return new_agent_text_message(result)

    async def cancel(self, request: RequestContext):
        return new_agent_text_message("Weather request cancelled.")

weather_agent = WeatherAgent()
