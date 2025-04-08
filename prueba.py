from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import traceback


if not os.path.exists("capturas"):
    os.makedirs("capturas")


ruta_reporte = os.path.join("C:", "MisReportes")  
print(f"Ruta de los reportes: {ruta_reporte}") 


if not os.path.exists(ruta_reporte):
    os.makedirs(ruta_reporte)

def guardar_captura(driver, nombre):
    driver.save_screenshot(f"capturas/{nombre}.png")



######################################################
#reporte
def iniciar_reporte():
    reporte = """<html>
    <head>
        <title>Reporte de Pruebas de Librería</title>
        <style>
            body { font-family: Arial, sans-serif; }
            table { width: 100%; border-collapse: collapse; }
            th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
            th { background-color: #f2f2f2; }
            .pass { color: green; }
            .fail { color: red; }
            img { width: 200px; }
        </style>
    </head>
    <body>
        <h1>Reporte de Pruebas - Librería Online</h1>
        <h2>Resumen de Pruebas</h2>
        <table>
            <tr><th>Total de Pruebas</th><td>0</td></tr>
            <tr><th>Pruebas Pasadas</th><td>0</td></tr>
            <tr><th>Pruebas Fallidas</th><td>0</td></tr>
        </table>
        <h2>Detalle de las Pruebas</h2>
        <table id="detalle-pruebas">
            <tr>
                <th>Escenario</th>
                <th>Resultado</th>
                <th>Captura de Pantalla</th>
            </tr>"""
    return reporte


def actualizar_reporte(reporte, escenario, resultado, captura):
    resultado_color = "pass" if resultado == "Pasó" else "fail"
    reporte += f"""
    <tr>
        <td>{escenario}</td>
        <td class="{resultado_color}">{resultado}</td>
        <td><img src="capturas/{captura}.png" alt="{escenario}"></td>
    </tr>"""
    return reporte

def finalizar_reporte(reporte, total, pasadas, fallidas):
    reporte = reporte.replace("0</td>", f"{total}</td>", 1)
    reporte = reporte.replace("0</td>", f"{pasadas}</td>", 1)
    reporte = reporte.replace("0</td>", f"{fallidas}</td>", 1)
    reporte += """
        </table>
    </body>
</html>"""
    
    # guardar reporte
    try:
        with open(os.path.join(ruta_reporte, "reporte_pruebas.html"), "w") as archivo:
            archivo.write(reporte)
        print(f"Reporte guardado correctamente en {os.path.join(ruta_reporte, 'reporte_pruebas.html')}")
    except Exception as e:
        print(f"Error al guardar el reporte: {e}")




######################################################

driver = webdriver.Chrome()

reporte = iniciar_reporte() 

#conteo de pruebas
total_pruebas = 0
pruebas_pasadas = 0
pruebas_fallidas = 0


######################################################


#pruebas
try:
  
    total_pruebas += 1
    driver.get("http://127.0.0.1:5500/index.html")
    time.sleep(2)
    guardar_captura(driver, "1_pagina_cargada")
    reporte = actualizar_reporte(reporte, "Abrir la página", "Pasó", "1_pagina_cargada")
    pruebas_pasadas += 1

    total_pruebas += 1
    assert "Inicio" in driver.title
    guardar_captura(driver, "2_titulo_correcto")
    reporte = actualizar_reporte(reporte, "Verificar título", "Pasó", "2_titulo_correcto")
    pruebas_pasadas += 1

    
    total_pruebas += 1
    driver.find_element(By.LINK_TEXT, "Libros").click()
    time.sleep(2)
    guardar_captura(driver, "3_libros_link")  # Cambié el nombre de la captura
    reporte = actualizar_reporte(reporte, "Verificar enlace 'Libros'", "Pasó", "3_libros_link")
    pruebas_pasadas += 1

   
    total_pruebas += 1
    driver.find_element(By.LINK_TEXT, "Autores").click()
    time.sleep(2)
    guardar_captura(driver, "4_autores_link")  # Cambié el nombre de la captura
    reporte = actualizar_reporte(reporte, "Verificar enlace 'Autores'", "Pasó", "4_autores_link")
    pruebas_pasadas += 1

   
    total_pruebas += 1
    driver.find_element(By.LINK_TEXT, "Contacto").click()
    time.sleep(2)
    guardar_captura(driver, "5_contacto_link")  # Cambié el nombre de la captura
    reporte = actualizar_reporte(reporte, "Verificar enlace 'Contacto'", "Pasó", "5_contacto_link")
    pruebas_pasadas += 1

   
    total_pruebas += 1
    assert "Explora Nuestros Libros y Autores" in driver.page_source
    guardar_captura(driver, "6_texto_principal")
    reporte = actualizar_reporte(reporte, "Verificar texto principal", "Pasó", "6_texto_principal")
    pruebas_pasadas += 1

   
    finalizar_reporte(reporte, total_pruebas, pruebas_pasadas, total_pruebas - pruebas_pasadas)
    print("✔ Todas las pruebas pasaron correctamente.")



######################################################


except Exception as e:
    print(" Error durante la prueba:")
    traceback.print_exc()
    guardar_captura(driver, "error")
    reporte = actualizar_reporte(reporte, "Error en la prueba", "Falló", "error")
    finalizar_reporte(reporte, total_pruebas, pruebas_pasadas, total_pruebas - pruebas_pasadas)

finally:
    driver.quit()
