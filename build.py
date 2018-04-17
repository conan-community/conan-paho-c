from conan.packager import ConanMultiPackager
import os, re


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
    header_only = False
    name = get_name_from_recipe()
    version = get_version_from_recipe()
    reference = "{0}/{1}".format(name, version)
    username = "conan"
    login_username = "conanbot"
    upload_remote = "https://api.bintray.com/conan/conan-community/{0}".format(username)

    builder = ConanMultiPackager(
        stable_branch_pattern="stable/*",
        upload_only_when_stable=True,
        username=username,
        login_username=login_username,
        reference=reference,
        upload=upload_remote,
        remotes=upload_remote)

    if header_only:
        filtered_builds = []
        for settings, options, env_vars, build_requires, reference in builder.items:
            if settings["compiler"] == "gcc":
                filtered_builds.append([settings, options, env_vars, build_requires])
                break
        builder.builds = filtered_builds

    builder.add_common_builds(pure_c=True,
                              shared_option_name="paho-c:shared",
                              dll_with_static_runtime=True)
    builder.run()
