import mysql.connector as ms
x=ms.connect(host="localhost",user="root",password="")
cur=x.cursor()

cur.execute("create database moody_music;")
cur.execute("use moody_music;")
x.commit()
cur.execute("create table happy_hollywood(SNo int(5) primary key, SongName varchar(30) not null, URL varchar(50) unique)") 
cur.execute("insert into happy_hollywood(SNo , SongName, URL) values"
            "(1,'Good_life','https://www.youtube.com/watch?v=wZs8LxMCzNw'),"
            "(2,'High_hopes','https://www.youtube.com/watch?v=fH_OnJk6QqU'),"
            "(3,'Dont_you_need_somebody','https://www.youtube.com/watch?v=CF2EtPcBDuc'),"
            "(4,'Stereo_hearts','https://www.youtube.com/watch?v=1NEaaoFb3sA'),"
            "(5,'Uptown_funk','https://www.youtube.com/watch?v=CeYuFSBkkVw'),"
            "(6,'Live_while_we_are_young','https://www.youtube.com/watch?v=TREkkS9gZp4'),"
            "(7,'Levitating','https://www.youtube.com/watch?v=-Ileb6iOIag'),"
            "(8,'Slow_down','https://www.youtube.com/watch?v=YwPCo8r-IEU'),"
            "(9,'Sugar','https://www.youtube.com/watch?v=N1BcpzPGlYQ'),"
            "(10,'Stay','https://www.youtube.com/watch?v=LS2ifrLAadU'),"
            "(11,'MeNecesita','https://www.youtube.com/watch?v=Zyimac4WRI0'),"
            "(12,'Love_myself','https://www.youtube.com/watch?v=Oyb-8pALrY8'),"
            "(13,'Golden','https://www.youtube.com/watch?v=vevTpPyqn5Q'),"
            "(14,'Hey_mama','https://www.youtube.com/watch?v=ERMRWk1bwqo'),"
            "(15,'Polaroid','https://www.youtube.com/watch?v=Xo52XCvaBbc')")
x.commit()            
cur.execute("create table sad_hollywood(SNo int(5) primary key, SongName varchar(30) not null, URL varchar(50) unique)")
cur.execute("insert into sad_hollywood(SNo , SongName, URL) values"
            "(1,'Arcade','https://www.youtube.com/watch?v=PNozaFzqOvI'),"
            "(2,'Bad_liar','https://www.youtube.com/watch?v=fZE5UxVQTXI'),"
            "(3,'Wrong_direction','https://www.youtube.com/watch?v=39xGflo5kTs'),"
            "(4,'Falling','https://www.youtube.com/watch?v=dSDehTfGYK4'),"
            "(5,'It_will_be_okay','https://www.youtube.com/watch?v=q_HNcBjHlPY'),"
            "(6,'Drivers_license','https://www.youtube.com/watch?v=b9wbionpQ7E'),"
            "(7,'Takeaway','https://www.youtube.com/watch?v=GQrIiqPQ-KY'),"
            "(8,'I_hate_you_I_love_you','https://www.youtube.com/watch?v=EtLtZoCwquw'),"
            "(9,'You_broke_me_first','https://www.youtube.com/watch?v=QXzC2eiHBG8'),"
            "(10,'Hello','https://www.youtube.com/watch?v=be12BC5pQLE'),"
            "(11,'Let_me_down_slowly','https://www.youtube.com/watch?v=jLNrvmXboj8'),"
            "(12,'Little_do_you_know','https://www.youtube.com/watch?v=GP4okspbfMM'),"
            "(13,'Used_to_love','https://www.youtube.com/watch?v=eZBcktiUg-Y'),"
            "(14,'So_far_away','https://www.youtube.com/watch?v=kd-kM0xx2iE'),"
            "(15,'Tired','https://www.youtube.com/watch?v=YnaEoCY_vzc')")
x.commit()

cur.execute("create table angry_hollywood(SNo int(5) primary key, SongName varchar(30) not null, URL varchar(50) unique)")
cur.execute("insert into angry_hollywood(SNo , SongName, URL) values"
            "(1,'Unstoppable','https://www.youtube.com/watch?v=h3h035Eyz5A'),"
            "(2,'Wrecking_Ball','https://www.youtube.com/watch?v=Itzk9W4YXw4'),"
            "(3,'Natural','https://www.youtube.com/watch?v=V5M2WZiAy6k'),"
            "(4,'Ciao_adios','https://www.youtube.com/watch?v=PP8icQneZgY'),"
            "(5,'Radioactive','https://www.youtube.com/watch?v=vrgaB9xu7GM'),"
            "(6,'One_more_night','https://www.youtube.com/watch?v=RQKRetgSlgc'),"
            "(7,'Rolling_in_the_deep','https://www.youtube.com/watch?v=AIYpdjQVidc'),"
            "(8,'Whatever_it_takes','https://www.youtube.com/watch?v=M66U_DuMCS8'),"
            "(9,'Bad_blood','https://www.youtube.com/watch?v=CXKEdnasDto'),"
            "(10,'Who_do_you_love','https://www.youtube.com/watch?v=hPc7m1ffj3s'),"
            "(11,'Dont_let_me_down','https://www.youtube.com/watch?v=mywyuiAbww4'),"
            "(12,'Animals','https://www.youtube.com/watch?v=0GVExpdmoDs'),"
            "(13,'IDGAF','https://www.youtube.com/watch?v=C4GGx--QFr8'),"
            "(14,'Young_blood','https://www.youtube.com/watch?v=Vwhrqd3UaKo'),"
            "(15,'Drag_me_down','https://www.youtube.com/watch?v=hzT1sZcmbZw')")
x.commit()
cur.execute("create table sad_kollywood(SNo int(5) primary key, SongName varchar(30) not null, URL varchar(50) unique)")
cur.execute("insert into sad_kollywood(SNo , SongName, URL) values"
            "(1,'Ellu_vaya_pookalaye','https://www.youtube.com/watch?v=paycN-BEzsg'),"
            "(2,'Poi_Vazhva','https://www.youtube.com/watch?v=wX9XyhqlcMk'),"
            "(3,'Kanave_kanave','https://www.youtube.com/watch?v=DQgIut9r0JE'),"
            "(4,'Nenje_yezhu','https://www.youtube.com/watch?v=qNKlMJl87NQ'),"
            "(5,'Poi_varava','https://www.youtube.com/watch?v=c3ulw7fMKfo'),"
            "(6,'Othayilae_ulagam','https://www.youtube.com/watch?v=cCXc7-ghBDU'),"
            "(7,'Po_urave','https://www.youtube.com/watch?v=od4udyuWKV8'),"
            "(8,'Yen_ennai_pirinthai','https://www.youtube.com/watch?v=gCL8hGIUuRg'),"
            "(9,'Maathare_maathare','https://www.youtube.com/watch?v=AWWKiVp8cTU'),"
            "(10,'Life_of_Ram','https://www.youtube.com/watch?v=psi5C9WM3i0'),"
            "(11,'Nenjame','https://www.youtube.com/watch?v=uxm526y9jHY'),"
            "(12,'Dheivangal_Ellaam','https://www.youtube.com/watch?v=wdyYIVUnZho'),"
            "(13,'Kayilae_Aagasam','https://www.youtube.com/watch?v=lgk-d05PQ_0'),"
            "(14,'Karuvinil_Enai','https://www.youtube.com/watch?v=6LDf5_1Y_ss'),"
            "(15,'Nalla_nanban','https://www.youtube.com/watch?v=EC_FSgiHK_k')")
x.commit()
cur.execute("create table happy_kollywood(SNo int(5) primary key, SongName varchar(30) not null, URL varchar(50) unique)")
cur.execute("insert into happy_kollywood(SNo , SongName, URL) values"
            "(1,'Vaathi_coming','https://www.youtube.com/watch?v=v3smjiDu3-8'),"
            "(2,'Yaakai_Thiri','https://www.youtube.com/watch?v=stHk8B5mta4'),"
            "(3,'Yelo_Pullelo','https://youtu.be/nfH0pa0VSBI?si=Yyh1UwQSLz-TZL5r'),"
            "(4,'Chill_bro','https://www.youtube.com/watch?v=WkW4_tkOgbo'),"
            "(5,'Yethi_yethi','https://www.youtube.com/watch?v=QzsQGb-c_cQ'),"
            "(6,'What_A_Karvaad','https://www.youtube.com/watch?v=POlJvn-hMIc'),"
            "(7,'Pista_The_Run_Anthem','https://www.youtube.com/watch?v=SuuypjzzqRw'),"
            "(8,'Sirikkalam_Parakkalam','https://www.youtube.com/watch?v=1k7UJcEj5JU'),"
            "(9,'Heartile_Battery','https://www.youtube.com/watch?v=9D4PQOha4Og'),"
            "(10,'Tum_tum','https://www.youtube.com/watch?v=yGUKYKSJJc8'),"
            "(11,'Urvashi_Urvashi','https://www.youtube.com/watch?v=7r5L1Cga7lM'),"
            "(12,'Kadhal_cricket','https://www.youtube.com/watch?v=N21uTmDPtAw'),"
            "(13,'Boomi_Enna_Suthudhe','https://www.youtube.com/watch?v=zECI6I8R6bU'),"
            "(14,'Rowdy_Baby','https://www.youtube.com/watch?v=7GdtgiEIJ0c'),"
            "(15,'Gala_gala','https://www.youtube.com/watch?v=-jTLGbn-WaI')")

x.commit()
cur.execute("create table angry_kollywood(SNo int(5) primary key, SongName varchar(30) not null, URL varchar(50) unique)")
cur.execute("insert into angry_kollywood(SNo , SongName, URL) values"
            "(1,'Asuran-Blood_Bath','https://www.youtube.com/watch?v=xnt0tZJwBEg'),"
            "(2,'Dheera_dheera','https://www.youtube.com/watch?v=Qf3zl3QJ0QM'),"
            "(3,'Polakatum_Para_Para','https://www.youtube.com/watch?v=dZN4TD9Ane0'),"
            "(4,'Oru_Naalil','https://www.youtube.com/watch?v=H3ssvu6MSZI'),"
            "(5,'Theemai_Dhaan_Vellum','https://www.youtube.com/watch?v=tkql_yvuSK0')," 
            "(6,'Surviva','https://www.youtube.com/watch?v=QNZiwr7nYMk'),"
            "(7,'Kandaa_Vara_Sollunga','https://www.youtube.com/watch?v=xqxF-KM-CxI'),"
            "(8,'Unakkulle_Mirugam','https://www.youtube.com/watch?v=yC47kjWY9eQ'),"
            "(9,'Neruppu_da','https://www.youtube.com/watch?v=LHaGDT6Pdbk'),"
            "(10,'Porkkalam','https://www.youtube.com/watch?v=1UvJIebrqMo'),"
            "(11,'Karuppu_Vellai','https://www.youtube.com/watch?v=oRbcHJNePXk'),"
            "(12,'Hey_Mama','https://www.youtube.com/watch?v=1a8MtHySeAg'),"
            "(13,'Petta_Paraak','https://www.youtube.com/watch?v=dG84Kn5ehHA'),"
            "(14,'Kaala-Katravai_Patravai','https://www.youtube.com/watch?v=2WG--2Z5uNo'),"
            "(15,'VIP_Title_Song','https://www.youtube.com/watch?v=qcnqkr7oeNg')")
x.commit()
cur.execute("create table happy_bollywood(SNo int(5) primary key, SongName varchar(30) not null, URL varchar(50) unique)")
cur.execute("insert into happy_bollywood(SNo , SongName, URL) values"
            "(1,'Sooraj_Dooba_Hain','https://www.youtube.com/watch?v=5AnRJXsLMUo'),"
            "(2,'Love_You_Zindagi','https://www.youtube.com/watch?v=rwn0Zs7ELzc'),"
            "(3,'First_Class','https://www.youtube.com/watch?v=xHkHeU1QZGU'),"
            "(4,'Badtameez_Dil','https://www.youtube.com/watch?v=pkEOCa0v9Ak'),"
            "(5,'Makhna','https://www.youtube.com/watch?v=xNn1vcZ51vg')," 
            "(6,'Gallan_Goodiyaan','https://www.youtube.com/watch?v=FLz2eQtI_1w'),"
            "(7,'Chogada','https://www.youtube.com/watch?v=koPYhWqpTVk'),"
            "(8,'Milegi_Milegi','https://www.youtube.com/watch?v=SKpuHn-OxeY'),"
            "(9,'Galti_Se_Mistake','https://www.youtube.com/watch?v=Li409NHgJ2M'),"
            "(10,'Buddhu_Sa_Mann','https://www.youtube.com/watch?v=Zo4WsI14s3g'),"
            "(11,'Matargashti','https://www.youtube.com/watch?v=iid7cxx0keU'),"
            "(12,'Maahi_Ve','https://www.youtube.com/watch?v=s8aAlUynpEY'),"
            "(13,'Bang_Bang','https://www.youtube.com/watch?v=ZcP_bvfqJaw'),"
            "(14,'Chammak_Challo','https://www.youtube.com/watch?v=zlUK41dCaQQ'),"
            "(15,'London_Thumakda','https://www.youtube.com/watch?v=87uhO75MqdQ')")
x.commit()
cur.execute("create table sad_bollywood(SNo int(5) primary key, SongName varchar(30) not null, URL varchar(50) unique)")
cur.execute("insert into sad_bollywood(SNo , SongName, URL) values"
            "(1,'Agar_Tum_Saath_Ho','https://www.youtube.com/watch?v=elorsX7uG_Y'),"
            "(2, 'Mile_Ho_Tum_Humko','https://www.youtube.com/watch?v=2qLgVd3ZyRo'),"
            "(3,'Tera_Yaar_Hoon_Main','https://www.youtube.com/watch?v=3Bwubdo-2aY'),"
            "(4,'Ae_Dil_Hai_Mushkil','https://www.youtube.com/watch?v=C6fN3GizNRE'),"
            "(5,'Jeena_Jeena','https://www.youtube.com/watch?v=UMOFhrxZ2eQ')," 
            "(6,'Dilbara','https://www.youtube.com/watch?v=-CsexhHAiyM'),"
            "(7,'Asal_Mein','https://www.youtube.com/watch?v=jabs2RM7Tqo'),"
            "(8,'Tum_Hi_Aana','https://www.youtube.com/watch?v=srPQJktsRGo'),"
            "(9,'Teri_Mitti','https://www.youtube.com/watch?v=tionpZAVPd4'),"
            "(10,'Sun_saathiya','https://www.youtube.com/watch?v=fKxEXm9qG4k'),"
            "(11,'Kalank_Title_Track','https://www.youtube.com/watch?v=Grr0FlC8SQA'),"
            "(12,'Hamdard','https://www.youtube.com/watch?v=mUPIJCs8-bE'),"
            "(13,'Kabira','https://www.youtube.com/watch?v=CyLDe7rw48w'),"
            "(14,'Sunn_Raha_Hai_Na_Tu','https://www.youtube.com/watch?v=z3UHfi9vpbc'),"
            "(15,'Shayad','https://www.youtube.com/watch?v=OnAyBZQc1vk')")
x.commit()
cur.execute("create table angry_bollywood(SNo int(5) primary key, SongName varchar(30) not null, URL varchar(50) unique)")
cur.execute("insert into angry_bollywood(SNo , SongName, URL) values"
            "(1,'Just_Go_To_Hell_Dil','https://www.youtube.com/watch?v=qSewQ6Nx6Bo'),"
            "(2,'Bekhayali','https://www.youtube.com/watch?v=NO4BUCFJPqQ'),"
            "(3,'Dua_Karo','https://www.youtube.com/watch?v=ppBT5y9Axow'),"
            "(4,'Khalibali','https://www.youtube.com/watch?v=T87X4j20oMs'),"
            "(5,'Dhaakad','https://www.youtube.com/watch?v=jP05InqSvbY')," 
            "(6,'Apna_Time_Aayega','https://www.youtube.com/watch?v=37kJXjkn7pA'),"
            "(7,'Pachtaoge','https://www.youtube.com/watch?v=xfU92LzhBws'),"
            "(8,'Brothers_Anthem','https://www.youtube.com/watch?v=lcs_GXu8IA0'),"
            "(9,'Yalgaar','https://www.youtube.com/watch?v=ANdqyUX5rho'),"
            "(10,'Jee_Karda','https://www.youtube.com/watch?v=57iE0s93kSQ'),"
            "(11,'Parwah_Nahi','https://www.youtube.com/watch?v=EcfMONkpZQ8'),"
            "(12,'Bezubaan_Phir_Se','https://www.youtube.com/watch?v=cmILxxuV2uw'),"
            "(13,'Sultan_Title_Song','https://www.youtube.com/watch?v=MrhJU7mnk58'),"
            "(14,'Dangal-Title_Track','https://www.youtube.com/watch?v=jMfvlh0tjyo'),"
            "(15,'Jagga_Jiteya','https://www.youtube.com/watch?v=nG3OBxYNWkE')")
x.commit()







