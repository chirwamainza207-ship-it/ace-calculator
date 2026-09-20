[app]
# (str) Title of your application
title = Ace Calculator

# (str) Package name
package.name = acecalc

# (str) Package domain (needed for android packaging)
package.domain = org.ace

# (str) Source code directory where main.py sits
source.dir = .

# (list) Source files to include (let's catch everything)
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

# (int) Target Android API
android.api = 34

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to fetch
android.ndk = 25b

# (list) Architecture to build for
android.archs = arm64-v8a

# (bool) Auto-accept licenses (crucial for GitHub Actions!)
android.accept_sdk_license = True

# (bool) Allow backup
android.allow_backup = True
