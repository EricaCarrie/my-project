def calculate_day_of_year(year, month, day):  
    """  
    计算给定日期 (年、月、日) 是这一年的第几天。

    参数： 
    year: 给定的年份，例如 2023。  
    month: 给定的月份，例如 1 或 2。  
    day: 给定的日期，例如 1 或 28。

    返回值： 
    这一年的第几天，例如 1 表示第一天，31 表示最后一天。  
    """  
    # 将日期转换为 0 表示公元前，1 表示公元  
    year = int(year)  
    month = int(month)  
    day = int(day)  
    year_day = (year * 365 + month * 30 + day) // 100  # 计算年份的天数  
    if month == 2 and day == 28:  # 特殊情况，2 月份有 29 天  
        year_day += 1  
    if month in [4, 6, 9, 11] and day == 30:  # 特殊情况，4、6、9、11 月份有 30 天  
        year_day += 1  
    if month in [1, 3, 5, 7, 8, 10, 12] and day == 31:  # 特殊情况，1、3、5、7、8、10、12 月份有 31 天  
        year_day += 1  
    return year_day // 4  # 取模以确保是闰年  
