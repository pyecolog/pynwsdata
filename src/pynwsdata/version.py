
def read_version() -> str:
    #
    # read the project version from the version file
    #
    # if the following are true, then also update the current
    # version file
    #
    # - if the current version file is writeable
    # - if the project file pyproject.toml is available and
    #    has a newer last modified time than the version file
    # - if the 'packaging' module is installed within the immediate
    #   python env, e.g installed via project dev dependencies
    # - lastly, if the project file provides a newer version string
    #   than the current version file
    #
    # if any of those conditions are not met and the current
    # version file can be read, returns a string representing
    # the first line in the current version file
    #
    # if the current version file cannot be read, returns the
    # string "0.0.0"
    #
    # implementation notes:
    #
    # - when this file is evaluated using ipython %run, warnings
    #   might not show up immediately
    #
    # - additional dependencies are imported as needed, below
    #
    from warnings import warn
    import os
    import shlex

    this_dir = os.path.dirname(os.path.abspath(__file__))
    version_file = os.path.join(this_dir, "version")
    if os.path.exists(version_file):
        try:
            version_stream = open(version_file, "r+")
            can_write = True
        except PermissionError:
            version_stream = open(version_file, "r")
            can_write = False
        with version_stream:
            this_version = version_stream.read().strip()

            try:
                from packaging.version import parse as parse_version
            except ImportError:
                # optional dev dependencies are not installed
                return this_version


            # normalize the version string
            try:
                this_v = parse_version(this_version)
            except BaseException as exc:
                warn(UserWarning(exc), stacklevel=2)
                return this_version
            else:
                this_version = str(this_v)

            # ensure the version file is up to date
            project_file = os.path.abspath(os.path.join(this_dir, "..", "..", "pyproject.toml"))
            if os.path.exists(project_file) and can_write:

                try:
                    project_stream = open(project_file)
                except BaseException:
                    warn(UserWarning(exc), stacklevel=2)
                    return this_version

                with project_stream:

                    st_proj = os.stat(project_stream.fileno())
                    st_vers = os.stat(version_stream.fileno())

                    if st_proj.st_mtime <= st_vers.st_mtime:
                        return this_version

                    project_version = this_version
                    for line in project_stream.readlines():
                        try:
                            first, *rest = shlex.split(line)
                        except ValueError:
                            continue
                        if rest and first == "version":
                            try:
                                _, project_version = rest
                                break
                            except ValueError:
                                warn(UserWarning("Unreadable version entry in project file", line, project_file),
                                    stacklevel=2)
                                return this_version

                    # normalize the project version string
                    try:
                        project_v = parse_version(project_version)
                    except BaseException as exc:
                        warn(UserWarning(exc), stacklevel=2)
                        return this_version
                    else:
                        project_version = str(project_v)

                    if project_v > this_v:
                        warn(UserWarning("Updating project version file (orig, new)", this_version, project_version),
                            stacklevel=2),
                        try:
                            version_stream.seek(0)
                            version_stream.write(project_version)
                            version_stream.write(os.linesep)
                        except BaseException as exc:
                            warn(UserWarning(exc), stacklevel=2)
                    else:
                        try:
                            os.utime(version_stream.fileno(), None)
                        except BaseException as exc:
                            warn(UserWarning(exc), stacklevel=2)

                    return str(project_v)

            # no update
            return this_version
    else:
        warn(UserWarning("Version file not found", version_file), stacklevel=2)
        return "0.0.0"


VERSION: str = read_version()
