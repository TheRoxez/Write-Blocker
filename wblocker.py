import os

def Blok():
    os.system("lsblk -o NAME,VENDOR,MOUNTPOINT | grep sd | grep -v sda")
    selected_disk = input("Hangi diski bloklamak istiyorsunuz? (sdb1, sdc5, sdt6)")
    os.system("sudo mount -o remount,ro /dev/{}".format(selected_disk))
    mounted_disk = os.popen("mount | grep /dev/{}".format(selected_disk)).read().strip()
    if "ro" in mounted_disk:
        print("Write Block Başarıyla Uygulandı.")
    else:
        print("İşlem Başarısız.")

def UnBlok():
    os.system("lsblk -o NAME,VENDOR,MOUNTPOINT | grep sd | grep -v sda")
    selected_disk = input("Hangi diski bağlamak istiyorsunuz? (sdb1, sdc5, sdt6)")
    os.system("sudo mount -o remount,rw /dev/{}".format(selected_disk))
    mounted_disk = os.popen("mount | grep /dev/{}".format(selected_disk)).read().strip()
    if "rw" in mounted_disk:
        print("Write Block Başarıyla Kaldırıldı.")
    else:
        print("İşlem Başarısız.")

def main():
    islem = input("İşlem belirtin (block/unblock): ")
    if islem == "block":
        Blok()
    elif islem == "unblock":
        UnBlok()
    else:
        print("Geçersiz işlem belirtildi. Lütfen block veya unblock olarak belirtin.")

if __name__ == '__main__':
    main()
