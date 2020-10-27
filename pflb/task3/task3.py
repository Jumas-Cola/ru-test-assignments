import datetime
import sys

def parse_log(filepath, date_from, date_to):
    with open(filepath, encoding='utf8') as log_file:
        lines = log_file.readlines()
        total_volume = float(lines[1])
        current_volume = float(lines[2])
        start_volume = current_volume
        
        total_top_up = 0
        fail_top_up = 0
        water_up = 0
        fail_water_up = 0

        total_scoop = 0
        fail_scoop = 0
        water_down = 0
        fail_water_down = 0

        log_lines = lines[3:]
        for line in log_lines:
            dt, other = line.split('–')
            date_log = datetime.datetime.strptime(dt.strip(), '%Y-%m-%dT%H:%M:%S.%fZ')
            if date_from < date_log < date_to:
                command = other[other.find('-') + 1: other.rfind(' ')].strip()
                vol = float(other[other.rfind(' '):-2])
                if command == 'wanna top up':
                    total_top_up += 1
                    if total_volume >= current_volume + vol:
                        current_volume += vol
                        water_up += vol
                    else:
                        fail_top_up += 1
                        fail_water_up += vol
                elif command == 'wanna scoop':
                    total_scoop += 1
                    if 0 <= current_volume - vol:
                        current_volume -= vol
                        water_down += vol
                    else:
                        fail_scoop += 1
                        fail_water_down += vol

    
    with open('task3.csv', 'w', encoding='utf8') as output:
        output.write('total_top_up,percent_fail_top_up,water_up,fail_water_up,total_scoop,percent_fail_scoop,water_down,fail_water_down,start_volume,end_volume\n')
        output.write(','.join(str(i) for i in (total_top_up, fail_top_up/total_top_up*100 if total_top_up else 0, water_up, fail_water_up, 
            total_scoop, fail_scoop/total_scoop*100 if total_scoop else 0, water_down, fail_water_down, start_volume, current_volume)))


def main():
    filepath = sys.argv[1]
    date_from = datetime.datetime.strptime(sys.argv[2], '%Y-%m-%dT%H:%M:%S')
    date_to = datetime.datetime.strptime(sys.argv[3], '%Y-%m-%dT%H:%M:%S')
    parse_log(filepath, date_from, date_to)


if __name__ == '__main__':
    main()
