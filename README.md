## Package Deprecation Notice

The CCI has taken ownership of the public Conan package for this library, which can be found at the following links:

https://github.com/conan-io/conan-center-index

Conan Community will keep this version of the package on Github and Bintray, however it will no longer be maintained or supported.
Users are advised to update their projects to use the official Conan package maintained by Conan Center Index immediately.


[![Download](https://api.bintray.com/packages/conan-community/conan/paho-c%3Aconan/images/download.svg) ](https://bintray.com/conan-community/conan/paho-c%3Aconan/_latestVersion)
[![Build Status Travis](https://travis-ci.org/conan-community/conan-paho-c.svg)](https://travis-ci.org/conan-community/conan-paho-c)
[![Build Status AppVeyor](https://ci.appveyor.com/api/projects/status/github/conan-community/conan-paho-c?svg=true)](https://ci.appveyor.com/project/ConanCIintegration/conan-paho-c)

## Conan package recipe for [*paho-c*](https://github.com/eclipse/paho.mqtt.c)

The Eclipse Paho project provides open-source client implementations of MQTT
and MQTT-SN messaging protocols aimed at new, existing, and emerging applications for the Internet
of Things (IoT)

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/conan-community/conan/paho-c%3Aconan).


## Issues

If you wish to report an issue or make a request for a package, please do so here:

[Issues Tracker](https://github.com/conan-community/community/issues)


## For Users

### Basic setup

    $ conan install paho-c/1.3.0@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    paho-c/1.3.0@conan/stable

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . conan/stable


### Available Options
| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| shared      | False |  [True, False] |
| fPIC      | True |  [True, False] |
| SSL      | False |  [True, False] |
| async      | True |  [True, False] |


## Add Remote

Conan Community has its own Bintray repository, however, we are working to distribute all package in the Conan Center:

    $ conan remote add conan-center "https://conan.bintray.com"


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package paho-c.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](LICENSE)
