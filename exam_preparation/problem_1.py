jobs = [int(job) for job in input().split(", ")]
interested_job_index = int(input())
clock_cycles = 0
index_counter = 0

for job in jobs:
    if job < jobs[interested_job_index]:
        clock_cycles += job
    elif job == jobs[interested_job_index]:
        if index_counter < interested_job_index:
            clock_cycles += job

    index_counter += 1

print(clock_cycles + jobs[interested_job_index])