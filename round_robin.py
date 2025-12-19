from collections import deque

def round_robin(processes, quantum):
    queue = deque(processes)

    while queue:
        process, time = queue.popleft()
        if time > quantum:
            print(f"{process} runs for {quantum}")
            queue.append((process, time - quantum))
        else:
            print(f"{process} finishes in {time}")


if __name__ == "__main__":
    processes = [
        ("P1", 5),
        ("P2", 3),
        ("P3", 7)
    ]

    round_robin(processes, quantum=2)
