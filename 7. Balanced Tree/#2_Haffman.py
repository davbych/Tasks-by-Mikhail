import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanTree:
    def __init__(self, text):
        self.text = text
        self.root = None
        self.codes = {}

    def build_tree(self):
        if not self.text:
            return

        freq = defaultdict(int)
        for char in self.text:
            freq[char] += 1

        heap = [HuffmanNode(char, freq) for char, freq in freq.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = HuffmanNode(None, left.freq + right.freq, left, right)
            heapq.heappush(heap, merged)

        self.root = heap[0]
        self._generate_codes(self.root, "")

    def _generate_codes(self, node, current_code):
        if node is None:
            return
        if node.char is not None:
            self.codes[node.char] = current_code or "0"
        else:
            self._generate_codes(node.left, current_code + "0")
            self._generate_codes(node.right, current_code + "1")

    def encode(self, text):
        if not self.codes:
            self.build_tree()
        return ''.join(self.codes[char] for char in text)

    def decode(self, encoded_text):
        if self.root is None:
            self.build_tree()
        decoded = []
        node = self.root
        for bit in encoded_text:
            node = node.left if bit == '0' else node.right
            if node.char is not None:
                decoded.append(node.char)
                node = self.root
        return ''.join(decoded)



text = "мама мыла раму"

huffman = HuffmanTree(text)
huffman.build_tree()

print("Таблица кодов Хаффмана:")
for char, code in sorted(huffman.codes.items()):
    print(f"'{char}': {code}")

encoded = huffman.encode(text)
print(f"\nИсходный текст: {text}")
print(f"Закодированный текст: {encoded}")
print(f"Длина закодированного текста: {len(encoded)} бит")

decoded = huffman.decode(encoded)
print(f"Декодированный текст: {decoded}")
print(f"Совпадает с оригиналом: {text == decoded}")
