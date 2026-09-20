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

# Modernized stable API targets to fix the OpenSSL crash
android.api = 34
android.minapi = 24
android.ndk_path =
android.accept_sdk_license = True
android.allow_backup = True

# Kept short and quiet so it doesn't hit log limits!
log_level = 1
