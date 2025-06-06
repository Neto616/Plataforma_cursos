import React, { useState } from "react";
import "../styles/auth.css";

function FormularioCompra({ onClose, courseTitle }) {
  const [tarjeta, setTarjeta] = useState("");
  const [vencimiento, setVencimiento] = useState("");
  const [cvv, setCvv] = useState("");

  // Formatear número de tarjeta (xxxx xxxx xxxx xxxx)
  const handleTarjetaChange = (e) => {
    const value = e.target.value.replace(/\D/g, ""); // Eliminar todo lo que no sea número
    const formatted = value.match(/.{1,4}/g)?.join(" ") ?? "";
    setTarjeta(formatted);
  };

  // Formatear vencimiento (MM/AA)
  const handleVencimientoChange = (e) => {
    let value = e.target.value.replace(/\D/g, ""); // Solo números
    if (value.length >= 3) {
      value = value.slice(0, 4); // máximo 4 dígitos
      value = value.slice(0, 2) + "/" + value.slice(2);
    }
    setVencimiento(value);
  };

  // Permitir borrar correctamente el slash
  const handleVencimientoKeyDown = (e) => {
    if (e.key === "Backspace") {
      const value = vencimiento;
      if (value.length === 3) {
        setVencimiento(value.slice(0, 2));
        e.preventDefault();
      }
    }
  };

  // Solo números para CVV
  const handleCvvChange = (e) => {
    const value = e.target.value.replace(/\D/g, "");
    setCvv(value.slice(0, 4)); // máximo 4 dígitos
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Tarjeta:", tarjeta);
    console.log("Vencimiento:", vencimiento);
    console.log("CVV:", cvv);
    // Aquí iría el procesamiento del pago
  };

  return (
    <div className="modal-overlay">
      <div className="modal-split modal-compra-container">
        <div className="modal-left">
          <button className="modal-close" onClick={onClose}>
            ×
          </button>

          <h3 className="modal-title">Comprar Certificado</h3>
          <p className="modal-subtitle">
            Curso: <strong>{courseTitle}</strong>
            <br />
            Completa tus datos para continuar.
          </p>

          <form onSubmit={handleSubmit}>
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

            <button type="submit">Finalizar Compra</button>
          </form>
        </div>

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
