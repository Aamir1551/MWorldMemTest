import subprocess

num_blocks = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000]
num_blocks_space = [1, 100, 200, 300, 400, 500]
world_size_min_x = "0"
world_size_max_x = "100"
world_size_min_y = "0"
world_size_max_y = "100"
world_size_min_z = "0"
world_size_max_z = "100"
world_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


f = open("spaceTimings.txt", "a")
for i in range(10):
    a = i
    for j in num_blocks_space:
        i = 2 ** a
        i = str(i)
        j = str(j)
        result = subprocess.run(["valgrind", "--tool=massif", "--time-unit=B", "--stacks=yes", "--massif-out-file=massif.out."+i+"_"+j ,"./build/simulation/environment/simulation", "10", j, j, j, j, j, j,
                                 world_size_min_x, i, world_size_min_y, i, world_size_min_z,
                                 i], stdout=subprocess.PIPE).stdout.decode('utf-8')
        f.write(result)

f.close()
