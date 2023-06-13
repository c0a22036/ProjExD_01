import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ!こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    tmr = 0
    x = 0  # 横座標の初期値

    image_list = [kk_img, pg.transform.rotate(kk_img, 2),pg.transform.rotate(kk_img, 4),pg.transform.rotate(kk_img, 6),pg.transform.rotate(kk_img, 8),pg.transform.rotate(kk_img, 10),pg.transform.rotate(kk_img, 8),pg.transform.rotate(kk_img, 6),pg.transform.rotate(kk_img, 4),pg.transform.rotate(kk_img, 2),]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.blit(bg_img, (x, 0))  # 背景画像の横座標を指定して表示
        screen.blit(image_list[tmr % len(image_list)], (300, 200))  # 画像の表示位置を指定
        pg.display.update()
        tmr += 1
        x -= 1  # 背景画像の横座標を更新

        if x <= -800:  # 背景画像が画面外に移動したらリセット
            x = 0
            

        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

