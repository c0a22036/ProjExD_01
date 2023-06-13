import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    # 背景画像をロード
    bg_img1 = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.image.load("ex01/fig/pg_bg.jpg")

    # 背景画像の横座標の初期値
    x = 0

    # 3.pngを読み込み、Surfaceを生成
    kk_img = pg.image.load("ex01/fig/3.png")
    # 左右を反転
    kk_img = pg.transform.flip(kk_img, True, False)

    # 画像Surfaceを要素とするリストを生成
    image_list = [kk_img, pg.transform.rotate(kk_img, 10)]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.blit(bg_img1, [x, 0])
        screen.blit(bg_img2, [x - 1600, 0])

        # 画像Surfaceを交互に表示
        image_index = tmr % len(image_list)
        image = image_list[image_index]
        screen.blit(image, (300, 200))

        pg.display.update()
        tmr += 1
        clock.tick(100)

        # 背景画像の横座標を更新
        x = (x - 1) % 1600


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()