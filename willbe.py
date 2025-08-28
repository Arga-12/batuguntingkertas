import time

yui = """
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣀⣤⡤⣦⣤⡴⣲⣖⠶⡴⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⢻⣻⣝⡮⢷⣳⢮⣗⢯⣞⣻⣽⣶⣛⢿⣲⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⢶⢯⣳⡭⣟⡶⣝⡾⣻⢼⡳⣞⢯⡞⣵⣻⠾⣭⢷⣟⣮⢗⣻⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⣯⢞⡽⣞⢷⣻⡝⣞⣧⢿⣱⢯⣳⢯⣳⢯⣳⡭⣟⣭⢿⣻⢿⣭⣛⣮⢟⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠔⢚⣭⡺⣝⣳⡽⢾⣽⢻⣄⢷⣏⡿⣽⢾⣹⡞⣵⡻⣼⡳⢧⣟⢮⣳⢯⡽⣻⣖⣻⡼⣫⣞⣵⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠀⢠⣴⢻⣖⣻⣭⢷⣻⣟⢮⣟⣼⠜⢤⣿⢯⣳⢧⣟⣳⢿⣱⣿⣻⢼⣫⢗⡯⡾⣽⡞⣵⣏⢷⡞⣵⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠊⠀⠀⢀⣼⢻⡼⣳⡽⣶⣻⢿⣟⢮⣻⠎⠁⠀⢸⡟⣮⢗⡯⣞⠿⣏⡷⣻⣯⡗⣯⢾⣹⡽⣞⣿⢳⡞⣯⢞⣳⡽⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⢀⡼⣇⣿⢣⣟⣿⣟⣻⣿⣜⡿⠃⠀⠀⠀⣿⢻⣇⡿⣻⣼⠃⣟⣧⢟⣧⢿⣣⢟⣧⢻⣿⢟⣧⠿⣜⡿⣣⠿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣻⡼⣣⣿⣛⢾⣼⣿⡷⡞⠀⠀⠀⠀⠀⣾⣏⡾⣵⣛⡎⠀⠹⣞⢯⣻⢾⣱⡟⣮⢟⡼⣿⣺⡝⣯⢞⡽⣛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⢳⣽⣛⣶⣿⣿⣿⣿⡟⠀⠀⣠⣤⡀⠈⡏⣽⡞⣵⣻⠀⠀⠀⠸⣯⡽⣟⡶⣫⢷⣫⢟⣿⣱⢯⣳⢏⡿⣹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢠⡞⣧⣿⣿⣿⣿⣿⣿⡇⢠⡞⢠⣖⢓⠉⠀⠘⡽⣧⢿⠀⠠⠀⠀⢸⣳⣯⢗⣯⣳⣯⠾⣽⣫⣞⡷⢯⣝⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⢀⡁⡆⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠘⠂⣿⣿⡟⠀⠀⠀⠙⣞⣏⢠⢚⣛⡻⣆⠳⣯⡟⡶⣽⣷⡻⣽⣳⡾⣽⢫⡾⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡰⠨⠀⡞⠈⠁⠀⠀⠀⠀⣸⣿⣿⣿⡿⠛⠋⣱⣿⣿⡇⠀⠁⠿⠟⠀⠀⠀⠀⠀⠈⠹⣰⣿⣿⠈⡞⡇⣝⡾⡽⣽⣷⡻⣽⢿⡝⣾⣹⣽⣳⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠄⡄⣤⠙⠀⡆⠀⠀⠀⠀⠉⣼⣿⠟⠁⠀⢰⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⢁⢇⣿⢺⣝⣿⣿⣽⢋⣟⡞⣧⠷⣏⣷⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠨⢁⠂⠀⡀⠁⠀⠀⠀⠀⠀⣻⠏⠀⠀⠀⠀⠻⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠟⠁⢠⣿⡝⣧⣿⣻⠾⠇⢨⣞⡽⣣⣟⡿⢾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⠀⠀⠀⠠⢢⡀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⢸⡟⣽⣷⣄⠀⠀⠀⢠⣀⡀⢀⠀⠀⠀⠀⠀⢀⣴⡿⣿⡾⢿⡼⢃⢃⣴⢻⣜⢷⣻⣼⣟⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠀⠀⣡⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣸⣿⣿⣿⣷⣄⠀⠸⣯⢝⣻⠀⠀⠀⣠⣖⡟⣮⢿⣏⣿⣿⢷⣏⠿⣜⡯⣞⢯⡷⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡁⢁⣼⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣧⡀⠁⠉⠁⠀⣠⡟⣷⢺⣝⣯⣷⣻⣛⣮⢷⣺⣻⡝⡾⣭⢿⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣷⣾⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⠋⢲⠒⢂⣿⢳⣯⡽⠗⣺⢷⣣⢷⣫⣾⣷⣟⣧⠿⠙⠁⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠
⠐⢿⣿⣿⣿⣿⣿⣿⣿⣦⣤⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⠿⢡⣤⣂⠒⠟⠚⠉⠀⢀⡰⣯⣳⣿⣿⣿⣿⣿⣾⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢄⡎⣿⣟
⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠛⢠⣴⢧⡙⡟⡀⠀⠀⠂⢈⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⢀⡠⣠⣦⣾⣻⣿⡇⢸⢻
⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⠟⡎⡄⢃⢸⠰⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡀⣠⣴⡵⣿⣷⡿⣿⣿⣽⢿⣧⠸⡏
⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⠧⢾⣼⠸⠀⢸⠀⣇⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣯⠺⣾⣽⣿⣿⣽⣿⣿⣯⡿⣿⣿⡿⡀⣷
⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠁⠀⡟⢡⣾⣿⠁⡇⡇⡎⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⡏⢲⣯⠉⢨⠀⢸⣿⣿⣽⣿⣿⣽⣿⣿⣽⣿⣿⣷⡟
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⡿⠿⠋⠉⠀⢀⣠⣴⡵⠿⣿⣿⢘⢹⣈⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣯⣷⠟⠙⠀⣼⠋⠀⠇⠀⢰⣿⣿⣷⣻⣿⣷⣿⡷⠿⠛⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠁⠀⠀⠀⠀⡴⣿⠟⢿⣿⣶⡀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣻⠋⣟⣿⣟⠇⠂⠰⡇⠀⢈⠀⠀⢸⣷⣿⠷⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣶⣾⣝⣼⣿⣿⣿⠆⢹⣿⣯⣽⣿⣿⣯⣿⣾⠉⣿⣿⣿⡀⢸⣿⠏⢀⡇⠀⡁⠀⠈⠆⠀⠈⠣⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣾⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣯⢿⣿⣿⣯⡀⠿⣿⣯⣷⣾⣿⣄⡀⠙⠀⠃⠀⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⡿⣟⠻⡛⢿⣿⡟⣉⠙⣿⣿⣿⣿⣿⢻⣿⢸⣿⣿⣿⠸⣿⣻⣿⣿⣿⣿⣯⣷⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣿⣿⣿⠏⠒⢀⠤⡴⠀⠈⡇⢒⣶⣿⣯⣿⣸⣿⢸⡿⣌⣿⣼⣿⢿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⠀⠀⠀⠀⠀⣺⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⢇⣘⠧⣟⠁⢴⡃⠕⢧⠐⡛⣿⡟⣿⣯⣿⣷⣽⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢹⣿⣿⣇⠀⠂⠀⠀⠔⣠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⢹⠿⣧⢗⠀⠟⡇⠂⢸⡀⢶⢳⠿⠛⣽⢫⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠈⣿⣿⣿⣷⣶⣶⣶⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""


print(yui)
time.sleep(2)
print(f"\nSelamat datang di rumah Arga (don't ask me why, Yui is here)")

def konnichiwa():
    while True:
        print("""Anggap seperti rumah `sendiri` yaa: 
                1. Buka toples jajan
                2. Ambil minumam
                3. Ambil permen
                q. Exit""")
        
        pilihan = input("Mau ngapain? : ")

        if pilihan == "1":
            menu_jajanan()
        elif pilihan == "2":
            menu_minuman()
        elif pilihan == "3":
            menu_permen()
        elif pilihan == "sendiri":
            print("'iloveyou'")
        elif pilihan == "q":
            print("Are you willing us to dear each other?")
            break
        else:
            print("Waduh gitu tah...")
        
def menu_jajanan():
    while True:
            print("""\nMau pilih jajan apa?
                1. Coklat
                2. Kripik
                3. Biskuat""")
            jajan = input("Aku mau jajan: ")
            if jajan == "1":
                print("Masih ingat kah dengan CatBury nyaa? <_<\n")
            elif jajan == "2":
                print("Kripik K nya Keysa <3\n")
            elif jajan == "3":
                print("Apa bedanya biskuit sama biskuat?\n")
            else:
                print("Jajannya yang itu lagi kosong dik\n")
            break

def menu_minuman():
    while True:
            print("""\nMau minum apa?
                1. Air Putih
                2. Air Hangat
                3. Air Dingin""")
            minum = input("Aku mau minum: ")
            if minum == "1":
                print("Still fresh like the old one\n")
            elif minum == "2":
                print("Sharing and dear each other\n")
            elif minum == "3":
                print("Cold and bold for the path ourself seek\n")
            else:
                print("Awas minumnya jatoh\n")
            break

def menu_permen():
    while True:
            print("""\nMau permen apa?
                1. Lolipop
                2. Moe moe
                3. Yupi""")
            permen = input("Aku mau permen: ")
            if permen == "1":
                print("Yummy and sweet like u\n")
            elif permen == "2":
                print("Kawaii as the same, moe moe kyun~\n")
            elif permen == "3":
                print("Yupi lope lope enak yah\n")
            else:
                print("Diabetes karena permen? apa karena kecantikan mu?\n")
            break


if __name__ == "__main__":
    konnichiwa()