import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from time import sleep
from random import choice
import art
from colorama import Fore, init

init(autoreset=True)

Art = art.text2art("Kronos")
print(Fore.LIGHTGREEN_EX + Art)
print(Fore.YELLOW + "Su İçme Hatırlatıcısı")

print(f"""
PORT NUMARALARI 
------------------------
{Fore.BLUE}Hotmail: {Fore.MAGENTA}25/465
{Fore.LIGHTRED_EX}Gmail/Yahoo: {Fore.MAGENTA}587/465
{Fore.LIGHTBLUE_EX}Outlook: {Fore.MAGENTA}587
------------------------""")

port =input("Mail smtp portunuzu giriniz: ")
kullanici_mail = input("Mail: ")
kullanici_pass = input("SMTP Şifre: ")
alici_mail = input("Alıcı mail: ")


karakter = ("Aşk bir sudur iç iç kudur.",
            f"Sudan daha yumuşak ve ince başka bir şey yoktur; fakat önüne çıkan her şeyi sürükleyecek ve "
            f"parçalayabilecek kadar "
            "güçlüdür. \n -Lao Tzu",
            f"Su, her şeyi temizler; ama yalnız yüz karasını temizleyemez. \n -Muallim Naci",
            f"Suyun değeri, kuyu kuruyunca anlaşılır. \n Thomas Fuller",
            "Eğer su kaynağı senin kendi ruhundan fışkırmazsa, susuzluğunu dindiremezsin. \n Wolfgang Van Goethe",
            "Taşı delen suyun gücü değil, damlaların sürekliliğidir. ",
            "Su: Akarsa nehir, \n düşerse şelale, \n durulursa göl olur.",
            "Suya düştüğünüz için değil sudan çıkamadığınız için boğulursunuz. ",
            "Yokluğunla mum misali erirken bile suya hasret toprak gibi beklerim seni.",
            "Su uyur, düşman uyumaz.",
            "Suyun Faydaları: \n Sindirim sistemini çalıştırır. \n Hücrelere oksijen ve besin taşır. \n Cildi tazeler "
            "ve güzelleştirir. \n Vücut ısısını dengeler. \n Böbrek ve karaciğerdeki toksinleri temizler. \n Mineral, "
            "vitamin ve diğer besin maddelerin emilmesini sağlar. ",
            "Suyun Cilde Faydaları: \n Cildin kırışık olmasını geciktirir. \n Cildin kuru kalmasını engeller. "
            "Nemlendirir. \n Cildin gözenekleri açar. Ferahlık verir. \n Cildi besler ve tazeler. ",
            "Su İçmenin Saça Faydaları: \n Saça zarar veren zararlı maddeleri yok eder.. \n Saçtaki elektriklenmeyi "
            "azaltır. \n Saç dökülmesine karşı etkilidir. \n Boyalı saçlar için renk tutma özelliği vardır.",
            "Vücudun kontrol merkezi olan beyin de diğer organlar gibi sağlıklı çalışmak için suya ihtiyaç duyar. "
            "Uzamış susuzlukta unutkanlık, dikkat eksikliği, uyku hali, algıda ve hareketlerde azalma, sinirlilik "
            "olur. Sağlıklı zihinsel faaliyetler için su şart.",
            "Beynimizin yüzde 85’i sudur. Vücudumuzda yeteri kadar besin ve su yoksa stres altında hissederiz. Açlık "
            "ve susuzluğa dayanamamamızın sebebi beynimize bu durumlarda yakıt yani besin ve su gitmemesidir. Gün "
            "içerisinde gergin ve huzursuz olan kişiler yeterli su içmiyor olabilirler.",
            "Damar içinde dolaşan kanın büyük bir kısmı sudan oluşur. Kan, hücreler için gerekli oksijeni taşır. Su "
            "tüketimi yetersiz olursa, kan hacmi azalır, kan dolaşımı hızı yavaşlar, kan koyulaşır, aritmi gelişir, "
            "tansiyon düşer, tansiyon düşmesine bağlı bayılmalar görülebilir. Bu da kalbe ve diğer organlara giden "
            "kan miktarını azaltır, koyulaşan kan damarların tıkanmasına neden olabilir. Özellikle hayati öneme sahip "
            "olan beyin damarları ve kalp koroner damarları gibi ince damarlarda tıkanmalara neden olarak kalp krizi "
            "ve felç gibi hastalıkların ortaya çıkmasını kolaylaştırır.",
            "Her gün vücuttan idrarla ortalama 1500 ml, ciltten terleme ve buharlaşma yoluyla 400 ml, dışkı ile 200 "
            "ml, solunum havasını nemlendirmek için solunum yoluyla ortalama 300 ml su harcanır. Toplamda her gün "
            "ortalama 2500 ml su kaybedilir. Yaz aylarında bu miktar yaklaşık 500 ml daha fazladır. Yiyeceklerden "
            "aldığımız su ise bu ihtiyacın sadece yüzde 20-30’unu karşılamaya yeter. Sağlıklı bir hayat için mutlaka "
            "günde 2-3 litre su içmeliyiz.",
            "Her yıl sudan kaynaklanan nedenlerden dolayı 3.5 milyon insan hayatını kaybetmekte.",
            "Afrika ve Asya kıtalarında yaşayan insanlar su biriktirmek için ortalama 6 km yol yürümek zorundalar.",
            "Neredeyse 700 milyon Çinli mikroplu su içiyor.",
            "Her 9 kişiden 1'i ıslah edilmiş su kaynağına ulaşamıyor.",
            "Kemiklerimizin %31'i sudan oluşuyor."
            )

while True:

    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(kullanici_mail, kullanici_pass)

        mesaj = MIMEMultipart()
        mesaj["From"] = kullanici_mail  # Gönderen
        mesaj["To"] = alici_mail  # Alıcı
        mesaj["Subject"] = "Su iç"  # Konusu

        body = str(choice(karakter))

        body_text = MIMEText(body, "plain")  #
        mesaj.attach(body_text)

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        print(f"Mail başarılı bir şekilde gönderildi. İçerik : {body}")
        mail.close()
        sleep(1800)

    except:
        print("Hata:", sys.exc_info()[0])
