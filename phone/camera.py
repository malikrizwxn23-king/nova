from __future__ import annotations
from phone.android import ANDROID, Intent, start_activity_for_result

REQUEST_CAMERA = 4101

class CameraManager:
    """Launches Android's camera app. Capture is completed by Android's camera UI."""
    def open_camera(self):
        if not ANDROID:
            return {"status": "unsupported", "message": "Camera is available on Android builds."}
        intent = Intent(Intent.ACTION_CAMERA_BUTTON)
        try:
            # ACTION_IMAGE_CAPTURE is the portable camera contract.
            intent = Intent(Intent.ACTION_IMAGE_CAPTURE)
            start_activity_for_result(intent, REQUEST_CAMERA)
            return {"status": "success", "message": "Camera opened."}
        except Exception as exc:
            return {"status": "error", "message": f"Could not open camera: {exc}"}

    def take_photo(self):
        return self.open_camera()
