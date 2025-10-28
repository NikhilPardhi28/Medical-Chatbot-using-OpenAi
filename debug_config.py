from pathlib import Path

cfg_path = Path("C:/Users/VIDARBHA ZO/Desktop/arogyabot/configs/config.yaml")

print("🔍 Reading raw config file...")
with open(cfg_path, "rb") as f:  # read in binary
    data = f.read()

print("Raw bytes:", data[:100])  # show first 100 bytes
print("\nAs text:\n")
print(data.decode("utf-8", errors="replace"))
