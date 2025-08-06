# from huggingface_hub import hf_hub_download
# import os

# # Directory where files will be saved
# SAVE_DIR = "./data"
# os.makedirs(SAVE_DIR, exist_ok=True)

# # Corrected filenames including subfolder for test split
# files_to_download = [
#     ("bespokelabs/bespoke-manim", "train-00000-of-00001.parquet"),
# ]

# for repo_id, filename in files_to_download:
#     print(f"Downloading {filename} from {repo_id}...")
#     try:
#         hf_hub_download(
#             repo_id=repo_id,
#             filename=filename,
#             repo_type="dataset",
#             local_dir=SAVE_DIR
#         )
#         print(f"✅ Downloaded {filename}")
#     except Exception as e:
#         print(f"❌ Failed to download {filename} from {repo_id}")
#         print(e)

# print(f"\n📁 All files (that succeeded) are saved in: {SAVE_DIR}/")


from huggingface_hub import hf_hub_download, list_repo_files
from datasets import load_dataset
import os
import pandas as pd

# Directory where files will be saved
SAVE_DIR = "./data"
os.makedirs(SAVE_DIR, exist_ok=True)

def download_bespoke_manim_dataset():
    """Download the Bespoke-Manim dataset using the datasets library"""
    
    print("🔄 Loading Bespoke-Manim dataset...")
    
    try:
        # Method 1: Use datasets library (recommended for HF datasets)
        print("📥 Downloading using datasets library...")
        dataset = load_dataset("bespokelabs/bespoke-manim", split="train")
        
        # Save as parquet file
        output_file = os.path.join(SAVE_DIR, "bespoke-manim-train.parquet")
        dataset.to_parquet(output_file)
        print(f"✅ Dataset saved to: {output_file}")
        print(f"📊 Dataset info: {len(dataset)} rows, {len(dataset.column_names)} columns")
        print(f"📋 Columns: {dataset.column_names}")
        
        # Also save as CSV for easier viewing
        csv_file = os.path.join(SAVE_DIR, "bespoke-manim-train.csv")
        dataset.to_csv(csv_file)
        print(f"✅ Dataset also saved as CSV: {csv_file}")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to download using datasets library: {str(e)}")
        
        # Method 2: Try to list files and download manually
        print("\n🔄 Trying to list repository files...")
        try:
            files = list_repo_files("bespokelabs/bespoke-manim", repo_type="dataset")
            print("📋 Available files in repository:")
            for file in files:
                print(f"  📄 {file}")
            
            # Try to download parquet files
            parquet_files = [f for f in files if f.endswith('.parquet')]
            
            if parquet_files:
                print(f"\n📥 Found {len(parquet_files)} parquet files, downloading...")
                for file in parquet_files:
                    try:
                        print(f"Downloading {file}...")
                        local_path = hf_hub_download(
                            repo_id="bespokelabs/bespoke-manim",
                            filename=file,
                            repo_type="dataset",
                            local_dir=SAVE_DIR
                        )
                        print(f"✅ Downloaded: {local_path}")
                    except Exception as download_error:
                        print(f"❌ Failed to download {file}: {str(download_error)}")
            else:
                print("❌ No parquet files found in repository")
                
        except Exception as list_error:
            print(f"❌ Failed to list repository files: {str(list_error)}")
            
        return False

# Run the download
success = download_bespoke_manim_dataset()

if success:
    print(f"\n🎉 Download completed successfully!")
else:
    print(f"\n💡 If download failed, you can try accessing the dataset directly at:")
    print(f"   https://huggingface.co/datasets/bespokelabs/bespoke-manim")
    print(f"   Or use the dataset viewer: https://huggingface.co/datasets/bespokelabs/bespoke-manim/viewer/default/train")

print(f"\n📁 Check your files in: {SAVE_DIR}/")

# List what was actually downloaded
print("\n📋 Files in download directory:")
for root, dirs, files in os.walk(SAVE_DIR):
    for file in files:
        file_path = os.path.join(root, file)
        relative_path = os.path.relpath(file_path, SAVE_DIR)
        file_size = os.path.getsize(file_path)
        print(f"  📄 {relative_path} ({file_size:,} bytes)")
        
        # If it's a parquet file, show some info about it
        if file.endswith('.parquet'):
            try:
                df = pd.read_parquet(file_path)
                print(f"      📊 {len(df)} rows, {len(df.columns)} columns")
            except Exception as e:
                print(f"      ❌ Could not read parquet file: {str(e)}")