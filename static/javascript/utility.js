var utility = {}



/* 时区转换 */
utility.localtime = function(utc_time)
{
    let datetime = new Date(utc_time)
    datetime = new Date(Date.UTC(datetime.getFullYear(),
                                datetime.getMonth(),
                                datetime.getDate(),
                                datetime.getHours(),
                                datetime.getMinutes(),
                                datetime.getSeconds()))
    return datetime.toLocaleString()
}