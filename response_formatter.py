from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.utils import new_agent_text_message


class ResponseFormatter(AgentExecutor):
    async def execute(self, request: RequestContext):
        context = request.agent_context
        weather = context.processed_results.get("weather")
        flights = context.processed_results.get("flights")

        response = []
        if weather:
            response.append(f"Weather Info:\n{weather}")
        if flights:
            response.append(f"Flight Info:\n{flights}")
        if not response:
            response.append("No info available.")

        return new_agent_text_message("\n\n".join(response))

    async def cancel(self, request: RequestContext):
        return new_agent_text_message("Response formatting cancelled.")

response_formatter = ResponseFormatter()
