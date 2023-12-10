#Profe para recordarle usar el comando pip para instalar la libreria automata como en collab
from tkinter import *
from tkinter import font
from automata.fa.dfa import DFA
import random
t=Tk()
t.title('máquina expendedora')
t.minsize(1280,720)
t.maxsize(1280,720)
ca=Canvas(t,width=1350,height=800,bg='#c6da52')
ca.place(x=-2,y=-2)


ca.create_text((1190,37),text='Máquina de Ponqués',fill=('#ffffff'), font=('Comic Sans MS',12))
ca.create_text((1190,40),text='Máquina de Ponqués', font=('Comic Sans MS',12))

#Esto crea donde van los productos
def drawShowcase(x,y):
    ca.create_rectangle((x,y,x+310,y+170),fill='#ffffff')
    ca.create_rectangle((x,y+170,x+310,y+200),fill='#ffffff')
    ca.create_line((x,y+170,x+10,y+130))
    ca.create_line((x+10,y+130,x+300,y+130))
    ca.create_line((x+300,y+130,x+310,y+170))
    ca.create_line((x+10,y+130,x+10,y))
    ca.create_line((x+300,y+130,x+300,y))
drawShowcase(20,20)
drawShowcase(20,230)
drawShowcase(20,440)

drawShowcase(400,20)
drawShowcase(400,230)
drawShowcase(400,440)

drawShowcase(780,20)
drawShowcase(780,230)
drawShowcase(780,440)

#Todo lo siguiente es lo que sirve para que aparezca texto a la derecha
selectcake = {
    "Tipo de bizcocho": "",
    "Tipo de relleno": "",
    "Tipo de cobertura": "",
    "Tipo de decoración": "",
    "Forma del pastel": "",
    "Tamaño del pastel": "",
    "Textura del pastel": "",
    "Adicional": ""
}





def selectcaketip():
    ca.delete("selected_text")
    ca.create_rectangle((1115, 60, 1270, 600), fill='#ffffff')
    ca.create_text((1190, 69),text='Usted ha seleccionado:',font=('Microsoft Yaisho', 8),fill='#000000')
    ca.create_line((1140, 80, 1250, 80), fill='#000000')
    ca.create_line((1140, 575, 1250, 575), fill='#000000')
    ca.create_text((1190, 585), text='Total', font=('Microsoft Yaisho', 8), fill='#000000')
    i = 0
    text = ''
    for key, value in selectcake.items():
        if value != "":
            text += f'{key}: {value}\n'
    text += '\nLista de calificaciones:\n'
    for i, rating in enumerate(lista):
        text += f'{i + 1}: {rating}\n'
    
    ca.create_text((1125, 85), text=text, font=('Microsoft Yaisho', 8), fill='#000000', anchor='nw', tags="selection_text")


def operationtip(text):
    ca.create_rectangle((1115, 670, 1270, 710), fill='#ffffff')
    ca.create_text((1190, 690), text=text, fill='#000000', font=('Comic Sans MS', 7))


def addselectcake(option_type, option_value):
    global selectcake, ratings, selection_locked

    if selection_locked:
        operationtip('Las selecciones están bloqueadas.\n Presione Limpiar para cambiar.')
        return

    if selectcake[option_type] == "":
       
        order = list(selectcake.keys())
        current_index = order.index(option_type)
        previous_option = order[current_index - 1] if current_index > 0 else None

        if previous_option is None or selectcake[previous_option] != "":
           
            selectcake[option_type] = option_value
            operationtip('Haga clic para \nconfirmar la selección')

            
            if option_value in ["Vainilla", "C. pastelera", "Merengue", "Frutas", "Redondo", "Pequeño", "Esponjoso", "Chips de Choco." ]:
                lista.append(1)
            elif option_value in ["Chocolate", "Chantilly","Ganache", "Flores", "Cuadrado", "Mediano", "Húmedo", "Sprinkles"]:
                lista.append(2)
            elif option_value in ["Tres leches", "Arequipe", "Mora", "Infantil", "Rectangular", "Grande", "Crema", "Ninguno"]:
                lista.append(3)

            selectcaketip()

            if current_index == len(order) - 1:
                selection_locked = True
                operationtip('Todas las selecciones realizadas. \nLas selecciones están bloqueadas.')
        else:
            operationtip(f'Seleccione "{previous_option}" \nantes de "{option_type}".')

    else:
        operationtip('Ya ha seleccionado.')

#Esto elimina todo el texto
def clear_selections():
    global selectcake, lista, selection_locked
    selectcake = {
        "Tipo de bizcocho": "",
        "Tipo de relleno": "",
        "Tipo de cobertura": "",
        "Tipo de decoración": "",
        "Forma del pastel": "",
        "Tamaño del pastel": "",
        "Textura del pastel": "",
        "Adicional": ""
    }
    lista = []
    selection_locked = False
    operationtip('Opciones limpiadas.\n Puede seleccionar nuevas.')
    ca.delete("selection_text")



#Esto también pero hace que aparezca el precio
def purchase():
    #creo que acá iría el codigo del automata que calcule el precio, en la lista estarían guardadas las opciones
    global selectcake, lista, selection_locked
    strings=''
    lista.append("-")
    for i in lista:
        strings=strings+str(i)

    dfaPrecio = DFA(
    states={'inicio','6000', '6001', '8000','2000', '5000', '3000', '3001', '4000', '3002', '5001', '8001', '4001', '5002', '7000', '10000', '25000', '40000', '60000', '2001', '3003', '4002','4003', '3004', '0000','Final'},
    input_symbols={'-','1','2','3'},
    transitions={
        'inicio': {'-': 'inicio','1': '6000', '2': '6001', '3':'8000'},
        '6000': {'-': '6000','1': '2000', '2': '5000', '3':'3000'},
        '6001': {'-': '6001','1': '2000', '2': '5000', '3':'3000'},
        '8000': {'-': '8000','1': '2000', '2': '5000', '3':'3000'},
        '2000':{'-': '2000','1': '3001', '2': '4000', '3':'3002'},
        '5000':{'-': '5000','1': '3001', '2': '4000', '3':'3002'},
        '3000':{'-': '3000','1': '3001', '2': '4000', '3':'3002'},
        '3001':{'-': '3001','1': '5001', '2': '8001', '3':'4001'},
        '4000':{'-': '4000','1': '5001', '2': '8001', '3':'4001'},
        '3002':{'-': '3002','1': '5001', '2': '8001', '3':'4001'},
        '5001':{'-': '5001','1': '5002', '2': '7000', '3':'10000'},
        '8001':{'-': '8001','1': '5002', '2': '7000', '3':'10000'},
        '4001':{'-': '4001','1': '5002', '2': '7000', '3':'10000'},
        '5002':{'-': '5002','1': '25000', '2': '40000', '3':'60000'},
        '7000':{'-': '7000','1': '25000', '2': '40000', '3':'60000'},
        '10000':{'-': '10000','1': '25000', '2': '40000', '3':'60000'},
        '25000':{'-': '25000','1': '2001', '2': '3003', '3':'4002'},
        '40000':{'-': '40000','1': '2001', '2': '3003', '3':'4002'},
        '60000':{'-': '60000','1': '2001', '2': '3003', '3':'4002'},
        '2001':{'-': '2001','1': '4003', '2': '3004', '3':'0000'},
        '3003':{'-': '3003','1': '4003', '2': '3004', '3':'0000'},
        '4002':{'-': '4002','1': '4003', '2': '3004', '3':'0000'},
        '4003':{'-': 'Final','1': '4003', '2': '4003', '3':'4003'},
        '3004':{'-': 'Final','1': '3004', '2': '3004', '3':'3004'},
        '0000':{'-': 'Final','1': '0000', '2': '0000', '3':'0000'},
        'Final':{'-': 'Final','1': 'Final', '2': 'Final', '3':'Final'}
        },
    initial_state='inicio',
    final_states={'Final'}
    )

    myList=list(dfaPrecio.validate_input(strings,step=True))
    Sum=0
    for i in range(len(myList)):
        if myList[i]!='inicio' and myList[i]!='Final':
            Sum=Sum+(round(int(myList[i])/10)*10)
    print(Sum)
    ca.create_text((1190, 560), text=(str(Sum)+" COP"), fill='#000000', font=('Comic Sans MS', 7))
    selectcake = {
        "Tipo de bizcocho": "",
        "Tipo de relleno": "",
        "Tipo de cobertura": "",
        "Tipo de decoración": "",
        "Forma del pastel": "",
        "Tamaño del pastel": "",
        "Textura del pastel": "",
        "Adicional": ""
    }
    selection_locked = False
    operationtip('Compra confirmada')
    ca.delete("selection_text")
    
    lista = []

    
#Los botones de limpiar y confirmar/comprar

Button(t, font=('Microsoft Yaisho', 7), width=8, height=1, text='Limpiar',
       command=clear_selections).place(x=1115, y=635)
Button(t, font=('Microsoft Yaisho', 7), width=8, height=1, text='Confirmar',
       command=purchase).place(x=1190, y=635)

#Esto crea las imagenes de las bolsas

def drawBag(x,y,color1,color2,color3):
    #sombra
    ca.create_oval((x-5,y+77,x+65,y+87),fill='#999999')
    #  
    ca.create_rectangle((x,y,x+60,y+7),fill=color1)
    #medio
    ca.create_polygon((x,y+7,x+60,y+7,x+59,y+17,x+58,y+27,x+57,y+37,x+57,y+47,x+58,y+57,x+59,y+67,x+60,y+77,\
                       x,y+77,x+1,y+67,x+2,y+57,x+3,y+47,x+3,y+37,x+2,y+27,x+1,y+17,x,y+7),fill=color1)
    #  
    ca.create_polygon((x+1,y+67,x+2,y+57,x+3,y+47,x+59,y+17,x+58,y+27,x+57,y+37,x+1,y+67),fill=color2)
    ca.create_polygon((x,y+77,x+1,y+67,x+57,y+37,x+57,y+47,x,y+77),fill=color3)
    #    
    ca.create_line((x,y+7,x+60,y+7,x+59,y+17,x+58,y+27,x+57,y+37,x+57,y+47,x+58,y+57,x+59,y+67,x+60,y+77,\
                    x,y+77,x+1,y+67,x+2,y+57,x+3,y+47,x+3,y+37,x+2,y+27,x+1,y+17,x,y+7))
    #  
    ca.create_rectangle((x, y+77, x + 60, y + 84), fill=color1)
 
drawBag(50,90,'#D7BB94','#ffffff','#CEC0AC')
drawBag(150,90,'#534634','#ffffff','#CEC0AC')
drawBag(250,90,'#902308','#ffffff','#CEC0AC')

drawBag(50,300,'#D6D28E','#ffffff','#FAEFCA')
drawBag(150,300,'#7E642D','#ffffff','#fcc75a')
drawBag(250,300,'#FD2E07','#ffffff','#FFFD4F')

drawBag(50,510,'#ffffff','#D6D28E','#fcc75a')
drawBag(150,510,'#2D250A','#ffffff','#534E3B')
drawBag(250,510,'#83C9B0','#ffffff','#C0E7D9')

drawBag(425,90,'#CCFFAB','#ffffff','#8A9D7E')
drawBag(525,90,'#FFABF7','#ffffff','#947E9D')
drawBag(625,90,'#FFFC00','#ffffff','#fcc75a')

drawBag(425,300,'#413D43','#ffffff','#928D95')
drawBag(525,300,'#413D43','#ffffff','#928D95')
drawBag(625,300,'#413D43','#ffffff','#928D95')

drawBag(425,510,'#C5BDCA','#ffffff','#010101')
drawBag(525,510,'#C5BDCA','#ffffff','#010101')
drawBag(625,510,'#C5BDCA','#ffffff','#010101')

drawBag(800,90,'#E1C078','#ffffff','#C2C0BB')
drawBag(900,90,'#E4DCCA','#ffffff','#C2C0BB')
drawBag(1000,90,'#E1CEA4','#ffffff','#C2C0BB')

drawBag(800,300,'#534634','#ffffff','#D7BB94')
drawBag(900,300,'#FF0000','#ffffff','#002CFF')

#Esto crea opciones y los cuadros de escoger

def drawOption(x, y, option_type, options):
    ca.create_text((x+150, y-160), text=option_type, font=('Microsoft Yaisho', 9), fill='#000000')
    for i, option in enumerate(options):
        Button(t, text=option, width=9, height=1, font=('Microsoft Yaisho', 7),
               command=lambda opt=option: addselectcake(option_type, opt)).place(x=x + 20 + i * 100, y=y)

drawOption(30, 193, "Tipo de bizcocho", ["Vainilla", "Chocolate", "Tres leches"])
drawOption(30, 403, "Tipo de relleno", ["C. pastelera", "Chantilly", "Arequipe"])
drawOption(30, 613, "Tipo de cobertura", ["Merengue", "Ganache", "Mora"])
drawOption(400, 193, "Tipo de decoración", ["Frutas", "Flores", "Infantil"])
drawOption(400, 403, "Forma del pastel", ["Redondo", "Cuadrado", "Rectangular"])
drawOption(400, 613, "Tamaño del pastel", ["Pequeño", "Mediano", "Grande"])
drawOption(780, 193, "Textura del pastel", ["Esponjoso", "Húmedo", "Crema"])
drawOption(780, 403, "Adicional", ["Chips de Choco.", "Sprinkles", "Ninguno"])

def drawannouncement(x,y,text):
    ca.create_rectangle((x,y,x+200,y+50),fill='#ffff8b')
    ca.create_text((x+100, y+20), text=text, fill='#000000', font=('Comic Sans MS', 14))

#Relleno


drawannouncement(830,500,'¡PROXIMAMENTE!')

#ACA COMIENZA TODO
operationtip('Comience')
lista = []
selection_locked = False
selectcaketip()
t.mainloop()
for i, rating in enumerate(lista):
    print(f'{i}:{rating} ')
