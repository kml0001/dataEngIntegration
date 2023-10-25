from Functions import export_functions, import_functions


def flatten_project(projects):
    flattened_data = []
    for project in projects:
        flattened_project = project.copy()
        custom_fields = dict(project).get("custom_fields")
        parent = dict(project).get("parent")
        if parent is not None:
            project.pop("parent")

        # procesamiento del custom_field
        if custom_fields:
            project.pop("custom_fields")
            for field in custom_fields:
                flattened_project["custom_fields_id"] = field["id"]
                flattened_project["custom_fields_name"] = field["name"]
                flattened_project["custom_fields_value"] = field["value"]

        # procesamiento del parent
        if parent is not None:
            flattened_project["parent_id"] = dict(parent).get("id")
            flattened_project["parent_name"] = dict(parent).get("name")
        else:
            flattened_project["parent_id"] = -1
            flattened_project["parent_name"] = ""
        flattened_data.append(flattened_project)

    return flattened_data


# raw_projects = import_functions.from_json("raw_projects.json")

raw_projects = import_functions.from_json_s3(
    "bucketfor008182637297", "redmine/projects/raw_data/raw_projects.json"
)

flattened_projects = flatten_project(raw_projects)

# export_functions.to_json(flattened_projects, "flattened_projects.json")

export_functions.to_json_s3(
    flattened_projects,
    "bucketfor008182637297",
    "redmine/projects/raw_data/raw_projects.json",
)
