pilihan="y"
while pilihan=="y":
    print("""
    ==============================
    
    ## daftar Menu Kopi Ilkom ##
 
    ==============================
    1. Ekspresso 
    2. Cappuccino 
    3. Moccacino
    4. vanilla Latte
    5. Hazelnut latte
    ==============================
    """)
    pesan=str(input("masukkan pilihan anda : "))
    if pesan == "1":
        listnama= "Ekspresso"
    elif pesan == "2":
            listnama= "Cappuccino"
    elif pesan == "3":
            listnama= "Moccacino"
    elif pesan == "4":
            listnama= "vanilla Latte"
    elif pesan == "5":
            listnama= "Hazelnut latte"
    
    print("Anda memilih ",listnama)
    pilihan=input("apakah anda ingin order kembali Y/N =")