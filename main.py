import utils.session
from fastapi import FastAPI, Request
from agents.weather_agent import weather_agent
from agents.flight_agent import flight_agent
from response_formatter import response_formatter
from a2a.server.agent_execution import RequestContext

app = FastAPI()

weather_agent.next_agent = flight_agent
flight_agent.next_agent = response_formatter

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_text = body.get("input_text", "")

    context = RequestContext()
    context.input_text = user_text

    response = await weather_agent.execute(context)
    return {"response": response}
