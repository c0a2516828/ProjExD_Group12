import math
import os
import random
import sys
import time
import pygame as pg


WIDTH = 1100  # ゲームウィンドウの幅
HEIGHT = 650  # ゲームウィンドウの高さ
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Chat:
    """
    ゲーム画面に出力させる文字を出力
    """
    def __init__(self):
        pass
    def sent(self, massage):
        pass

class Event:
    """
    戦闘をするか宝箱を取るか選択する。
    どちらが出るかはランダム
    """
    def __init__(self):
        pass
    def select():
        pass

class Player:
    def __init__(self):
        pass
    def action():
        pass
    def winBounus():
        pass

class Enemy:
    """
    敵キャラを管理するクラス
    """
    def __init__(self, name, hp, atk,img_path,special=False):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.special = special  # 特殊敵（攻撃されたらゲームオーバー）
        # 敵画像を読み込む
        self.image = pg.image.load(img_path)

        # 画像位置：横中央、縦は上に張り付き
        self.x = (WIDTH - self.image.get_width()) // 2
        self.y = 0

        # 貯め攻撃用
        self.charge_turn = 0

    @staticmethod
    def apper():
        """
        敵を確率で出現させる
        1: hp10 atk10（80%）
        2: hp300 atk100（15%）
        3: hp10000 atk0（5%）攻撃されたらゲームオーバー
        """
        r = random.random()

        if r < 0.80:
            # 80%
            enemy = Enemy("廃れた像", 10, 10,"IMG_廃れた像.jpg")
        elif r < 0.95:
            # 15%
            # 黄金像の強化処理
            base_hp = 300
            base_atk = 50

            Enemy.golden_count = 0

            hp = base_hp * (2**Enemy.golden_count)
            atk = base_atk * (2**Enemy.golden_count)

            Enemy.golden_count += 1

            enemy = Enemy("黄金像", hp, atk, "IMG_黄金像.jpg")
        else:
            # 5%
            enemy = Enemy("退学馬", 10000, 0,"IMG_退学馬.jpg", special=True)

        Chat.sent(f"{enemy.name} が現れた！")
        return enemy

    def action(self, player):
        """
        敵の行動（攻撃・回復・貯め攻撃）
        """
        # 特殊敵は攻撃しない
        if self.special:
            Chat.sent(f"{self.name} はこちらを見つめている…")
            return

        # 行動をランダム選択
        act = random.choice(["attack", "heal"])

        # 通常攻撃
        if act == "attack":
            dmg = self.atk
            Chat.sent(f"{self.name} の攻撃！ {dmg} ダメージ！")
            player.hp -= dmg

        # 回復（自分のHPの半分回復)
        elif act == "heal":
            heal_amount = self.hp // 4
            self.hp += heal_amount
            Chat.sent(f"{self.name} は{heal_amount}回復した！")

def main():
    pg.display.set_caption("ゲーム")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load(f"IMG_2090.jpg")
    scene = "null"
    stage = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
        
        if scene == "start":
            continue
        elif scene == "battle_myTurn":
            Player.action()
            scene = Player.finishScene()
        elif scene == "battle_enemyTurn":
            Enemy.apper()
            Enemy.action()
        elif scene == "finish_battle":
            Player.winBounus()
        elif scene == "select_action":
            Event.select()
        elif scene == "finish":
            continue

        
        screen.blit(bg_img, [0, 0])
        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()