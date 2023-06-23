meme_dict = { 
    "LOL" : "Tertawa terbahak - bahak / ngakak" , 
    "CMIIW" : "Correct e if I'm wrong" , 
    "OTW" : "Lagi di jalan" , 
    "ATM" : "At the moment",
}

for i in range(3):
    word = input("Masukkan sebuah singkatan yang anda tidak mengerti dengan huruf kapital semua")



    if word in meme_dict.keys() : 
        print(meme_dict[word])
    
    else : 
        print("Singkatan tidak tersedia di dalam kamus.")
