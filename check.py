input_wheel = 20,1
input_form = 300
input_height = 30
input_density = 15
input_procent = 14


some_list = [input_wheel, input_form, input_height, input_density, input_procent]
if all([i.isnumeric() for i in some_list]):
    volume_result = round(((3.14 * float(input_form) ** 2 * float(input_height)) / 4000000 - (
                3.14 * float(input_wheel) ** 2 * float(input_height)) / 4000000) * float(input_density), 3)

    volume = 'Общий объем: ' + str(volume_result)
    volumePP = 'Объем Преполимера: ' + str(round(volume_result * 100 / (float(input_procent) + 100), 3))
    print(volume)
    print(volumePP)