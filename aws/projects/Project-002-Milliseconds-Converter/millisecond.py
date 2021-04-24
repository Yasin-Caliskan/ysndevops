def convert(millisecond):
    hour_in_millisecond = 60*60*1000
    hour = millisecond // hour_in_millisecond
    millisecond_left = millisecond % hour_in_millisecond

    minute_in_millisecond = 60*1000
    minute = millisecond_left // minute_in_millisecond
    millisecond_left = millisecond_left % minute_in_millisecond

    second = millisecond_left // 1000

    return f'{hours} hour/s '*(hours!=0) + f'{minutes} minute/s '*(minutes!=0) + f'{seconds} 
    second/s '*(seconds!=0) or f'just {millisecond} millisecond/s'


print(convert(60001))