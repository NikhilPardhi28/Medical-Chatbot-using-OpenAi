import yaml

# 🔥 Use the full path directly
cfg_path = r"C:\Users\VIDARBHA ZO\Desktop\arogyabot\configs\config.yaml"
print(f"Looking for config at: {cfg_path}")

with open(cfg_path, "r", encoding="utf-8") as f:
    raw = f.read()

print("\n--- RAW FILE CONTENTS ---")
print(raw)
print("-------------------------\n")

cfg = yaml.safe_load(raw)

if cfg:
    print("✅ YAML Parsed Successfully!")
    print(cfg)
else:
    print("❌ YAML is empty or invalid")
