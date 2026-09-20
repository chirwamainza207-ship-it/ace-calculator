[app]
title = Ace Calculator
package.name = acecalc
package.domain = org.ace
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.1,hostpython3
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Stable compiler target versions
android.api = 33
android.minapi = 21
android.ndk_path =
android.accept_sdk_license = True
android.allow_backup = True

# Standard logging level to read the exact error output line
log_level = 2
