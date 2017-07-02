from random import choices, randint
import string

def r_str_end():
    return str.join('', choices(string.ascii_uppercase + string.digits, k=randint(1,8)))

def random_ending():
    a = ['.csv', '.log', '.txt.' ]
    for _ in range(5):
        a.append(r_str_end())
    return a
    
def mach_beg():
    rand_beg_num = str(randint(2,20))
    main_beg = '1T'
    rand_num = str(randint(1, 99999))
    rand_char = choices(string.ascii_uppercase, k =1)[0]
    return str.join('', (rand_beg_num , rand_char , rand_num.zfill(5))), str.join( '', (main_beg , rand_num.zfill(5)))
   

def log_generate(number):
    # '1X03656_20170622_000_148331.log'
    
    all_logs = []
    for _ in range(number):
        rand_date = ''.join(choices(string.digits, k=8))
        rand_log_daily = ''.join(choices(string.digits, k=3))
        random_log_all = ''.join(choices(string.digits, k=6))
        both_beginning = mach_beg()
        all_endings = random_ending()
        for value in both_beginning:
            log = str.join('_', (value, rand_date, rand_log_daily, random_log_all))
            for ending in all_endings:
                all_logs.append(str.join('.', (log, ending)))
                
    f = open("myfile.txt", "w")
    f.write("\n".join(map(lambda x: str(x), all_logs)))
    f.close()
    
    
log_generate(50)
    
   

    