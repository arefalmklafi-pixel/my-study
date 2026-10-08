[app]
title = My Study
package.name = mystudy
package.domain = org.mystudy
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 31
android.minapi = 21
android.archs = arm64-v8a
