from __future__ import annotations
import platform
from phone.android import ANDROID, Context

class DeviceInfo:
    @staticmethod
    def get_battery_level():
        if not ANDROID: return {"status":"unsupported","message":"Battery information is available on Android builds."}
        try:
            activity = __import__("phone.android", fromlist=["activity"]).activity()
            bm = activity.getSystemService(Context.BATTERY_SERVICE)
            return {"status":"success","battery":bm.getIntProperty(4)}
        except Exception as exc: return {"status":"error","message":str(exc)}
    @staticmethod
    def get_system_info():
        return {"status":"success","platform":platform.platform(),"python_version":platform.python_version(),"android":ANDROID}
