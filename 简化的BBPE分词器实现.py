class DeepSeekTokenizer:
    def __init__(self, vocab_path, merges_path):
        self.vocab = self._load_vocab(vocab_path)
        self.merges = self._load_merges(merges_path)
        self.byte_encoder = self._bytes_to_unicode()

    def _bytes_to_unicode(self):
        """将字节映射到Unicode字符"""
        bs = list(range(ord('!'), ord('~') + 1)) + \
             list(range(ord('¡'), ord('¬') + 1)) + \
             list(range(ord('®'), ord('ÿ') + 1))
        cs = bs[:]
        n = 0
        for b in range(2 ** 8):
            if b not in bs:
                bs.append(b)
                cs.append(2 ** 8 + n)
                n += 1
        return dict(zip(bs, [chr(c) for c in cs]))

    def encode(self, text):
        """将文本编码为token IDs"""
        # 1. 将文本转为字节
        bpe_tokens = [self.byte_encoder[b] for b in text.encode('utf-8')]

        # 2. 应用BPE合并规则
        while len(bpe_tokens) > 1:
            pairs = self._get_pairs(bpe_tokens)
            min_pair = min(pairs, key=lambda p: self.merges.get(p, float('inf')))
            if min_pair not in self.merges:
                break
            bpe_tokens = self._merge(bpe_tokens, min_pair)

        # 3. 映射到词汇表ID
        return [self.vocab[token] for token in bpe_tokens]

    def decode(self, token_ids):
        """将token IDs解码为文本"""
        tokens = [self.vocab_inv[id] for id in token_ids]
        text = ''.join(tokens)
        # 将Unicode字符转回字节
        return bytearray([self.unicode_to_byte[c] for c in text]).decode('utf-8')