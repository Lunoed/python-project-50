def stringify(value):
    if isinstance(value, dict):
        return "[complex value]"
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    return f"'{str(value)}'" if isinstance(value, str) else str(value)


def render(diff, path=""):
    diff_raws = []
    for key in sorted(diff.keys()):
        node = diff[key]
        status = node["status"]
        new_path = f"{path}.{key}" if path else str(key)
        if status == "removed":
            raw = f"Property '{new_path}' was {status}"
            diff_raws.append(raw)
        elif status == "added":
            value = stringify(node["value"])
            raw = f"Property '{new_path}' was {status} with value: {value}"
            diff_raws.append(raw)
        elif status == "changed":
            old = stringify(node["old_value"])
            new = stringify(node["new_value"])
            raw = f"Property '{new_path}' was updated. From {old} to {new}"
            diff_raws.append(raw)
        elif status == "nested":
            diff_raws.extend(render(node["children"], new_path))
        else:
            pass
    return diff_raws


def format_plain(diff: dict) -> str:
    lines = render(diff)
    return "\n".join(lines)
