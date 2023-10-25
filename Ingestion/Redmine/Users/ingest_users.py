from Functions import ingest_functions, export_functions

raw_users = ingest_functions.iterative_get_rest_api(
    "users", "https://redmine.generalsoftwareinc.net/users.json"
)
export_functions.to_json(raw_users, "raw_users.json")

# export_functions.to_json_s3(
#     raw_users,
#     "bucketfor008182637297",
#     "redmine/users/raw_data/raw_users.json",
# )
