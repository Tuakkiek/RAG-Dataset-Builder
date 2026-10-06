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

# Get all block of a specific type 
def get_block_by_type(pages, target_type): 
    results = [] 

    for page_index, page in enumerate(pages): 
        blocks = page.get("blocks", [])

        for block in blocks: 
            block_type = block.get("type", "unknow")

            if block_type == target_type: 
                results.append(
                    {
                        "page_index": page_index, 
                        "block": block
                    }
                )

    return results

# Show block type statistics by page
def show_block_type_per_page(pages):
    print("\n" + "=" * 80)
    print("BLOCK TYPE PER PAGE")
    print("=" * 80)

    for page_index, page in enumerate(pages): 
        blocks = page.get("blocks", [])

        counts = {} 

        for block in blocks: 
            block_type = block.get("type", "unknow")

            if block_type not in counts: 
                counts[block_type] = 0

            counts[block_type] += 1

        print(f"Page {page_index}")

        for block_type, count in counts.items():
            print(
                f"- {block_type}: {count}"
            )

def main():

    if not FILE_PATH.exists():
        print("Không tìm thấy file:")
        print(FILE_PATH)
        return

    data = load_json(FILE_PATH)

    print("Type of data:")
    print(type(data))

    print("\nNumber of data keys:")
    print(len(data))

    print("\nKeys:")
    print(data.keys())

    pages = data.get("pages", [])

    print("\nType of pages:")
    print(type(pages))

    print("\nTotal number of pages:")
    print(len(pages))

    total_blocks = count_total_blocks(pages)
    print(f"\nTotal block: {total_blocks}")

    block_count = count_block_types(pages)
    print("\nBlock types:")
    for block_type, count in block_count.items(): 
        print(f"{block_type}:   {count}")

    show_blocks_per_page(pages)

    max_blocks, max_page = find_page_with_most_blocks(pages)

    print("\nPage with most blocks:")
    print(f"Page: {max_page}")
    print(f"Blocks: {max_blocks}")

    show_block_type_per_page(pages)


if __name__ == "__main__":
    main()