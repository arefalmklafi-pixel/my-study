[app]
title = My Study
package.name = mystudy
package.domain = org.mystudy
source.dir =.
source.include_exts = py,png,jpg,jpeg,kv,atlas
version = 1.0
requirements = python3==3.10.9,kivy==2.3.0
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
