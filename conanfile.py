import os
from conans import ConanFile, CMake, tools


class PahocConan(ConanFile):
    name = "paho-c"
    version = "1.2.0"
    license = "EPL-1.0"
    homepage = "https://github.com/eclipse/paho.mqtt.c"
    description = """The Eclipse Paho project provides open-source client implementations of MQTT
and MQTT-SN messaging protocols aimed at new, existing, and emerging applications for the Internet
of Things (IoT)"""
    url = "https://github.com/conan-community/conan-paho-c"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "SSL": [True, False], "asynchronous": [True, False]}
    default_options = "shared=False", "SSL=False", "asynchronous=False"
    generators = "cmake"
    exports = "LICENSE"

    @property
    def source_subfolder(self):
        return "sources"

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        tools.get("%s/archive/v%s.zip" % (self.homepage, self.version))
        os.rename("paho.mqtt.c-%s" % self.version, self.source_subfolder)
        cmakelists_path = "%s/CMakeLists.txt" % self.source_subfolder
        tools.replace_in_file(cmakelists_path,
                              "PROJECT(\"paho\" C)",
                              """PROJECT("paho" C)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()""")
        tools.replace_in_file(cmakelists_path, "ADD_SUBDIRECTORY(test)", "")
        tools.replace_in_file(cmakelists_path,
                              "ADD_DEFINITIONS(-D_CRT_SECURE_NO_DEPRECATE -DWIN32_LEAN_AND_MEAN -MD)",
                              "ADD_DEFINITIONS(-D_CRT_SECURE_NO_DEPRECATE -DWIN32_LEAN_AND_MEAN)")

    def requirements(self):
        if self.options.SSL:
            self.requires("OpenSSL/1.0.2n@conan/stable")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["PAHO_BUILD_DOCUMENTATION"] = False
        cmake.definitions["PAHO_BUILD_SAMPLES"] = False
        cmake.definitions["PAHO_BUILD_DEB_PACKAGE"] = False
        cmake.definitions["PAHO_BUILD_STATIC"] = not self.options.shared
        cmake.definitions["PAHO_WITH_SSL"] = self.options.SSL
        cmake.configure(source_folder=self.source_subfolder)
        cmake.build()

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy("*.h", dst="include", src="%s/src" % self.source_subfolder)
        self.copy("*paho*.dll", dst="bin", keep_path=False)
        self.copy("*paho*.dylib", dst="lib", keep_path=False)
        self.copy("*paho*.so*", dst="lib", keep_path=False)
        self.copy("*paho*.a", dst="lib", keep_path=False)
        self.copy("*paho*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = []

        if self.options.shared and self:
            if self.options.asynchronous:
                if self.options.SSL:
                    self.cpp_info.libs.append("paho-mqtt3as")
                else:
                    self.cpp_info.libs.append("paho-mqtt3a")
            else:
                if self.options.SSL:
                    self.cpp_info.libs.append("paho-mqtt3cs")
                else:
                    self.cpp_info.libs.append("paho-mqtt3c")
        else:
            if self.options.asynchronous:
                if self.options.SSL:
                    self.cpp_info.libs.append("paho-mqtt3as-static")
                else:
                    self.cpp_info.libs.append("paho-mqtt3a-static")
            else:
                if self.options.SSL:
                    self.cpp_info.libs.append("paho-mqtt3cs-static")
                else:
                    self.cpp_info.libs.append("paho-mqtt3c-static")

        if self.settings.os == "Windows":
            if not self.options.shared:
                self.cpp_info.libs.append("ws2_32")
                if self.settings.compiler == "gcc":
                    self.cpp_info.libs.append("wsock32") # (MinGW) needed?
        else:
            if self.settings.os == "Linux":
                self.cpp_info.libs.append("c")
                self.cpp_info.libs.append("dl")
                self.cpp_info.libs.append("pthread")
            elif self.settings.os == "FreeBSD":
                self.cpp_info.libs.append("compat")
                self.cpp_info.libs.append("pthread")
            else:
                self.cpp_info.libs.append("c")
                self.cpp_info.libs.append("pthread")
