[app]
title = NOVA
package.name = nova
package.domain = com.nova.ai
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json
version = 0.2.0
requirements = python3,kivy,kivymd,pyjnius
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,CAMERA,READ_CONTACTS,POST_NOTIFICATIONS
android.archs = arm64-v8a
android.minapi = 23
android.api = 34
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
