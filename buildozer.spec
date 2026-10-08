[app]
title = My Game
package.name = mygame
package.domain = org.aref.mygame
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.0
orientation = landscape

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
p4a.bootstrap = sdl2
