PS C:\Users\user\OneDrive\Escritorio\Test Backend Java\Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process ----> (Tener en cuenta si se utiliza sistema operativo de Windows, ejecutar
primero este comando )
Test Backend Java\venv\Scripts> .\activate
--------------------------------------------------------------------------------

(venv)Test Backend Java> uvicorn main:app --reload

Ejecutar: uvicorn main:app --reload

Para ejecuatr y probar los endpoint con las operaciones en el CRUD, se debe de dirigir a la ruta: http://127.0.0.1:8000/docs

Instalar extensiones
pip install fastapi

Servidor ASGI uvicorn
pip install "uvicorn[standard]"

pip freeze > requirements.txt

Descargar extensiones de fastapi la ruta es: https://fastapi.tiangolo.com/es/

PD: tienen alguna duda favor me contactan para ayudar en lo que se necesite.



