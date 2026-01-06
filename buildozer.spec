
[app]
title = Colossus Admin
package.name = colossusadmin
package.domain = org.colossus
source.dir = .
source.include_exts = py,kv,json,ini
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = armeabi-v7a, arm64-v8a
# Se precisar permissões, adicione aqui:
# android.permissions = INTERNET
