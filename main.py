import hashlib

class BitCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "A sends 2 BC (BitCoin) to B"
t2 = "C sends 2 BC (BitCoin) to D"
t3 = "E sends 2 BC (BitCoin) to F"
t4 = "G sends 2 BC (BitCoin) to H"
t5 = "I sends 2 BC (BitCoin) to J"
t6 = "K sends 2 BC (BitCoin) to L"

initial_block = BitCoinBlock("Initial String", [t1, t2])
print(initial_block.block_data)
print(initial_block.block_hash+"\n")

second_block = BitCoinBlock(initial_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash+"\n")

third_block = BitCoinBlock(second_block.block_hash, [t5, t6])
print(third_block.block_data)
print(third_block.block_hash+"\n")
