import os
from huggingface_hub import HfApi, CommitOperationAdd

token = os.environ.get("HF_TOKEN")
api = HfApi(token=token)

repo_id = "Leon4gr45/openagenticresearch"
repo_type = "space"

print("Uploading files via single commit...")

api.create_commit(
    repo_id=repo_id,
    repo_type=repo_type,
    operations=[
        CommitOperationAdd(
            path_in_repo="Dockerfile",
            path_or_fileobj="docker/huggingface/Dockerfile"
        )
    ],
    commit_message="Fix Dockerfile UID 1000 issue"
)
print("Done.")
