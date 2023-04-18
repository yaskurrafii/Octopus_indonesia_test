def harga(n, harga_barang):
    res = []
    # make a list of tuple that tuple being (harga, kota)
    harga_per_kota = sorted(list(zip(harga_barang,range(1, n + 1) )))
    print(harga_per_kota)
    for i in range(n):
        harga = harga_barang[i]
        kota = i+1
        if harga >= kota and harga != 1:
            for harga_kota_lain, kota_lain in harga_per_kota:
                if kota > kota_lain:
                    harga_baru = (kota - kota_lain) + harga_kota_lain
                else:
                    harga_baru = (kota_lain - kota) + harga_kota_lain
                if harga_kota_lain >= harga:
                    res.append(harga)
                    break
                else:
                    harga = harga_baru
        else:
            res.append(harga)
    print(res)

h = [1, 4, 2, 4]
n = 4
harga(n, h)