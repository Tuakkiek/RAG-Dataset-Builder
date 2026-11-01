import json 
from pathlib import Path 

FILE_PATH = Path("../data/mineru/02_giao-trinh/vi/VI_TX_010_Giao trinh xu ly anh/structured_content.json")

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f) 

def main(): 
    data = load_json(FILE_PATH) 

    total_pages = len(data["pages"])
    total_blocks = 0 

    block_counts = {} 

    for page in data["pages"]: 
        blocks = page.get("blocks", []) 

        total_blocks += len(blocks) 

        for block in blocks: 
            block_type = block.get("type", "unknown") 

            if block_type not in block_counts: 
                block_counts[block_type] = 0 

            block_counts[block_type] += 1

    print(f"Total pages: {total_pages}")
    print(f"Total blocks: {total_blocks}")

    print("\nBlock types: ")

    for block_type, count in block_counts.items(): 
        print(f"{block_type}: {count}")

if __name__ == "__main__":
    main()