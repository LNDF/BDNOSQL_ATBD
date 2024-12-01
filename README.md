# BDNOSQL_ATBD
Arquitectura tecnológica para Big Data

## Preparación de entorno
1. Clonar la repo
```
git lone https://github.com/LNDF/BDNOSQL_ATBD.git
```
2. Entrar en la repo
```
cd BDNOSQL_ATBD
```
3. Crear un virtual environment
```
python -m venv .env
```
4. Activar el virtual environment

En Linux
```
source .env/bin/activate
```
En Windows
```
.\.env\Scripts\activate
```
5. Instala las dependencias
```
pip install -r requirements.txt
```
6. Modificar `load.py` y `queries.py` con la dirección, usuario y contraseá correctas de la base de datos de MongoDB
## Cargar los datos
```
python load.py
```
## Realizar las consultas
```
python quieries.py
```