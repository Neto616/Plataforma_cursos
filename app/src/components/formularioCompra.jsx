import React, { useState } from "react";
import "../styles/auth.css"; // Estilos del formulario modal de compra

// Componente FormularioCompra: muestra un modal para ingresar datos de tarjeta y comprar un certificado.
// Recibe como props:
// - onClose: función para cerrar el modal.
// - courseTitle: nombre del curso que se está comprando.
function FormularioCompra({ onClose, courseTitle, courseId }) {
  // Estados para los campos del formulario
  const [tarjeta, setTarjeta] = useState("");
  const [vencimiento, setVencimiento] = useState("");
  const [cvv, setCvv] = useState("");

  // Manejador para formatear el número de tarjeta en tiempo real (XXXX XXXX XXXX XXXX)
  const handleTarjetaChange = (e) => {
    const value = e.target.value.replace(/\D/g, ""); // Elimina todo lo que no sea número
    const formatted = value.match(/.{1,4}/g)?.join(" ") ?? ""; // Agrupa cada 4 dígitos
    setTarjeta(formatted);
  };

  // Manejador para formatear la fecha de vencimiento (MM/AA)
  const handleVencimientoChange = (e) => {
    let value = e.target.value.replace(/\D/g, ""); // Solo números
    if (value.length >= 3) {
      value = value.slice(0, 4); // Máximo 4 dígitos
      value = value.slice(0, 2) + "/" + value.slice(2); // Inserta el slash
    }
    setVencimiento(value);
  };

  // Permite borrar el slash del campo de vencimiento al presionar Backspace
  const handleVencimientoKeyDown = (e) => {
    if (e.key === "Backspace") {
      const value = vencimiento;
      if (value.length === 3) {
        setVencimiento(value.slice(0, 2));
        e.preventDefault();
      }
    }
  };

  // Manejador para limitar el CVV a solo números y máximo 4 dígitos
  const handleCvvChange = (e) => {
    const value = e.target.value.replace(/\D/g, "");
    setCvv(value.slice(0, 4));
  };

  // Al enviar el formulario, muestra los datos por consola (simula una compra)
  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("Tarjeta:", tarjeta);
    console.log("Vencimiento:", vencimiento);
    console.log("CVV:", cvv);
    // Aquí iría el procesamiento del pago real
    const peticion = await fetch("http://localhost:8000/comprar-certificado", { method: "POST", headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ curso_id: courseId })
    });
    const resultado = await peticion.json();
    console.log(resultado);
    if(resultado.estatus == 1) {
      onClose();
      return alert("Certificado comprado");
    }
    else if(resultado.estatus == 0){
      onClose();
      return alert("El curso ya lo has comprado")
    }
    else{
      onClose();
      return alert("Favor de iniciar sesion")
    }
  };

  return (
    <div className="modal-overlay">
      <div className="modal-split modal-compra-container">
        {/* Sección izquierda del modal: formulario */}
        <div className="modal-left">
          {/* Botón para cerrar el modal */}
          <button className="modal-close" onClick={onClose}>×</button>

          {/* Título e información del curso */}
          <h3 className="modal-title">Comprar Certificado</h3>
          <p className="modal-subtitle">
            Curso: <strong>{courseTitle}</strong><br />
            Completa tus datos para continuar.
          </p>

          {/* Formulario de compra */}
          <form onSubmit={handleSubmit}>
            {/* Campo para el número de tarjeta */}
            <label htmlFor="tarjeta">Número de tarjeta:</label>
            <input
              id="tarjeta"
              type="text"
              inputMode="numeric"
              placeholder="0000 0000 0000 0000"
              value={tarjeta}
              onChange={handleTarjetaChange}
              maxLength="19"
              required
            />

            {/* Fila con vencimiento y CVV */}
            <div className="form-row">
              <div>
                <label htmlFor="vencimiento">Vencimiento:</label>
                <input
                  id="vencimiento"
                  type="text"
                  inputMode="numeric"
                  placeholder="MM/AA"
                  value={vencimiento}
                  onChange={handleVencimientoChange}
                  onKeyDown={handleVencimientoKeyDown}
                  required
                />
              </div>
              <div>
                <label htmlFor="cvv">CVV:</label>
                <input
                  id="cvv"
                  type="text"
                  inputMode="numeric"
                  placeholder="123"
                  className="cvv"
                  value={cvv}
                  onChange={handleCvvChange}
                  required
                />
              </div>
            </div>

            {/* Botón para enviar el formulario */}
            <button type="submit">Finalizar Compra</button>
          </form>
        </div>

        {/* Sección derecha del modal: información adicional */}
        <div className="modal-right">
          <h4>¿Qué sucede luego del pago?</h4>
          <p>
            Una vez se realice el pago de tu certificado,<br />
            accederás automáticamente a un examen de conocimientos.<br />
            Al aprobarlo, recibirás tu certificado digital por correo.
          </p>
        </div>
      </div>
    </div>
  );
}

export default FormularioCompra;
