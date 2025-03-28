def read_file(file_path: str) -> str:
    """Read content from a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
    
def process_text(text: str) -> list[tuple[str, int]]:
    """Process text and return top 10 most frequent words."""
    words = text.lower().split()
    words = [''.join(char for char in word if char.isalnum()) for word in words]
    word_count = {}
    for word in words:
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]


def write_results(results: list[tuple[str, int]], output_path: str) -> None:
    """Write results to output file."""
    with open(output_path, 'w', encoding='utf-8') as file:
        for word, count in results:
            file.write(f"{word}-{count}\n")