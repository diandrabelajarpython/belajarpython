
username =input("username : ") == "admin"
pw =input("password : ") =="admin"
#hasil login
hasil_login = username and pw
#visibilas cek
if hasil_login == True :
    print("login berhasil")
    print("=== Cek Kelayakan palang pintu ===")
    lampu = input("lampu menyala , press y or no : ") == "y"
    if lampu == True :
        print("status lampu menyala")
    else : 
        print("status lampu mati,perbaiki !!!") 
        
    sirine = input("sirine menyala normal , press y or n : ") == "y"
    if sirine == True :
        print("sirine normal")
    else :
        print("sirine tidak normal , perbaiki!!!")   
    
    cek_visibilitas = [lampu == True , sirine == True]
    
    visibilitas = all(visibilitas for visibilitas in cek_visibilitas)
 #portal cek   
    if visibilitas == True :
        print("visibilitas normal , lanjut cek fungsi")
        print("cek portal")
        fungsi_portal = input(" portal menutup dengan sempurnna , press y or n") == "y"
        if fungsi_portal == True :
            print("fungsi portal normal")
        else : 
            print("fungsi portal tidak normal")
        print("cek Kelengkapan portal")
        kelengkapan_portal = input("apakah ada portal yang cacat ?? press y or n") == "n"
        if kelengkapan_portal == True :
            print(" cek kelayakan akhir ")
            
            cek_fungsi= [fungsi_portal == True , kelengkapan_portal == True]
            
            fungsi = all(fungsi for fungsi in cek_fungsi)
            
            kelayakan_akhir = visibilitas or fungsi
            
            if kelayakan_akhir == True : 
                print("PALANG PINTU NORMAL")
            else : 
                print("PALANG PINTU TIDAK NORMAL , LAKUKAN PERBAIKAN")   
        else : 
            print("perbaiki segera")       
    else : 
        print("visibilitas tidak normall , perbaiki segera")  
else : 
    print("login gagal")    