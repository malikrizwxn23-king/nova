from __future__ import annotations
import re
from phone.android import ANDROID, Intent, start_activity

class AlarmManager:
    def set_alarm(self, time_value: str):
        if not time_value:
            return {"status": "error", "message": "No alarm time was provided."}
        if not ANDROID:
            return {"status": "unsupported", "message": "Alarm control is available on Android builds."}
        match = re.search(r"(\d{1,2})(?::(\d{2}))?\s*(am|pm)", time_value, re.I)
        if not match:
            return {"status": "error", "message": "Use a time such as 7:30 PM."}
        hour = int(match.group(1)); minute = int(match.group(2) or 0); ap = match.group(3).lower()
        if ap == "pm" and hour != 12: hour += 12
        if ap == "am" and hour == 12: hour = 0
        intent = Intent("android.intent.action.SET_ALARM")
        intent.putExtra("android.intent.extra.alarm.HOUR", hour)
        intent.putExtra("android.intent.extra.alarm.MINUTES", minute)
        start_activity(intent)
        return {"status": "success", "message": f"Alarm set for {time_value}."}

    def set_timer(self, duration: str):
        if not duration:
            return {"status": "error", "message": "No timer duration was provided."}
        if not ANDROID:
            return {"status": "unsupported", "message": "Timer control is available on Android builds."}
        match = re.search(r"(\d+)\s*(second|seconds|sec|minute|minutes|min|hour|hours|hr)", duration, re.I)
        if not match:
            return {"status": "error", "message": "Use a duration such as 10 minutes."}
        value = int(match.group(1)); unit = match.group(2).lower()
        seconds = value * (3600 if unit.startswith("hour") or unit == "hr" else 60 if unit.startswith("min") else 1)
        intent = Intent("android.intent.action.SET_TIMER")
        intent.putExtra("android.intent.extra.alarm.LENGTH", seconds)
        start_activity(intent)
        return {"status": "success", "message": f"Timer set for {duration}."}
