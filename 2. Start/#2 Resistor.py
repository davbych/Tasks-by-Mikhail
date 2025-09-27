get_resistor_value = input("Пиши цвета тут(4 цвета): "). split()
rings = {
    "bk":1,
    "br":10,
    "rd":10**2,
    "or":10**2,
    "yl":10**4,
    "gr":10**5,
    "bl":10**6,
    "vi":10**7,
    "gy":10**8,
    "wh":10**9,
    "au":"-",
    "ag":"-",
    "-":"-"
}
Toch = {
    "bk":"-",
    "br":"1",
    "rd":"2",
    "or":"-",
    "yl":"5",
    "gr":"0.5",
    "bl":"0.25",
    "vi":"0.1",
    "gy":"0.05",
    "wh":"-",
    "au":"5",
    "ag":"10",
    "-":"20"
}
nom1=rings[get_resistor_value[0]]
nom2=rings[get_resistor_value[1]]
nom0=str(nom1)+str(nom2)
mnoj=rings[get_resistor_value[2]]
Tocchnost=Toch[get_resistor_value[3]]
if (get_resistor_value[0] == get_resistor_value[1]) or (get_resistor_value[1] == get_resistor_value[2]) or (get_resistor_value[2] == get_resistor_value[3]) or (get_resistor_value[0] == get_resistor_value[3]) or (get_resistor_value[0] == get_resistor_value[2]):
    print("ERROR")
else:
    print(int(nom0)*mnoj, ", ", Tocchnost)