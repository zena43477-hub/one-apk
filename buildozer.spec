[app]
title = Button Test
package.name = buttontest
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 0.1
requirements = python3==3.10.12,hostpython3==3.10.12,pygame,pgzero
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.api = 33
android.minapi = 24
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
