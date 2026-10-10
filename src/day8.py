from pathlib import Path 
from transformers import AutoTokenizer


FILE_PATH = Path("../data/mineru/02_giao-trinh/vi/VI_TX_011_Machine Learning co ban/VI_TX_011_Machine Learning co ban.md")

TOKENIZER_NAME = "Qwen/Qwen3-Embedding-0.6B"

MAX_TOKENS = 512


def load_text(file_path): 
    with open(file_path, "r", encoding="utf-8") as f: 
        return f.read()

def count_tokens(
    text, 
    tokenizer
): 
    token_ids = tokenizer.encode(
        text,
        add_special_tokens=False
    )

    return len(token_ids)

def split_by_paragraphs(
    text,
    tokenizer, 
    max_tokens
): 
    paragraphs = text.split("\n\n")

    chunks = [] 
    current_chunk = [] 

    for paragraph in paragraphs: 
        
        paragraph = paragraph.strip() 

        if not paragraph: 
            continue
        
        candidate = (
            current_chunk + [paragraph]
        )

        candidate_text = "\n\n".join(candidate)

        candidate_tokens = count_tokens(
            candidate_text, 
            tokenizer
        )

        if candidate_tokens <= max_tokens: 
            current_chunk.append(
                paragraph
            )
        else: 
            if current_chunk: 
                chunk_text = "\n\n".join(
                    current_chunk
                )

                chunks.append(chunk_text)

                current_chunk = [paragraph]

    if current_chunk:
        
        chunk_text = "\n\n".join(current_chunk)

        chunks.append(chunk_text)

    return chunks

def show_chunk_stats(
    chunks, 
    tokenizer
):  
    if not chunks: 
        print("There are no chunks at all")
        return 
    
    token_counts = [] 

    for chunk in chunks: 
        
        count = count_tokens(
            chunk, 
            tokenizer
        )

        token_counts.append(count)

    average = (
        sum(token_counts) / len(token_counts)
    )

    print("\nChunk statistics")
    print("=" * 80)

    print("Number of chunks: ", len(chunks))

    print("Min token: ", min(token_counts))

    print("Max token: ", max(token_counts))

    print("Avegare tokens: ", round(average, 2))

def print_first_chunk(
    chunks, 
    tokenizer, 
    n=3
): 
    for index, chunk in enumerate(chunks[:n], start=1): 
        
        print("\n" + "=" * 80)

        print(
            f"CHUNK_{index:04d}"
        )

        print("=" * 80)

        print(
            "Token count: ", count_tokens(
                chunk, 
                tokenizer
            )
        )

        print() 

        print(chunk)


def main(): 
    if not FILE_PATH.exists(): 
        print("File not found")
        print(FILE_PATH)
        return 

    print("Loading tokenizer...")

    tokenizer = (
        AutoTokenizer.from_pretrained(
            TOKENIZER_NAME
        )
    )

    text = load_text(
        FILE_PATH
    )

    print("Total tokens: ", count_tokens(text, tokenizer))

    print("Max token per chunk: ", MAX_TOKENS)

    chunks = split_by_paragraphs(
        text, 
        tokenizer, 
        MAX_TOKENS
    )

    show_chunk_stats(
        chunks, 
        tokenizer
    )

    print_first_chunk(
        chunks,
        tokenizer, 
        n=3
    )

if __name__ == "__main__": 
    main()