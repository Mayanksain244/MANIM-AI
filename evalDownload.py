import evaluate

# Trigger downloads and cache them locally
print("Downloading 'accuracy' metric...")
evaluate.load("accuracy")

print("Downloading 'f1' metric...")
evaluate.load("f1")

print("\n✓ Metrics downloaded and cached successfully.")
