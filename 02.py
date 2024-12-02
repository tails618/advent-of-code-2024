# day 2

def check_report(report_list: list[int]) -> bool:
    increments: list[int] = [report_list[i + 1] - report_list[i] for i in range(len(report_list) - 1)]
    return set(increments) <= {1, 2, 3} or set(increments) <= {-1, -2, -3}

reports: list[str] = open('02-data.txt', 'r').readlines()
safe_counter_pt1: int = 0
safe_counter_pt2: int = 0

report: str
for report in reports:
    split_report: list[str] = report.split()
    report_list: list[int] = list(map(int, split_report))
    if check_report(report_list):
        safe_counter_pt1 += 1
        safe_counter_pt2 += 1
    else:
        for i in range(len(report_list)):
            report_list_minus_one = report_list[:i] + report_list[i + 1:]
            if check_report(report_list_minus_one):
                safe_counter_pt2 += 1
                break

print(safe_counter_pt1)
print(safe_counter_pt2)
