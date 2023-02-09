import random
import threading
from typing import Union

from sqlalchemy import BigInteger, Boolean, Column, Integer, String, UnicodeText

from KynanRobot.modules.helper_funcs.msg_types import Types
from KynanRobot.modules.sql import BASE, SESSION

DEFAULT_WELCOME = "Hei {first}, apa kabar?"
DEFAULT_GOODBYE = "Senang mengenalmu!"

DEFAULT_WELCOME_MESSAGES = [
    "{first} di sini!", 
    "Hii {first} Nimbrung ya",
    "Genos, {first} di sini.",
    "waww, liar {first} telah muncul.",
    "{first} datang seperti singa!",
    "{first} telah bergabung di pesta Anda.",
    "{first} baru bergabung. Bisakah saya mendapatkan kesembuhan??",
    "{first} baru saja bergabung dengan obrolan - asdgfhak!",
    "{first} baru bergabung. Semuanya, terlihat sibuk!",
    "Welcome, {first}. Tinggal sebentar dan dengarkan.",
    "Welcome, {first}. Kami mengharapkanmu ( ͡° ͜ʖ ͡°)",
    "Welcome, {first}. Kami harap Anda membawa pizza.",
    "Welcome, {first}. Tinggalkan senjatamu di dekat pintu.",
    "Swoooosh. {first} Baru saja mendarat ke group ini.",
    "Kuatkan dirimu. {first} baru saja bergabung dengan obrolan.",
    "{first} baru bergabung. Sembunyikan pisangmu.",
    "{first} baru saja tiba. Sepertinya OP - tolong nerf.",
    "{first} baru saja meluncur ke obrolan.",
    "{first} telah muncul di obrolan.",
    "SiBesar {first} telah muncul!",
    "welcome, {first} nimbrung di vcg yah.",
    "{first} melompat ke dalam obrolan. Kanguru!!",
    "{first} baru saja muncul. Pegang bir saya.",
    "Penantang! {first} telah muncul!",
    "Ini burung! Ini pesawat! Tidak apa-apa, hanya saja {first}.",
    "Ini {first}! Memuji matahari! \o/",
    "Tidak akan pernah memberi {first} ke atas. Tidak akan pernah membiarkan {first} turun.",
    "Ha! {first} telah bergabung! Anda mengaktifkan kartu jebakan saya!",
    "Hai! dengarkan! {first} telah bergabung!",
    "Kami telah menunggumu {first}",
    "Berbahaya untuk pergi sendiri, ambil {first}!",
    "{first} telah bergabung dengan obrolan! Ini sangat efektif!",
    "Semangat, cinta! {first} ada di sini!",
    "{first} ada di sini, seperti yang dinubuatkan.",
    "{first} telah tiba. Pesta selesai.",
    "{first} ada di sini untuk menendang pantat dan mengunyah permen karet. Dan {first} kehabisan permen karet.",
    "Halo. Apakah {first} yang Anda cari?",
    "{first} telah bergabung. Tunggu sebentar dan dengarkan!",
    "Mawar itu merah, violet itu biru, {first} bergabung dengan obrolan ini denganmu",
    "Selamat datang {first}, Hindari Pukulan jika Anda bisa!",
    "Itu burung! Ini pesawat! - Tidak, itu {first}!",
    "{first} Bergabung! - Oke.",  # Discord welcome messages end.
    "Semua Salam {first}!",
    "Hai, {first}. Jangan mengintai, hanya Villans yang melakukannya.",
    "{first} telah bergabung dengan bus pertempuran.",
    "Penantang baru masuk!",  # Tekken
    "Ok!",
    "{first} baru saja jatuh ke dalam obrolan!",
    "Sesuatu baru saja jatuh dari langit! - oh, itu {first}.",
    "{first} Baru saja diteleportasi ke dalam obrolan!",
    "Hai, {first}, tunjukkan Lisensi Hunter Anda!", # Hunter Hunter
    "Aku mencari Garo, oh tunggu nvm itu {first}.", # One Punch man s2
    "Pergi pergi {first}, Selamat pilihan!",
    "Jalankan Hutan! ..Maksudku...{first}.",
    "{first} lakukan 100 push-up, 100 sit-up, 100 squat, dan lari 10km SETIAP HARI!!!", # One Punch ma
    "Hah?\nApakah seseorang dengan tingkat bencana baru saja bergabung?\nOh, tunggu, ini cuma {first}.",  # One Punch ma
    "Hey, {first}, pernah dengar King Engine?", #One Punch ma
    "Hei, {first}, kosongkan kantongmu.",
    "Hei, {first}!, apakah kamu kuat?",
    "Panggil Avengers! - {first} baru saja bergabung dengan obrolan.",
    "{first} bergabung. Anda harus membangun tiang tambahan.",
    "Ermagherd. {first} ada di sini.",
    "Datang untuk Balap Siput, Tetap untuk Chimichangas!",
    "Siapa yang butuh Google? Anda adalah segalanya yang kami cari.",
    "Tempat ini harus memiliki WiFi gratis, karena saya merasakan koneksi.",
    "Bicaralah teman dan masuk.",
    "Selamat datang kamu",
    "Welcome {first}, putrimu ada di kastil lain.",
    "Hi {first}, Selamat Datang di sisi gelap.",
    "Hola {first}, waspadalah terhadap orang-orang dengan tingkat bencana",
    "Hey {first}, kami memiliki droid yang Anda cari.", "Dia {first}\Ini bukan tempat yang aneh, ini rumah saya, ini orang-orangnya yang aneh.", "Oh, hei {first} apa kata sandinya ?",
    "Hey {first}, Aku tahu apa yang akan kita lakukan hari ini",
    "{first} baru bergabung, waspada mereka bisa jadi mata-mata.",
    "{first} bergabung dengan grup, dibaca oleh Mark Zuckerberg, CIA dan 35 lainnya.",
    "Welcome {first}, awas monyet jatuh.",
    "Semuanya hentikan apa yang kalian lakukan, Kami sekarang di hadapan {first}.",
    "Hey {first}, Apakah Anda ingin tahu bagaimana saya mendapatkan bekas luka ini?",
    "Welcome {first}, jatuhkan senjata Anda dan lanjutkan ke pemindai mata-mata.",
    "Stay safe {first}, Jaga jarak sosial 3 meter antara pesan Anda.",  # Corona memes lmao
    "Hey {first}, Apakah Anda tahu saya pernah meninju meteorit?",
    "Kamu di sini sekarang {first}, Perlawanan sia-sia",
    "{first} baru saja tiba, kekuatannya kuat dengan yang ini.",
    "{first} baru saja bergabung atas perintah presiden.",
    "Hai {first}, gelasnya setengah penuh atau setengah kosong?",
    "Yipee {first} tiba.",
    "Welcome {first}, jika Anda seorang agen rahasia tekan 1, jika tidak, mulailah percakapan",
    "{first}, aku merasa kita tidak berada di Kansas lagi.",
    "Mereka mungkin mengambil hidup kita, tetapi mereka tidak akan pernah mengambil {first} kita.",
    "Pantainya jelas! Kalian bisa keluar guys, hanya saja {first}.",
    "Welcome {first}, tidak memperhatikan orang yang mengintai.",
    "Selamat datang {first}, semoga kekuatan menyertaimu.",
    "Semoga yang {first} bersamamu.",
    "{first} baru saja bergabung. Hei, di mana Perry?",
    "{first} baru saja bergabung. Oh, ini dia, Perry.",
    "Tuan-tuan dan nyonya-nyonya, saya berikan kepada Anda ...  {first}.",
    "Lihatlah skema jahat baruku, {first}-Inator.",
    "Ah, {first} si Platipus, kamu tepat pada waktunya... untuk terjebak.",
    "{first} baru saja tiba. Nonaktifkan Jambe!",  # One Piece Sanji
    "{first} baru saja tiba. Aschente!",  # No Game No Life
    "{first} katakan Aschente untuk bersumpah demi janji.",  # No Game No Life
    "{first} baru bergabung. apakah kamu membutuhkan hikari?",  # Steins Gate
    "Hiiiii Selamat datang {first}!",  # weeabo shit
    "Hi {first}, apa itu 1000-7?",  # tokyo ghoul
    "Datang. Saya tidak ingin menghancurkan tempat ini",  # hunter x hunter
    "Aku... aku... Shirohige!...tunggu..salah anime.",  # one Piece
    "Hey {first}...pernahkah kamu mendengar kata-kata ini??",  # BNHA
    "Tidak bisakah seorang pria tidur sebentar di sekitar sini??",  # Kamina Falls – Gurren Lagann
    "Saatnya seseorang menempatkanmu di tempatmu, {first}.",  # Hellsing
    "Unit-01 diaktifkan kembali..",  # Neon Genesis: Evangelion
    "Bersiaplah untuk masalah ... Dan buatlah menjadi dua kali lipat",  # Pokemon
    "Hey {first}, apakah Anda Menantang Saya??",  # Shaggy
    "Oh? Anda Mendekati Saya?",  # jojo
    "hei lihatlah owner saya @JustRex?",  # jojo jap ver
    "Aku tidak bisa mengalahkanmu tanpa mendekat",  # jojo
    "Hoho! Lalu datanglah sedekat yang kamu mau.", #jojo
    "Hoho! Dewa juubun chikazukanai youi", #jojo jap ver
    "Tebak siapa yang selamat dari waktunya di Neraka, {first}.",  # jojo
    "Berapa banyak roti yang kamu makan seumur hidupmu?", #jojo
    "Apa katamu? Tergantung jawabanmu, aku mungkin harus menghajarmu!", #jojo
    "Oh? Kamu mendekatiku? selamat datang?",  # jojo
    "Apa yang kamu cari digroup ini? btw Selamat datang",  # jojo
    "{first} baru saja masuk ke grup!",
    "hell yeeahhh, {first} sudah masuk group ini.",
    "Sugoi, Dekai. {first} bergabung!",
    "{first}, apakah kamu tahu dewa kematian menyukai apel?",  # Death Note owo
    "Saya akan mengambil keripik kentang .... dan memakannya",  # Death Note owo
    "lariiiii {first} sudah datang!",  # Tokyo Ghoul
    "selamat datang 😊.",  # op
    "{first} baru bergabung! Persneling kedua!",  # Op
    "Omae wa mou....shindeiru",
    "Hey {first}, Teratai desa daun mekar dua kali!",  # Naruto stuff begins from here
    "{first} Bergabung! omote renge!",
    "{first}! Saya, Madara! nyatakan kamu yang terkuat",
    "{first}, kali ini aku akan meminjamkanmu kekuatanku. ",  # Kyuubi to naruto
    "{first}, selamat datang di desa konoha!",  # Naruto thingies end here
    "Di hutan, Anda harus menunggu ... sampai dadu membaca lima atau delapan.",  # Jumanji stuff
    "Dr.{first} Arkeolog terkenal dan penjelajah internasional,\nSelamat datang di Jumanji!\nNasib Jumanji terserah Anda sekarang.",
    "{first}, ini tidak akan menjadi misi yang mudah - monyet memperlambat ekspedisi.",  # End of Jumanji stuff
    "Ingat, ingat, Tanggal Lima November, Pengkhianatan dan Plot Bubuk Mesiu. Saya tidak tahu alasan mengapa Pengkhianatan Bubuk Mesiu harus dilupakan.", # V for Vendetta
    "Selamat Datang Digroup ini",  # V for Vendetta
    "Di belakang {first} ada lebih dari sekedar daging. Di bawah pengguna ini ada sebuah ide... dan ide adalah antipeluru.", # V for Vendetta
    "Cintai amarahmu, bukan sangkarmu.",  # V for Vendetta
    "Singkirkan cakar baumu dariku, dasar kera kotor!", # Planet kera
    "selamat datang, sayangku {first}.",
    "Dia sekarang ada digroup - {first}.",
    "huuu. {first} selamat datang",
    "Ikutlah denganku jika kamu ingin hidup",
]
DEFAULT_GOODBYE_MESSAGES = [
    "{first} akan dirindukan.",
    "{first} baru saja offline.",
    "{first} telah meninggalkan group.",
    "{first} telah meninggalkan group.",
    "{first} telah meninggalkan group.",
    "{first} telah meninggalkan daerah ini",
    "{first} lari dari kenyataan.",
    "Senang mengenalmu, selamat tinggal, {first}!",
    "itu merupakan waktu yang menyenangkan, goodbye {first}.",
    "Kami berharap dapat melihat Anda lagi segera, {first}.",
    "Aku ingin mengucapkan selamat tinggal, {first}.",
    "Goodbye {first}! Tebak siapa yang akan merindukanmu :')",
    "Goodbye {first}! Ini akan menjadi kesepian tanpamu.",
    "Tolong jangan tinggalkan aku sendiri di tempat ini, {first}!",
    "Semoga berhasil menemukan group asik yang lebih baik dari kami, {first}!",
    "Anda tahu kami akan merindukanmu {first}. Benar? Benar? Benar?",
    "Selamat, {first}! Anda resmi bebas dari kekacauan ini.",
    "{first}. Anda adalah lawan yang layak diperjuangkan.",
    "kamu pergi, {first}? {first} telah meninggalkan group.",
    "Bawa dia fotonya",
    "silahlan pergi!!!",
    "Babay {first}",
    "Keluar lo sono!",
    "Kenapa cepat Sekali keluar?",
    "Apakah Kamu harus keluar group?",
    "KELUAR LO SONO!",
    "BABAYYY",
    "Dia sudah pergi",
    "Dia pergi",
    "Keluar keluar keluarr",
    "Apakah secepat itu kamu pergi?",
    "Keluar",
    "Temui orang asing tanpa prasangka",
    "Orang yang digantung tidak akan membawa keberuntungan untukmu hari ini",
    "Apa yang ingin kamu lakukan hari ini?",
    "Kamu gelap di dalam",
    "Pernahkah Anda melihat pintu keluar?",
    "Kenapa ga dari dulu keluarnya?.",
    "Selamat menempuh Hidup baru.",
    "Anda salah memainkannya, beri saya pengontrolnya",
    "Percayalah pada orang baik",
    "Hidup untuk mati.",
    "Selamat Tinggal",
    "Yah, itu tidak berharga",
    "Saya ketiduran!",
    "Semoga banyak masalahmu",
    "Hidup lamamu hancur",
    "Selalu lihat sisi baiknya",
    "Berbahaya untuk pergi sendirian",
    "Kamu tidak akan pernah dimaafkan",
    "Anda tidak memiliki siapa pun untuk disalahkan kecuali diri Anda sendiri",
    "Si jelek keluar group",
    "Si Jomblo keluar group",
    "Tidak ada yang tahu masalah yang Anda lihat",
    "Kamu terlihat gemuk kamu harus lebih banyak berolahraga",
    "apakah group ini jelek, sampai kamu sekarang keluar?",
    "Kenapa begitu biru?",
    "Iblis yang menyamar",
    "Sudah pergi dan tak kembali",
    "SILAHKAN PERGI JANGAN KEMBALI",
]
# Line 111 to 152 are references from https://bindingofisaac.fandom.com/wiki/Fortune_Telling_Machine


class Welcome(BASE):
    __tablename__ = "welcome_pref"
    chat_id = Column(String(14), primary_key=True)
    should_welcome = Column(Boolean, default=True)
    should_goodbye = Column(Boolean, default=True)
    custom_content = Column(UnicodeText, default=None)

    custom_welcome = Column(
        UnicodeText, default=random.choice(DEFAULT_WELCOME_MESSAGES)
    )
    welcome_type = Column(Integer, default=Types.TEXT.value)

    custom_leave = Column(UnicodeText, default=random.choice(DEFAULT_GOODBYE_MESSAGES))
    leave_type = Column(Integer, default=Types.TEXT.value)

    clean_welcome = Column(BigInteger)

    def __init__(self, chat_id, should_welcome=True, should_goodbye=True):
        self.chat_id = chat_id
        self.should_welcome = should_welcome
        self.should_goodbye = should_goodbye

    def __repr__(self):
        return "<Chat {} should Welcome new users: {}>".format(
            self.chat_id, self.should_welcome
        )


class WelcomeButtons(BASE):
    __tablename__ = "welcome_urls"
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(String(14), primary_key=True)
    name = Column(UnicodeText, nullable=False)
    url = Column(UnicodeText, nullable=False)
    same_line = Column(Boolean, default=False)

    def __init__(self, chat_id, name, url, same_line=False):
        self.chat_id = str(chat_id)
        self.name = name
        self.url = url
        self.same_line = same_line


class GoodbyeButtons(BASE):
    __tablename__ = "leave_urls"
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(String(14), primary_key=True)
    name = Column(UnicodeText, nullable=False)
    url = Column(UnicodeText, nullable=False)
    same_line = Column(Boolean, default=False)

    def __init__(self, chat_id, name, url, same_line=False):
        self.chat_id = str(chat_id)
        self.name = name
        self.url = url
        self.same_line = same_line


class WelcomeMute(BASE):
    __tablename__ = "welcome_mutes"
    chat_id = Column(String(14), primary_key=True)
    welcomemutes = Column(UnicodeText, default=False)

    def __init__(self, chat_id, welcomemutes):
        self.chat_id = str(chat_id)  # ensure string
        self.welcomemutes = welcomemutes


class WelcomeMuteUsers(BASE):
    __tablename__ = "human_checks"
    user_id = Column(Integer, primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    human_check = Column(Boolean)

    def __init__(self, user_id, chat_id, human_check):
        self.user_id = user_id  # ensure string
        self.chat_id = str(chat_id)
        self.human_check = human_check


class CleanServiceSetting(BASE):
    __tablename__ = "clean_service"
    chat_id = Column(String(14), primary_key=True)
    clean_service = Column(Boolean, default=True)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)

    def __repr__(self):
        return "<Chat used clean service ({})>".format(self.chat_id)


Welcome.__table__.create(checkfirst=True)
WelcomeButtons.__table__.create(checkfirst=True)
GoodbyeButtons.__table__.create(checkfirst=True)
WelcomeMute.__table__.create(checkfirst=True)
WelcomeMuteUsers.__table__.create(checkfirst=True)
CleanServiceSetting.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()
WELC_BTN_LOCK = threading.RLock()
LEAVE_BTN_LOCK = threading.RLock()
WM_LOCK = threading.RLock()
CS_LOCK = threading.RLock()


def welcome_mutes(chat_id):
    try:
        welcomemutes = SESSION.query(WelcomeMute).get(str(chat_id))
        if welcomemutes:
            return welcomemutes.welcomemutes
        return False
    finally:
        SESSION.close()


def set_welcome_mutes(chat_id, welcomemutes):
    with WM_LOCK:
        prev = SESSION.query(WelcomeMute).get((str(chat_id)))
        if prev:
            SESSION.delete(prev)
        welcome_m = WelcomeMute(str(chat_id), welcomemutes)
        SESSION.add(welcome_m)
        SESSION.commit()


def set_human_checks(user_id, chat_id):
    with INSERTION_LOCK:
        human_check = SESSION.query(WelcomeMuteUsers).get((user_id, str(chat_id)))
        if not human_check:
            human_check = WelcomeMuteUsers(user_id, str(chat_id), True)

        else:
            human_check.human_check = True

        SESSION.add(human_check)
        SESSION.commit()

        return human_check


def get_human_checks(user_id, chat_id):
    try:
        human_check = SESSION.query(WelcomeMuteUsers).get((user_id, str(chat_id)))
        if not human_check:
            return None
        human_check = human_check.human_check
        return human_check
    finally:
        SESSION.close()


def get_welc_mutes_pref(chat_id):
    welcomemutes = SESSION.query(WelcomeMute).get(str(chat_id))
    SESSION.close()

    if welcomemutes:
        return welcomemutes.welcomemutes

    return False


def get_welc_pref(chat_id):
    welc = SESSION.query(Welcome).get(str(chat_id))
    SESSION.close()
    if welc:
        return (
            welc.should_welcome,
            welc.custom_welcome,
            welc.custom_content,
            welc.welcome_type,
        )

    else:
        # Welcome by default.
        return True, DEFAULT_WELCOME, None, Types.TEXT


def get_gdbye_pref(chat_id):
    welc = SESSION.query(Welcome).get(str(chat_id))
    SESSION.close()
    if welc:
        return welc.should_goodbye, welc.custom_leave, welc.leave_type
    else:
        # Welcome by default.
        return True, DEFAULT_GOODBYE, Types.TEXT


def set_clean_welcome(chat_id, clean_welcome):
    with INSERTION_LOCK:
        curr = SESSION.query(Welcome).get(str(chat_id))
        if not curr:
            curr = Welcome(str(chat_id))

        curr.clean_welcome = int(clean_welcome)

        SESSION.add(curr)
        SESSION.commit()


def get_clean_pref(chat_id):
    welc = SESSION.query(Welcome).get(str(chat_id))
    SESSION.close()

    if welc:
        return welc.clean_welcome

    return False


def set_welc_preference(chat_id, should_welcome):
    with INSERTION_LOCK:
        curr = SESSION.query(Welcome).get(str(chat_id))
        if not curr:
            curr = Welcome(str(chat_id), should_welcome=should_welcome)
        else:
            curr.should_welcome = should_welcome

        SESSION.add(curr)
        SESSION.commit()


def set_gdbye_preference(chat_id, should_goodbye):
    with INSERTION_LOCK:
        curr = SESSION.query(Welcome).get(str(chat_id))
        if not curr:
            curr = Welcome(str(chat_id), should_goodbye=should_goodbye)
        else:
            curr.should_goodbye = should_goodbye

        SESSION.add(curr)
        SESSION.commit()


def set_custom_welcome(
    chat_id, custom_content, custom_welcome, welcome_type, buttons=None
):
    if buttons is None:
        buttons = []

    with INSERTION_LOCK:
        welcome_settings = SESSION.query(Welcome).get(str(chat_id))
        if not welcome_settings:
            welcome_settings = Welcome(str(chat_id), True)

        if custom_welcome or custom_content:
            welcome_settings.custom_content = custom_content
            welcome_settings.custom_welcome = custom_welcome
            welcome_settings.welcome_type = welcome_type.value

        else:
            welcome_settings.custom_welcome = DEFAULT_WELCOME
            welcome_settings.welcome_type = Types.TEXT.value

        SESSION.add(welcome_settings)

        with WELC_BTN_LOCK:
            prev_buttons = (
                SESSION.query(WelcomeButtons)
                .filter(WelcomeButtons.chat_id == str(chat_id))
                .all()
            )
            for btn in prev_buttons:
                SESSION.delete(btn)

            for b_name, url, same_line in buttons:
                button = WelcomeButtons(chat_id, b_name, url, same_line)
                SESSION.add(button)

        SESSION.commit()


def get_custom_welcome(chat_id):
    welcome_settings = SESSION.query(Welcome).get(str(chat_id))
    ret = DEFAULT_WELCOME
    if welcome_settings and welcome_settings.custom_welcome:
        ret = welcome_settings.custom_welcome

    SESSION.close()
    return ret


def set_custom_gdbye(chat_id, custom_goodbye, goodbye_type, buttons=None):
    if buttons is None:
        buttons = []

    with INSERTION_LOCK:
        welcome_settings = SESSION.query(Welcome).get(str(chat_id))
        if not welcome_settings:
            welcome_settings = Welcome(str(chat_id), True)

        if custom_goodbye:
            welcome_settings.custom_leave = custom_goodbye
            welcome_settings.leave_type = goodbye_type.value

        else:
            welcome_settings.custom_leave = DEFAULT_GOODBYE
            welcome_settings.leave_type = Types.TEXT.value

        SESSION.add(welcome_settings)

        with LEAVE_BTN_LOCK:
            prev_buttons = (
                SESSION.query(GoodbyeButtons)
                .filter(GoodbyeButtons.chat_id == str(chat_id))
                .all()
            )
            for btn in prev_buttons:
                SESSION.delete(btn)

            for b_name, url, same_line in buttons:
                button = GoodbyeButtons(chat_id, b_name, url, same_line)
                SESSION.add(button)

        SESSION.commit()


def get_custom_gdbye(chat_id):
    welcome_settings = SESSION.query(Welcome).get(str(chat_id))
    ret = DEFAULT_GOODBYE
    if welcome_settings and welcome_settings.custom_leave:
        ret = welcome_settings.custom_leave

    SESSION.close()
    return ret


def get_welc_buttons(chat_id):
    try:
        return (
            SESSION.query(WelcomeButtons)
            .filter(WelcomeButtons.chat_id == str(chat_id))
            .order_by(WelcomeButtons.id)
            .all()
        )
    finally:
        SESSION.close()


def get_gdbye_buttons(chat_id):
    try:
        return (
            SESSION.query(GoodbyeButtons)
            .filter(GoodbyeButtons.chat_id == str(chat_id))
            .order_by(GoodbyeButtons.id)
            .all()
        )
    finally:
        SESSION.close()


def clean_service(chat_id: Union[str, int]) -> bool:
    try:
        chat_setting = SESSION.query(CleanServiceSetting).get(str(chat_id))
        if chat_setting:
            return chat_setting.clean_service
        return False
    finally:
        SESSION.close()


def set_clean_service(chat_id: Union[int, str], setting: bool):
    with CS_LOCK:
        chat_setting = SESSION.query(CleanServiceSetting).get(str(chat_id))
        if not chat_setting:
            chat_setting = CleanServiceSetting(chat_id)

        chat_setting.clean_service = setting
        SESSION.add(chat_setting)
        SESSION.commit()


def migrate_chat(old_chat_id, new_chat_id):
    with INSERTION_LOCK:
        chat = SESSION.query(Welcome).get(str(old_chat_id))
        if chat:
            chat.chat_id = str(new_chat_id)

        with WELC_BTN_LOCK:
            chat_buttons = (
                SESSION.query(WelcomeButtons)
                .filter(WelcomeButtons.chat_id == str(old_chat_id))
                .all()
            )
            for btn in chat_buttons:
                btn.chat_id = str(new_chat_id)

        with LEAVE_BTN_LOCK:
            chat_buttons = (
                SESSION.query(GoodbyeButtons)
                .filter(GoodbyeButtons.chat_id == str(old_chat_id))
                .all()
            )
            for btn in chat_buttons:
                btn.chat_id = str(new_chat_id)

        SESSION.commit()
