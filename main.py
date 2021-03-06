import random
import pygame
import pygame_menu
import pickle
import os.path
import glob



num = 1

# http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids
# \-> how to detect mouse and change grid

def count_neighbors(grid2count, posInRow, posInCol):
    """returns number of ALIVE neighbors from a given position on a given grid using try except approach"""
    count = 0

    for x in range(-1, 2):
        for y in range(-1, 2):
            try:
                if grid2count[posInRow + x][posInCol + y] == 1:
                    count += 1
            except:
                count += 0

    count -= grid2count[posInRow][posInCol]  # doesn't count itself

    return count


def count_neighbors_wrap_around(grid2count, posInRow, posInCol, row_Count, col_Count):
    """returns number of ALIVE neighbors from a given position on a given grid using wrap around approach"""
    count = 0

    for x in range(-1, 2):
        for y in range(-1, 2):
            if grid2count[(posInRow + x) % row_Count][(posInCol + y) % col_Count] == 1:
                count += 1

    count -= grid2count[posInRow][posInCol]  # doesn't count itself

    return count


def make2D_grid(rows, cols):
    """Returns a 2d grid filled with zeros"""
    grid = []

    for x in range(0, cols):
        grid.append([])
        for y in range(0, rows):
            grid[x].append(0)

    return grid


def make2D_grid_random_fill(rows, cols):
    """Returns a 2d grid filled with RANDOM zeros and ones"""
    grid = []

    for x in range(0, cols):
        grid.append([])
        for y in range(0, rows):
            if random.randint(0, 2) == 0:  # 33% change of filling square
                grid[x].append(1)
            else:
                grid[x].append(0)

    return grid

def deleteImages():
    try:
        for file in glob.glob("*.png"):
            file_to_delete = file
            os.remove(file_to_delete)
            print("Encontro imagen " + file)


    except:
        print("Error while deleting file ", file)
        pass


# ------------------------ Settings ------------------------ #
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# This sets the WIDTH and HEIGHT of each square in the grid
SQUARE_SIZE = 10
WIDTH = SQUARE_SIZE
HEIGHT = SQUARE_SIZE

# This sets the margin between each cell
MARGIN = 1

# This sets the number of columns and rows
COL_COUNT = 100
ROW_COUNT = 100

grid = make2D_grid(rows=COL_COUNT, cols=ROW_COUNT)

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [((COL_COUNT * WIDTH) + (COL_COUNT * MARGIN) + MARGIN),
               (ROW_COUNT * HEIGHT) + (ROW_COUNT * MARGIN) + MARGIN]

screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Game of Life NFT")

# Loop until the user clicks the close button.
done = False

done_first_board = False
grid_saved = None



# Used to manage how fast the screen updates
clock = pygame.time.Clock()

directory = os.getcwd()

os.chdir(directory)

# We look for .png in the local dir. The .png is a picture with a transparency. Can be created in Photoshop
# Only one .png must be at the dir
for file in glob.glob("*.png"):
    backgroundImage = file
    print("Encontro imagen "+  file)




# We conveert to transparent so the grid boar will be visible
background_image = pygame.image.load(file).convert_alpha()
# adjust the image to the windows size
background_image = pygame.transform.scale(background_image, (WINDOW_SIZE))

# move to the
os.chdir("Depot")
print(screen)

Life_speed = 7  # Speed of the game in "Life Phase"

instructions = """
--- Drawing phase --- 
MOUSE - Left and Right click to paint or clear square
S - Stop Drawing Phase and Start Life Phase
m - Reset to first painting  
k - load saved pickle file
C - Clear grid
R - Fill grid at random
Q - Quit Game
--- Life Phase ---
S - Stop Life Phase and Start Drawing Phase
O - To Decrease speed
P - To Increase speed
Q - Quit Game"""
print(instructions)
# -------- Main Program Loop -----------

running_game = True
if os.path.isfile("grid_saved.pickle"):
    with open('grid_saved.pickle', 'rb') as f:
        grid = pickle.load(f)

while running_game:
    print("Drawing NFT Phase")
    pygame.display.set_caption("Game of Life (Drawing NFT Phase)")
    

    while not done:

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                running_game = False  # flag to exit program
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)

                mouseButtonPressed = pygame.mouse.get_pressed()

                mouseState = 0

                if mouseButtonPressed == (1, 0, 0): # left click -> paints green
                    mouseState = 1
                elif mouseButtonPressed == (0, 0, 1): # right click -> paints white
                    mouseState = 0

                try:
                    # Set that location to zero or one
                    grid[row][column] = mouseState
                    print("Click", mouseState, ":", pos, "Grid coordinates: ", row, column)

                except:
                    # print("Error out of range\nClick ", pos, "Grid coordinates: ", row, column)
                    pass

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    print("\"s\" key was pressed\nand Drawing phase exited")
                    deleteImages()
                    num = 1
                    done = True
                    done_first_board = True

                elif event.key == pygame.K_r:
                    print("\"r\" key was pressed\nand random grid was created")
                    grid = make2D_grid_random_fill(rows=COL_COUNT, cols=ROW_COUNT)

                elif event.key == pygame.K_m:
                    print("\"m\" key was pressed\nand First NFT Board Loaded")
                    grid = grid_saved
                    pygame.display.flip()
                    done_first_board = False

                elif event.key == pygame.K_k:
                    print("\"k\" key was pressed\nand pickle file was Loaded")
                    with open('grid_saved.pickle', 'rb') as f:
                        grid = pickle.load(f)

                    pygame.display.flip()
                    done_first_board = False

                elif event.key == pygame.K_c:
                    print("\"c\" key was pressed\nand grid was cleared")
                    grid = make2D_grid(rows=COL_COUNT, cols=ROW_COUNT)
                elif event.key == pygame.K_q:
                    print("\"q\" key was pressed\nand Game ended")
                    done = True
                    running_game = False



        # Set the screen background
        screen.fill(BLACK)

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COL_COUNT):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

            if not done_first_board:
                grid_saved = grid
                with open('grid_saved.pickle', 'wb') as f:
                    pickle.dump(grid_saved, f)
                # print(grid_saved)

        # Limit to 60 frames per second
        clock.tick(60)
        screen.blit(background_image, [0, 0])
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()



    if running_game == True:
        done = False

    else:
        done = True



    running_caption_plus_speed = "".join(["Conway's Game of Life (Life Phase) Speed: ", str(Life_speed)])
    pygame.display.set_caption(running_caption_plus_speed)
    # ----------------------- The game HAS LIFE here --------------------- #
    while not done:
        done_first_board = True

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                running_game = False # flag to exit program
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:

                    print("\"s\" key was pressed\nand Life phase exited")
                    done = True
                elif event.key == pygame.K_o:
                    if Life_speed > 1:
                        Life_speed -= 1
                        running_caption_plus_speed = "".join(
                            ["Conway's Game of Life (Life Phase) Speed: ", str(Life_speed)])
                        pygame.display.set_caption(running_caption_plus_speed)
                        print("\"o\" key was pressed\nand the speed was decreased to:", Life_speed)
                    else:
                        print("\"o\" key was pressed\nand the speed remains:", Life_speed)
                elif event.key == pygame.K_p:
                    Life_speed += 1
                    running_caption_plus_speed = "".join(
                        ["Conway's Game of Life (Life Phase) Speed: ", str(Life_speed)])
                    pygame.display.set_caption(running_caption_plus_speed)
                    print("\"p\" key was pressed\nand the speed was increased to:", Life_speed)
                elif event.key == pygame.K_q:
                    print("\"q\" key was pressed\nand Game ended")
                    done = True
                    running_game = False

        # Set the screen background
        screen.fill(BLACK)

        # ------------- Draw the grid -------------- #
        for row in range(ROW_COUNT):
            for column in range(COL_COUNT):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])



        # ----------- Compute new board --------------- #
        newGrid = make2D_grid(rows=COL_COUNT, cols=ROW_COUNT)

        for row in range(ROW_COUNT):
            for column in range(COL_COUNT):

                # neighborsCount = count_neighbors(grid2count=grid, posInCol=column, posInRow=row) # try except
                neighborsCount = count_neighbors_wrap_around(grid2count=grid, posInCol=column, posInRow=row,
                                                             col_Count=COL_COUNT, row_Count=ROW_COUNT)  # wrap around



                if grid[row][column] == 1:
                    if neighborsCount < 2:  # Each cell with one or no neighbors dies, as if by solitude.
                        newGrid[row][column] = 0
                    elif neighborsCount > 3:  # Each cell with four or more neighbors dies, as if by overpopulation.
                        newGrid[row][column] = 0
                    elif neighborsCount == 2 or neighborsCount == 3:  # Each cell with two or three neighbors survives
                        newGrid[row][column] = 1

                elif grid[row][column] == 0 and neighborsCount == 3:  # Each cell with three neighbors becomes populated
                    newGrid[row][column] = 1



        grid = newGrid.copy()

        # now save the drawing
        # can save as .bmp .tga .png or .jpg

        fname = str(num)+"_" + file
        pygame.image.save(screen, fname)
        print("file {} has been saved".format(fname))
        num = num+1
        # Limit frames per second
        clock.tick(Life_speed)

        # Go ahead and update the screen with what we've drawn.
        screen.blit(background_image, [0, 0])
        pygame.display.flip()

    print("Exited Life Phase")
    if running_game == True:
        done = False
    else:
        done = True

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
print("Game Ended")
pygame.quit()