from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from core.command_router import CommandRouter
from core.intent_parser import IntentParser

@dataclass
class AIResponse:
    text:str; intent:str; target:Optional[str]=None; parameters:dict|None=None; status:str="success"

class AIEngine:
    def __init__(self,parser=None,router=None): self.parser=parser or IntentParser(); self.router=router or CommandRouter()
    def process(self,user_input,confirmed=False):
        parsed=self.parser.parse(user_input); result=self.router.execute(parsed.intent,parsed.target,parsed.parameters,confirmed=confirmed)
        if parsed.intent=="GREETING": text="Hello, I'm NOVA, and I'm ready."
        else: text=result.message
        return AIResponse(text,parsed.intent,result.target,result.parameters,result.status)
