[app]
title = Artemis Patch Manager
package.name = artemispatchmanager
package.domain = org.artemis.patchmanager

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,yml,yaml

version = 2.0.0

# Dependencies: include kivy and pyyaml or whatever parsing libs you use
requirements = python3,kivy==2.3.0,pyyaml,requests,urllib3,certifi

orientation = portrait

# Android specific permissions for reading/writing patch files
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE
android.api = 34
android.minapi = 26
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
