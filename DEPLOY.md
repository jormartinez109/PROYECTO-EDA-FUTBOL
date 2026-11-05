# Publicar Football Myths vs Data en Streamlit Community Cloud

El código y el dataset limpio ya están en la raíz de este repositorio:

- `app.py`
- `datos_limpios.csv`
- `requirements.txt`

El repositorio puede permanecer **privado** y la aplicación configurarse como **pública**. Streamlit permite cambiar la privacidad desde los ajustes de la app.

## 1. Conectar Streamlit con GitHub

1. Abre [Streamlit Community Cloud](https://share.streamlit.io/).
2. Inicia sesión con GitHub.
3. Para que Streamlit pueda leer este repositorio privado, abre los ajustes de tu cuenta de Streamlit.
4. Entra en **Linked accounts** → **Source control** → **Connect** y autoriza el acceso a los repositorios privados.

## 2. Crear la aplicación

1. En el espacio de trabajo de Streamlit, pulsa **Create app**.
2. Selecciona el repositorio `jormartinez109/PROYECTO-EDA-FUTBOL`.
3. Selecciona la rama `main`.
4. Indica `app.py` como archivo principal.
5. Opcionalmente, elige un subdominio reconocible, por ejemplo `football-myths-vs-data`, si está disponible.
6. Pulsa **Deploy** y espera a que termine la instalación de las dependencias.

## 3. Hacer pública la aplicación

Una vez desplegada:

1. Abre los ajustes de la aplicación.
2. Entra en **Sharing**.
3. En **Who can view this app**, selecciona **This app is public and searchable**.
4. Guarda los cambios.

La aplicación tendrá una dirección con el dominio `streamlit.app`. Copia esa URL para compartirla. No se debe inventar la dirección antes de que Streamlit termine el despliegue.

## 4. Comprobación final

- Comprueba que la app abre sin errores.
- Revisa que aparecen las seis pestañas.
- Prueba los filtros de liga, temporada y periodo.
- Revisa que los gráficos cambian al modificar los filtros.
- Abre el enlace en una ventana privada o en otro navegador para confirmar que cualquier persona puede verla sin iniciar sesión.

## Privacidad

Aunque el repositorio siga siendo privado, la app pública permite que otras personas consulten la aplicación y los datos que esta presenta. Asegúrate de que el contenido del repositorio y el dataset son adecuados para compartir públicamente.

## Documentación oficial

- [Conectar la cuenta de GitHub](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account)
- [Desplegar una aplicación](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)
- [Compartir y cambiar la privacidad de la app](https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app)
