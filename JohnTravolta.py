#Muhammad Hugo Athallah Hardy
#11190910000035

def hitung_gaji(work_time):
    salary = work_time * 15_000

    if work_time == 0:
        total_salary = 0
        return total_salary

    elif work_time > 40:
        overtime = work_time - 40
        default = work_time - overtime

        main_salary = default * 15_000
        additional_salary = overtime * 15_000 * 1.5
        total_salary = main_salary + additional_salary
        return total_salary

    else:
        total_salary = work_time * 15_000
        return total_salary

def bisa_tabung(work_time, spending):
    salary = hitung_gaji(work_time)
    if salary > spending:
        tabungan = salary - spending
        print('Bisa menabung sebanyak: ', tabungan)
    elif salary == spending:
        print('tidak bisa menabung')
    else:
        print('cari tambahan')


jam_kerja = int(input('Masukkan jam kerja dalam seminggu: '))
pengeluaran = int(input('Masukkan pengeluaran: '))

bisa_tabung(jam_kerja, pengeluaran)
