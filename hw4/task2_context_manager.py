from time import time, sleep


class timer:
    def __init__(self, block_name):
        self.block_name = block_name

    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time() - self.start_time
        print(f"timer: block '{self.block_name}' executed in {elapsed_time:.3f} sec")


if __name__ == '__main__':
    with timer('doing some sleeps'):
        sleep(1)
        sleep(2)
        sleep(3)
