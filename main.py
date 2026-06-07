meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROLF": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidak setujuan",
            "CREEPY": "menakutkan, tidak menyenangkan"}
print(meme_dict)
for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        yesno= input('kata tidak ditemukan, mau menambahkannya?(yes/no)')
        if yesno == 'yes':
            kunci = input('Tambahkan kunci baru yang tidak ditemukan :')
            nilai = input('Tambahkan nilai kunci')
            meme_dict[kunci] = nilai
            print(meme_dict)
        else:
            print(' ')
