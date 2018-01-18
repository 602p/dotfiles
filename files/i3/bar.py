import sys
import json
import subprocess

def get_brightness():
    with open("/sys/class/backlight/radeon_bl0/brightness", 'r') as b:
        with open("/sys/class/backlight/radeon_bl0/max_brightness", 'r') as m:
            return (int(b.read())/int(m.read()))*100

def get_ram_usage():
    return (float([i for i in subprocess.check_output("free -h | grep Mem:", shell=True).decode("ascii").split(" ") if i][2][:-1])/7.8)*100


def print_line(message):
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()

def read_line():
    """ Interrupted respecting reader for stdin. """
    # try reading a line, removing any extra whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    # Skip the first line which contains the version header.
    print_line(read_line())

    # The second line contains the start of the infinite array.
    print_line(read_line())

    while True:
        line, prefix = read_line(), ''
        # ignore comma at start of lines
        if line.startswith(','):
            line, prefix = line[1:], ','

        j = json.loads(line)
        # insert information into the start of the json, but could be anywhere
        # CHANGE THIS LINE TO INSERT SOMETHING ELSE
        j.insert(4, {'full_text' : '☀%03i%%'%get_brightness(), 'name' : 'bright', 'color':'#aaaa00'})
        j.insert(5, {'full_text' : '%02i%% R'%get_ram_usage(), 'name' : 'ram'})
        # and echo back new encoded json
        print_line(prefix+json.dumps(j))
