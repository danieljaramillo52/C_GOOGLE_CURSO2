# Leer un csv simple. 
import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f: # Cada row se reifere a una fila del archivo CSV.
    # Cada fila es una lista de valores separados por comas.
    # Por ejemplo, si la fila es "John Doe, 1234567890, Developer", row será ['John Doe', '1234567890', 'Developer']
    # Preivamente sabemos que el archivo csv_file.txt tiene el siguiente contenido de tres columnas: nombre, teléfono y rol.
    name, phone, role = row # Desempaquetamos la fila en las variables correspondientes.
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()


# Escribir un CSV simple.
host = [["workstation.local", "192.168.25.46"], ["server.local", "193.1.24.1"]]

with open("hosts.csv", "w", newline='') as host_csv:
    writer = csv.writer(host_csv, delimiter=',')
    # Vamos a escribir las filas 
    writer.writerows(host)  # Escribe todas las filas de la lista 'host' en el archivo CSV.
    # También podemos escribir una fila a la vez
    # writer.writerow(host[0])  # Escribe la primera fila en el archivo CSV.
    # writer.writerow(host[1])  # Escribe la segunda fila en el archivo CSV.
    
# Los csv pueden tener los encabezados de las columnas en la primera fila del csv. 
#Supongaos el siguiente csv con encabezados:
with open("hosts_with_headers.csv", "w", newline='') as host_csv:
    writer = csv.writer(host_csv, delimiter=',')
    # Escribimos los encabezados de las columnas
    writer.writerow(["Hostname", "IP Address"])  # Escribe los encabezados en la primera fila.
    writer.writerows(host)  # Escribe todas las filas de la lista 'host' en el archivo CSV.
    
# Podemos acceder al archivo CSV con el módulo csv.DictReader para leer los datos como diccionarios.
with open("hosts_with_headers.csv", "r") as host_csv:
    reader = csv.DictReader(host_csv)  # Crea un lector de diccionarios a partir del archivo CSV.
    for row in reader:  # Itera sobre cada fila del lector de diccionarios.
        print("Hostname: {}, IP Address: {}".format(row["Hostname"], row["IP Address"]))
   
        
# Vamos a hacer lo contrario, escribir un CSV a partir de un diccionario.
data = [
    {"Hostname": "workstation.local", "IP Address": "1"}, 
    {"Hostname": "server.local", "IP Address": "2"},
    {"Hostname": "router.local", "IP Address": "3"}
]
with open("hosts_from_dict.csv", "w", newline='') as host_csv:
    writer = csv.DictWriter(host_csv, fieldnames=["Hostname", "IP Address"], delimiter=',')
    writer.writeheader()  # Escribe los encabezados de las columnas.
    writer.writerows(data)  # Escribe todas las filas del diccionario 'data' en el archivo CSV.
