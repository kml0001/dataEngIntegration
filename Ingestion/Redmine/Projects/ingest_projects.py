from Functions import ingest_functions, export_functions

raw_projects = ingest_functions.iterative_get_rest_api_admin_net(
    "projects", "https://redmine.generalsoftwareinc.net/projects.json?"
)

export_functions.to_json(raw_projects, "raw_projects.json")

# export_functions.to_json_s3(
#     raw_projects,
#     "bucketfor008182637297",
#     "redmine/projects/raw_data/raw_projects.json",
# )
