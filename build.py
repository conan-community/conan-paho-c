from conan.packager import ConanMultiPackager
import os, re, platform


def get_value_from_recipe(search_string):
    with open("conanfile.py", "r") as conanfile:
        contents = conanfile.read()
        result = re.search(search_string, contents)
    return result

def get_name_from_recipe():
    return get_value_from_recipe(r'''name\s*=\s*["'](\S*)["']''').groups()[0]

def get_version_from_recipe():
    return get_value_from_recipe(r'''version\s*=\s*["'](\S*)["']''').groups()[0]

if __name__ == "__main__":
    name = get_name_from_recipe()
    username = "conan"
    channel = "stable"
    version = get_version_from_recipe()
    login_username = "conanbot"
    reference = "{0}/{1}".format(name, version)
    upload_remote = "https://api.bintray.com/conan/conan-community/{0}".format(username)

    builder = ConanMultiPackager(
        username=username,
        channel=channel,
        login_username=login_username,
        reference=reference,
        upload=upload_remote,
        remotes=upload_remote)

    builder.add_common_builds(pure_c=True,
                              shared_option_name="paho-c:shared",
                              dll_with_static_runtime=True)
    builder.run()
