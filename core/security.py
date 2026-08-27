class Security:
    HIGH_RISK_ACTIONS={"MAKE_CALL"}
    MEDIUM_RISK_ACTIONS={"SEND_MESSAGE","SEND_WHATSAPP","TAKE_PHOTO","OPEN_CAMERA","SET_ALARM","SET_TIMER"}
    @staticmethod
    def requires_confirmation(intent_name): return (intent_name or "").upper() in Security.HIGH_RISK_ACTIONS|Security.MEDIUM_RISK_ACTIONS
    @staticmethod
    def confirmation_message(intent_name): return "Please confirm this action before NOVA continues."
