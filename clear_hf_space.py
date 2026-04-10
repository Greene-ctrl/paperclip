import os
from huggingface_hub import HfApi

token = os.environ.get("HF_TOKEN")
api = HfApi(token=token)

repo_id = "Leon4gr45/openagenticresearch"
repo_type = "space"

files = api.list_repo_files(repo_id=repo_id, repo_type=repo_type)
for f in files:
    if f != ".gitattributes":
        print(f"Deleting {f}...")
        try:
            api.delete_file(path_in_repo=f, repo_id=repo_id, repo_type=repo_type)
        except Exception as e:
            print(f"Failed to delete {f}: {e}")

print("Done clearing repo.")
