# conan-paho-c

![conan-paho-c image](/images/conan-paho-c.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/paho-c%3Aconan/images/download.svg?version=1.2.0%3Astable)](https://bintray.com/conan-community/conan/paho-c%3Aconan/1.2.0%3Astable/link)
[![Build Status](https://travis-ci.org/conan-community/conan-paho-c.svg?branch=stable%2F1.2.0)](https://travis-ci.org/conan-community/conan-paho-c)
[![Build status](https://ci.appveyor.com/api/projects/status/b15m00302vlt843c/branch/stable/1.2.0?svg=true)](https://ci.appveyor.com/project/danimtb/conan-paho-c/branch/stable/1.2.0)

[Conan.io](https://conan.io) package for [paho.mqtt.c](https://github.com/eclipse/paho.mqtt.c) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conan-community/conan/paho-c%3Aconan).

## For Users: Use this package

### Basic setup

    $ conan install paho-c/1.2.0@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    paho-c/1.2.0@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)
