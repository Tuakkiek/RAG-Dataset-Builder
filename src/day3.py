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

# Count the total number of blocks
def count_total_blocks(pages): 
    total_blocks = 0

    for page in pages: 
        blocks = page.get("blocks", []) 
        total_blocks += len(blocks) 

    return total_blocks

# Display the number of blocks for each page
def show_blocks_per_page(pages): 
    print("\n" + "=" * 80)
    print("Blocks per page:")
    print("=" * 80)

    for page_index, page in enumerate(pages): 
        blocks = page.get("blocks", [])

        print(
            f"Page {page_index}:", 
            f"{len(blocks)} blocks"
        )

# Find the page with the most blocks 
def find_page_with_most_blocks(pages): 
    max_blocks = 0 
    max_page = None 

    for page_index,page in enumerate(pages):
        blocks = page.get("blocks", [])

        current_count = len(blocks)

        if current_count > max_blocks: 
            max_blocks = current_count
            max_page = page_index

    return max_blocks, max_page 

def main():
    data = load_json(FILE_PATH)

    pages = data.get("pages", [])

    print(find_page_with_most_blocks(pages))

if __name__ == "__main__":
    main()