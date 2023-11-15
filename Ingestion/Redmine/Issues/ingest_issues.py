from Functions import ingest_functions, export_functions

raw_issues = ingest_functions.iterative_get_rest_api(
    "issues", "https://redmine.generalsoftwareinc.com/issues.json?status_id=closed,"
)

export_functions.to_json(raw_issues, "raw_issues.json")

# export_functions.to_json_s3(
#     raw_issues,
#     "bucketfor008182637297",
#     "students/camilo/redmine/projects/raw_data/raw_projects.json",
# )
