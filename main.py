import asyncio
import csv

import aiohttp
from bs4 import BeautifulSoup

LEYES = 15520


async def fetch_law(law_number, session, semaphore):
    url = "https://normas.gba.gob.ar/resultados"
    params = {"q[terms][raw_type]": "Law", "q[terms][number]": law_number}
    async with semaphore:
        try:
            async with session.get(url, params=params, timeout=10) as response:
                if response.status != 200:
                    return None
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")

                # Extraer el número de ley y la URL
                h3 = soup.find("h3", class_="card-title rule-name")
                if not h3:
                    return None
                a_tag = h3.find("a")
                if not a_tag:
                    return None

                numero_ley = a_tag.get_text(strip=True).replace(
                    "Ley ", ""
                )  # Eliminar "Ley "
                law_href = a_tag.get("href")
                if law_href and law_href.startswith("/"):
                    law_href = "https://normas.gba.gob.ar" + law_href

                # Extraer el resumen
                blockquote = soup.find("blockquote")
                if not blockquote:
                    return None
                resumen = blockquote.get_text(strip=True)

                return (numero_ley, resumen, law_href)
        except Exception:
            # Si ocurre cualquier error, se asume que la ley no existe o hubo fallo en la consulta
            return None


async def main():
    # Semáforo para limitar las solicitudes concurrentes (puedes ajustar el valor según tu entorno).
    semaphore = asyncio.Semaphore(200)
    results = []

    async with aiohttp.ClientSession() as session:
        # Creamos las tareas para cada ley del 1 al 15000.
        tasks = [fetch_law(i, session, semaphore) for i in range(1, 15520)]

        # Procesamos las tareas a medida que se van completando.
        for future in asyncio.as_completed(tasks):
            result = await future
            if result is not None:
                results.append(result)
                # Mostrar en pantalla el número de ley encontrada
                print(f"Ley encontrada: {result[0]}")

    # Guardar los resultados en un archivo CSV con el formato: numero_ley, resumen, url
    with open("leyes.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["numero_ley", "resumen", "url"])
        for row in results:
            writer.writerow(row)


if __name__ == "__main__":
    asyncio.run(main())
