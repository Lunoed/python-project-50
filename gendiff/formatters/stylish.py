def stringify(value, level) -> str:
    if isinstance(value, dict):
        lines = ["{"]
        innner_indent = "    " * (level + 1)
        for key in sorted(value.keys()):
            v = stringify(value[key], level + 1)
            lines.append(f"{innner_indent}{key}: {v}")
        lines.append(f"{'    ' * level}}}")
        return "\n".join(lines)
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    return str(value)


def render(diff, level) -> list:
    lines = []
    indent = "    " * level
    sign_indent = "    " * (level - 1) + "  "
    for key in sorted(diff.keys()):
        node = diff[key]
        status = node["status"]

        if status == "nested":
            lines.append(f"{indent}{key}: {{")
            lines.extend(render(node["children"], level + 1))
            lines.append(f"{indent}}}")
        elif status == "unchanged":
            val = stringify(node["value"], level)
            lines.append(f"{indent}{key}: {val}")
        elif status == "added":
            val = stringify(node["value"], level)
            lines.append(f"{sign_indent}+ {key}: {val}")
        elif status == "removed":
            val = stringify(node["value"], level)
            lines.append(f"{sign_indent}- {key}: {val}")
        elif status == "changed":
            old = stringify(node["old_value"], level)
            new = stringify(node["new_value"], level)
            lines.append(f"{sign_indent}- {key}: {old}")
            lines.append(f"{sign_indent}+ {key}: {new}")
    return lines


def format_stylish(diff: dict) -> str:
    lines = ["{"]
    lines.extend(render(diff, 1))
    lines.append("}")
    return "\n".join(lines)
