Import("env")


def skip_asm_from_build(node):
    """
    `node.name` - a name of File System Node
    `node.get_path()` - a relative path
    `node.get_abspath()` - an absolute path

     to ignore file from a build process, just return None
    """
    if "WireGuard-ESP32/crypto/cortex" in node.get_path():
        print(f"Exclude {node.get_path()}")
        return None

    return node


env.AddBuildMiddleware(skip_asm_from_build, "*")
