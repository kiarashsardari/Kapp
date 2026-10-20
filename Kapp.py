import math
import pyttsx3
from prettytable import PrettyTable as ptt
welc = ptt(["wellcom to Kiarash app!"])
welc.add_row(["Password is 123"])
print(welc)
def symbols():
        sp=ptt(["operations → " ,"Riaziyat","Mosavi Ha","Namaad Ha","Felesh Ha","Ashkall","Aadad", "Cancle"])
        sp.add_row(["Symbols → ","R", "M","N","F","A","D", "C"])
        print(sp)
        sps=input("Chois a symbol: ")
        if sps.upper() == "R" :
                p1=ptt(["±", "×","÷"])
                p1.add_row(["√","∛", "∜"])   
                print(p1)
                symbols()
        elif sps.upper()=="M":
                p2=ptt(["≤", "≥", "≅"])
                p2.add_row(["≈" ,"≡" ,"≠"])
                print(p2)
                symbols()
        elif sps.upper()=="N":
                p3=ptt(["β", "ε", "θ", "π", "ρ" ,"µ", "Ω" ,"κ"])
                p3.add_row(["∞", "∝", "∪", "∩" ,"∅" ,"°" ,"∆", "∈"])
                print(p3)
                symbols()
        elif sps.upper()=="F":
                p4=ptt(["←", "→","↑","↓" ,"↔"])
                p4.add_row(["↕", "↖", "↗", "↘" ,"↙"])
                print(p4)
                symbols()
        elif sps.upper()=="A":
                p5=ptt(['∎', '◊', '□', '○', '◌', '●' ,'◦' ,'Ꙩ'])
                p5.add_row(['۩', '≡' ,'⌂', '∴', '⋮' ,'⋯', '﴾' ,'﴿'])
                print(p5)
                symbols()
        elif sps.upper()=="D":
                p6=ptt([' ₀  ₁  ₂  ₃  ₄  ₅  ₆  ₇  ₈  ₉ ',' ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹ '])
                p6.add_row([' ²  ³  ⁴  ⁵  ⁶  ⁷  ⁸  ⁹  ⁿ ','⅓ ⅔ ⅕ ⅖ ⅗ ⅘ ⅙ ⅚ ⅛ ⅜ ⅝ ⅞ ⅟ '])
                print(p6)
                symbols()
        elif sps.upper()=="C":
                print("")
                koly()
        else:
                print('''
Pleas try again:
                ''')
                symbols()

def faseleh():
        def fk():
                print("""Fasele Noghtei Ba Mokhtasate (x₀,y₀) Az Khati Ba Moadeleye ax+by+c=0
                """)
                a=int(input("a: "))
                print("")
                b=int(input("b: "))
                print("")
                c=int(input("c: "))
                print("")
                x1=int(input("x₀(Tule Noghte): "))
                print("")
                y1=int(input("y₀(Arze Noghte): "))
                print("")
                ax=a*x1
                by=b*y1
                a2=a**2
                b2=b**2
                js=ax+by+c
                jmj=a2+b2
                jm=math.sqrt(jmj)
                print(js/jm)
                faseleh()
        def fn():
                print("""Tul Va Arze 2 Noghte Ke Mikhahid Fasele Ye Bein Anha Ra Bedast Avarid Ra Vared Konid.
                """)
                x1=int(input("x₁: "))
                print("")
                y1=int(input("y₁: "))
                print("")
                x2=int(input("x₂: "))
                print("")
                y2=int(input("y₂: "))
                print("")
                x21=(x2-x1)**2
                y21=(y2-y1)**2
                xy=x21+y21
                xy2=math.sqrt(xy)
                print("Faseleye Beine Noghat:",xy2)
                print("")
                faseleh()
        fp=ptt(["operations->","Fasele Ye Do Noghte Az Ham", "Fasele Ye Noghte Az Khat"])
        fp.add_row(["Symbol->","N","K"])
        print(fp)
        print('')      
        s=input("What Do You Want To Do? ")
        print('')      
        if s.upper()=="N":
                fn()
                print("""""")
        elif s.upper()=="K":
                fk()
                print("""
                """)        
        elif s.upper()=="C":
                koly()
        else :
                print("""Pleas Choise a Correct Symbol:                
                """)
                faseleh()
def calcu():
    import math
    from math import pow as p
    from math import lcm as l
    from math import gcd as g
    from prettytable import PrettyTable as ptt
    def Primenumbers():
        print("""
        """)
        welcome=ptt(["Number detector"])
        welcome.add_row(["Please choose a number smaller than seven digits"])
        print(welcome)   
        num=int(input("""Enter your number: """))  
        maghsom_elayh_ha=0
        for i in range(1,num+1):
                if num%i == 0:
                        maghsom_elayh_ha +=1
        if num == 1:
                print("""
This number is neither prime nor composite
        """)
        elif num == 0:
                print("""
This number is neither prime nor composite
        """)
        elif maghsom_elayh_ha == 2:
                print("""
This is a prime number
        """)
        else:
                print("""
This is a composite number""")
    def Fibonacci():
        p=int(input("fibonachi siqens from one to: "))
        s,k=0,1
        while k<p:
            print(k)
            s,k=k,s+k
    def Multiplicationt():
        num1= int(input("Multiplication Table from one to: "))
        for i in range(1,num1+1):
            for j in range(1,num1+1):
                print(format(i*j, "3d"),end =" ")
            print()
    def Root():
        num1= int(input("number for root: "))
        print("√", f'{num1:,}', "=", f'{math.sqrt(num1):,}')


    def ecal():
        tacl=ptt(["Cancle","+","-","÷","xⁿ","×", "Sine", "Cosine","Tangent","Cotangent","Logarithm","|x|","π","LCM","GCD"])
        tacl.add_row(["C","+","-","/","x**n","*","sin(x)","cos(x)","tan(x)","cot(x)","log(x)","abs(x)","pi","lcm(x,y)","gcd(x,y)"])
        print(tacl)
        e1=input("Do any calculations here(C=Cancle): ")
        while e1 !="c": 
            e=eval(e1)
            print("",e)
            print("")
            e1=input("Do any calculations here(C=Cancle): ")
    
    def calc():
        print("""
""")
    t = ptt(["operations->","Cancle","Root","Multiplication table",'Number detector',"Fibonacci relationship"])
    t.add_row(["Symbols->","C","R","M","N","F"])
    tt = ptt(["operations->","Calculator"])
    tt.add_row(["Symbols->","CL"])
    print(t)
    print(tt)
    op= input('symbol : ')
    if op.upper() == "N":
        Primenumbers()
        print("""
""")
        calcu()
    elif op=="F":
        Fibonacci()
        print("""
""")
        calcu()
    elif op.upper() == "C":
        print("ok")
        print("""
""")
        koly()
    elif op.upper() == "R":
        Root()
        print("""
""")
        calcu()
    elif op.upper() == "M":
        Multiplicationt()
        print("""
""")
        calcu()
    elif op.upper()=="CL":
        print("""
""")
        ecal()
        print("""
""")
        calcu()
    else:
        print("your symbol is false please try again : ")
        print("""
        
""")
        calcu()
def game():
    import random
    ba= ptt(["cancle", "your death year", "your car in later"])
    ba.add_row(["C", "DY", "CAR"])
    print(ba)
    m= input("enter your name game: ")
    if m.upper()=="C":
        print("ok")
        print("""
""")
        koly()
    elif m.upper()=="DY":
        q=input("your name : ")
        print("")
        q1=input("your last name : ")
        print("")
        q2=input(("your age : "))
        print("")
        year=["2023","2036","2064","2039","2046","2027","2028","2029","2030","2031","2035","2034","2041","2044","2048","2049","2053","2057","2058","2063","2065","2069","2071","2076","2073","2078","2082","2086","2088","2092","2091","2022","2027","2033","2055","2029","2092","2044","2061","2059","3094"]
        print("your death year is", random.choice(year))
        print("""
""")
        game()
    elif m.upper()=="CAR":
        ip = input("your name : ")
        print("")
        ipn = input("last name : ")
        print("")
        i = input("your age : ")
        print("")
        k = ["206" , "207", "301", "405", "407", '508', '2008', '7X', '8S', 'H30 crass', 'k112', 'S30', 'S5', 'S7', 'Arisan', 'Tara', 'Tondar 90', 'Tondar+' , 'Tondar Pickup', 'Dena', 'Rana', 'Roa', 'Rira', 'Samand', 'Soren', 'Pars', 'Vanet Bardo', 'Pickup Tonland', 'Kapcher', 'Kizashi', 'Grand Vitara', 'Optima', 'SantaFe', 'Tucson', 'Accent5DR', 'Ioniq Hybrid', 'Genesis', 'Veloster', 'i30', 'i40', 'Sonata', 'Elantra' ,'Malibo', 'Carera S', 'Kine Turbo' , 'Range Rover', 'Z4', 'Quattroporte', 'Mercedes Benz SL500', 'Mercedes Benz G63', 'Gran Turismo MC', 'Porsche Cayman', 'Jaguar XJL', 'Porsche 911 Carrera', 'Mercedes Benz SL', 'Maserati Ghibli', 'Chevrolet Malibu', 'Toyota RAV4', 'Haima S7', 'Hyundai Rio', 'Mazda 3', 'Suzuki Alto', 'Proton S16', 'Holden Barina', 'Honda Jazz', 'Chery J1', 'Ford Fiesta', 'Nissan Micra', 'Toyota Yaris', 'Hilux', 'Perado', 'Reno Floens']#, '', '', '', '', '', '', '', '', '', '' ,'', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ,'' ,'']
        print("your care in later is", random.choice(k))
        print("""
""")
        game()
    else:
        print("please try again: ")
        print("""
""")
        game()        
def wip():    
        import os
        import subprocess
        import re
        command_output = subprocess.run(["netsh", "wlan", "show", "profile"], capture_output = True).stdout.decode()
        profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
        wifi_list = list()
        if len(profile_names) != 0:
            for name in profile_names:
                wifi_profile = dict()
                profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
                if re.search("Security key           : Absent", profile_info):
                   continue
                else:
                    wifi_profile["Name"] = name
                    profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
                    password = re.search("Key Content            : (.*)\r", profile_info_pass)
                    if password == None:
                        wifi_profile["password"] = None
                    else:
                        wifi_profile["password"] = password[1]
                    wifi_list.append(wifi_profile)
        for x in range(len(wifi_list)):
                print(wifi_list[x])
        with open('wifi.txt', 'w+') as fh:
            for x in wifi_list:
                fh.write(f"Name: {x['Name']}\n Password: {x['password']}\n")
        def createNewConnection(name, SSID, password):
            config = """<?xml version=\"1.0\"?>
        <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
            <name>"""+name+"""</name>
            <SSIDConfig>
                <SSID>
                    <name>"""+SSID+"""</name>
                </SSID>
             </SSIDConfig>
             <connectionType>ESS</connectionType>
             <connectionMode>auto</connectionMode>
             <MSM>
                 <security>
                        <authEncryption>
                                <authentication>WPA2PSK</authentication>
                                <encryption>AES</encryption>
                                <useOneX>false</useOneX>
                        </authEncryption>
                        <sharedKey>
                                <keyType>passPhrase</keyType>
                                <protected>false</protected>
                        <keyMaterial>"""+password+"""</keyMaterial>
                    </sharedKey>
                </security>
            </MSM>
        </WLANProfile>"""
            command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
            with open(name+".xml", 'w') as file:
                file.write(config)
            os.system(command)
        def connect(name, SSID):
            command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
            os.system(command)
        def displayAvailableNetworks():
            command = "netsh wlan show networks interface=Wi-Fi"
            os.system(command)
        displayAvailableNetworks()
        k=input("C=Cancle : ")
        if k.upper()=="C":
            print("""
            """)
            koly()
def Pythagorean():
        v=input('N-Y(C=Cancle) Do you enter hypotenuse?: ')
        print("")
        if v.upper()=="Y":
            vat=int(input("hypotenuse : "))
            print("")
            zel=int(input("side : "))
            print("")
            print(f'{vat:,}','^2', '= H^2 +', f'{zel:,}','^2')
            print("")
            print("H^2 =", f'{zel:,}', "^2 -", f'{vat:,}', "^2")
            print("")
            zell=zel**2
            vatt=vat**2
            print("H^2 =", f'{zell:,}', '-', f'{vatt:,}')
            print("")
            rr=zell-vatt
            print('H^2 =', f'{rr:,}')
            print("")
            ff=rr**0.5
            print('H =', ff)
            print("")
            Pythagorean()
        elif v.upper()=="N":
            z1=int(input("side 1: "))
            print("")
            z2=int(input("side 2: "))
            print("")
            print("V^2 = ", f'{z1:,}','^2', "+", f'{z2:,}','^2')  
            print("")
            z11=z1**2
            z22=z2**2
            z12=z11+z22
            print("V^2 = ",f'{z11:,}', "+",f'{z22:,}' )
            print("")
            print("V^2 = ", f'{z12:,}')
            print("")
            z122= z12**0.5
            print("V = ", f'{z122:,}')
            print("")
            Pythagorean()
        elif v.upper()=="C":
            print("""
            """)
            koly()
        else:
            Pythagorean()
def pas():
    from prettytable import PrettyTable as ptt
    ipt=input("password: ")
    prd="123"
    if ipt==prd:
        print("""
""")
        koly()
    else:
        print("error!")
        pas()
def calendar() :
    def ki():
        from prettytable import PrettyTable as ptt
        import calendar as cal
        gh=ptt(["operation->", "Cancle", "Tedad Rooz Ha", "Date"])
        gh.add_row(["symbol->", "C", "T", "D"])
        print(gh)
        v=input("symbol: ")
        if v.upper()=="C":
                print("ok")
                print("""
""")
                koly()
        elif v.upper() =="T": 
                print("""""")
                a=int(input("Tedad Rooz Ha: "))
                print("""""")
                a1=a/365
                a2=a%365
                a3=a2/30
                a4=a2%30
                print(int(a1),"sal")
                print("""""")
                print(int(a3),"mah")
                print("""""")
                print(int(a4),"rooz")
                print("""""")
                ki()
        elif v.upper() =="D":
                print("""""")
                y =input("year: ")
                print("""""")
                y1=int(y)
                m = int( input("month: "))
                print("""
""")
                print(cal.month(y1,m))
                ki()

    ki()
def table():
    sardar= ptt(["Tedad soton ha ->", "1", "2", "3", "4", "5", "Cancel(type C)"])
    sardar.add_row(["->", "chand", "ta", "soton", "entekhab", "mikonid", "?"])
    print(sardar)
    w=input("vared konid: ")
    if w == "1":    
        print("""
""")
        p1=input("matn bala: ")
        print("""
""")
        p2=input("matn pain: ")
        print("""
""")
        x = ptt([p1])
        x.add_row([p2])
        print(x)
        print("""
""")
        table()
    elif w== "2":
        print("""
""")
        pp1=input("matn bala sotun1: ")
        print("""
""")
        pp2=input("matn pain sotun1: ")
        print("""
""")
        p3= input("matn bala sotun2: ")
        print("""
""")
        p4= input("matn pain sotun2: ")
        print("""
""")
        b = ptt([pp1,p3])
        b.add_row([pp2,p4])
        print(b)
        print("""
""")
        table()
    elif w== "3":
        print("""
""")
        pp11=input("matn bala sotun1: ")
        print("""
""")
        pp22=input("matn pain sotun1: ")
        print("""
""")
        p33= input("matn bala sotun2: ")
        print("""
""")
        p44= input("matn pain sotun2: ")
        print("""
""")
        o= input("matn bala sotun3: ")
        print("""
""")
        o1= input("matn pain sotun3: ")
        print("""
""")
        j = ptt([pp11,p33,o])
        j.add_row([pp22,p44,o1])
        print(j)
        print("""
""")
        table()
    elif w=="4":
        print("""
""")
        ppp11=input("matn bala sotun1: ")
        print("""
""")
        ppp22=input("matn pain sotun1: ")
        print("""
""")
        pp33= input("matn bala sotun2: ")
        print("""
""")
        pp44= input("matn pain sotun2: ")
        print("""
""")
        oo= input("matn bala sotun3: ")
        print("""
""")
        oo1= input("matn pain sotun3: ")
        print("""
""")
        o2= input("matn bala sotun4: ")
        print("""
""")
        o3= input("matn pain sotun4: ")
        print("""
""")
        i = ptt([ppp11,pp33,oo,o2])
        i.add_row([ppp22,pp44,oo1,o3])
        print(i)
        print("""
""")
        table()
    elif w=="5":
        print("""
""")
        p1=input("matn bala sotun1: ")
        print("""
""")
        p2=input("matn pain sotun1: ")
        print("""
""")
        p3= input("matn bala sotun2: ")
        print("""
""")
        p4= input("matn pain sotun2: ")
        print("""
""")
        p5= input("matn bala sotun3: ")
        print("""
""")
        p6= input("matn pain sotun3: ")
        print("""
""")
        p7= input("matn bala sotun4: ")
        print("""
""")
        p8= input("matn pain sotun4: ")
        print("""
""")
        p9= input("matn bala sotun5: ")
        print("""
""")
        p10= input("matn pain sotun5: ")
        print("""
""")
        ol = ptt([p1,p3,p5,p7,p9])
        ol.add_row([p2,p4,p6,p8,p10])
        print(ol)
        print("""
""")
        table()
    elif w.upper()=="C":
        print("ok")
        print("""
""")
        koly()
    else:
        print("please try again: ")
        print("""
""")      
        table()
def say() :
    def p():
        import pyttsx3
        kas=ptt(["operations->", "Cancle"])
        kas.add_row(["symbol->", "C"])
        print(kas)
        x=input("text (C = Cancle) : ")
        if x.upper()=="C":
            print("ok")
            print("""
""")
            koly()
        elif len(x) == 0:
            print("""please try again:
             """)
            say()
        else:
            s1 = pyttsx3.init()
            s1.say(x)
            s1.runAndWait()
            print("""
""")
            p()
    p()
def koly():
    from prettytable import PrettyTable as ptt
    kiara = ptt(["operations->", "Calculator", "Games", "Date", "Text Reader","Pythagorean", "Table","WiFis", "Fasele","Symbols","Cancel"])
    kiara.add_row(["symbols->", "Cl", "G", "D", "T","P", "Ta", "W", "F","S","C"])
    print(kiara)
    n= input("Please select your symbol according to the tables : ")
    if n.upper() == "CL":   
        print("""
""")
        calcu()
    elif n.upper()=="S":
        print("""
        """)
        symbols()
    elif n.upper()=="F":
        print("""
        """)
        faseleh()
    elif n.upper()=="P":
        print("""
        """)
        Pythagorean()
    elif n.upper()=="W":
        print("""
""")
        wip()
    elif n.upper()=="TA":
        
        print("""
""")
        table()
    elif n.upper()=="G":
        
        print("""
""")
        game()
    elif n.upper()=="D":
        
        print("""
""")
        calendar()
    elif n.upper() == "T":
        
        print("""
""")
        say()
    elif n.upper()== "C":
        print("""
""")
        print("OK! By.")
    else:
        print("please try again: ")
        print("""
""")
        koly()
pas()
