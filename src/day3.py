import json
from pathlib import Path


FILE_PATH = Path("../data/mineru/02_giao-trinh/vi/VI_TX_010_Giao trinh xu ly anh/structured_content.json")


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Count the number of each type of block 
def count_block_types(pages): 
    block_counts ={} 

    for page in pages: 
        blocks = page.get("blocks", [])

        for block in blocks: 
            block_type = block.get("type", "unknown")

            if block_type not in block_counts: 
                block_counts[block_type] = 0

            block_counts[block_type] += 1
    
    return block_counts

def main():
    data = load_json(FILE_PATH)

    pages = data.get("pages", [])

    block_counts = count_block_types(pages)
    print(block_counts)

if __name__ == "__main__":
    main()