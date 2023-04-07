import os

def Blok():
    diskler = os.popen("lsblk -o NAME,VENDOR,MOUNTPOINT | grep -v loop | grep /media" ).read().strip()
    #os modülünün popen parametresini kullanarak terminalde komut yazabiliyoruz read çıkan sonucun tamamını boşluklarla beraber okuduğu için strip ile boşlukları kaldırıyoruz
     if not diskler:
        print("Listelenecek disk bulunamadı.")
        return
    print(diskler)
    selected_disk = input("Hangi diski bloklamak istiyorsunuz? (sdb1, sdc5, sdt6)")
    os.system("sudo mount -o remount,ro /dev/{}".format(selected_disk))
    # seçtiğimiz diske terminal komutu ile read only düzenine getiriyoruz ve değişikliği uygulayacağımız diske entegre ediceğimiz için format fonksiyonunu kullanıyoruz
    mounted_disk = os.popen("mount | grep /dev/{}".format(selected_disk)).read().strip()
    #burada seçtiğimiz diski ekrana tekrar yazdırıyor
    if "ro" in mounted_disk:
        #read only komutu başarılı olarak entegre edildiyse
        print("Write Block Başarıyla Uygulandı.")
    else:
        print("İşlem Başarısız.")

def UnBlok():
    diskler = os.popen("lsblk -o NAME,VENDOR,MOUNTPOINT | grep -v loop | grep /media"").read().strip()
    if not diskler:
        print("Listelenecek disk bulunamadı.")
        return
    print(diskler)
    selected_disk = input("Hangi diski bağlamak istiyorsunuz? (sdb1, sdc5, sdt6)")
    os.system("sudo mount -o remount,rw /dev/{}".format(selected_disk))
    #bu kısımda yukarıdaki read only işlemlerini kaldırma gerçekleşiyor
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
                       # main fonksiyonumuzda 2 seçenek sunuluyor bloklama yada bloklanmayı kaldırma seçenekleri eğer block seçeneği çalışırsa Block fonksiyonu çalışır unblock seçilirse UnBlock fonksiyonu çalışır

if __name__ == '__main__':
    main()
