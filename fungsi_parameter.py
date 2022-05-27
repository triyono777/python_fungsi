def ucapan_selamat(nama):
    print('halo ', nama, " apa kabar?")


# ucapan_selamat('Triyono')


# fungsi positional


def greetings(nama, waktu):
    print('halo', nama, 'selamat', waktu)


# greetings()


# greetings('triyono', 'pagi')
# greetings('pagi', 'triyono')
# greetings(waktu='siang', nama='triyono')

def selamat(waktu="pagi"):
    print('halo, selamat ', waktu)


# data_selamat = selamat('siang')
# print(data_selamat)


def penjumlahan(a, b):
    hasil = a+b
    return hasil


hasil_jumlah = penjumlahan(10, 5)

print(hasil_jumlah)
