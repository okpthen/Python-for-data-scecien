# import os
# import math
import time
import shutil


def format_time(seconds):
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range):
    # total = len(lst)
    # size = os.get_terminal_size().columns
    # size -= 5
    # size -= 3 + len(str(total)) * 2
    # def print_line(percent, num_colored, num_empty, p):
    #     print('\r', end='')
    #     print(f'{percent:3}%|{"█" * num_colored}{" " * num_empty}| ', end='')
    #     print("{i:{lenght}}".format(i=p, lenght=len(str(total))), end='')
    #     print(f'/{total}', end='', flush=True)

    # for i in lst:
    #     if i % 20 == 0:
    #         percent = int(i / total * 100)
    #         num_colored = math.ceil(size * percent / 100)
    #         num_empty = size - num_colored
    #         print_line(percent, num_colored, num_empty, i)
    #     yield i
    # print_line(100, size, 0, total)
    total = len(lst)
    start_time = time.time()

    terminal_width = shutil.get_terminal_size().columns - 30
    progress_bar_width = terminal_width - 10

    for i, item in enumerate(lst, start=1):
        progress = int(i / total * progress_bar_width)
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time
        eta = (total - i) / speed

        elapsed_formatted = format_time(elapsed_time)
        eta_formatted = format_time(eta)

        progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
        progress_percentage = progress * 100 // progress_bar_width
        progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"
        time_info = f"[{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"

        print(f"\r{progress_info} {time_info}", end="", flush=True)
        yield item
