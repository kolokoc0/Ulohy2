from PIL import Image

queen_img = Image.open("queen.png")
queen_img = queen_img.resize((125,125))

def prepare_matrix():
    matrix = []
    sub_matrix = []
    for y in range(8):
        for x in range(8):
            sub_matrix.append(0)
        matrix.append(sub_matrix)
        sub_matrix = [ ]
    return matrix

matrix = prepare_matrix()

def prepare_board():
    img = Image.new("RGB",(1000,1000),"white")
    pixels = img.load()
    temp = True
    for y in range(0,1000):
        for x in range(0,1000):
            if (y//125)%2==0:
                if (x//125)%2==0:
                    pixels[x,y] = (255,255,255)
                else:
                    pixels[x,y] = (0,0,0)
            elif (y//125)%2==1:
                if (x//125)%2 == 0:
                    pixels[x,y] = (0,0,0)
                else:
                    pixels[x,y] = (255,255,255)
    return img

def place_queens(placement):
    for row in placement:
        for num in row:
            if num==1:
                y = ((placement.index(row))*125)
                x = ((row.index(num))*125)
                img_new.paste(queen_img,(y,x),queen_img) 
    return img_new

def check(x:int,y:int) -> bool:
    for j in range(8):
        for i in range(8):
            if j==y:
                if matrix[y][i]==1:
                    return False
            elif i==x:
                if matrix[j][x]==1:
                    return False
            elif i+j==x+y:
                if matrix[j][i]==1:
                    return False
            elif i-j==x-y:
                if matrix[j][i]==1:
                    return False
    return True
name = 1
count = 0
def drticka(dama:int):
    global matrix,count,name,img_new
    if dama==8:
        print(matrix)
        print("-"*210)
        count +=1
        img_new = prepare_board()
        img_new = place_queens(matrix)
        img_new.save(f"Solution{name}.png",)
        name+=1
    else:
        for i in range(8):
            if check(i,dama):
                matrix[dama][i] = 1
                drticka(dama+1)
                matrix[dama][i] = 0

drticka(0)
print(count)
