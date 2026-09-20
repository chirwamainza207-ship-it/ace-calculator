[app]
title = Ace Calculator
package.name = acecalc
package.domain = org.ace

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Modernized stable API targets
android.api = 34
android.minapi = 24
android.ndk_path = 
android.accept_sdk_license = True
android.allow_backup = True

# Target only modern 64-bit architecture to prevent runner timeout
android.archs = arm64-v8a

# Set verbosity level to show errors clearly
log_level = 2

# Clean requirements pinning compatible packages
requirements = python3, kivy==2.3.1, cython==3.0.11

# Force python-for-android to use updated recipes
p4a.branch = master
