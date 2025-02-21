import pygame, os, random
from dict import streak_mul
import webbrowser

WIDTH = 800
HEIGHT = 620
card_gap = 10
card_width_number = 6
card_height_number = 5
point = 10
FPS = 60

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Where's my replica?")

bg_img = pygame.transform.scale(pygame.image.load(os.path.join("img\Other", "bg.jpg")).convert_alpha(), (WIDTH, HEIGHT))
_2_P_Btn = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "2_P_Btn.png")).convert_alpha(), (96, 72))
mouse_dot_img = pygame.image.load(os.path.join("img\Other", "mouse_dot.png"))
card_back_img = pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_Back", "Card_Back_1.png")).convert_alpha(), (72, 112))
P1_avt = pygame.transform.scale(pygame.image.load(os.path.join("img\Other", "P1_avt.png")).convert_alpha(), (90, 90))
P2_avt = pygame.transform.scale(pygame.image.load(os.path.join("img\Other", "P2_avt.png")).convert_alpha(), (90, 90))
streak_name = [0, "streak_1.png"]
streak_name.extend(["streak_" + str(i) + ".png" for i in range(2, 16)])
crown_img = pygame.transform.scale(pygame.image.load(os.path.join("img\Other", "crown.png")).convert_alpha(), (165, 180))
home_btn = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "home_btn.png")).convert_alpha(), (70, 59))
replay_btn = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "replay_btn.png")).convert_alpha(), (70, 59))
gray_label = pygame.image.load(os.path.join("img\Other", "gray_label.png"))
back_btn = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "back_btn.png")).convert_alpha(), (70, 59))
option_btn = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "option_btn.png")).convert_alpha(), (70, 59))
sign_img = pygame.transform.scale(pygame.image.load(os.path.join("img\Other", "sign.png")).convert_alpha(), (360, 200))
yes_checkbox = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "yes_checkbox.png")).convert_alpha(), (24, 24))
no_checkbox = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "no_checkbox.png")).convert_alpha(), (24, 24))
sign_2_img = pygame.transform.scale(pygame.image.load(os.path.join("img\Other", "sign_2.png")).convert_alpha(), (160, 100))
pause_btn_img = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "pause_btn.png")).convert_alpha(), (70, 59))
about_us_img = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "about_us.png")).convert_alpha(), (60, 25))
resume_btn_img = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "resume_btn.png")).convert_alpha(), (70, 59))
menu_banner = pygame.transform.scale(pygame.image.load(os.path.join("img\Other", "menu_banner.png")).convert_alpha(), (540, 180))
bot_btn = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "bot.png")).convert_alpha(), (96, 72))
bot_easy_btn = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "easy.png")).convert_alpha(), (96, 72))
bot_normal_btn = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "normal.png")).convert_alpha(), (96, 72))
bot_hard_btn = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "hard.png")).convert_alpha(), (96, 72))
_1_P_Btn = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "1_P_Btn.png")).convert_alpha(), (96, 72))
score_board = pygame.transform.scale(pygame.image.load(os.path.join("img\Other", "score_board.png")).convert_alpha(), (200, 180))
score_table = pygame.transform.scale(pygame.image.load(os.path.join("img\Other", "record_table.png")).convert_alpha(), (350, 220))

gray_label.set_alpha(200)
_2_P_Btn.set_colorkey((215, 241, 242))
home_btn.set_colorkey((215, 241, 242))
replay_btn.set_colorkey((215, 241, 242))
back_btn.set_colorkey((215, 241, 242))
option_btn.set_colorkey((215, 241, 242))
pause_btn_img.set_colorkey((215, 241, 242))
mouse_dot_img.set_colorkey((255, 255, 255))
card_back_img.set_colorkey((255, 255, 255))
P1_avt.set_colorkey((255, 255, 255))
P2_avt.set_colorkey((255, 255, 255))
crown_img.set_colorkey((255, 255, 255))
sign_img.set_colorkey((255, 255, 255))
yes_checkbox.set_colorkey((0, 0, 0))
no_checkbox.set_colorkey((0, 0, 0))
sign_2_img.set_colorkey((255, 255, 255))
resume_btn_img.set_colorkey((0, 0, 0))
menu_banner.set_colorkey((255, 255, 255))
about_us_img.set_colorkey((255, 255, 255))
bot_btn.set_colorkey((215, 241, 242))
bot_easy_btn.set_colorkey((215, 241, 242))
bot_normal_btn.set_colorkey((215, 241, 242))
bot_hard_btn.set_colorkey((215, 241, 242))
_1_P_Btn.set_colorkey((215, 241, 242))

Btn_2P_mask = pygame.mask.from_surface(_2_P_Btn)
mouse_dot_mask = pygame.mask.from_surface(mouse_dot_img)
card_back_mask = pygame.mask.from_surface(card_back_img)
home_btn_mask = pygame.mask.from_surface(home_btn)
replay_btn_mask = pygame.mask.from_surface(replay_btn)
back_btn_mask = pygame.mask.from_surface(back_btn)
option_btn_mask = pygame.mask.from_surface(option_btn)
pause_btn_mask = pygame.mask.from_surface(pause_btn_img)
checkbox_mask = pygame.mask.from_surface(yes_checkbox)
about_us_mask = pygame.mask.from_surface(about_us_img)
resume_btn_mask = pygame.mask.from_surface(resume_btn_img)
bot_btn_mask = pygame.mask.from_surface(bot_btn)
bot_easy_btn_mask = pygame.mask.from_surface(bot_easy_btn)
bot_normal_btn_mask = pygame.mask.from_surface(bot_normal_btn)
bot_hard_btn_mask = pygame.mask.from_surface(bot_hard_btn)
Btn_1P_mask = pygame.mask.from_surface(_1_P_Btn)

start_card_pos = (WIDTH // 2 - (card_width_number // 2) * (card_back_img.get_width() + card_gap) - card_gap // 2, HEIGHT // 2 - ((card_height_number) * card_back_img.get_height() + (card_height_number - 1) * card_gap) // 2)

card_rotation = []
card_rotation.append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_Back", "Card_Back_1.png")).convert_alpha(), (72, 112)))
card_rotation.append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_Back", "Card_Back_2.png")).convert_alpha(), (int(72 * 0.95), 112)))
card_rotation.append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_Back", "Card_Back_3.png")).convert_alpha(), (int(72 * 0.95 * 0.95), 112)))
card_rotation.append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_Back", "Card_Back_4.png")).convert_alpha(), (int(72 * 0.95 * 0.95 * 0.79), 112)))
card_rotation.append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_Back", "Card_Back_5.png")).convert_alpha(), (int(72 * 0.95 * 0.95 * 0.79 * 0.82), 112)))
card_rotation.append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_Back", "Card_Back_6.png")).convert_alpha(), (int(72 * 0.95 * 0.95 * 0.79 * 0.82 * 0.59), 112)))
card_rotation.append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_Back", "Card_Back_7.png")).convert_alpha(), (int(72 * 0.95 * 0.95 * 0.79 * 0.82 * 0.59 * 0.53), 112)))

card_rotation_sprites = [card_rotation[:] for i in range(15)]

for i in range(15) :
    card_rotation_sprites[i].append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_" + str(i), "Card_" + str(i) + "_1.png")).convert_alpha(), (int(72 * 0.95 * 0.95 * 0.79 * 0.82 * 0.59 * 0.53), 112)))
    card_rotation_sprites[i].append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_" + str(i), "Card_" + str(i) + "_2.png")).convert_alpha(), (int(72 * 0.95 * 0.95 * 0.79 * 0.82 * 0.59), 112)))
    card_rotation_sprites[i].append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_" + str(i), "Card_" + str(i) + "_3.png")).convert_alpha(), (int(72 * 0.95 * 0.95 * 0.79 * 0.82), 112)))
    card_rotation_sprites[i].append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_" + str(i), "Card_" + str(i) + "_4.png")).convert_alpha(), (int(72 * 0.95 * 0.95 * 0.79), 112)))
    card_rotation_sprites[i].append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_" + str(i), "Card_" + str(i) + "_5.png")).convert_alpha(), (int(72 * 0.95 * 0.95), 112)))
    card_rotation_sprites[i].append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_" + str(i), "Card_" + str(i) + "_6.png")).convert_alpha(), (int(72 * 0.95), 112)))
    card_rotation_sprites[i].append(pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_" + str(i), "Card_" + str(i) + "_7.png")).convert_alpha(), (72, 112)))

disappear_effect = [pygame.transform.scale(pygame.image.load(os.path.join("img\Effect", "Disappear_" + str(i) + ".jpg")).convert_alpha(), (60, 60)) for i in range(3)]

screenshot = 0

for i in range(3) :
    disappear_effect[i].set_colorkey((152, 152, 152))

music_choice = random.randint(0, 2)
pygame.mixer.music.load(os.path.join("sound", "background_" + str(music_choice) + ".mp3"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

music_list = [0, 0, 0]
music_list[music_choice] = 1
music_name = ['Lifelike', 'Inspiring Cinematic Ambient', 'Chill Abstract Intention']
music_file_name = ['Background_' + str(i) + '.mp3' for i in range(3)]

flip_card_sound = pygame.mixer.Sound(os.path.join("sound", "flipcard.mp3"))
score_sound = pygame.mixer.Sound(os.path.join("sound", "score.mp3"))
card_appear_sound = pygame.mixer.Sound(os.path.join("sound", "card_appear.mp3"))

flip_card_sound.set_volume(10)
score_sound.set_volume(10)
card_appear_sound.set_volume(16)

state = 'menu'
game_mode = 0

max_turn = [50, 35, 25]
turn_left = 0
current_1P_diff = 0
record_1P = [0, 0, 0]
record_Bot = [0, 0, 0]
score_per_turn_left = 2
diff_score = [50, 100, 200]
change_dict = {2 : 0,
               5 : 1,
               8 : 2}

current_bot_diff = 0

card_table = []

class Card :
    max_reveal_duration = FPS // 2
    max_revealing = 28
    appear_gap = 2
    max_appear_duration = ((card_height_number - 1) * (card_height_number + 1) + (card_width_number - 1) + 1) * appear_gap

    def __init__(self, id, pos, pixel_pos, image, isRevealed, size) :
        self.id = id
        self.pos = pos
        self.pixel_pos = pixel_pos
        self.image = image
        self.isRevealed = isRevealed
        self.size = size
        self.reveal_duration = 0
        self.reveal_change = 0
        self.revealing_duration = 0
        self.isRevealing = 0
        self.isHidden = 0
        if id >= 0 :
            self.image = pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_" + str(id), "Card_" + str(id) + "_7.png")).convert_alpha(), card_back_img.get_size())
        self.appear_animation_count = 0

    def __eq__(self, other) :
        return self.id == other.id and self.pos == other.pos

class Streak_Effect :
    duration = FPS // 2

    def __init__(self, streak_count, pos) :
        self.streak_count = streak_count
        self.pos = pos
        if streak_count == 1 :
            self.max_width = 60
        else :
            self.max_width = 100
        self.max_height = 30
        self.width = 0
        self.height = 0

    def update(self) :
        self.width += (self.max_width / Streak_Effect.duration)
        self.height += (self.max_height / Streak_Effect.duration)
        return (int(self.width), int(self.height))

class Disappear_Effect :
    base = 6
    max_duration = len(disappear_effect) * base

    def __init__(self, pos) :
        self.pos = pos
        self.duration = 0

class Score_Effect :

    def __init__(self, pos, score) :
        FONT = pygame.font.SysFont("consolas", 20)
        self.score_render = FONT.render("+" + str(score), True, (252, 140, 39))
        self.pos = pos
        self.duration = 0
        self.max_duration = FPS // 3

class Bot :

    def __init__(self, len) :
        self.id_memories = [-1 for _ in range(len * 2)]
        self.card_memories = [Null_Card[0] for _ in range(len * 2)]
        self.choices = [Null_Card[0], Null_Card[0]]
        self.cd = FPS
        self.max_cd = FPS
        self.cursor = 0

    def calc_choices(self) :
        global card_table
        for i in range(len(self.id_memories)) :
            if self.id_memories[i] != -1 :
                if self.id_memories.count(self.id_memories[i]) == 2 and self.card_memories.count(self.card_memories[i]) == 1 :
                    self.choices[0] = self.card_memories[i]
                    tmp_id = self.id_memories[i]
                    self.id_memories[i] = -1
                    self.card_memories[i] = Null_Card[0]
                    self.choices[1] = self.card_memories[self.id_memories.index(tmp_id)]
                    tmp_index = self.id_memories.index(tmp_id)
                    self.id_memories[tmp_index] = -1
                    self.card_memories[tmp_index] = Null_Card[0]
                    break

        if self.choices[1] != Null_Card[0] :
            return
        while (True) :
            self.choices[0] = random.choice(card_table)
            if not self.card_memories.count(self.choices[0]) :
                break
        if self.id_memories.count(self.choices[0].id) :
            self.choices[1] = self.card_memories[self.id_memories.index(self.choices[0].id)]
            tmp_index = self.id_memories.index(self.choices[0].id)
            self.id_memories[tmp_index] = -1
            self.card_memories[tmp_index] = Null_Card[0]
        else :
            while (True) :
                self.choices[1] = random.choice(card_table)
                if not self.card_memories.count(self.choices[1]) and self.choices[0] != self.choices[1] :
                    break

score_effects = []

current_turn = 1

base_card = []
base_list = [i for i in range(40)]

for i in range(15) :
    base_card.append(Card(i, (0, 0), (0, 0), card_back_img, 0, card_back_img.get_size()))
    base_card.append(Card(i, (0, 0), (0, 0), card_back_img, 0, card_back_img.get_size()))

def interact_obj(mx, my, obj_rect) :
    if mx > obj_rect[0] + obj_rect[2] or mx < obj_rect[0] :
        return False
    if my > obj_rect[1] + obj_rect[3] or my < obj_rect[1] :
        return False
    return True

def menu() :
    global running, state, card_table, game_mode

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == pygame.BUTTON_LEFT :
                if mouse_dot_mask.overlap_area(Btn_2P_mask, ((WIDTH - _2_P_Btn.get_width()) // 2 - mx, 480 - _2_P_Btn.get_height() // 2 - my)) :
                    state = 'play_2P'
                    card_table = shuffle_card()
                    pygame.mouse.set_cursor(0)
                    reset_2P()
                    card_appear_sound.play(1)
                    return
                if mouse_dot_mask.overlap_area(bot_btn_mask, ((WIDTH - bot_btn.get_width()) // 2 - mx, 400 - bot_btn.get_height() // 2 - my)) :
                    state = 'choose_difficult'
                    game_mode = 'vsBot'
                    return
                if mouse_dot_mask.overlap_area(Btn_1P_mask, ((WIDTH - _1_P_Btn.get_width()) // 2 - mx, 320 - _1_P_Btn.get_height() // 2 - my)) :
                    state = 'choose_difficult'
                    game_mode = 'play_1P'
                    return
                if mouse_dot_mask.overlap_area(option_btn_mask, (WIDTH - option_btn.get_width() - 10 - mx, 10 - my)) :
                    state = 'option'
                    return
                if interact_obj(mx, my, [10, HEIGHT - about_us_img.get_height() - 10, *about_us_img.get_size()]) :
                    webbrowser.open("www.grsos.wordpress.com")

    window.blit(bg_img, (0, 0))
    window.blit(option_btn, (WIDTH - option_btn.get_width() - 10, 10))

    window.blit(about_us_img, (10, HEIGHT - about_us_img.get_height() - 10))
    window.blit(menu_banner, ((WIDTH - menu_banner.get_width()) // 2, 50))

    interact = 0

    if mouse_dot_mask.overlap_area(Btn_2P_mask, ((WIDTH - _2_P_Btn.get_width()) // 2 - mx, 480 - _2_P_Btn.get_height() // 2 - my)) :
        interact = 1
        tmp_Btn_2P = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "2_P_Btn.png")).convert_alpha(), (96 * 1.2, 72 * 1.2))
        tmp_Btn_2P.set_colorkey((215, 241, 242))
        window.blit(tmp_Btn_2P, ((WIDTH - tmp_Btn_2P.get_width()) // 2, 480 - tmp_Btn_2P.get_height() // 2))
    else :
        window.blit(_2_P_Btn, ((WIDTH - _2_P_Btn.get_width()) // 2, 480 - _2_P_Btn.get_height() // 2))

    if mouse_dot_mask.overlap_area(bot_btn_mask, ((WIDTH - bot_btn.get_width()) // 2 - mx, 400 - bot_btn.get_height() // 2 - my)) :
        interact = 1
        tmp_bot_btn = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "bot.png")).convert_alpha(), (96 * 1.2, 72 * 1.2))
        tmp_bot_btn.set_colorkey((215, 241, 242))
        window.blit(tmp_bot_btn, ((WIDTH - tmp_bot_btn.get_width()) // 2, 400 - tmp_bot_btn.get_height() // 2))
    else :
        window.blit(bot_btn, ((WIDTH - bot_btn.get_width()) // 2, 400 - bot_btn.get_height() // 2))

    if mouse_dot_mask.overlap_area(Btn_1P_mask, ((WIDTH - _1_P_Btn.get_width()) // 2 - mx, 320 - _1_P_Btn.get_height() // 2 - my)) :
        interact = 1
        tmp_1P_btn = pygame.transform.scale(pygame.image.load(os.path.join("img\Button", "1_P_Btn.png")).convert_alpha(), (96 * 1.2, 72 * 1.2))
        tmp_1P_btn.set_colorkey((215, 241, 242))
        window.blit(tmp_1P_btn, ((WIDTH - tmp_1P_btn.get_width()) // 2, 320 - tmp_1P_btn.get_height() // 2))
    else :
        window.blit(_1_P_Btn, ((WIDTH - _1_P_Btn.get_width()) // 2, 320 - _1_P_Btn.get_height() // 2))

    if mouse_dot_mask.overlap_area(option_btn_mask, (WIDTH - option_btn.get_width() - 10 - mx, 10 - my)) :
        interact = 1
    if interact_obj(mx, my, [10, HEIGHT - about_us_img.get_height() - 10, *about_us_img.get_size()]):
        interact = 1
    if interact :
        pygame.mouse.set_cursor(11)
    else :
        pygame.mouse.set_cursor(0)

    pygame.display.update()

def shuffle_card() :
    global base_card, base_list

    base_list = [i for i in range(40)]
    base_card = []

    for i in range(15):
        base_card.append(Card(i, (0, 0), (0, 0), card_back_img, 0, card_back_img.get_size()))
        base_card.append(Card(i, (0, 0), (0, 0), card_back_img, 0, card_back_img.get_size()))

    tmp_list = base_list[0 : card_height_number * card_width_number]
    random.shuffle(tmp_list)
    random.shuffle(tmp_list)

    tmp_card = base_card[0 : card_height_number * card_width_number]
    for i in range(card_height_number) :
        for j in range(card_width_number) :
            tmp_card[tmp_list[i * (card_height_number + 1) + j]].pos = (i, j)
            tmp_card[tmp_list[i * (card_height_number + 1) + j]].pixel_pos = (start_card_pos[0] + (card_back_img.get_width() + card_gap) * j, start_card_pos[1] + (card_back_img.get_height() + card_gap) * i)
            tmp_card[tmp_list[i * (card_height_number + 1) + j]].appear_duration = (i * (card_height_number + 1) + j + 1) * Card.appear_gap

    return tmp_card

Null_Card = []
Null_Card.append(Card(-1, (0, 0), (0, 0), card_back_img, 0, (0, 0)))

checkbox_list = [yes_checkbox, no_checkbox]

score = [0, 0]
turn = 0
current_streak = 0
music_state = 0
FirstCard = Null_Card[:][0]
SecondCard = Null_Card[:][0]
streak_effects = []
disappear_effects = []

def reset_2P() :
    global score, turn, current_streak, FirstCard, SecondCard, unClickable, streak_effects, disappear_effects
    score = [0, 0]
    turn = 0
    current_streak = 0
    FirstCard = Null_Card[:][0]
    SecondCard = Null_Card[:][0]
    unClickable = int(Card.max_appear_duration * 1.3)
    streak_effects = []
    disappear_effects = []

unClickable = 0

def score_display(text, pos) :
    FONT = pygame.font.SysFont('consolas', 20)
    score_render = FONT.render(text, True, (0, 0, 0))
    window.blit(score_render, (pos[0] - score_render.get_width() // 2, pos[1] - score_render.get_height() // 2))

def show_turn(player, pos) :
    FONT = pygame.font.SysFont('consolas', 24)
    turn_render = FONT.render("P" + str(player + 1) + " Turn", True, (0, 0, 255) if not player else (255, 0, 0))
    window.blit(turn_render, (pos[0] - turn_render.get_width() // 2, pos[1] - turn_render.get_height() // 2))

def show_turn_w_bot(turn, pos) :
    FONT = pygame.font.SysFont('consolas', 24)
    turn_render = FONT.render(("P" if not turn else "C") + " Turn", True, (0, 0, 255) if not turn else (255, 0, 0))
    window.blit(turn_render, (pos[0] - turn_render.get_width() // 2, pos[1] - turn_render.get_height() // 2))

def display_result(text, pos, player) :
    FONT = pygame.font.SysFont('consolas', 30, bold = True)
    result_render = FONT.render(text, True, (0, 0, 255) if player == 0 else (255, 0, 0) if player == 1 else (0, 255, 0))
    window.blit(result_render, (pos[0] - result_render.get_width() // 2, pos[1] - result_render.get_height() // 2))

def draw_record_table(value) :
    window.blit(score_board, (WIDTH - score_board.get_width() - 10, 10))
    FONT = pygame.font.SysFont("consolas", 26)
    easy_score = FONT.render(str(value[0]), True, (0, 0, 0))
    normal_score = FONT.render(str(value[1]), True, (0, 0, 0))
    hard_score = FONT.render(str(value[2]), True, (0, 0, 0))
    x_center = WIDTH - 10 - 50
    y_start = 65
    window.blit(easy_score, (x_center - easy_score.get_width() // 2, y_start))
    window.blit(normal_score, (x_center - normal_score.get_width() // 2, y_start + 45))
    window.blit(hard_score, (x_center - hard_score.get_width() // 2, y_start + 90))

def play_2P() :
    global previous_state, running, FirstCard, SecondCard, unClickable, turn, current_streak, score, streak_effects, card_table, state, screenshot, score_effects

    mx, my = pygame.mouse.get_pos()
    mouse_clicked = 0

    has_score_effect = 0

    if FirstCard.reveal_duration :
        FirstCard.reveal_duration -= FirstCard.reveal_change
        if FirstCard.reveal_duration == Card.max_reveal_duration // 2 :
            if FirstCard.id == SecondCard.id and FirstCard.pos != SecondCard.pos :
                current_streak += 1
                if not turn :
                    new_streak_effect = Streak_Effect(current_streak, (20 + P1_avt.get_width() // 2, HEIGHT - 20 - P1_avt.get_height() - 70))
                    streak_effects.append(new_streak_effect)
                else :
                    new_streak_effect = Streak_Effect(current_streak, (20 + P2_avt.get_width() // 2, 20 + P2_avt.get_height() + 70))
                    streak_effects.append(new_streak_effect)
                new_disappear_effect = Disappear_Effect((FirstCard.pixel_pos[0] + card_back_img.get_width() // 2, FirstCard.pixel_pos[1] + card_back_img.get_height() // 2))
                disappear_effects.append(new_disappear_effect)
                new_disappear_effect = Disappear_Effect((SecondCard.pixel_pos[0] + card_back_img.get_width() // 2, SecondCard.pixel_pos[1] + card_back_img.get_height() // 2))
                disappear_effects.append(new_disappear_effect)
                card_table.remove(FirstCard)
                card_table.remove(SecondCard)
                unClickable = 0
                FirstCard = Null_Card[:][0]
                SecondCard = Null_Card[:][0]
                score[turn] += int(streak_mul[current_streak] * point)
                score_sound.play()
                has_score_effect = int(streak_mul[current_streak] * point)
            else :
                turn = 1 - turn
                current_streak = 0
                flip_card_sound.play()
        if not FirstCard.reveal_duration :
            FirstCard.isRevealed = 0
            FirstCard.reveal_change = 0
            FirstCard.isHidden = 1
            FirstCard = Null_Card[:][0]
    if SecondCard.reveal_duration :
        SecondCard.reveal_duration -= SecondCard.reveal_change
        if not SecondCard.reveal_duration :
            SecondCard.isRevealed = 0
            SecondCard.reveal_change = 0
            SecondCard.isHidden = 1
            SecondCard = Null_Card[:][0]
    if unClickable :
        unClickable -= 1
        if unClickable :
            pygame.mouse.set_cursor(0)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == pygame.BUTTON_LEFT and not unClickable:
                mouse_clicked = 1
                if mouse_dot_mask.overlap_area(home_btn_mask, (WIDTH // 2 - home_btn.get_width() - 10 - mx, HEIGHT // 2 + 130 - my)) and not len(card_table):
                    state = 'menu'
                    return
                if mouse_dot_mask.overlap_area(replay_btn_mask, (WIDTH // 2 + 10 - mx, HEIGHT // 2 + 130 - my)) and not len(card_table):
                    state = 'play_2P'
                    card_table = shuffle_card()
                    pygame.mouse.set_cursor(0)
                    reset_2P()
                    card_appear_sound.play(1)
                    return
                if mouse_dot_mask.overlap_area(pause_btn_mask, (WIDTH - pause_btn_img.get_width() - 10 - mx, 10 - my)) and len(card_table):
                    state = 'pause'
                    previous_state = 'play_2P'
                    pygame.image.save(window, os.path.join("img", "screenshot.png"))
                    screenshot = pygame.image.load(os.path.join("img", "screenshot.png"))
                    return

    window.blit(bg_img, (0, 0))
    window.blit(P1_avt, (20, (HEIGHT - 20 - P1_avt.get_height())))
    window.blit(P2_avt, (20, 20))
    score_display("Score: " + str(score[0]), (20 + P1_avt.get_width() // 2, HEIGHT - 20 - P1_avt.get_height() - 20))
    score_display("Score: " + str(score[1]), (20 + P2_avt.get_width() // 2, 20 + P2_avt.get_height() + 20))
    show_turn(turn, (20 + P1_avt.get_width() // 2, HEIGHT - 20 - P1_avt.get_height() - 40) if not turn else (20 + P2_avt.get_width() // 2, 20 + P2_avt.get_height() + 40))

    if has_score_effect :
        pos = (20 + P1_avt.get_width() // 2, HEIGHT - 20 - P1_avt.get_height() - 20) if not turn else (20 + P2_avt.get_width() // 2, 20 + P2_avt.get_height() + 20)
        FONT = pygame.font.SysFont("consolas", 20)
        score_render = FONT.render("Score: " + (str(score[0]) if not turn else str(score[1])), True, (0, 0, 0))
        new_score_effect = Score_Effect((pos[0] + score_render.get_width() // 2 + 2, pos[1] - score_render.get_height() // 2), has_score_effect)
        score_effects.append(new_score_effect)

    for effect in streak_effects[:] :
        size = effect.update()
        tmp_streak_img = pygame.transform.scale(pygame.image.load(os.path.join("img\Streak", streak_name[effect.streak_count])).convert_alpha(), size)
        tmp_streak_img.set_colorkey((255, 255, 255))
        window.blit(tmp_streak_img, (effect.pos[0] - size[0] // 2, effect.pos[1] - size[1] // 2))
        if size[0] == effect.max_width or size[1] == effect.max_height :
            streak_effects.remove(effect)

    for effect in disappear_effects[:] :
        window.blit(disappear_effect[effect.duration // Disappear_Effect.base], (effect.pos[0] - disappear_effect[effect.duration // Disappear_Effect.base].get_width() // 2, effect.pos[1] - disappear_effect[effect.duration // Disappear_Effect.base].get_height() // 2))
        effect.duration += 1
        if effect.duration == Disappear_Effect.max_duration :
            disappear_effects.remove(effect)

    interact = 0

    for i in range(len(card_table)) :
        if card_table[i].appear_duration :
            card_table[i].appear_duration -= 1
        if not card_table[i].appear_duration and card_table[i].appear_animation_count != 14:
            tmp_card_back = card_rotation_sprites[card_table[i].id][6 - card_table[i].appear_animation_count // 2]
            tmp_card_back.set_colorkey((255, 255, 255))
            window.blit(tmp_card_back, (card_table[i].pixel_pos[0] + (card_back_img.get_width() - tmp_card_back.get_width()) // 2, card_table[i].pixel_pos[1] + (card_back_img.get_height() - tmp_card_back.get_height()) // 2))
            card_table[i].appear_animation_count += 1
        if not card_table[i].appear_duration and card_table[i].appear_animation_count == 14:
            if not card_table[i].isRevealed and not card_table[i].isRevealing and not card_table[i].isHidden:
                if mouse_dot_mask.overlap_area(card_back_mask, (card_table[i].pixel_pos[0] - mx, card_table[i].pixel_pos[1] - my)) and mouse_clicked :
                    card_table[i].isRevealing = 1
                    card_table[i].reveal_duration = Card.max_reveal_duration
                    unClickable = Card.max_reveal_duration // 1.5
                    flip_card_sound.play()
                elif mouse_dot_mask.overlap_area(card_back_mask, (card_table[i].pixel_pos[0] - mx, card_table[i].pixel_pos[1] - my)) and not unClickable:
                    interact = 1
                    tmp_card_back = pygame.transform.scale(pygame.image.load(os.path.join("img\Card\Card_Back", "Card_Back_1.png")).convert_alpha(), (72 * 1.1, 112 * 1.1))
                    tmp_card_back.set_colorkey((255, 255, 255))
                    window.blit(tmp_card_back, (card_table[i].pixel_pos[0] + (card_back_img.get_width() - tmp_card_back.get_width()) // 2, card_table[i].pixel_pos[1] + (card_back_img.get_height() - tmp_card_back.get_height()) // 2))
                else :
                    window.blit(card_back_img, (card_table[i].pixel_pos))
            elif not card_table[i].isRevealing and not card_table[i].isHidden:
                window.blit(card_table[i].image, card_table[i].pixel_pos)
            elif not card_table[i].isHidden :
                tmp_card_back = card_rotation_sprites[card_table[i].id][card_table[i].isRevealing // 2]
                window.blit(tmp_card_back, (card_table[i].pixel_pos[0] + (card_back_img.get_width() - tmp_card_back.get_width()) // 2, card_table[i].pixel_pos[1] + (card_back_img.get_height() - tmp_card_back.get_height()) // 2))
                card_table[i].isRevealing += 1
                unClickable = Card.max_reveal_duration // 3
                if card_table[i].isRevealing == Card.max_revealing :
                    card_table[i].isRevealing = 0
                    card_table[i].isRevealed = 1
                    if FirstCard == Null_Card[0] :
                        FirstCard = card_table[i]
                        FirstCard.reveal_duration = Card.max_reveal_duration
                    else :
                        SecondCard = card_table[i]
                        SecondCard.reveal_duration = Card.max_reveal_duration
                        unClickable = Card.max_reveal_duration
                        FirstCard.reveal_change = 1
                        SecondCard.reveal_change = 1
            else :
                tmp_card_back = card_rotation_sprites[card_table[i].id][13 - card_table[i].isRevealing // 2]
                window.blit(tmp_card_back, (card_table[i].pixel_pos[0] + (card_back_img.get_width() - tmp_card_back.get_width()) // 2, card_table[i].pixel_pos[1] + (card_back_img.get_height() - tmp_card_back.get_height()) // 2))
                card_table[i].isRevealing += 1
                unClickable = Card.max_reveal_duration // 2
                if card_table[i].isRevealing == Card.max_revealing:
                    card_table[i].isRevealing = 0
                    card_table[i].isHidden = 0

    for score_effect in score_effects[:] :
        window.blit(score_effect.score_render, score_effect.pos)
        score_effect.duration += 1
        if score_effect.duration == score_effect.max_duration :
            score_effects.remove(score_effect)

    if not len(card_table):
        window.blit(gray_label, (0, 0))
        pos = (WIDTH // 2, (HEIGHT - crown_img.get_height()) // 2 - 15 + crown_img.get_height() + 30)

        window.blit(crown_img, ((WIDTH - crown_img.get_width()) // 2 + 2, (HEIGHT - crown_img.get_height()) // 2 - 15))
        if score[0] > score[1] :
            window.blit(P1_avt, ((WIDTH - P1_avt.get_width()) // 2, (HEIGHT - P1_avt.get_height()) // 2))
            display_result("Player 1 Win", pos, 0)
        elif score[1] > score[0] :
            window.blit(P2_avt, ((WIDTH - P2_avt.get_width()) // 2, (HEIGHT - P2_avt.get_height()) // 2))
            display_result("Player 2 Win", pos, 1)
        else :
            display_result("Tie", pos, -1)
        window.blit(home_btn, (WIDTH // 2 - home_btn.get_width() - 10, HEIGHT // 2 + 130))
        window.blit(replay_btn, (WIDTH // 2 + 10, HEIGHT // 2 + 130))

        if (mouse_dot_mask.overlap_area(home_btn_mask, (WIDTH // 2 - home_btn.get_width() - 10 - mx, HEIGHT // 2 + 130 - my)) and not len(card_table)) or (mouse_dot_mask.overlap_area(replay_btn_mask, (WIDTH // 2 + 10 - mx, HEIGHT // 2 + 130 - my)) and not len(card_table)):
            interact = 1
    else :
        window.blit(pause_btn_img, (WIDTH - pause_btn_img.get_width() - 10, 10))
        if mouse_dot_mask.overlap_area(pause_btn_mask, (WIDTH - pause_btn_img.get_width() - 10 - mx, 10 - my)) :
            interact = 1

    if not interact :
        pygame.mouse.set_cursor(0)
    else :
        pygame.mouse.set_cursor(11)

    pygame.display.update()

def option() :
    global running, state, music_state

    mx, my = pygame.mouse.get_pos()

    FONT = pygame.font.SysFont("consolas", 20)
    NAME_FONT = pygame.font.SysFont("consolas", 14)
    music_render = FONT.render("Music", True, (0, 0, 0))
    base_music_render = music_render.get_width()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == pygame.BUTTON_LEFT :
                if mouse_dot_mask.overlap_area(option_btn_mask, (10 - mx, 10 - my)) :
                    state = 'menu'
                    pygame.mouse.set_cursor(0)
                    return
                if mouse_dot_mask.overlap_area(checkbox_mask, ((WIDTH - sign_img.get_width()) // 2 + 20 + music_render.get_width() + 8 - mx, (HEIGHT - sign_img.get_height()) // 2 + 20 - 2 - my)) :
                    music_state = 1 - music_state
                    if music_state :
                        pygame.mixer.music.pause()
                    else :
                        pygame.mixer.music.unpause()
                for i in range(3) :
                    pos = ((WIDTH - sign_img.get_width()) // 2 + 20 + base_music_render + 8, (HEIGHT - sign_img.get_height()) // 2 + 20 - 2 + (yes_checkbox.get_height() + 5) * (i + 1) + 2)
                    if mouse_dot_mask.overlap_area(checkbox_mask, (pos[0] - mx, pos[1] - my)) :
                        for j in range(3) :
                            if i != j :
                                music_list[j] = 0
                            else :
                                music_list[j] = 1
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(os.path.join("sound", music_file_name[i]))
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)

    window.blit(bg_img, (0, 0))
    window.blit(back_btn, (10, 10))
    window.blit(sign_img, ((WIDTH - sign_img.get_width()) // 2, (HEIGHT - sign_img.get_height()) // 2))

    window.blit(music_render, ((WIDTH - sign_img.get_width()) // 2 + 20, (HEIGHT - sign_img.get_height()) // 2 + 20))

    window.blit(checkbox_list[music_state], ((WIDTH - sign_img.get_width()) // 2 + 20 + music_render.get_width() + 8, (HEIGHT - sign_img.get_height()) // 2 + 20 - 2))

    FONT = pygame.font.SysFont("consolas", 30, bold = True)
    text = FONT.render("Option", True, (0, 0, 0))
    window.blit(sign_2_img, ((WIDTH - sign_2_img.get_width()) // 2, 120 - sign_2_img.get_height() // 2))
    window.blit(text, ((WIDTH - text.get_width()) // 2, 120 - text.get_height() // 2 + 10))

    interact = 0

    if not music_state :
        for i in range(3) :
            music_render = NAME_FONT.render(music_name[i], True, (0, 0, 0))
            pos = ((WIDTH - sign_img.get_width()) // 2 + 20 + base_music_render + 8, (HEIGHT - sign_img.get_height()) // 2 + 20 - 2 + (yes_checkbox.get_height() + 5) * (i + 1))
            window.blit(checkbox_list[1 - music_list[i]], pos)
            window.blit(music_render, (pos[0] + yes_checkbox.get_width() + 8, pos[1] + 8))
            if mouse_dot_mask.overlap_area(checkbox_mask, (pos[0] - mx, pos[1] - my)) :
                interact = 1

    if mouse_dot_mask.overlap_area(option_btn_mask, (10 - mx, 10 - my)) or mouse_dot_mask.overlap_area(checkbox_mask, ((WIDTH - sign_img.get_width()) // 2 + 20 + base_music_render + 8 - mx, (HEIGHT - sign_img.get_height()) // 2 + 20 - 2 - my)) :
        interact = 1

    if not interact :
        pygame.mouse.set_cursor(0)
    else :
        pygame.mouse.set_cursor(11)

    pygame.display.update()

previous_state = 0

def pause() :
    global running, screenshot, state

    window.blit(screenshot, (0, 0))
    window.blit(gray_label, (0, 0))

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == pygame.BUTTON_LEFT :
                if mouse_dot_mask.overlap_area(replay_btn_mask, (WIDTH // 2 - back_btn.get_width() - 10 - mx, (HEIGHT + sign_2_img.get_height()) // 2 + 10 - my)) :
                    state = previous_state
                    pygame.mouse.set_cursor(0)
                    return
                if mouse_dot_mask.overlap_area(home_btn_mask, (WIDTH // 2 + 10 - mx, (HEIGHT + sign_2_img.get_height()) // 2 + 10 - my)) :
                    state = 'menu'
                    pygame.mouse.set_cursor(0)
                    return

    window.blit(sign_2_img, ((WIDTH - sign_2_img.get_width()) // 2, (HEIGHT - sign_2_img.get_height()) // 2))
    FONT = pygame.font.SysFont("consolas", 30, bold = True)
    pause_render = FONT.render("PAUSE", True, (0, 0, 0))
    window.blit(pause_render, ((WIDTH - pause_render.get_width()) // 2, (HEIGHT - pause_render.get_height()) // 2 + 10))

    window.blit(back_btn, (WIDTH // 2 - back_btn.get_width() - 10, (HEIGHT + sign_2_img.get_height()) // 2 + 10))
    window.blit(home_btn, (WIDTH // 2 + 10, (HEIGHT + sign_2_img.get_height()) // 2 + 10))

    interact = 0

    if mouse_dot_mask.overlap_area(back_btn_mask, (WIDTH // 2 - back_btn.get_width() - 10 - mx, (HEIGHT + sign_2_img.get_height()) // 2 + 10 - my)) or mouse_dot_mask.overlap_area(back_btn_mask, (WIDTH // 2 + 10 - mx, (HEIGHT + sign_2_img.get_height()) // 2 + 10 - my)) :
        interact = 1

    if interact :
        pygame.mouse.set_cursor(11)
    else :
        pygame.mouse.set_cursor(0)

    pygame.display.update()

bot = 0

def vsBot() :
    global cnt, running, FirstCard, SecondCard, unClickable, turn, current_streak, score, streak_effects, card_table, state, screenshot, score_effects, current_turn, current_bot_diff, bot, record_Bot, previous_state

    mx, my = pygame.mouse.get_pos()
    mouse_clicked = 0

    has_score_effect = 0

    if turn :
        if bot.cd :
            bot.cd -= 1

        if not bot.cd and len(card_table):
            bot.choices[bot.cursor].isRevealing = 1
            bot.choices[bot.cursor].reveal_duration = Card.max_reveal_duration
            bot.choices[bot.cursor] = Null_Card[0]
            flip_card_sound.play()
            bot.cursor = 1 - bot.cursor
            bot.cd = bot.max_cd

    if FirstCard.reveal_duration:
        FirstCard.reveal_duration -= FirstCard.reveal_change
        if FirstCard.reveal_duration == Card.max_reveal_duration // 2:
            if FirstCard.id == SecondCard.id and FirstCard.pos != SecondCard.pos and SecondCard != Null_Card[0]:
                if (current_turn > len(bot.id_memories) // 2) :
                    bot.id_memories.pop(0)
                    bot.id_memories.pop(0)
                    bot.id_memories.extend([-1, -1])
                    bot.card_memories.pop(0)
                    bot.card_memories.pop(0)
                    bot.card_memories.extend([Null_Card[0], Null_Card[0]])
                    while (bot.card_memories.count(FirstCard)) :
                        tmp_index = bot.card_memories.index(FirstCard)
                        bot.id_memories[tmp_index] = -1
                        bot.card_memories[tmp_index] = Null_Card[0]
                    while (bot.card_memories.count(SecondCard)) :
                        tmp_index = bot.card_memories.index(SecondCard)
                        bot.id_memories[tmp_index] = -1
                        bot.card_memories[tmp_index] = Null_Card[0]
                current_streak += 1
                if not turn:
                    new_streak_effect = Streak_Effect(current_streak, (
                    20 + P1_avt.get_width() // 2, HEIGHT - 20 - P1_avt.get_height() - 70))
                    streak_effects.append(new_streak_effect)
                else:
                    new_streak_effect = Streak_Effect(current_streak, (
                    20 + P2_avt.get_width() // 2, 20 + P2_avt.get_height() + 70))
                    streak_effects.append(new_streak_effect)
                new_disappear_effect = Disappear_Effect((FirstCard.pixel_pos[0] + card_back_img.get_width() // 2,
                                                         FirstCard.pixel_pos[1] + card_back_img.get_height() // 2))
                disappear_effects.append(new_disappear_effect)
                new_disappear_effect = Disappear_Effect((SecondCard.pixel_pos[0] + card_back_img.get_width() // 2,
                                                         SecondCard.pixel_pos[1] + card_back_img.get_height() // 2))
                disappear_effects.append(new_disappear_effect)
                card_table.remove(FirstCard)
                card_table.remove(SecondCard)
                unClickable = 0
                FirstCard = Null_Card[:][0]
                SecondCard = Null_Card[:][0]
                score[turn] += int(streak_mul[current_streak] * point)
                score_sound.play()
                has_score_effect = int(streak_mul[current_streak] * point)
                if turn and len(card_table):
                    bot.calc_choices()
                    bot.cd = bot.max_cd
            else:
                if (current_turn > len(bot.id_memories) // 2) :
                    while (bot.card_memories.count(FirstCard)) :
                        tmp_index = bot.card_memories.index(FirstCard)
                        bot.id_memories[tmp_index] = -1
                        bot.card_memories[tmp_index] = Null_Card[0]
                    while (bot.card_memories.count(SecondCard)) :
                        tmp_index = bot.card_memories.index(SecondCard)
                        bot.id_memories[tmp_index] = -1
                        bot.card_memories[tmp_index] = Null_Card[0]
                    bot.id_memories.pop(0)
                    bot.id_memories.pop(0)
                    bot.id_memories.extend([FirstCard.id, SecondCard.id])
                    bot.card_memories.pop(0)
                    bot.card_memories.pop(0)
                    bot.card_memories.extend([FirstCard, SecondCard])
                else :
                    while (bot.card_memories.count(FirstCard)) :
                        tmp_index = bot.card_memories.index(FirstCard)
                        bot.id_memories[tmp_index] = -1
                        bot.card_memories[tmp_index] = Null_Card[0]
                    while (bot.card_memories.count(SecondCard)) :
                        tmp_index = bot.card_memories.index(SecondCard)
                        bot.id_memories[tmp_index] = -1
                        bot.card_memories[tmp_index] = Null_Card[0]
                    bot.id_memories[(current_turn - 1) * 2] = FirstCard.id
                    bot.id_memories[(current_turn - 1) * 2 + 1] = SecondCard.id
                    bot.card_memories[(current_turn - 1) * 2] = FirstCard
                    bot.card_memories[(current_turn - 1) * 2 + 1] = SecondCard
                turn = 1 - turn
                current_streak = 0
                flip_card_sound.play()
                if turn and len(card_table):
                    bot.calc_choices()
                    bot.cd = bot.max_cd
            current_turn += 1
        if not FirstCard.reveal_duration:
            FirstCard.isRevealed = 0
            FirstCard.reveal_change = 0
            FirstCard.isHidden = 1
            FirstCard = Null_Card[:][0]
    if SecondCard.reveal_duration:
        SecondCard.reveal_duration -= SecondCard.reveal_change
        if not SecondCard.reveal_duration:
            SecondCard.isRevealed = 0
            SecondCard.reveal_change = 0
            SecondCard.isHidden = 1
            SecondCard = Null_Card[:][0]
    if unClickable:
        unClickable -= 1
        if unClickable:
            pygame.mouse.set_cursor(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT and not unClickable:
                mouse_clicked = 1
                if mouse_dot_mask.overlap_area(home_btn_mask, (
                WIDTH // 2 - home_btn.get_width() - 10 - mx, HEIGHT // 2 + 130 + (90 if score[0] > score[1] else 0) - my)) and not len(card_table):
                    state = 'menu'
                    return
                if mouse_dot_mask.overlap_area(replay_btn_mask,
                                               (WIDTH // 2 + 10 - mx, HEIGHT // 2 + 130 + (90 if score[0] > score[1] else 0) - my)) and not len(card_table):
                    state = 'vsBot'
                    bot = Bot(current_bot_diff)
                    card_table = shuffle_card()
                    pygame.mouse.set_cursor(0)
                    reset_2P()
                    card_appear_sound.play(1)
                    return
                if mouse_dot_mask.overlap_area(pause_btn_mask,
                                               (WIDTH - pause_btn_img.get_width() - 10 - mx, 10 - my)) and len(
                        card_table):
                    state = 'pause'
                    previous_state = 'vsBot'
                    pygame.image.save(window, os.path.join("img", "screenshot.png"))
                    screenshot = pygame.image.load(os.path.join("img", "screenshot.png"))
                    return

    window.blit(bg_img, (0, 0))
    window.blit(P1_avt, (20, (HEIGHT - 20 - P1_avt.get_height())))
    window.blit(P2_avt, (20, 20))
    score_display("Score: " + str(score[0]), (20 + P1_avt.get_width() // 2, HEIGHT - 20 - P1_avt.get_height() - 20))
    score_display("Score: " + str(score[1]), (20 + P2_avt.get_width() // 2, 20 + P2_avt.get_height() + 20))
    show_turn_w_bot(turn, (20 + P1_avt.get_width() // 2, HEIGHT - 20 - P1_avt.get_height() - 40) if not turn else (
    20 + P2_avt.get_width() // 2, 20 + P2_avt.get_height() + 40))

    if has_score_effect:
        pos = (20 + P1_avt.get_width() // 2, HEIGHT - 20 - P1_avt.get_height() - 20) if not turn else (
        20 + P2_avt.get_width() // 2, 20 + P2_avt.get_height() + 20)
        FONT = pygame.font.SysFont("consolas", 20)
        score_render = FONT.render("Score: " + (str(score[0]) if not turn else str(score[1])), True, (0, 0, 0))
        new_score_effect = Score_Effect(
            (pos[0] + score_render.get_width() // 2 + 2, pos[1] - score_render.get_height() // 2), has_score_effect)
        score_effects.append(new_score_effect)

    for effect in streak_effects[:]:
        size = effect.update()
        tmp_streak_img = pygame.transform.scale(
            pygame.image.load(os.path.join("img\Streak", streak_name[effect.streak_count])).convert_alpha(), size)
        tmp_streak_img.set_colorkey((255, 255, 255))
        window.blit(tmp_streak_img, (effect.pos[0] - size[0] // 2, effect.pos[1] - size[1] // 2))
        if size[0] == effect.max_width or size[1] == effect.max_height:
            streak_effects.remove(effect)

    for effect in disappear_effects[:]:
        window.blit(disappear_effect[effect.duration // Disappear_Effect.base], (
        effect.pos[0] - disappear_effect[effect.duration // Disappear_Effect.base].get_width() // 2,
        effect.pos[1] - disappear_effect[effect.duration // Disappear_Effect.base].get_height() // 2))
        effect.duration += 1
        if effect.duration == Disappear_Effect.max_duration:
            disappear_effects.remove(effect)

    interact = 0

    for i in range(len(card_table)):
        if card_table[i].appear_duration:
            card_table[i].appear_duration -= 1
        if not card_table[i].appear_duration and card_table[i].appear_animation_count != 14:
            tmp_card_back = card_rotation_sprites[card_table[i].id][6 - card_table[i].appear_animation_count // 2]
            tmp_card_back.set_colorkey((255, 255, 255))
            window.blit(tmp_card_back, (
            card_table[i].pixel_pos[0] + (card_back_img.get_width() - tmp_card_back.get_width()) // 2,
            card_table[i].pixel_pos[1] + (card_back_img.get_height() - tmp_card_back.get_height()) // 2))
            card_table[i].appear_animation_count += 1
        if not card_table[i].appear_duration and card_table[i].appear_animation_count == 14:
            if not card_table[i].isRevealed and not card_table[i].isRevealing and not card_table[i].isHidden:
                if mouse_dot_mask.overlap_area(card_back_mask, (
                card_table[i].pixel_pos[0] - mx, card_table[i].pixel_pos[1] - my)) and mouse_clicked and not turn:
                    card_table[i].isRevealing = 1
                    card_table[i].reveal_duration = Card.max_reveal_duration
                    unClickable = Card.max_reveal_duration // 1.5
                    flip_card_sound.play()
                elif mouse_dot_mask.overlap_area(card_back_mask, (
                card_table[i].pixel_pos[0] - mx, card_table[i].pixel_pos[1] - my)) and not unClickable and not turn:
                    interact = 1
                    tmp_card_back = pygame.transform.scale(
                        pygame.image.load(os.path.join("img\Card\Card_Back", "Card_Back_1.png")).convert_alpha(),
                        (72 * 1.1, 112 * 1.1))
                    tmp_card_back.set_colorkey((255, 255, 255))
                    window.blit(tmp_card_back, (
                    card_table[i].pixel_pos[0] + (card_back_img.get_width() - tmp_card_back.get_width()) // 2,
                    card_table[i].pixel_pos[1] + (card_back_img.get_height() - tmp_card_back.get_height()) // 2))
                else:
                    window.blit(card_back_img, (card_table[i].pixel_pos))
            elif not card_table[i].isRevealing and not card_table[i].isHidden:
                window.blit(card_table[i].image, card_table[i].pixel_pos)
            elif not card_table[i].isHidden:
                tmp_card_back = card_rotation_sprites[card_table[i].id][card_table[i].isRevealing // 2]
                window.blit(tmp_card_back, (
                card_table[i].pixel_pos[0] + (card_back_img.get_width() - tmp_card_back.get_width()) // 2,
                card_table[i].pixel_pos[1] + (card_back_img.get_height() - tmp_card_back.get_height()) // 2))
                card_table[i].isRevealing += 1
                unClickable = Card.max_reveal_duration // 3
                if card_table[i].isRevealing == Card.max_revealing:
                    card_table[i].isRevealing = 0
                    card_table[i].isRevealed = 1
                    if FirstCard == Null_Card[0]:
                        FirstCard = card_table[i]
                        FirstCard.reveal_duration = Card.max_reveal_duration
                    else:
                        SecondCard = card_table[i]
                        SecondCard.reveal_duration = Card.max_reveal_duration
                        unClickable = Card.max_reveal_duration
                        FirstCard.reveal_change = 1
                        SecondCard.reveal_change = 1
            else:
                tmp_card_back = card_rotation_sprites[card_table[i].id][13 - card_table[i].isRevealing // 2]
                window.blit(tmp_card_back, (
                card_table[i].pixel_pos[0] + (card_back_img.get_width() - tmp_card_back.get_width()) // 2,
                card_table[i].pixel_pos[1] + (card_back_img.get_height() - tmp_card_back.get_height()) // 2))
                card_table[i].isRevealing += 1
                unClickable = Card.max_reveal_duration // 2
                if card_table[i].isRevealing == Card.max_revealing:
                    card_table[i].isRevealing = 0
                    card_table[i].isHidden = 0

    for score_effect in score_effects[:]:
        window.blit(score_effect.score_render, score_effect.pos)
        score_effect.duration += 1
        if score_effect.duration == score_effect.max_duration:
            score_effects.remove(score_effect)

    if not len(card_table):
        window.blit(gray_label, (0, 0))
        pos = (WIDTH // 2, (HEIGHT - crown_img.get_height()) // 2 - 15 + crown_img.get_height() + 30 - (90 if score[0] > score[1] else 0))

        window.blit(crown_img, ((WIDTH - crown_img.get_width()) // 2 + 2, (HEIGHT - crown_img.get_height()) // 2 - 15 - (90 if score[0] > score[1] else 0)))
        if score[0] > score[1]:
            window.blit(P1_avt, ((WIDTH - P1_avt.get_width()) // 2, (HEIGHT - P1_avt.get_height()) // 2 - 90))
            y_start = 360
            window.blit(score_table, ((WIDTH - score_table.get_width()) // 2, y_start - 10 - 50))
            display_result("You Win", pos, 0)
            record_Bot[change_dict[current_bot_diff]] = max(record_Bot[change_dict[current_bot_diff]], score[0] + diff_score[change_dict[current_bot_diff]])
            width = 300
            height = 250
            FONT = pygame.font.SysFont("consolas", 26)
            score_txt = FONT.render("Base score: ", True, (0, 0, 0))
            diff_txt = FONT.render(str(diff_dict[change_dict[current_bot_diff]]) + " mode score: ", True, (0, 0, 0))
            total_txt = FONT.render("Total score: ", True, (0, 0, 0))
            record_txt = FONT.render("Highest score: ", True, (0, 0, 0))
            score_render = FONT.render(str(score[0]), True, (0, 0, 0))
            diff_render = FONT.render(str(diff_score[change_dict[current_bot_diff]]), True, (0, 0, 0))
            total_render = FONT.render(str(score[0] + diff_score[change_dict[current_bot_diff]] + turn_left * score_per_turn_left),
                                       True, (0, 0, 0))
            record_render = FONT.render(str(record_Bot[change_dict[current_bot_diff]]), True, (0, 0, 0))
            window.blit(score_txt, ((WIDTH - width) // 2, y_start))
            window.blit(score_render, ((WIDTH + width) // 2 - score_render.get_width(), y_start))
            window.blit(diff_txt, ((WIDTH - width) // 2, y_start + 30))
            window.blit(diff_render, ((WIDTH + width) // 2 - diff_render.get_width(), y_start + 30))
            pygame.draw.line(window, (0, 0, 255), ((WIDTH - width) // 2 - 20, y_start + 90),
                             ((WIDTH + width) // 2 + 20, y_start + 90), width=5)
            window.blit(total_txt, ((WIDTH - width) // 2, y_start + 100))
            window.blit(total_render, ((WIDTH + width) // 2 - total_render.get_width(), y_start + 100))
            window.blit(record_txt, ((WIDTH - width) // 2, y_start + 130))
            window.blit(record_render, ((WIDTH + width) // 2 - record_render.get_width(), y_start + 130))
        elif score[1] > score[0]:
            window.blit(P2_avt, ((WIDTH - P2_avt.get_width()) // 2, (HEIGHT - P2_avt.get_height()) // 2))
            display_result("You lose", pos, 1)
        else:
            display_result("Tie", pos, -1)
        window.blit(home_btn, (WIDTH // 2 - home_btn.get_width() - 10, HEIGHT // 2 + 130 + (90 if score[0] > score[1] else 0)))
        window.blit(replay_btn, (WIDTH // 2 + 10, HEIGHT // 2 + 130 + (90 if score[0] > score[1] else 0)))

        if (mouse_dot_mask.overlap_area(home_btn_mask, (
        WIDTH // 2 - home_btn.get_width() - 10 - mx, HEIGHT // 2 + 130 + (90 if score[0] > score[1] else 0) - my)) and not len(card_table)) or (
                mouse_dot_mask.overlap_area(replay_btn_mask,
                                            (WIDTH // 2 + 10 - mx, HEIGHT // 2 + 130 + (90 if score[0] > score[1] else 0) - my)) and not len(card_table)):
            interact = 1
    else:
        window.blit(pause_btn_img, (WIDTH - pause_btn_img.get_width() - 10, 10))
        if mouse_dot_mask.overlap_area(pause_btn_mask, (WIDTH - pause_btn_img.get_width() - 10 - mx, 10 - my)):
            interact = 1

    if not interact:
        pygame.mouse.set_cursor(0)
    else:
        pygame.mouse.set_cursor(11)

    pygame.display.update()

def choose_difficult(game_mode) :
    global running, state, card_table, bot, current_bot_diff, current_1P_diff, turn_left

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == pygame.BUTTON_LEFT :
                if mouse_dot_mask.overlap_area(bot_easy_btn_mask, ((WIDTH // 6) - bot_easy_btn.get_width() // 2 + 100 - mx, (HEIGHT - bot_easy_btn.get_height()) // 2 - my)) :
                    if game_mode == 'vsBot' :
                        state = 'vsBot'
                        bot = Bot(2)
                        current_bot_diff = 2
                    else :
                        state = 'play_1P'
                        current_1P_diff = 0
                        turn_left = max_turn[current_1P_diff]
                    card_table = shuffle_card()
                    pygame.mouse.set_cursor(0)
                    reset_2P()
                    card_appear_sound.play(1)
                    return
                if mouse_dot_mask.overlap_area(bot_normal_btn_mask, ((WIDTH // 2) - bot_normal_btn.get_width() // 2 - mx, (HEIGHT - bot_normal_btn.get_height()) // 2 - my)) :
                    if game_mode == 'vsBot':
                        state = 'vsBot'
                        bot = Bot(5)
                        current_bot_diff = 5
                    else :
                        state = 'play_1P'
                        current_1P_diff = 1
                        turn_left = max_turn[current_1P_diff]
                    card_table = shuffle_card()
                    pygame.mouse.set_cursor(0)
                    reset_2P()
                    card_appear_sound.play(1)
                    return
                if mouse_dot_mask.overlap_area(bot_hard_btn_mask, (((WIDTH // 6) * 5) - bot_hard_btn.get_width() // 2 - 100 - mx, (HEIGHT - bot_hard_btn.get_height()) // 2 - my)) :
                    if game_mode == 'vsBot':
                        state = 'vsBot'
                        bot = Bot(8)
                        current_bot_diff = 8
                    else :
                        state = 'play_1P'
                        current_1P_diff = 2
                        turn_left = max_turn[current_1P_diff]
                    card_table = shuffle_card()
                    pygame.mouse.set_cursor(0)
                    reset_2P()
                    card_appear_sound.play(1)
                    return
                if mouse_dot_mask.overlap_area(back_btn_mask, (10 - mx, 10 - my)) :
                    state = 'menu'
                    return

    window.blit(bg_img, (0, 0))

    draw_record_table(record_1P if game_mode == "play_1P" else record_Bot)

    window.blit(bot_easy_btn, ((WIDTH // 6) - bot_easy_btn.get_width() // 2 + 100, (HEIGHT - bot_easy_btn.get_height()) // 2))
    window.blit(bot_normal_btn, ((WIDTH // 2) - bot_normal_btn.get_width() // 2, (HEIGHT - bot_normal_btn.get_height()) // 2))
    window.blit(bot_hard_btn, (((WIDTH // 6) * 5) - bot_hard_btn.get_width() // 2 - 100, (HEIGHT - bot_hard_btn.get_height()) // 2))
    window.blit(back_btn, (10, 10))

    interact = 0

    if mouse_dot_mask.overlap_area(bot_easy_btn_mask, ((WIDTH // 6) - bot_easy_btn.get_width() // 2 + 100 - mx, (HEIGHT - bot_easy_btn.get_height()) // 2 - my)) or mouse_dot_mask.overlap_area(bot_normal_btn_mask, ((WIDTH // 2) - bot_normal_btn.get_width() // 2 - mx, (HEIGHT - bot_normal_btn.get_height()) // 2 - my)) or mouse_dot_mask.overlap_area(bot_hard_btn_mask, (((WIDTH // 6) * 5) - bot_hard_btn.get_width() // 2 - 100 - mx, (HEIGHT - bot_hard_btn.get_height()) // 2 - my)) or mouse_dot_mask.overlap_area(back_btn_mask, (10 - mx, 10 - my)) :
        interact = 1

    if interact :
        pygame.mouse.set_cursor(11)
    else :
        pygame.mouse.set_cursor(0)

    pygame.display.update()

diff_dict = ["Easy", "Normal", "Hard"]

def play_1P() :
    global previous_state, running, FirstCard, SecondCard, unClickable, turn, current_streak, score, streak_effects, card_table, state, screenshot, score_effects, current_turn, turn_left, record_1P

    mx, my = pygame.mouse.get_pos()
    mouse_clicked = 0

    has_score_effect = 0

    if FirstCard.reveal_duration:
        FirstCard.reveal_duration -= FirstCard.reveal_change
        if FirstCard.reveal_duration == Card.max_reveal_duration // 2:
            turn_left -= 1
            if FirstCard.id == SecondCard.id and FirstCard.pos != SecondCard.pos:
                current_streak += 1
                if not turn:
                    new_streak_effect = Streak_Effect(current_streak, (
                    20 + P1_avt.get_width() // 2, HEIGHT - 20 - P1_avt.get_height() - 70))
                    streak_effects.append(new_streak_effect)
                else:
                    new_streak_effect = Streak_Effect(current_streak,
                                                      (20 + P2_avt.get_width() // 2, 20 + P2_avt.get_height() + 70))
                    streak_effects.append(new_streak_effect)
                new_disappear_effect = Disappear_Effect((FirstCard.pixel_pos[0] + card_back_img.get_width() // 2,
                                                         FirstCard.pixel_pos[1] + card_back_img.get_height() // 2))
                disappear_effects.append(new_disappear_effect)
                new_disappear_effect = Disappear_Effect((SecondCard.pixel_pos[0] + card_back_img.get_width() // 2,
                                                         SecondCard.pixel_pos[1] + card_back_img.get_height() // 2))
                disappear_effects.append(new_disappear_effect)
                card_table.remove(FirstCard)
                card_table.remove(SecondCard)
                unClickable = 0
                FirstCard = Null_Card[:][0]
                SecondCard = Null_Card[:][0]
                score[turn] += int(streak_mul[current_streak] * point)
                score_sound.play()
                has_score_effect = int(streak_mul[current_streak] * point)
            else:
                current_streak = 0
                flip_card_sound.play()
        if not FirstCard.reveal_duration:
            FirstCard.isRevealed = 0
            FirstCard.reveal_change = 0
            FirstCard.isHidden = 1
            FirstCard = Null_Card[:][0]
    if SecondCard.reveal_duration:
        SecondCard.reveal_duration -= SecondCard.reveal_change
        if not SecondCard.reveal_duration:
            SecondCard.isRevealed = 0
            SecondCard.reveal_change = 0
            SecondCard.isHidden = 1
            SecondCard = Null_Card[:][0]
    if unClickable:
        unClickable -= 1
        if unClickable:
            pygame.mouse.set_cursor(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT and not unClickable:
                mouse_clicked = 1
                if mouse_dot_mask.overlap_area(home_btn_mask, (
                        WIDTH // 2 - home_btn.get_width() - 10 - mx, HEIGHT // 2 + 130 + (90 if not len(card_table) else 0) - my)) and (not len(card_table) or not turn_left):
                    state = 'menu'
                    return
                if mouse_dot_mask.overlap_area(replay_btn_mask,
                                               (WIDTH // 2 + 10 - mx, HEIGHT // 2 + 130 + (90 if not len(card_table) else 0) - my)) and (not len(card_table) or not turn_left):
                    state = 'play_1P'
                    turn_left = max_turn[current_1P_diff]
                    card_table = shuffle_card()
                    pygame.mouse.set_cursor(0)
                    reset_2P()
                    card_appear_sound.play(1)
                    return
                if mouse_dot_mask.overlap_area(pause_btn_mask,
                                               (WIDTH - pause_btn_img.get_width() - 10 - mx, 10 - my)) and len(
                    card_table) and turn_left:
                    state = 'pause'
                    previous_state = 'play_1P'
                    pygame.image.save(window, os.path.join("img", "screenshot.png"))
                    screenshot = pygame.image.load(os.path.join("img", "screenshot.png"))
                    return


    window.blit(bg_img, (0, 0))
    window.blit(P1_avt, (20, (HEIGHT - 20 - P1_avt.get_height())))
    score_display("Score: " + str(score[0]), (20 + P1_avt.get_width() // 2, HEIGHT - 20 - P1_avt.get_height() - 20))

    FFONT = pygame.font.SysFont('consolas', 16)
    turn_render = FFONT.render("Turn left: " + str(turn_left), True, (0, 0, 0))
    window.blit(turn_render, (20 + (P1_avt.get_width() - turn_render.get_width()) // 2, 20))

    if has_score_effect:
        pos = (20 + P1_avt.get_width() // 2, HEIGHT - 20 - P1_avt.get_height() - 20) if not turn else (
            20 + P2_avt.get_width() // 2, 20 + P2_avt.get_height() + 20)
        FONT = pygame.font.SysFont("consolas", 20)
        score_render = FONT.render("Score: " + (str(score[0]) if not turn else str(score[1])), True, (0, 0, 0))
        new_score_effect = Score_Effect(
            (pos[0] + score_render.get_width() // 2 + 2, pos[1] - score_render.get_height() // 2), has_score_effect)
        score_effects.append(new_score_effect)

    for effect in streak_effects[:]:
        size = effect.update()
        tmp_streak_img = pygame.transform.scale(
            pygame.image.load(os.path.join("img\Streak", streak_name[effect.streak_count])).convert_alpha(), size)
        tmp_streak_img.set_colorkey((255, 255, 255))
        window.blit(tmp_streak_img, (effect.pos[0] - size[0] // 2, effect.pos[1] - size[1] // 2))
        if size[0] == effect.max_width or size[1] == effect.max_height:
            streak_effects.remove(effect)

    for effect in disappear_effects[:]:
        window.blit(disappear_effect[effect.duration // Disappear_Effect.base], (
            effect.pos[0] - disappear_effect[effect.duration // Disappear_Effect.base].get_width() // 2,
            effect.pos[1] - disappear_effect[effect.duration // Disappear_Effect.base].get_height() // 2))
        effect.duration += 1
        if effect.duration == Disappear_Effect.max_duration:
            disappear_effects.remove(effect)

    interact = 0

    for i in range(len(card_table)):
        if card_table[i].appear_duration:
            card_table[i].appear_duration -= 1
        if not card_table[i].appear_duration and card_table[i].appear_animation_count != 14:
            tmp_card_back = card_rotation_sprites[card_table[i].id][6 - card_table[i].appear_animation_count // 2]
            tmp_card_back.set_colorkey((255, 255, 255))
            window.blit(tmp_card_back, (
                card_table[i].pixel_pos[0] + (card_back_img.get_width() - tmp_card_back.get_width()) // 2,
                card_table[i].pixel_pos[1] + (card_back_img.get_height() - tmp_card_back.get_height()) // 2))
            card_table[i].appear_animation_count += 1
        if not card_table[i].appear_duration and card_table[i].appear_animation_count == 14:
            if not card_table[i].isRevealed and not card_table[i].isRevealing and not card_table[i].isHidden:
                if mouse_dot_mask.overlap_area(card_back_mask, (
                        card_table[i].pixel_pos[0] - mx,
                        card_table[i].pixel_pos[1] - my)) and mouse_clicked and not turn and turn_left:
                    card_table[i].isRevealing = 1
                    card_table[i].reveal_duration = Card.max_reveal_duration
                    unClickable = Card.max_reveal_duration // 1.5
                    flip_card_sound.play()
                elif mouse_dot_mask.overlap_area(card_back_mask, (
                        card_table[i].pixel_pos[0] - mx,
                        card_table[i].pixel_pos[1] - my)) and not unClickable and not turn and turn_left:
                    interact = 1
                    tmp_card_back = pygame.transform.scale(
                        pygame.image.load(os.path.join("img\Card\Card_Back", "Card_Back_1.png")).convert_alpha(),
                        (72 * 1.1, 112 * 1.1))
                    tmp_card_back.set_colorkey((255, 255, 255))
                    window.blit(tmp_card_back, (
                        card_table[i].pixel_pos[0] + (card_back_img.get_width() - tmp_card_back.get_width()) // 2,
                        card_table[i].pixel_pos[1] + (card_back_img.get_height() - tmp_card_back.get_height()) // 2))
                else:
                    window.blit(card_back_img, (card_table[i].pixel_pos))
            elif not card_table[i].isRevealing and not card_table[i].isHidden:
                window.blit(card_table[i].image, card_table[i].pixel_pos)
            elif not card_table[i].isHidden:
                tmp_card_back = card_rotation_sprites[card_table[i].id][card_table[i].isRevealing // 2]
                window.blit(tmp_card_back, (
                    card_table[i].pixel_pos[0] + (card_back_img.get_width() - tmp_card_back.get_width()) // 2,
                    card_table[i].pixel_pos[1] + (card_back_img.get_height() - tmp_card_back.get_height()) // 2))
                card_table[i].isRevealing += 1
                unClickable = Card.max_reveal_duration // 3
                if card_table[i].isRevealing == Card.max_revealing:
                    card_table[i].isRevealing = 0
                    card_table[i].isRevealed = 1
                    if FirstCard == Null_Card[0]:
                        FirstCard = card_table[i]
                        FirstCard.reveal_duration = Card.max_reveal_duration
                    else:
                        SecondCard = card_table[i]
                        SecondCard.reveal_duration = Card.max_reveal_duration
                        unClickable = Card.max_reveal_duration
                        FirstCard.reveal_change = 1
                        SecondCard.reveal_change = 1
            else:
                tmp_card_back = card_rotation_sprites[card_table[i].id][13 - card_table[i].isRevealing // 2]
                window.blit(tmp_card_back, (
                    card_table[i].pixel_pos[0] + (card_back_img.get_width() - tmp_card_back.get_width()) // 2,
                    card_table[i].pixel_pos[1] + (card_back_img.get_height() - tmp_card_back.get_height()) // 2))
                card_table[i].isRevealing += 1
                unClickable = Card.max_reveal_duration // 2
                if card_table[i].isRevealing == Card.max_revealing:
                    card_table[i].isRevealing = 0
                    card_table[i].isHidden = 0

    for score_effect in score_effects[:]:
        window.blit(score_effect.score_render, score_effect.pos)
        score_effect.duration += 1
        if score_effect.duration == score_effect.max_duration:
            score_effects.remove(score_effect)

    if not turn_left and len(card_table):
        window.blit(gray_label, (0, 0))
        pos = (WIDTH // 2, (HEIGHT - crown_img.get_height()) // 2 - 15 + crown_img.get_height() + 30)
        window.blit(crown_img, ((WIDTH - crown_img.get_width()) // 2 + 2, (HEIGHT - crown_img.get_height()) // 2 - 15))
        display_result("You lose", pos, 1)
        window.blit(home_btn, (WIDTH // 2 - home_btn.get_width() - 10, HEIGHT // 2 + 130))
        window.blit(replay_btn, (WIDTH // 2 + 10, HEIGHT // 2 + 130))

        if (mouse_dot_mask.overlap_area(home_btn_mask, (
                WIDTH // 2 - home_btn.get_width() - 10 - mx, HEIGHT // 2 + 130 - my)) and not len(card_table)) or (
                mouse_dot_mask.overlap_area(replay_btn_mask,
                                            (WIDTH // 2 + 10 - mx, HEIGHT // 2 + 130 - my)) and not len(card_table)):
            interact = 1

    if not len(card_table) :
        window.blit(gray_label, (0, 0))
        pos = (WIDTH // 2, (HEIGHT - crown_img.get_height()) // 2 - 15 + crown_img.get_height() + 30 - 90)

        window.blit(crown_img, ((WIDTH - crown_img.get_width()) // 2 + 2, (HEIGHT - crown_img.get_height()) // 2 - 15 - 90))
        window.blit(P1_avt, ((WIDTH - P1_avt.get_width()) // 2, (HEIGHT - P1_avt.get_height()) // 2 - 90))
        y_start = 360
        window.blit(score_table, ((WIDTH - score_table.get_width()) // 2, y_start - 10 - 50))
        display_result("You Win", pos, 0)
        record_1P[current_1P_diff] = max(record_1P[current_1P_diff], score[0] + turn_left * score_per_turn_left + diff_score[current_1P_diff])
        window.blit(home_btn, (WIDTH // 2 - home_btn.get_width() - 10, HEIGHT // 2 + 130 + 90))
        window.blit(replay_btn, (WIDTH // 2 + 10, HEIGHT // 2 + 130 + 90))
        width = 300
        height = 250
        FONT = pygame.font.SysFont("consolas", 26)
        score_txt = FONT.render("Base score: ", True, (0, 0, 0))
        diff_txt = FONT.render(str(diff_dict[current_1P_diff]) + " mode score: ", True, (0, 0, 0))
        turn_txt = FONT.render(str(turn_left) + " turn left: ", True, (0, 0, 0))
        total_txt = FONT.render("Total score: ", True, (0, 0, 0))
        record_txt = FONT.render("Highest score: ", True, (0, 0, 0))
        score_render = FONT.render(str(score[0]), True, (0, 0, 0))
        diff_render = FONT.render(str(diff_score[current_1P_diff]), True, (0, 0, 0))
        turn_render = FONT.render(str(turn_left * score_per_turn_left), True, (0, 0, 0))
        total_render = FONT.render(str(score[0] + diff_score[current_1P_diff] + turn_left * score_per_turn_left), True,(0, 0, 0))
        record_render = FONT.render(str(record_1P[current_1P_diff]), True, (0, 0, 0))
        window.blit(score_txt, ((WIDTH - width) // 2, y_start))
        window.blit(score_render, ((WIDTH + width) // 2 - score_render.get_width(), y_start))
        window.blit(diff_txt, ((WIDTH - width) // 2, y_start + 30))
        window.blit(diff_render, ((WIDTH + width) // 2 - diff_render.get_width(), y_start + 30))
        window.blit(turn_txt, ((WIDTH - width) // 2, y_start + 60))
        window.blit(turn_render, ((WIDTH + width) // 2 - turn_render.get_width(), y_start + 60))
        pygame.draw.line(window, (0, 0, 255), ((WIDTH - width) // 2 - 20, y_start + 90), ((WIDTH + width) // 2 + 20, y_start + 90), width = 5)
        window.blit(total_txt, ((WIDTH - width) // 2, y_start + 100))
        window.blit(total_render, ((WIDTH + width) // 2 - total_render.get_width(), y_start + 100))
        window.blit(record_txt, ((WIDTH - width) // 2, y_start + 130))
        window.blit(record_render, ((WIDTH + width) // 2 - record_render.get_width(), y_start + 130))


    elif turn_left :
        window.blit(pause_btn_img, (WIDTH - pause_btn_img.get_width() - 10, 10))
        if mouse_dot_mask.overlap_area(pause_btn_mask, (WIDTH - pause_btn_img.get_width() - 10 - mx, 10 - my)):
            interact = 1

    if not turn_left :
        if (mouse_dot_mask.overlap_area(home_btn_mask, (
                WIDTH // 2 - home_btn.get_width() - 10 - mx, HEIGHT // 2 + 130 - my))) or (
                mouse_dot_mask.overlap_area(replay_btn_mask,
                                            (WIDTH // 2 + 10 - mx, HEIGHT // 2 + 130 - my))):
            interact = 1
    if not len(card_table) :
        if (mouse_dot_mask.overlap_area(home_btn_mask, (
                WIDTH // 2 - home_btn.get_width() - 10 - mx, HEIGHT // 2 + 130 + 90 - my))) or (
                mouse_dot_mask.overlap_area(replay_btn_mask,
                                            (WIDTH // 2 + 10 - mx, HEIGHT // 2 + 130 + 90 - my))):
            interact = 1

    if not interact:
        pygame.mouse.set_cursor(0)
    else:
        pygame.mouse.set_cursor(11)

    pygame.display.update()

running = True
clock = pygame.time.Clock()

with open("data.txt", "r") as file_r :
    for i in range(2) :
        data = file_r.readline().split()
        if not i :
            record_1P[0] = int(data[-3])
            record_1P[1] = int(data[-2])
            record_1P[2] = int(data[-1])
        else :
            record_Bot[0] = int(data[-3])
            record_Bot[1] = int(data[-2])
            record_Bot[2] = int(data[-1])

while running :
    clock.tick(FPS)

    if state == 'menu' :
        menu()
    elif state == 'option' :
        option()
    elif state == 'choose_difficult' :
        choose_difficult(game_mode)
    elif state == 'play_1P' :
        play_1P()
    elif state == 'vsBot' :
        vsBot()
    elif state == 'play_2P' :
        play_2P()
    elif state == 'pause' :
        pause()

with open("data.txt", "w") as file_w :
    for i in range(2) :
        if not i :
            file_w.writelines("- 1P : " + str(record_1P[0]) + " " + str(record_1P[1]) + " " +  str(record_1P[2]) + "\n")
        else :
            file_w.writelines("- Bot : " + str(record_Bot[0]) + " " + str(record_Bot[1]) + " " + str(record_Bot[2]))