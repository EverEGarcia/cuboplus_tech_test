import hashlib
import time

# Function to verify if a block hash meets the difficulty level
def proof_of_work(previous_hash, difficulty):
    """
    Function to simulate Proof of Work (PoW) verification.
    The goal is to find a hash that starts with a certain number of zeros based on the difficulty level.
    """
    prefix = '0' * difficulty  # Target prefix (leading zeros based on difficulty)
    nonce = 0  # Start with nonce value at 0

    start_time = time.time()  # Start measuring time

    # Keep trying different nonce values until a valid hash is found
    while True:
        block_content = previous_hash + str(nonce)  # Combine previous hash and nonce
        block_hash = hashlib.sha256(block_content.encode()).hexdigest()  # Calculate hash

        # Check if the hash starts with the required number of zeros
        if block_hash.startswith(prefix):
            end_time = time.time()  # Stop measuring time
            return block_hash, nonce, end_time - start_time

        # Increment the nonce for the next attempt
        nonce += 1

# Main function to run the PoW verifier
if __name__ == "__main__":
    previous_hash = "0000000000000000000a8edc2b9f46e6c5aefbbd843a3fe98b207fcebc0bb6f0"  # Example previous hash

    # Set the difficulty level (number of leading zeros)
    difficulty_level = 4  # You can increase this value to test higher difficulty

    print(f"Running Proof of Work with difficulty level: {difficulty_level}")
    valid_hash, valid_nonce, time_taken = proof_of_work(previous_hash, difficulty_level)

    print(f"Valid hash: {valid_hash}")
    print(f"Nonce: {valid_nonce}")
    print(f"Time taken: {time_taken:.2f} seconds")
