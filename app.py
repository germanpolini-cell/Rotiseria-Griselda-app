import streamlit as st
import urllib.parse



st.set_page_config(page_title="Rotiseria GRISELDA")
st.title("Rotiseria GRISELDA")
st.write("Selecciona tu Vianda y enviamos por tu pedido por whatsApp.")

menu = {
    "Pollo con papas": 19000,
    "Milanesa con papas": 1700
}

st.subheader("Menu del dia")
pedido = {}
total = 0

for vianda, precio in menu.items():
    cantidad = st.number_input(
        f"{vianda} - ${precio}",
        min_value=0,
        max_value=20,
        step=1,
        key=vianda
    )
    if cantidad > 0:
        pedido[vianda] = (cantidad,precio * cantidad)
        total  += precio * cantidad

st.divider()        


st.subheader("Datos de entrega")
nombre = st.text_input("Tu nombre")
direccion = st.text_input("Tu direccion")
modalidad = st.radio("modalidad", ["Retiro en el local", "Envio a su domocilio"])
direccion = ""
if modalidad == "Envio a domicilio":
    direccion = st.text_input("Direccin de entrega")


if total > 0:
    st.subheader(f"Total a pagar: ${total}")

    if st.button("Comfirmar pedido"):
        if not nombre or ( modalidad == "Envio a domicilio" and not direccion):
            st.warning("Por favor completa tu nombre y direccion")

        else:
            texto = f"Hola soy *{nombre}*. Quiero hacer un pedido:\n\n"
            for vianda, (cant, subtotal) in pedido.items():
                texto += f"- {cant}x {vianda} (${subtotal})\n"
                texto += f"\n *Total:* ${total}\n"
                texto +=f"\n *Modalidad:* {modalidad}"
            if direccion:
                texto += f"\n*Direccion:* {direccion}"        


    Telefono_rotiseria = "5493492215442"
    url_wa = f"https://wa.me/{Telefono_rotiseria}?text={urllib.parse.quote(texto)}"

    st.success("Pedido listo. has clic abajo para enviarlo:")
    st.markdown(f"[Enviar pedido por whatsApp]({url_wa})", unsafe_allow_html = True)




