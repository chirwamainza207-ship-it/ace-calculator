[app]
# (str) Title of your application
title = Ace Calculator

# (str) Package name
package.name = acecalc

# (str) Package domain (needed for android packaging)
package.domain = org.ace

# (str) Source code directory where main.py sits
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.3.1,hostpython3

# (str) Supported orientations
orientation = portrait

# (bool) Use fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API (Stable 2026 build match)
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Let buildozer pick the correct NDK automatically
android.ndk_path =

# (bool) Auto-accept licenses (Crucial for automation platforms)
android.accept_sdk_license = True

# (bool) Allow backup
android.allow_backup = True
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 1
