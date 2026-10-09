INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"
with open(INPUT_FILE, "r", encoding = "utf-8") as f:
    next(f)
    score_m = 0
    score_p = 0
    score_e = 0
    students_count = 0
    best_st = 0
    best_st_name = ""
    current_st = 0
    current_st_name = ""
    m_avg = 0
    p_avg = 0
    e_avg = 0
    for line in f:
        lines = line.strip().split(",")
        score_m += int(lines[1])
        score_p += int(lines[2])
        score_e += int(lines[3])
        students_count += 1
        current_st = (int(lines[1]) + int(lines[2]) + int(lines[3]))/3
        current_st_name = lines[0]
        if current_st > best_st:
            best_st = current_st
            best_st_name = lines[0]
    m_avg = round (score_m/students_count, 1)
    p_avg = round (score_p/students_count, 1)
    e_avg = round (score_e/students_count, 1)

with open(OUTPUT_FILE, "w", encoding = "utf-8" ) as f:
    f.write(f"Середній бал по класу: \n")
    print(f"Середній бал по класу: \n")
    f.write(f"math: {m_avg}\n")
    print(f"math: {m_avg}\n")
    f.write(f"python: {p_avg}\n")
    print(f"python: {p_avg}\n")
    f.write(f"english: {e_avg}\n")
    print(f"english: {e_avg}\n")
    f.write(f"Найкращий студент {best_st_name} {best_st}")
    print(f"Найкращий студент {best_st_name} {best_st}")