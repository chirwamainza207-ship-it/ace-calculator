[app]
title = Ace Calculator
package.name = acecalc
package.domain = org.ace

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# 1. Fixed requirements (removed hostpython3 which causes modern conflicts)
requirements = python3, kivy==2.3.1

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# 2. Modernized stable API targets to fix the OpenSSL crash
android.api = 34
android.minapi = 24
android.ndk_path = 
android.accept_sdk_license = True
android.allow_backup = True

# 3. Explicitly target ONLY ONE architecture to stop the 20-minute timeout
android.archs = arm64-v8a

# 4. CRITICAL: Turned verbosity BACK ON so we can see errors if it fails
log_level = 2
