from core.ai_engine import AIEngine
from core.intent_parser import IntentParser
from core.command_router import CommandRouter


def test_intent_parser_open_app():
    parsed = IntentParser().parse("Open Instagram")
    assert parsed.intent == "OPEN_APP"
    assert parsed.target == "Instagram"


def test_ai_engine_greeting():
    response = AIEngine().process("hello nova")
    assert response.intent == "GREETING"
    assert "ready" in response.text.lower()


def test_router_make_call_requires_confirmation():
    result = CommandRouter().execute("MAKE_CALL", "Ali")
    assert result.status == "confirmation_required"


def test_unknown_command_is_safe():
    result = CommandRouter().execute("UNKNOWN")
    assert result.status == "unknown"
