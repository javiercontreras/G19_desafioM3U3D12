import sys
import copy

recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

for i in range(len(recordatorios)):
    new_format = "".join(recordatorios[i][0].split("-"))
    recordatorios[i][0] = new_format

#new format [20210512, hora , evento]]


continuar = True
while continuar:
    print("Inserte el numero asociado a las siguientes opciones ")
    print("Agregar un evento:           1 ") 
    print("Eliminar un evento:          2 ") 
    print("Editar los recordatorios:    3") 
    print("Mostrar los recordatorios:   4") 
    option = input("Su opcion :")


    if(option == '1' or  option == '2' or option =='3'):
        fecha= str(input("Inserta la fecha del evento en el siguiente formato  (aaaa-mm-dd) : "))
        hora= str(input("Inserta la hora del evento en el siguiente formato (hh:mm) : "))
        evento= str(input("Inserta el evento : "))
        new_fecha = "".join(fecha.split("-"))
        new_rec = [new_fecha, hora, evento]
            #Agrega nuevo recordatorio, en fecha y hora correspondiente
        indice = 0
        rec_eliminar = 0
        for j in range(len(recordatorios)):
            if recordatorios[j][0] > new_fecha:
                indice = j
                rec_eliminar = j
                print("fecha distinta")
                break
            elif recordatorios[j][0] == new_rec[0]:
                print("Misma fecha")
                #Se agrega el recordatorio en la hora correcta
                if recordatorios[j][1] <= new_rec[1]:
                    indice = j +1
                    rec_eliminar = j
                    break
                else:
                    indice = j
                    rec_eliminar = j
                    break
            else:
                indice = j+1
                rec_eliminar = j
                
        if(option == '1'):
            recordatorios.insert(indice,new_rec)
        elif(option == '2'):
            recordatorios.pop(rec_eliminar)
        elif(option== '3'):
            fecha= str(input("Inserta la fecha del evento en el siguiente formato  (aaaa-mm-hh) : "))
            new_fecha = "".join(fecha.split("-"))
            recordatorios[rec_eliminar][0] = new_fecha
    elif(option == '4'):
        show_lista = recordatorios
        print(recordatorios)
        show_lista = copy.deepcopy(recordatorios)
        for j in range(len(show_lista)):
            list_char = list(show_lista[j][0])
            year = "".join(list_char[:4])
            month = "".join(list_char[4:6])
            day = "".join(list_char[6:8])
            show_lista[j][0] = year+"-"+month+"-"+day
            print(show_lista[j])
        

    respuesta = input("Desea finalizar ? (Si/No) ")
    continuar = False if respuesta=='Si' else True



