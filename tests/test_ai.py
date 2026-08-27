from core.ai_engine import AIEngine
from core.command_router import CommandRouter
from core.intent_parser import IntentParser


def test_open_app_parsing():
    parsed = IntentParser().parse("Open YouTube")
    assert parsed.intent == "OPEN_APP"
    assert parsed.target == "YouTube"


def test_timer_parsing():
    parsed = IntentParser().parse("Set timer for 10 minutes")
    assert parsed.intent == "SET_TIMER"


def test_greeting_response():
    engine = AIEngine()
    response = engine.process("hello nova")
    assert response.intent == "GREETING"
    assert "NOVA" in response.text


def test_router_unknown():
    result = CommandRouter().execute("UNKNOWN")
    assert result.status == "unknown"
