import json
import pathlib
import re
from collections import defaultdict


HERE = pathlib.Path(".")


def find_robot_variables(project_root: pathlib.Path) -> dict[str, set[str]]:
    robot_files = project_root.rglob("*.robot")
    resource_files = project_root.rglob("*.resource")
    files_to_process = [*robot_files, *resource_files]

    robot_variables = defaultdict(set)

    variable_matcher = re.compile("([$@&%]{(.*?)})")

    for file_path in files_to_process:
        with open(file=file_path, mode="r", encoding="utf-8") as f:
            file_content = f.readlines()

            for line in file_content:
                matches = variable_matcher.findall(line)
                for match in matches:
                    squished_name = match[1].lower()
                    squished_name = "".join(squished_name.split())
                    squished_name = squished_name.replace("_", "")
                    robot_variables[squished_name].add(match[1])

    return robot_variables


robot_variables = find_robot_variables(HERE)

multiples = {k: list(v) for k, v in robot_variables.items() if len(v) > 1}

print(json.dumps(multiples, sort_keys=True, indent=4, separators=(",", ": ")))
