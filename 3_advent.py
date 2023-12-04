with open("3_advent.txt", 'r') as file:
    graph = [list(line.strip()) for line in file.readlines()]
# print(graph)

ROW_LENGTH = len(graph)
COL_LENGTH = len(graph[0])

def extract_numbers(row,col):
    # print("extracting")
    num = ""
    # Move leftward
    ncol = col
    while 0 <= ncol < COL_LENGTH and graph[row][ncol].isdigit():
        num = graph[row][ncol] + num  # Add digit on left side
        graph[row][ncol] = "."  # mark as seen
        ncol -= 1
    # Move rightward
    ncol = col + 1
    while 0 <= ncol < COL_LENGTH and graph[row][ncol].isdigit():
        num = num + graph[row][ncol]  # Add digit on right side
        graph[row][ncol] = "."  # mark digit as seen
        ncol += 1
    # print("extracted", num)
    return int(num)
def search_adjacents(row,col):
    graph[row][col] = "."  # Mark as seen
    # print("starting search...", row, col, graph[row][col])
    directions = [(1,0), (0,1), (-1, 0), (0, -1), (1,1), (1,-1), (-1, 1), (-1,-1)]
    sum_ = 0
    for x,y in directions:
        nrow = row + y
        ncol = col + x
        if 0 <= nrow < ROW_LENGTH and 0 <= ncol < COL_LENGTH and graph[nrow][ncol].isdigit():
            sum_ += extract_numbers(nrow,ncol)
    return sum_
ans = 0
# print("Graph", graph)
for i in range(ROW_LENGTH):
    for j in range(COL_LENGTH):
        if graph[i][j] != "." and not graph[i][j].isdigit():
            ans += search_adjacents(i,j)
print(ans)