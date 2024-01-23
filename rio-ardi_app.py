# rio-ardi_app.py

class CartItem:
    def __init__(self, name, harga):
        self.name = name
        self.harga = harga

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, harga):
        item = CartItem(name, harga)
        self.items.append(item)
        print(f'Barang "{name}" berhasil dimasukkan ke keranjang.')

    def remove_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f'Barang "{name}" berhasil dihapus dari keranjang belanja.')
                return
        print(f'Barang "{name}" tidak ditemukan di keranjang belanja.')

    def display_items(self):
        print('Barang di Keranjang:')
        for i, item in enumerate(self.items):
            print(f'{i}. {item.name} - Rp {item.harga:.2f}')

    def calculate_total(self):
        total = sum(item.harga for item in self.items)
        return total

if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    
    print(" Selamat Datang di Keranjang Belanja Toko Makmur !")

    while True:
        print("Menu:")
        print("1. Menambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang di Keranjang")
        print("4. Lihat Total Belanja")
        print("5. Exit")

        pilihan = input("Pilihan: ")

        if pilihan == '1':
            name = input("Masukkan nama barang: ")
            harga = float(input("Masukkan harga: "))
            shopping_cart.add_item(name, harga)

        elif pilihan == '2':
            name_to_remove = input("Masukkan nama barang yang ingin dihapus: ")
            shopping_cart.remove_item(name_to_remove)

        elif pilihan == '3':
            shopping_cart.display_items()

        elif pilihan == '4':
            total = shopping_cart.calculate_total()
            print(f'Total belanja: Rp {total:.2f}')

        elif pilihan == '5':
            print("Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur.")
            break

        else:
            print("Pilihannya salah. Coba lagi.\n")


import unittest

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart()

    def test_add_item(self):
        self.shopping_cart.add_item(" ")
        self.assertEqual(len(self.shopping_cart.items))

    def test_remove_item(self):
        self.shopping_cart.add_item(" ")
        self.shopping_cart.remove_item(" ")
        self.assertEqual(len(self.shopping_cart.items))

    def test_display_items(self):
        self.shopping_cart.add_item(" ")
        self.shopping_cart.add_item(" ")
        items_displayed = "Barang di Keranjang: "
        self.assertEqual(self.shopping_cart.display_items(), items_displayed)

    def test_calculate_total(self):
        self.shopping_cart.add_item(" ")
        self.shopping_cart.add_item(" ")
        total = self.shopping_cart.calculate_total()
        self.assertEqual(total)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)



