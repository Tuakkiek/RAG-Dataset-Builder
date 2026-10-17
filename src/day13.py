import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = (
    BASE_DIR
    / "data"
    / "mineru"
    / "02_giao-trinh"
    / "vi"
    / "VI_TX_010_Machine Learning co ban"
    / "structured_content.json"
)

OUTPUT_PATH = BASE_DIR / "data" / "processed" / "day13.json"

HEADING_TYPES = {
    "doc_title",
    "paragraph_title",
}

NUMBERED_HEADING_RE = re.compile(
    r"^\s*(\d+(?:\.\d+)*)(?:\.|\s)+"
)

MAX_HEADING_LEVEL = 4


def load_data(input_path):
    with open(input_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_text(data):
    texts = []
    for page in data.get("pages", []):
        for block in page.get("blocks", []):
            content = block.get("content", "")
            if isinstance(content, str) and content.strip():
                texts.append(content)
    return texts


def get_heading_level(block):
    block_type = block.get("type", "")
    title = str(block.get("content", "")).strip()
    
    if title == "doc_title" or block_type == "doc_title":
        return 1
        
    # Ví dụ: Chương 1..., Phần I...
    if re.match(r"^\s*(chương|phần)\b", title, re.IGNORECASE):
        return 1
        
    match = NUMBERED_HEADING_RE.match(title)
    if match:
        number = match.group(1)
        level = len(number.split("."))
        return min(level, MAX_HEADING_LEVEL)
        
    raw_level = block.get("level")
    if isinstance(raw_level, int) and not isinstance(raw_level, bool):
        return max(1, min(raw_level, MAX_HEADING_LEVEL))
        
    return 2


def update_heading_stack(stack, title, level):
    title = title.strip()
    if not title:
        return stack
    
    level = max(1, min(int(level), MAX_HEADING_LEVEL))
    
    while stack and stack[-1]["level"] >= level:
        stack.pop()
        
    stack.append({
        "level": level,
        "title": title,
    })
    return stack


def build_heading_hierarchy(data):
    records = []
    heading_stack = []
    
    for page in data.get("pages", []):
        page_idx = page.get("page_idx")
        for block_idx, block in enumerate(page.get("blocks", [])):
            block_type = block.get("type", "")
            content = block.get("content", "")
            
            if not isinstance(content, str):
                content = ""
                
            title = content.strip()
            is_heading = (
                block_type in HEADING_TYPES
                and bool(title)
                and title.casefold() != "mục lục"
            )
            
            heading_level = None
            if is_heading:
                heading_level = get_heading_level(block)
                update_heading_stack(
                    heading_stack,
                    title,
                    heading_level,
                )
                
            # Ép kiểu sang list để dữ liệu tường minh và dễ lưu JSON
            section_path = [
                item["title"]
                for item in heading_stack
            ]
            
            record = {
                "page_idx": page_idx,
                "source_index": block_idx,
                "type": block_type,
                "content": block.get("content", ""),
                "section_path": section_path,
            }
            
            if is_heading:
                record["heading_level"] = heading_level
                
            records.append(record)
            
    return records


def print_heading_hierarchy(records):
    print("=" * 80)
    print("HEADING HIERARCHY")
    print("=" * 80)
    
    heading_count = 0 

    for record in records:
        if "heading_level" not in record:
            continue
            
        level = record["heading_level"]
        title = record["content"]
        page_idx = record["page_idx"]  
        
        indent = "    " * (level - 1)
        print(f"{indent}H{level}: {title} [page_idx={page_idx}]")
        heading_count += 1
        
    print("=" * 80)
    print(f"Total number of headings: {heading_count}")


def save_data(data, output_path): 
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )


def main():
    if not INPUT_PATH.exists():
        print(f"File not found: {INPUT_PATH}")
        return
        
    data = load_data(INPUT_PATH)
    records = build_heading_hierarchy(data)

    print(f"Total number of pages: {len(data['pages'])}")
    print(f"Total number of blocks: {len(records)}")
    
    print_heading_hierarchy(records)
    save_data(records, OUTPUT_PATH)
    print(f"Result saved at: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()