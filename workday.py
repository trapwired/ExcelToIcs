class Workday:
    def __init__(self, iden: str, start: str, end: str, name: str = None):
        self.id = iden
        self.start = start
        self.end = end
        self.h_start = int(start[:2])
        self.m_start = int(start[3:])
        self.h_end = int(end[:2])
        self.m_end = int(end[3:])
        self.name = name

    def get_name(self):
        return self.name if self.name else self.id


def getWorkDays():
    res = []
    res.append(Workday('Heb', '08:00', '11:00'))
    res.append(Workday('NP', '19:30', '07:30'))
    res.append(Workday('3NP', '19:30', '07:30'))
    res.append(Workday('ET', '07:30', '16:30'))
    res.append(Workday('T', '07:30', '16:30'))
    res.append(Workday('3NP*', '19:30', '08:00'))
    res.append(Workday('TE/KO', '08:00', '17:00'))
    res.append(Workday('S', '13:45', '23:00'))
    res.append(Workday('KO/4P', '07:30', '19:30'))
    res.append(Workday('TP', '07:30', '19:30'))
    res.append(Workday('TP*', '07:30', '19:30'))
    res.append(Workday('3TP', '07:30', '19:30'))
    res.append(Workday('3TP*', '07:30', '19:30'))
    res.append(Workday('N', '22:30', '08:00'))
    res.append(Workday('N20', '20:00', '08:00'))
    res.append(Workday('S20', '13:45', '20:00'))
    return res


def is_nightshift(wd: Workday):
    return wd.id in ['NP', '3NP', '3NP*', 'N', 'N20']
