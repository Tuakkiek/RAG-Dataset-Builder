import re 
from pathlib import Path 
from transformers import AutoTokenizer

FILE_PATH = Path("../data/mineru/02_giao-trinh/vi/VI_TX_011_Machine Learning co ban/VI_TX_011_Machine Learning co ban.md")

TOKENIZER_NAME = "Qwen/Qwen3-Embedding-0.6B"

MAX_TOKENS = 512

DOC_ID = "VI_TX_011"

DOCUMENT_TITLE = "Machine Learning co ban"

def load_text(
    file_path
): 
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

def split_long_text_by_tokens(
    text, 
    tokenizer,
    max_tokens
): 
    token_ids = tokenizer.encode(
        text,
        add_special_tokens=False
    )

    chunks = [] 

    for start in range(
        0, 
        len(token_ids), 
        max_tokens
    ): 
        end = start + max_tokens

        chunk_ids = token_ids[start:end]

        chunk_text = tokenizer.decode(
            chunk_ids, 
            skip_special_tokens=True
        )

        chunks.append(chunk_text)

    return chunks

def split_by_sentences(
    text, 
    tokenizer, 
    max_tokens
): 
    sentences = re.split(
        r'(?<=[.!?])\s+',
        text
    )

    chunks = [] 
    current_chunk = [] 

    for sentence in sentences: 
        
        sentence = sentence.strip() 

        if not sentence: 
            continue 

        sentence_tokens = count_tokens(
            sentence, 
            tokenizer
        )

        if sentence_tokens > max_tokens: 
            if current_chunk:
                chunks.append(
                    " ".join(
                        current_chunk
                    )
                )

                current_chunk = [] 

            token_chunks = split_long_text_by_tokens(
                sentence, 
                tokenizer, 
                max_tokens
            )

            chunks.extend(
                token_chunks
            )

            continue


        candidate = current_chunk + [sentence]

        candidate_text = " ".join(candidate)

        candidate_tokens = count_tokens(
            candidate_text, 
            tokenizer
        )

        if candidate_tokens <= max_tokens: 
            current_chunk.append(
                sentence
            )

        else: 
            if current_chunk: 
                chunks.append(
                    " ".join(
                        current_chunk
                    )
                )
            
            current_chunk = [sentence]

    if current_chunk: 
        chunks.append(
            " ".join(
                current_chunk
            )
        )    

    return chunks

def split_by_paragraphs(
    text, 
    tokenizer, 
    max_tokens
): 
    paragraphs = text.split(
        "\n\n"
    )

    chunks = []
    current_chunk = [] 

    for paragraph in paragraphs: 
        
        paragraph = paragraph.strip()
        
        if not paragraph: 
            continue 

        paragraph_tokens = count_tokens(
            paragraph, 
            tokenizer
        )

        if paragraph_tokens > max_tokens: 
            
            if current_chunk: 
                chunks.append(
                    "\n\n".join(
                        current_chunk
                    )
                )

                current_chunk = []

            sentence_chunks = (
                split_by_sentences(
                    paragraph, 
                    tokenizer, 
                    max_tokens
                )
            )

            chunks.extend(
                sentence_chunks
            )

            continue

        candidate = (
            current_chunk
            + [paragraph]
        )

        candidate_text = "\n\n".join(
            candidate
        )

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
                chunks.append(
                    "\n\n".join(
                        current_chunk
                    )
                )
            
            current_chunk = [
                paragraph
            ]

    if current_chunk: 
        chunks.append(
            "\n\n".join(
                current_chunk
            )
        )
    
    return chunks

def make_chunk(
    chunk_id, 
    doc_id, 
    document_title, 
    text, 
    token_count
): 
    return {
        "chunk_id": chunk_id,
        "doc_id": doc_id, 
        "document_title": document_title, 
        "text": text, 
        "token_count": token_count
    }

def build_chunk_dataset(
    text_chunks, 
    tokenizer,
    doc_id, 
    document_title, 
): 
    dataset = [] 

    for index, text_chunk in enumerate(
        text_chunks,
        start = 1
    ): 
        chunk_id = (
            f"{doc_id}_C{index:04d}"
        )

        token_count = count_tokens(
            text_chunk, 
            tokenizer
        )

        chunk = make_chunk(
            chunk_id, 
            doc_id,
            document_title, 
            text_chunk,
            token_count
        )

        dataset.append(chunk)

    return dataset

def print_first_chunks(
    dataset, 
    n=3
):
    for chunk in dataset[:n]:
        
        print(
            "\n"
            + "=" * 80
        )

        print(
            "Chunk ID:", chunk["chunk_id"]
        )

        print(
            "Document ID:", chunk["doc_id"]
        )

        print(
            "Document title:", chunk["document_title"]
        )

        print(
            "Token count:", chunk["token_count"]
        )

        print(
            "=" * 80
        )

        print(chunk["text"])

def main(): 
    if not FILE_PATH.exists():
        print("File not found")
        print(FILE_PATH)
        return

    print("Loading tokenizer...")
    
    tokenizer = AutoTokenizer.from_pretrained(
        TOKENIZER_NAME
    )

    text = load_text(
        FILE_PATH
    )

    text_chunks = split_by_paragraphs(
        text, 
        tokenizer,
        MAX_TOKENS
    )

    dataset = build_chunk_dataset(
        text_chunks, 
        tokenizer, 
        DOC_ID, 
        DOCUMENT_TITLE
    )

    print(
        "Total chunks:", len(dataset)
    )

    print_first_chunks(
        dataset,
        n=3
    )

if __name__ == "__main__": 
    main()