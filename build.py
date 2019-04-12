# -*- coding: utf-8 -*-
from copy import deepcopy
from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(pure_c=True, dll_with_static_runtime=True)
    builds = list(builder.items)
    new_builds = deepcopy(builds)
    for build in new_builds:
        build.options['paho-c:asynchronous'] = False
    builder.items.extend(new_builds)
    builder.run()
