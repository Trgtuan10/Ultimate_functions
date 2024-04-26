#pip install huggingface_hub
#huggingface-cli login

from huggingface_hub import upload_file

path_to_file = "tazab_crop"
repo_id = "TrgTuan10/Dasha_Taran"  # Thay thế bằng repo ID của bạn trên Hugging Face

upload_file(
    path_or_fileobj=path_to_file,
    path_in_repo="data",
    repo_id=repo_id,
    repo_type="dataset",
)