"""Small optional Android bridge. Desktop runs safely without pyjnius."""
from __future__ import annotations

ANDROID = False
PythonActivity = None
Intent = None
Uri = None
Toast = None
Context = None
try:
    from jnius import autoclass
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    Intent = autoclass("android.content.Intent")
    Uri = autoclass("android.net.Uri")
    Toast = autoclass("android.widget.Toast")
    Context = autoclass("android.content.Context")
    ANDROID = True
except Exception:
    pass


def activity():
    return PythonActivity.mActivity if ANDROID else None


def start_activity(intent):
    if not ANDROID:
        return False
    activity().startActivity(intent)
    return True


def start_activity_for_result(intent, request_code: int):
    if not ANDROID:
        return False
    activity().startActivityForResult(intent, request_code)
    return True


def toast(message: str):
    if ANDROID:
        Toast.makeText(activity(), message, Toast.LENGTH_SHORT).show()
