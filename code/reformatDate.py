class Solution:
    def reformatDate(self, date: str) -> str:
        d,m,y = date.split(" ")
        fm={"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05',
            "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10',
            "Nov":'11', "Dec":'12'}
        d=d[:-2]
        if len(d)==1:
            return y+'-'+fm[m]+'-0'+d
        else:
            return y+'-'+fm[m]+'-'+d