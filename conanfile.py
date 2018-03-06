from conans import ConanFile, CMake, tools
import os


class PahocConan(ConanFile):
    name = "paho-c"
    version = "1.2.0"
    license = "Eclipse Public License - v 1.0"
    url = "https://github.com/eclipse/paho.mqtt.c"
    description = "<Description of Pahoc here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "SSL": [True, False], "asynchronous": [True, False]}
    default_options = "shared=False", "SSL=False", "asynchronous=False"
    generators = "cmake"

    def source(self):
        tools.get("%s/archive/v%s.zip" % (self.url, self.version))
        os.rename("paho.mqtt.c-%s" % self.version, "sources")
        tools.replace_in_file("sources/CMakeLists.txt", "PROJECT(\"paho\" C)", '''PROJECT("paho" C)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')
        tools.replace_in_file("sources/CMakeLists.txt", "ADD_SUBDIRECTORY(test)", "")

    def requirements(self):
        if self.options.SSL:
            pass  # TODO: Add OpenSSL dependency

    def build(self):
        cmake = CMake(self)
        cmake.definitions["PAHO_BUILD_DOCUMENTATION"] = False
        cmake.definitions["PAHO_BUILD_SAMPLES"] = False
        cmake.definitions["PAHO_BUILD_DEB_PACKAGE"] = False
        cmake.definitions["PAHO_BUILD_STATIC"] = not self.options.shared
        cmake.definitions["PAHO_WITH_SSL"] = self.options.SSL
        cmake.configure(source_folder="sources")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="sources/src")
        self.copy("*paho*.dll", dst="bin", keep_path=False)
        self.copy("*paho*.dylib", dst="lib", keep_path=False)
        self.copy("*paho*.so*", dst="lib", keep_path=False)
        self.copy("*paho*.a", dst="lib", keep_path=False)
        self.copy("*paho*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = []

        if self.settings.os == "Windows":
            if self.settings.compiler == "Visual Studio" and not self.options.shared:
                self.cpp_info.libs.append("ws2_32")
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

    def configure(self):
        del self.settings.compiler.libcxx
