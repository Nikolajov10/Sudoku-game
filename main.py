import pygame
from sudokuFun import *

# screen setup
pygame.init()
widthS = 610
heightS = 700
screen = pygame.display.set_mode((widthS, heightS))
pygame.display.set_caption('Sudoku')
# backend pattern
# making of table and check function
table = [[9, 0, 0, 0, 0, 6, 7, 3, 0],
         [0, 0, 0, 9, 4, 0, 0, 0, 2],
         [0, 2, 4, 0, 0, 0, 0, 0, 0],
         [0, 6, 5, 0, 0, 0, 0, 8, 3],
         [0, 0, 7, 0, 8, 0, 5, 0, 0],
         [8, 9, 0, 0, 0, 0, 4, 1, 0],
         [0, 0, 0, 0, 0, 0, 9, 7, 0],
         [7, 0, 0, 0, 2, 1, 0, 0, 0],
         [0, 8, 6, 7, 0, 0, 0, 0, 5]]

#images of numbers
list_of_images=[pygame.image.load('images/one.png'), pygame.image.load('images/two.png'), pygame.image.load(
    'images/three.png'), pygame.image.load('images/four.png'), pygame.image.load('images/five.png'), pygame.image.load(
    'images/six.png'), pygame.image.load('images/seven.png'), pygame.image.load('images/eight.png'), pygame.image.load(
    'images/nine.png')]
list_small_img=[pygame.image.load('images/s_one.png'), pygame.image.load('images/s_two.png'), pygame.image.load(
    'images/s_three.png'), pygame.image.load('images/s_four.png'), pygame.image.load('images/s_five.png'), pygame.image.load(
    'images/s_six.png'), pygame.image.load('images/s_seven.png'), pygame.image.load('images/s_eight.png'), pygame.image.load(
    'images/s_nine.png')]
# game loop
run = True
end=False
size=67
mouse_column=-1
mouse_row=-1
list_small_positionsX=[]
list_small_positionsY=[]
num_list=[]
len_of_small_lists=0
solve(table)

mistakes=0
font_m=pygame.font.Font('freesansbold.ttf',20)
while run:
    #time
    playing_time=pygame.time.get_ticks()
    playing_time=playing_time//1000
    seconds=playing_time%60
    minutes=playing_time//60
    if minutes<10:
        str_min='0'+str(minutes)
    else:
        str_min=str(minutes)
    if seconds<10:
        str_sec='0'+str(seconds)
    else:
        str_sec=str(seconds)
    time=font_m.render("TIME:"+str_min+":"+str_sec,True,(0,0,0))
    screen.fill((135,206,235))
    m_text = font_m.render('MISTAKES:' + str(mistakes), True, (255, 0, 100))
    screen.blit(m_text,(10,625))
    screen.blit(time,(500,625))
    for i in range(0,limit):
        if (i+1)%3==0:
            color=(100,0,100)
            width=4
        else:
            width=1
            color=(0,0,0)
        pygame.draw.line(screen,color,(6,size+i*size),(size*8+size,size+i*size),width)
        pygame.draw.line(screen,color,(size+i*size,6),(size+i*size,size+8*size),width)
    color=(100,0,100)
    width=5
    pygame.draw.line(screen,color,(6,6),(size+8*size,6),width)
    pygame.draw.line(screen, color, (6,6), (6, size+size*8),width)
    num=0
    for i in range(limit):
        for j in range(limit):
            if table[i][j]>0:
                screen.blit(list_of_images[table[i][j]-1], (6+j*(size-1), 6+i*(size-1)))
                num+=1
    if num==81:
        end=True
    pygame.mouse.set_visible(True)
    count=0
    while end and count<20_000:
        pygame.display.update()
        if event.type == pygame.QUIT:
            run=False
            end=False
        count+=1
        if count==20_000:
            run = False
            end = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            end=True
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                finish_table(table)
                end=True
                break
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            mouse_column = mouseX // size
            mouse_row = mouseY // size
            if mouse_row>8:
                mouse_row=-1
            if mouse_column>8:
                mouse_column=-1
        if event.type==pygame.KEYDOWN and mouse_row!=-1 and mouse_row!=-1:
            if event.key==pygame.K_1 and table[mouse_row][mouse_column]<=0:
                #ejection and insertion
                k=-1
                for i in range(0,len_of_small_lists):
                    if list_small_positionsX[i]==mouse_column and list_small_positionsY[i]==mouse_row:
                        k=0
                        num_list[i]=1
                if k==-1:
                    list_small_positionsX.append(mouse_column)
                    list_small_positionsY.append(mouse_row)
                    num_list.append(1)
                    len_of_small_lists += 1
            elif event.key == pygame.K_2 and table[mouse_row][mouse_column]<=0:
                # ejection and insertion
                k = -1
                for i in range(0, len_of_small_lists):
                    if list_small_positionsX[i] == mouse_column and list_small_positionsY[i] == mouse_row:
                        k = 0
                        num_list[i] = 2
                if k == -1:
                    list_small_positionsX.append(mouse_column)
                    list_small_positionsY.append(mouse_row)
                    num_list.append(2)
                    len_of_small_lists += 1
            elif event.key == pygame.K_3 and table[mouse_row][mouse_column]<=0:
                # ejection and insertion
                k = -1
                for i in range(0, len_of_small_lists):
                    if list_small_positionsX[i] == mouse_column and list_small_positionsY[i] == mouse_row:
                        k = 0
                        num_list[i] = 3
                if k == -1:
                    list_small_positionsX.append(mouse_column)
                    list_small_positionsY.append(mouse_row)
                    num_list.append(3)
                    len_of_small_lists += 1
            elif event.key == pygame.K_4 and table[mouse_row][mouse_column]<=0:
                # ejection and insertion
                k = -1
                for i in range(0, len_of_small_lists):
                    if list_small_positionsX[i] == mouse_column and list_small_positionsY[i] == mouse_row:
                        k = 0
                        num_list[i] = 4
                if k == -1:
                    list_small_positionsX.append(mouse_column)
                    list_small_positionsY.append(mouse_row)
                    num_list.append(4)
                    len_of_small_lists += 1
            elif event.key == pygame.K_5 and table[mouse_row][mouse_column]<=0:
                # ejection and insertion
                k = -1
                for i in range(0, len_of_small_lists):
                    if list_small_positionsX[i] == mouse_column and list_small_positionsY[i] == mouse_row:
                        k = 0
                        num_list[i] = 5
                if k == -1 and table[mouse_row][mouse_column]<=0:
                    list_small_positionsX.append(mouse_column)
                    list_small_positionsY.append(mouse_row)
                    num_list.append(5)
                    len_of_small_lists += 1
            elif event.key == pygame.K_6 and table[mouse_row][mouse_column]<=0:
                # ejection and insertion
                k = -1
                for i in range(0, len_of_small_lists):
                    if list_small_positionsX[i] == mouse_column and list_small_positionsY[i] == mouse_row:
                        k = 0
                        num_list[i] = 6
                if k == -1:
                    list_small_positionsX.append(mouse_column)
                    list_small_positionsY.append(mouse_row)
                    num_list.append(6)
                    len_of_small_lists += 1
            elif event.key == pygame.K_7 and table[mouse_row][mouse_column]<=0:
                # ejection and insertion
                k = -1
                for i in range(0, len_of_small_lists):
                    if list_small_positionsX[i] == mouse_column and list_small_positionsY[i] == mouse_row:
                        k = 0
                        num_list[i] = 7
                if k == -1 and table[mouse_row][mouse_column]<=0:
                    list_small_positionsX.append(mouse_column)
                    list_small_positionsY.append(mouse_row)
                    num_list.append(7)
                    len_of_small_lists += 1
            elif event.key == pygame.K_8 and table[mouse_row][mouse_column]<=0:
                # ejection and insertion
                k = -1
                for i in range(0, len_of_small_lists):
                    if list_small_positionsX[i] == mouse_column and list_small_positionsY[i] == mouse_row:
                        k = 0
                        num_list[i] =8
                if k == -1:
                    list_small_positionsX.append(mouse_column)
                    list_small_positionsY.append(mouse_row)
                    num_list.append(8)
                    len_of_small_lists += 1
            elif event.key == pygame.K_9 and table[mouse_row][mouse_column]<=0:
                # ejection and insertion
                k = -1
                for i in range(0, len_of_small_lists):
                    if list_small_positionsX[i] == mouse_column and list_small_positionsY[i] == mouse_row:
                        k = 0
                        num_list[i] = 9
                if k == -1:
                    list_small_positionsX.append(mouse_column)
                    list_small_positionsY.append(mouse_row)
                    num_list.append(9)
                    len_of_small_lists += 1
            if event.key==pygame.K_KP_ENTER and mouse_row!=-1 and mouse_column!=-1 and table[mouse_row][mouse_column]<=0:
                k=-1
                for i in range(0,len_of_small_lists):
                    if list_small_positionsX[i]==mouse_column and list_small_positionsY[i]==mouse_row:
                        k=i
                        break

                if  k!=-1 and abs(table[mouse_row][mouse_column])==num_list[k]:
                    table[mouse_row][mouse_column]=abs(table[mouse_row][mouse_column])
                    num_list.pop(k)
                    list_small_positionsY.pop(k)
                    list_small_positionsX.pop(k)
                    len_of_small_lists-=1
                else:
                    mistakes+=1
    for i in range(0,len_of_small_lists):
        screen.blit(list_small_img[num_list[i]-1],(6+list_small_positionsX[i]*size,6+list_small_positionsY[i]*size))
    if mouse_column>=0 and mouse_row>=0:
        pygame.draw.rect(screen, (255, 0, 0), [6 + mouse_column * (size-1), 6 + mouse_row * (size-1), size-2, size-2], 3)
    pygame.display.update()
pygame.quit()
