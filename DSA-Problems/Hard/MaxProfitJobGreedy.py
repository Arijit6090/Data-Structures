
def job_sequencing(deadline, profit):
    n = len(deadline)

    # Store job ID, deadline and profit
    jobs = []
    for i in range(n):
        jobs.append((i + 1, deadline[i], profit[i]))

    # Sort jobs by profit in descending order
    for i in range(n):
        for j in range(i + 1, n):
            if jobs[i][2] < jobs[j][2]:
                jobs[i], jobs[j] = jobs[j], jobs[i]

    # Create time slots
    max_deadline = max(deadline)
    slots = [None] * max_deadline
    total_profit = 0

    # Schedule jobs
    for job_id, due, money in jobs: # job id, dead line, money
        for t in range(min(due, max_deadline) - 1, -1, -1):
            if slots[t] is None:
                slots[t] = job_id
                total_profit += money
                break # exits the inner loop

    print("Scheduled Jobs:", slots)
    print("Maximum Profit:", total_profit)


deadlines = [5, 3, 3, 2, 4, 2]
profits = [200, 180, 190, 300, 120, 100]

job_sequencing(deadlines, profits)
