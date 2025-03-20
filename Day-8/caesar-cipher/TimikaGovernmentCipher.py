class TimikaGovernmentCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr((ord(char) - shift_base + self.shift) % 26 + shift_base)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        return self.encrypt(ciphertext, -self.shift)

    def display_encrypted_data(self, data):
        encrypted_data = self.encrypt(data)
        print(f"Encrypted Data: {encrypted_data}")

    def display_decrypted_data(self, data):
        decrypted_data = self.decrypt(data)
        print(f"Decrypted Data: {decrypted_data}")


if __name__ == "__main__":
    shift_value = 4
    cipher = TimikaGovernmentCipher(shift_value)

    document = "Laporan Kegiatan Pemerintah Kabupaten Timika"
    cipher.display_encrypted_data(document)

    encrypted_document = cipher.encrypt(document)
    cipher.display_decrypted_data(encrypted_document)
