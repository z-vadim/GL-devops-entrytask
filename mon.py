import psutil
import sys

#please comment string bellow if you don't build docker container
psutil.PROCFS_PATH = '/host-proc'


def check_mem():
    mem_info = {'virtual_memory': {
                 'total': psutil.virtual_memory().total/ 2**20,
                 'available': psutil.virtual_memory().available/ 2**20,
                 'used': psutil.virtual_memory().used/ 2**20,
                 'free': psutil.virtual_memory().free/ 2**20,
                 'percent': psutil.virtual_memory().percent
                },
                'swap_memory': {
                 'total': psutil.swap_memory().total/ 2**20,
                 'used': psutil.swap_memory().used/ 2**20,
                 'free': psutil.swap_memory().free/ 2**20,
                 'percent': psutil.swap_memory().percent
                }
            }
    return mem_info


def check_cpu():
    cpu_info = {'cpu': {
                 'idle': psutil.cpu_times().idle,
                 'user': psutil.cpu_times().user,
                 'guest': psutil.cpu_times().guest,
                 'iowait': psutil.cpu_times().iowait,
                 'system': psutil.cpu_times().system
                }
            }
    return cpu_info


def main(args):
    try:
        if args[1] == 'mem':
            print(check_mem())
        elif args[1] == 'cpu':
            print(check_cpu())
        else:
            print("You need enter metric name: 'cpu' or 'mem'")
    except:
        print("You need enter metric name: 'cpu' or 'mem'")


if __name__ == "__main__":
    main(sys.argv)
