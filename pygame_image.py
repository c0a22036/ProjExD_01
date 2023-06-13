import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    
    # 1. 背景画像を読み込み、Surfaceを生成
    bg_img = pg.image.load("pg_bg.jpg").convert()

    # 2. こうかとん画像を読み込み、Surfaceを生成し左右反転
    kk_img = pg.image.load("3.png").convert()
    kk_img_flipped = pg.transform.flip(kk_img, True, False)

    # 3. 画像Surfaceを要素とするリストを生成
    image_list = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.blit(bg_img, (0, 0))  # 4. 背景画像を表示

        # 5. 画像Surfaceを交互に表示
        image_index = tmr % len(image_list)
        image = image_list[image_index]
        screen.blit(image, (300, 200))

        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
