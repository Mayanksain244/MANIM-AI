from huggingface_hub import login , snapshot_download
import os
import shutil
from dotenv import load_env
load_env()

login(token="HUGGING_FACE_TOKEN")

def download_model_to_structure(model_id: str, save_root="./models"):
    # Convert model_id like "ProsusAI/finbert" → "ProsusAI--finbert"
    model_folder_name = model_id.replace("/", "--")
    
    # Define target path like ./models/ProsusAI--finbert/original
    original_path = os.path.join(save_root, model_folder_name, "original")
    os.makedirs(original_path, exist_ok=True)

    # Download the model to a temporary path
    temp_path = snapshot_download(
        repo_id=model_id,
        repo_type="model",
        local_dir="./.tmp_model_download",  # temp folder
        local_dir_use_symlinks=False
    )

    # Copy contents to original/ folder
    for item in os.listdir(temp_path):
        s = os.path.join(temp_path, item)
        d = os.path.join(original_path, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    # Clean temp folder
    shutil.rmtree("./.tmp_model_download", ignore_errors=True)

    print(f"✅ Downloaded '{model_id}' to: {original_path}")


# Example usage:
# download_model_to_structure("Qwen/CodeQwen1.5-7B-Chat")
download_model_to_structure("infly/OpenCoder-8B-Instruct")
download_model_to_structure("NTQAI/Nxcode-CQ-7B-orpo")
